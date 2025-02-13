import os
from ansys.mapdl.core import launch_mapdl
import statistics

mapdl = launch_mapdl(loglevel="WARNING", print_com=True, version=23.1, run_location=os.path.join(os.getcwd(),"workingDir"), override=True, nproc=4)

# clear database
mapdl.finish()
mapdl.run("/clear")

# read base cdb file
mapdl.cdread("db",os.path.join(os.getcwd(),"file.cdb"))

# solve
mapdl.run("/solu")

# define temperature bc
time_inc = 1
init_temp = 23
start_temp = 110
num_def_outputs = 5
mapdl.run("time_inc={}".format(time_inc))
mapdl.run("init_temp={}".format(init_temp))
mapdl.run("new_temp={}".format(start_temp))
mapdl.run("num_def_outputs={}".format(num_def_outputs))  # number of deformation outputs (my_def1,my_def2,...,my_defn)

# define temperature bc table and apply at my_temp
mapdl.run("init_time=0")
mapdl.run("end_time=init_time+time_inc")
mapdl.run("*dim,my_temp_table,table,2,1")
mapdl.run("*SET,my_temp_table(1,0),init_time,end_time")
mapdl.run("*SET,my_temp_table(1,1),init_temp,new_temp")
mapdl.d("my_temp", "temp", "%my_temp_table%")

# define output arrays
mapdl.get("nmax", "node", "", "num", "max")
mapdl.run("*dim,my_res,,nmax,4+num_def_outputs")
with mapdl.non_interactive:
    mapdl.run("*do,i,1,num_def_outputs")
    mapdl.cmsel("s", "my_def%i%")
    mapdl.run("*vget,my_res(1,4+i),node,1,nsel")
    mapdl.run("*enddo")
mapdl.run("*dim,my_res_mean,,num_def_outputs,4")
mapdl.allsel()

# start iterative process
for i in range(50):
    # set end time and solve
    mapdl.time("end_time")
    mapdl.solve()

    # read deformation values and compute mean values
    mapdl.run("*vget,my_res(1,1),node,1,u,x")
    mapdl.run("*vget,my_res(1,2),node,1,u,y")
    mapdl.run("*vget,my_res(1,3),node,1,u,z")
    mapdl.run("*voper,my_res(1,4),my_res(1,1),dot,my_res(1,1)")
    mapdl.run("*vfun,my_res(1,4),sqrt,my_res(1,4)")  # total deformation
    with mapdl.non_interactive:
        mapdl.run("*do,i,1,num_def_outputs")
        mapdl.run("*vmask,my_res(1,4+i)")
        mapdl.run("*vscfun,my_res_mean(i,1),mean,my_res(1,1)")
        mapdl.run("*vmask,my_res(1,4+i)")
        mapdl.run("*vscfun,my_res_mean(i,2),mean,my_res(1,2)")
        mapdl.run("*vmask,my_res(1,4+i)")
        mapdl.run("*vscfun,my_res_mean(i,3),mean,my_res(1,3)")
        mapdl.run("*vmask,my_res(1,4+i)")
        mapdl.run("*vscfun,my_res_mean(i,4),mean,my_res(1,4)")
        mapdl.run("*enddo")

    # get mean deformation values from mapdl arrays
    my_res_mean = mapdl.parameters["my_res_mean"]
    my_res_mean_x = my_res_mean[:, 0]  # my_res_mean_x[0] = x value for my_def1 ; my_res_mean_x[1] = x value for my_def2
    #mean_x = statistics.mean(my_res_mean_x)
    my_selection = my_res_mean[0, 0]
    #print(my_selection)
    #print('my_select=', my_res_mean_x_select)
    #print(my_res_mean_x)
    my_res_mean_y = my_res_mean[:, 1]  # my_res_mean_y[0] = y value for my_def1
    my_res_mean_z = my_res_mean[:, 2]  # my_res_mean_z[0] = z value for my_def1
    my_res_mean_tot = my_res_mean[:, 3]  # my_res_mean_tot[0] = total value for my_def1

    # do calculation of new temperature input using matlab (here: dummy)
    new_temp = start_temp + (my_selection * 1e6)

    # redefine temperature bc table and apply at my_temp
    mapdl.run("start_time=end_time")
    mapdl.run("end_time=start_time+time_inc")
    mapdl.run("start_temp=new_temp")
    mapdl.run("new_temp={}".format(new_temp))
    mapdl.run("*SET,my_temp_table(1,0),start_time,end_time")
    mapdl.run("*SET,my_temp_table(1,1),start_temp,new_temp")
    mapdl.d("my_temp", "temp", "%my_temp_table%")
    
mapdl.save("file","db")
mapdl.exit()

# copy result file from working directory to root directory
import shutil
shutil.copyfile(os.path.join(os.getcwd(),"workingDir","file.rst"),os.path.join(os.getcwd(),"file.rst"))