import math
# Catalog
d_screw_center = 25  # in catalog Bosch is Nominal diameter 25x10Rx3-4
d_screw_down = 24
d_nut = 40
d_Flang = 63
L_Flang = 12
L_lenght_Nut = 108
Initial_L = 0.000003948  #  3.948 [µm]
Mass_Table = 100  # Unit in kg
Pitch = 10  # lead
D_ball = 3  # ball diameter
i = 4  # number of ball track turns
Ca = 0.309  # Distance center for profile radius up and down
Cr = 0.368  # Distance center for profile radius left and right
Coeffradius_Profil_right = 0.52745  # This value is from the book from Spieß page 105, and is the mean value from left and right
Standrd_x = 4  # this value is from ISO DIN 6195
Standrd_y = 35  # this value is from ISO DIN 6195 but this value is diameter and must be calculated

# Fluid
Initial_T0 = 25  # °C
Initial_k = 40  # or 36-43   34.4
Initial_Cp = 448
Initial_ThermalConductivity = 45  # Thermal conductivity
Initial_SpecificHeat = 477  # Specific Heat rate
Initial_CTE = 15E-6  # Thermal expansion rate
Initial_thermalVal = 25
Initial_K_air = 0.026
Initial_Density_air = 1.1455
Initial_HeatCapacity_air = 1.005e3

# Geometry calculation
d_screw_up = d_screw_center + (d_screw_center - d_screw_down)
Standard_y_Calculation = (Standrd_y - d_screw_up) / 2
Initial_angle = 45  # this variable is for adapting angle
Initial_Ax_Flang = L_Flang  # X coordinate for flange
Initial_Ay_Flang = ((d_Flang - d_screw_up) / 2) - ((d_screw_center - d_screw_down) / 2)  # Y coordinate for flange depend on catalog
Initial_X_ball = (Standrd_x + ((((L_lenght_Nut / 2 + L_Flang) - (2 * Standrd_x)) - ((i - 1) * Pitch)) / 2))  # Z coordinate for center of ball  from left for example 12mm
Initial_Y_ball = 0.5  # Y coordinate for center of ball  for example 0.5mm
Initial_Radius_Profile = (D_ball / 2) + Coeffradius_Profil_right  # Radius for profile
Initial_X_profile1 = (Standrd_x + ((((L_lenght_Nut / 2 + L_Flang) - (2 * Standrd_x)) - ((i - 1) * Pitch)) / 2)) + Ca  # X coordinate for profile  for example 12.501mm in the right direction
Initial_X_profile2 = (Standrd_x + ((((L_lenght_Nut / 2 + L_Flang) - (2 * Standrd_x)) - ((i - 1) * Pitch)) / 2)) - Ca  # X coordinate for profile  for example 11.499mm in the left direction
Initial_Y_profile = Cr + Initial_Y_ball  # Y coordinate for profile for example 1.101mm
Initial_length_Nut_X = (L_lenght_Nut / 2) + L_Flang  # length Nut in X direction
Initial_length_Nut_Y = (d_nut - d_screw_up) / 2  # length Nut in Y direction
Initial_Ax_left = Standrd_x  # X left part
Initial_Ay_left = (Standrd_y - d_screw_up) / 2  # Y left part
Initial_Ax_right = Initial_Ax_left  # X right part
Initial_Ay_right = Initial_Ay_left  # Y right part
Initial_revolutions = i  # Number of revolutions
Initial_meshSize = 0.5  # Mesh size in mm
Initial_ball_storage = 5
Initial_D_nute = d_nut
Initial_d_screw_center = d_screw_center
Initial_d_screw_up = d_screw_up
Initial_D_ball = D_ball
Initial_Pitch = Pitch
Initial_Mass_table = Mass_Table
Initial_lenght_nut = L_lenght_Nut

# Forces / Properties / Stiffness
Initial_Rotation = 1800  # rpm
Initial_F_preload = 1275  # N  preload force
Initial_Density = 7.872  # density
Initial_CE = 0.4643
Initial_CK = 1.75808
Initial_frs = 0.55
Initial_fm = 0.55
Initial_Zt = 23       # This value is from matlab function that fc_stiff is
Initial_Stiffness = 40.64    #1.288e3

########################################## fc_constant_parameter

F_preload = Initial_F_preload
Parameters = {}
Parameters['Geometry'] = {}
Parameters['Geometry']['D_Screw'] = Initial_d_screw_center / 1000  # The unit has been defined meter
Parameters['Geometry']['D_Screw2'] = Initial_d_screw_up / 1000
Parameters['Geometry']['D_Ball'] = Initial_D_ball / 1000  # The unit has been defined meter
Parameters['Geometry']['Pitch'] = Initial_Pitch / 1000  # The unit has been defined meter
Parameters['Geometry']['AngleContact'] = Initial_angle

Parameters['Geometry']['Anglepitch'] = math.degrees(math.atan(Parameters['Geometry']['Pitch'] / (math.pi * Parameters['Geometry']['D_Screw2'])))  # The angle in pitch (degree)
Parameters['Geometry']['LengthNut'] = Initial_lenght_nut / (2 * 1000)  # The unit has been defined meter but for one Nut
Parameters['Geometry']['LenghtHelix'] = (Parameters['Geometry']['LengthNut'] / Parameters['Geometry']['Pitch']) *(math.sqrt(((math.pi * (Parameters['Geometry']['D_Screw']))**2) + (Parameters['Geometry']['Pitch'])**2))
Parameters['Geometry']['BallNumber'] = round(Parameters['Geometry']['LenghtHelix'] / Parameters['Geometry']['D_Ball'])  # The number of balls in one Nut
Parameters['Geometry']['fz'] = 0.7  # This Variable is the "rechnerische Anzahl der tragender Kugeln". Usually 0.7 to 0.95, Quelle: Buch:Das Steifigkeit... von Spieß Seite:34
Parameters['Geometry']['Zt'] = Parameters['Geometry']['fz'] * Parameters['Geometry']['BallNumber']
Parameters['Geometry']['RotationSpeed'] = Initial_Rotation  # The Rotation Speed rpm
Parameters['Geometry']['RoughnessBall'] = 8e-8  # The Roughness ball/s
Parameters['Geometry']['RoughnessScrew'] = 3e-7  # The Roughness screw
Parameters['Geometry']['RoughnessNut'] = 3e-7  # The Roughness nut/s

Parameters['Material'] = {}
Parameters['Material']['ElasticModulusScrew'] = 2.1e11  # The elasticity properties for the screw
Parameters['Material']['ElasticModulusBall'] = 2.1e11  # The elasticity properties for the ball/s
Parameters['Material']['ElasticModulusNut'] = 2.1e11  # The elasticity properties for the nut/s
Parameters['Material']['PoissinModulusScrew'] = 0.3  # The Poisson coefficient for the screw
Parameters['Material']['PoissinModulusBall'] = 0.3  # The Poisson coefficient for the ball/s
Parameters['Material']['PoissinModulusNut'] = 0.3  # The Poisson coefficient for the nut/s
Parameters['Material']['ViskosStatics'] = 68e-6  # The statics viscosity has been defined with a unit  m^2/s
Parameters['Material']['ViskosDynamics'] = 0.05  # The dynamics viscosity
Parameters['Material']['Density'] = Initial_Density  # The density has been defined with unit kg/m^3

Parameters['Constant'] = {}
Parameters['Constant']['G'] = 0.4276  # the dimensionless material
Parameters['Constant']['F_nut_Screw'] = 0.515  # This Variable is the curvature parameters for the screw and nut races. Usually 0.515 to 0.54
Parameters['Constant']['TemperatureInput'] = 25  # The input temperature °C
Parameters['Constant']['TemperatureNew'] = Initial_thermalVal
Parameters['Constant']['RotationalSpeed'] = Parameters['Geometry']['RotationSpeed']
Zt = round(((math.pi * Parameters['Geometry']['D_Screw2']) / ((math.cos(math.radians(Parameters['Geometry']['Anglepitch'])) * Parameters['Geometry']['D_Ball']))) - Initial_ball_storage)
Parameters['Geometry']['Mass_table'] = Initial_Mass_table / (2 * Zt)  # Kg
Parameters['Constant']['Preload1'] = (F_preload) / (math.cos(math.radians(Parameters['Geometry']['Anglepitch'])) * math.sin(math.radians(Parameters['Geometry']['AngleContact'])))
Parameters['Constant']['Preload2'] = (Parameters['Geometry']['Mass_table'] * 9.8) / (math.cos(math.radians(Parameters['Geometry']['Anglepitch'])) * math.sin(math.radians(Parameters['Geometry']['AngleContact'])))
Parameters['Constant']['Preload'] = Parameters['Constant']['Preload1'] + Parameters['Constant']['Preload2']
Parameters['Constant']['friction_a'] = -2.643  # The constant parameter for friction coefficient
Parameters['Constant']['friction_b'] = -0.002  # The constant parameter for friction coefficient
Parameters['Constant']['friction_c'] = 4.983e-7  # The constant parameter for friction coefficient
Parameters['Constant']['Kapa'] = 0.05  # Kapa is a factor used for defining the race curvature radius
Parameters['Constant']['density'] = Initial_Density  # Density for Stainless Steel Material
Parameters['Constant']['B'] = 1.42  # The parameter B is constant and depends on the roughness of the surfaces in Contacts
Parameters['Constant']['C'] = 0.8  # The parameter C is constant and depends on the roughness of the surfaces in Contacts
Parameters['Constant']['Mu0'] = 0.2  # Article: A new model to estimate friction torque in a ball screw system  Page 341

Parameters['Calculation'] = {}
Parameters['Calculation']['Nut_Rx'] = ((2 / Parameters['Geometry']['D_Ball']) - (2 * math.cos(math.radians(Parameters['Geometry']['AngleContact'])) / (Parameters['Geometry']['D_Screw'] + (Parameters['Geometry']['D_Ball'] * math.cos(math.radians(Parameters['Geometry']['AngleContact'])))))) ** -1
Parameters['Calculation']['Screw_Rx'] = ((2 / Parameters['Geometry']['D_Ball']) + (2 * math.cos(math.radians(Parameters['Geometry']['AngleContact'])) / (Parameters['Geometry']['D_Screw'] - (Parameters['Geometry']['D_Ball'] * math.cos(math.radians(Parameters['Geometry']['AngleContact'])))))) ** -1
Parameters['Calculation']['Nut_Ry'] = (Parameters['Constant']['F_nut_Screw'] * Parameters['Geometry']['D_Ball']) / (2 * Parameters['Constant']['F_nut_Screw'] - 1)
Parameters['Calculation']['Screw_Ry'] = (Parameters['Constant']['F_nut_Screw'] * Parameters['Geometry']['D_Ball']) / (2 * Parameters['Constant']['F_nut_Screw'] - 1)
Parameters['Calculation']['Nut_K'] = Parameters['Calculation']['Nut_Ry'] / Parameters['Calculation']['Nut_Rx']
Parameters['Calculation']['Screw_K'] = Parameters['Calculation']['Screw_Ry'] / Parameters['Calculation']['Screw_Rx']
Parameters['Material']['ElasticModulu_Ball_Nut'] = 2 * (((1 - Parameters['Material']['PoissinModulusBall'] ** 2) / Parameters['Material']['ElasticModulusBall']) + ((1 - Parameters['Material']['PoissinModulusNut'] ** 2) / Parameters['Material']['ElasticModulusNut'])) ** -1
Parameters['Material']['ElasticModulu_Ball_Screw'] = 2 * (((1 - Parameters['Material']['PoissinModulusBall'] ** 2) / Parameters['Material']['ElasticModulusBall']) + ((1 - Parameters['Material']['PoissinModulusScrew'] ** 2) / Parameters['Material']['ElasticModulusScrew'])) ** -1

def rpm_to_rad_per_sec(rpm):
    # Convert RPM to rad/s using the formula: rad/s = (rpm * 2 * pi) / 60
    rad_per_sec = (rpm * 2 * math.pi) / 60
    return rad_per_sec
rotational_speed_rad_per_s = (math.pi *(rpm_to_rad_per_sec(Parameters['Constant']['RotationalSpeed'])))/30
cos_angle_contact = math.cos(math.radians(Parameters['Geometry']['AngleContact']))
Parameters['Calculation']['Speed'] = rotational_speed_rad_per_s * (1 - ((Parameters['Geometry']['D_Ball'] * cos_angle_contact) / Parameters['Geometry']['D_Screw']) ** 2) * (Parameters['Geometry']['D_Screw'] / 4)
Parameters['Calculation']['Nut_Rd'] = (2 * Parameters['Geometry']['D_Ball'] * Parameters['Constant']['F_nut_Screw']) / (2 * Parameters['Constant']['F_nut_Screw'] + 1)
Parameters['Calculation']['Screw_Rd'] = (2 * Parameters['Geometry']['D_Ball'] * Parameters['Constant']['F_nut_Screw']) / (2 * Parameters['Constant']['F_nut_Screw'] + 1)
Parameters['Calculation']['Mass'] = Parameters['Constant']['density'] * (4 / 3) * math.pi * ((Parameters['Geometry']['D_Ball'] / 2) ** 3)
Parameters['Calculation']['Nut_a'] = (1.1552 * Parameters['Calculation']['Nut_Rx'] * Parameters['Calculation']['Nut_K'] ** 0.4676) * (Parameters['Constant']['Preload'] / (Parameters['Material']['ElasticModulu_Ball_Nut'] * Parameters['Calculation']['Nut_Rx'] ** 2)) ** (1 / 3)
Parameters['Calculation']['Screw_a'] = (1.1552 * Parameters['Calculation']['Screw_Rx'] * Parameters['Calculation']['Screw_K'] ** 0.4676) * (Parameters['Constant']['Preload'] / (Parameters['Material']['ElasticModulu_Ball_Screw'] * Parameters['Calculation']['Screw_Rx'] ** 2)) ** (1 / 3)
Parameters['Calculation']['Nut_b'] = (1.1502 * Parameters['Calculation']['Nut_Rx'] * Parameters['Calculation']['Nut_K'] ** (-0.1876)) * (Parameters['Constant']['Preload'] / (Parameters['Material']['ElasticModulu_Ball_Nut'] * Parameters['Calculation']['Nut_Rx'] ** 2)) ** (1 / 3)
Parameters['Calculation']['Screw_b'] = (1.1502 * Parameters['Calculation']['Screw_Rx'] * Parameters['Calculation']['Screw_K'] ** (-0.1876)) * (Parameters['Constant']['Preload'] / (Parameters['Material']['ElasticModulu_Ball_Screw'] * Parameters['Calculation']['Screw_Rx'] ** 2)) ** (1 / 3)
Parameters['Calculation']['Ra'] = (Parameters['Geometry']['D_Ball'] / 2) * ((1 + Parameters['Constant']['Kapa']) / (1 + (Parameters['Constant']['Kapa'] / 2)))
Parameters['Calculation']['Nut_E_Surf'] = ((2 * Parameters['Calculation']['Ra']) / Parameters['Calculation']['Nut_a']) * (Parameters['Geometry']['D_Ball'] * math.sin(math.radians(Parameters['Geometry']['AngleContact'])) / Parameters['Geometry']['D_Screw'])
Parameters['Calculation']['Screw_E_Surf'] = ((2 * Parameters['Calculation']['Ra']) / Parameters['Calculation']['Screw_a']) * (Parameters['Geometry']['D_Ball'] * math.sin(math.radians(Parameters['Geometry']['AngleContact'])) / Parameters['Geometry']['D_Screw'])
Parameters['Calculation']['Nut_fc'] = 1.0026 - 0.1653 * Parameters['Calculation']['Nut_E_Surf'] - 0.2638 * Parameters['Calculation']['Nut_E_Surf'] ** 2 - 2.5521 * Parameters['Calculation']['Nut_E_Surf'] ** 3 + 1.9749 * Parameters['Calculation']['Nut_E_Surf'] ** 4
Parameters['Calculation']['Screw_fc'] = 1.0026 - 0.1653 * Parameters['Calculation']['Screw_E_Surf'] - 0.2638 * Parameters['Calculation']['Screw_E_Surf'] ** 2 - 2.5521 * Parameters['Calculation']['Screw_E_Surf'] ** 3 + 1.9749 * Parameters['Calculation']['Screw_E_Surf'] ** 4
Parameters['Calculation']['Nut_fp'] = 0.0042 + 1.1045 * Parameters['Calculation']['Nut_E_Surf'] + 0.4625 * Parameters['Calculation']['Nut_E_Surf'] ** 2 - 0.5648 * Parameters['Calculation']['Nut_E_Surf'] ** 3
Parameters['Calculation']['Screw_fp'] = 0.0042 + 1.1045 * Parameters['Calculation']['Screw_E_Surf'] + 0.4625 * Parameters['Calculation']['Screw_E_Surf'] ** 2 - 0.5648 * Parameters['Calculation']['Screw_E_Surf'] ** 3
Parameters['Calculation']['frictionCoefficient'] = math.exp(Parameters['Constant']['friction_a'] + (Parameters['Constant']['friction_b'] * Parameters['Geometry']['RotationSpeed']) - (Parameters['Constant']['friction_c'] * Parameters['Geometry']['RotationSpeed'] ** 2))
Parameters['Calculation']['frictionCoefficientMuS'] = 0.11
Parameters['Calculation']['frictionCoefficientMb'] = 0.1
Parameters['Calculation']['loadParameter_New_Nut'] = Parameters['Constant']['Preload'] / (Parameters['Material']['ElasticModulu_Ball_Nut'] * Parameters['Calculation']['Nut_Rx'] ** 2)
Parameters['Calculation']['loadParameter_New_Screw'] = Parameters['Constant']['Preload'] / (Parameters['Material']['ElasticModulu_Ball_Screw'] * Parameters['Calculation']['Screw_Rx'] ** 2)
Parameters['Calculation']['Viscosity_ParameterB'] = 159.6 * math.log((Parameters['Material']['ViskosStatics'] * Parameters['Material']['Density']) / (1.8 * 10**-4))
Parameters['Calculation']['Viscosity_ParameterA'] = Parameters['Material']['ViskosStatics'] * Parameters['Material']['Density'] * math.exp(-Parameters['Calculation']['Viscosity_ParameterB'] / 135)
Parameters['Calculation']['ViscosityNew'] = (Parameters['Calculation']['Viscosity_ParameterA'] * math.exp(Parameters['Calculation']['Viscosity_ParameterB'] / (Parameters['Constant']['TemperatureNew'] + 95))) / Parameters['Material']['Density']
Parameters['Calculation']['SpeedParameter_New_Nut'] = (Parameters['Calculation']['ViscosityNew'] * Parameters['Calculation']['Speed']) / (Parameters['Material']['ElasticModulu_Ball_Nut'] * Parameters['Calculation']['Nut_Rx'])
Parameters['Calculation']['SpeedParameter_New_Screw'] = (Parameters['Calculation']['ViscosityNew'] * Parameters['Calculation']['Speed']) / (Parameters['Material']['ElasticModulu_Ball_Screw'] * Parameters['Calculation']['Screw_Rx'])
Parameters['Calculation']['Nut_h'] = 3.63 * Parameters['Calculation']['Nut_Rx'] * Parameters['Calculation']['SpeedParameter_New_Nut'] ** 0.66 * Parameters['Constant']['G'] ** 0.49 * Parameters['Calculation']['loadParameter_New_Nut'] ** -0.073 * (1 - math.exp(-0.68 * Parameters['Calculation']['Nut_a'] / Parameters['Calculation']['Nut_b']))
Parameters['Calculation']['Screw_h'] = 3.63 * Parameters['Calculation']['Screw_Rx'] * Parameters['Calculation']['SpeedParameter_New_Screw'] ** 0.66 * Parameters['Constant']['G'] ** 0.49 * Parameters['Calculation']['loadParameter_New_Screw'] ** -0.073 * (1 - math.exp(-0.68 * Parameters['Calculation']['Screw_a'] / Parameters['Calculation']['Screw_b']))
Parameters['Calculation']['Lambda_Nut'] = Parameters['Calculation']['Nut_h'] / math.sqrt(Parameters['Geometry']['RoughnessBall']**2 + Parameters['Geometry']['RoughnessNut']**2)
Parameters['Calculation']['Lambda_Screw'] = Parameters['Calculation']['Screw_h'] / math.sqrt(Parameters['Geometry']['RoughnessBall']**2 + Parameters['Geometry']['RoughnessScrew']**2)


Forces = {}
Forces['FB'] = 1 / Parameters['Geometry']['BallNumber']
Forces['FR_Nut'] = 2.86 * (Parameters['Material']['ElasticModulu_Ball_Nut']) * (Parameters['Calculation']['Nut_Rx'] ** 2) * (Parameters['Calculation']['Nut_K'] ** 0.348) * (Parameters['Constant']['G'] ** 0.022) * (Parameters['Calculation']['SpeedParameter_New_Nut'] ** 0.66) * (Parameters['Calculation']['loadParameter_New_Nut'] ** 0.47)
Forces['FR_Screw'] = 2.86 * (Parameters['Material']['ElasticModulu_Ball_Screw']) * (Parameters['Calculation']['Screw_Rx'] ** 2) * (Parameters['Calculation']['Screw_K'] ** 0.348) * (Parameters['Constant']['G'] ** 0.022) * (Parameters['Calculation']['SpeedParameter_New_Screw'] ** 0.66) * (Parameters['Calculation']['loadParameter_New_Screw'] ** 0.47)
Forces['FP_Nut'] = 2 * (Forces['FR_Nut']) * (1 + ((Parameters['Geometry']['D_Ball'] * math.cos(math.radians(Parameters['Geometry']['AngleContact']))) / Parameters['Geometry']['D_Screw']))
Forces['FP_Screw'] = 2 * (Forces['FR_Screw']) * (1 - ((Parameters['Geometry']['D_Ball'] * math.cos(math.radians(Parameters['Geometry']['AngleContact']))) / Parameters['Geometry']['D_Screw']))

Torque = {}
Torque['MC_Nut'] = 0.0806 * Parameters['Calculation']['frictionCoefficient'] * Parameters['Constant']['Preload'] * (Parameters['Calculation']['Nut_a']**2 / Parameters['Calculation']['Ra']) * Parameters['Calculation']['Nut_fc']
Torque['MC_Screw'] = 0.0806 * Parameters['Calculation']['frictionCoefficient'] * Parameters['Constant']['Preload'] * (Parameters['Calculation']['Screw_a']**2 / Parameters['Calculation']['Ra']) * Parameters['Calculation']['Screw_fc']
Torque['MP_Nut'] = (3/8) * Parameters['Calculation']['frictionCoefficient'] * Parameters['Constant']['Preload'] * Parameters['Calculation']['Nut_a'] * Parameters['Calculation']['Nut_fp']
Torque['MP_Screw'] = (3/8) * Parameters['Calculation']['frictionCoefficient'] * Parameters['Constant']['Preload'] * Parameters['Calculation']['Screw_a'] * Parameters['Calculation']['Screw_fp']
Torque['MER_Nut'] = 7.48e-7 * (Parameters['Geometry']['D_Ball'] / 2)**0.33 * Parameters['Constant']['Preload']**1.33 * (1 - 3.519e-36 * (Parameters['Calculation']['Nut_K'] - 1)**0.806 * (Parameters['Calculation']['frictionCoefficientMuS'] / 0.11))
Torque['MER_Screw'] = 7.48e-7 * (Parameters['Geometry']['D_Ball'] / 2)**0.33 * Parameters['Constant']['Preload']**1.33 * (1 - 3.519e-36 * (Parameters['Calculation']['Screw_K'] - 1)**0.806 * (Parameters['Calculation']['frictionCoefficientMuS'] / 0.11))
Torque['MB'] = Parameters['Calculation']['frictionCoefficientMb'] * (Parameters['Geometry']['D_Ball'] / 2) * Forces['FB']


# The total tangential force between a ball and the screw FS is the algebraic sum of the tangential contact forces in the rolling direction as FS = FRs + FSs.
# Article: A new model to estimate friction torque in a ball screw system

Fricrion = {}
Fricrion['force_FS'] = (
    (Torque['MC_Nut'] + Torque['MC_Screw'] + Torque['MER_Nut'] + Torque['MER_Screw'] + Torque['MB']) / Parameters['Geometry']['D_Ball'] +
    (Forces['FR_Nut'] + Forces['FR_Screw']) +
    ((Forces['FR_Nut'] + Forces['FR_Screw']) * Parameters['Geometry']['D_Ball'] * math.cos(math.radians(Parameters['Geometry']['AngleContact'])) / Parameters['Geometry']['D_Screw']) +
    Forces['FB'] / 2
)
# The total tangential force between a ball and the Nut FN is the algebraic sum of the tangential contact forces in the rolling direction as FN = FRn + FSn.
# Article: A new model to estimate friction torque in a ball screw system


Fricrion['force_FN'] = (
    (Torque['MC_Nut'] + Torque['MC_Screw'] + Torque['MER_Nut'] + Torque['MER_Screw'] + Torque['MB']) / Parameters['Geometry']['D_Ball'] +
    (Forces['FR_Nut'] + Forces['FR_Screw']) -
    ((Forces['FR_Nut'] + Forces['FR_Screw']) * Parameters['Geometry']['D_Ball'] * math.cos(math.radians(Parameters['Geometry']['AngleContact'])) / Parameters['Geometry']['D_Screw']) -
    Forces['FB'] / 2
)
#Rs is the radius of the ball-screw contact
Fricrion['Radius_Screw'] = (Parameters['Geometry']['D_Screw'] / 2) - (Parameters['Geometry']['D_Ball'] * math.cos(math.radians(Parameters['Geometry']['AngleContact'])) / 2)

# Rn is the radius of the ball-screw contact
Fricrion['Radius_Nut'] = (Parameters['Geometry']['D_Screw'] / 2) + (Parameters['Geometry']['D_Ball'] * math.cos(math.radians(Parameters['Geometry']['AngleContact'])) / 2)

# %% The friction torque generated by a ball Screw
Fricrion['Torque_Screw'] = Fricrion['force_FS'] * Fricrion['Radius_Screw']

#%% The friction torque generated by a ball Nut
Fricrion['Torque_Nut'] = Fricrion['force_FN'] * Fricrion['Radius_Nut']
#%% For a number of z loaded balls, the total friction torque acting on the screw is obtained by summing all friction torques in the ball-screw contacts
Fricrion['All_Torque_screw'] = Parameters['Geometry']['BallNumber'] * Fricrion['Torque_Screw']
# %% For a number of z loaded balls, the total friction torque acting on the nut is obtained by summing all friction torques in the ball-nut contacts
Fricrion['All_Torque_Nut'] = Parameters['Geometry']['BallNumber'] * Fricrion['Torque_Nut']
#%% For a number of z loaded balls, the total friction force acting on the screw is obtained by summing all friction force in the ball-screw contacts
Fricrion['All_Force_screw'] = Parameters['Geometry']['BallNumber'] * Fricrion['force_FS']
#%% For a number of z loaded balls, the total friction force acting on the nut is obtained by summing all friction force in the ball-nut contacts
Fricrion['All_Force_Nut'] = Parameters['Geometry']['BallNumber'] * Fricrion['force_FN']
##########################################
#########################################   Thermal
Parameters['Calculation']['speed_Nut'] = (Parameters['Geometry']['RotationSpeed'] * (Parameters['Geometry']['Pitch'] * 1000)) / 60
#%speed_Nut = 300;    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#%Weg = 400;          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

q_nut = (1000 * Fricrion['Torque_Nut'] / (math.pi * Parameters['Calculation']['Nut_a'] * Parameters['Calculation']['Nut_b'])) * (Parameters['Calculation']['speed_Nut'] / 1000)  # Watt
ee = Parameters['Calculation']['Nut_a'] / Parameters['Calculation']['Nut_b']
se = (16 * ee**1.75) / ((3 + ee**0.75) * (1 + 3 * ee**0.75))
# % k = 34.3;   % or 36-43
# % Cp = 448;
Alpha_Kappa = Initial_k / (Initial_Cp * Parameters['Constant']['density'])
pe = ((Parameters['Calculation']['speed_Nut'] / 1000) * Parameters['Calculation']['Nut_b']) / (2 * Alpha_Kappa)
T_max = (2 * q_nut * Parameters['Calculation']['Nut_a']) / (Initial_k * (math.sqrt(math.pi * (1.273 * se + pe))))


print(T_max)

a = (Initial_Stiffness*Initial_revolutions)**2
print(a)

new_Preload= math.sqrt((Initial_L)**3*((Initial_Stiffness*Initial_revolutions)**2))*10e8
print(new_Preload)
