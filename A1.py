import numpy as np
from skfuzzy import control as ctrl
from skfuzzy import membership as mf
import matplotlib.pyplot as plt

# Initialise fuzzy variables
ambient_light = ctrl.Antecedent(np.arange(0, 200, 0.1), 'ambient light')
distance = ctrl.Antecedent(np.arange(0, 110, 0.1), 'distance')
traffic_activity = ctrl.Antecedent(np.arange(0, 900, 1), 'traffic activity')
pedestrian_activity = ctrl.Antecedent(np.arange(0, 500, 1), 'pedestrian activity')
visibility = ctrl.Antecedent(np.arange(0, 2500, 1), 'visibility')
time_of_day = ctrl.Antecedent(np.arange(0, 24, 0.1), 'time of day')
brightness = ctrl.Consequent(np.arange(0, 18000, 1), 'brightness')
color_temp = ctrl.Consequent(np.arange(0, 6500, 1), 'color temp')

# Create fuzzy sets/membership functions 
ambient_light['very dark'] = mf.trimf(ambient_light.universe, [0, 10, 20]) #candlelight lit room
ambient_light['dark'] = mf.trimf(ambient_light.universe, [10, 20, 30]) #room lit by a device screen
ambient_light['moderate'] = mf.trimf(ambient_light.universe, [20, 85, 150]) #room with curtains drawn on a cloudy day
ambient_light['bright'] = mf.trimf(ambient_light.universe, [100, 150, 200]) #well-lit indoor enviroment that provides decent visibility
ambient_light['very bright'] = mf.trapmf(ambient_light.universe, [150, 175, 200, 200]) #bright (office lighting)
ambient_light.view()

# Distance from the street lamp (meters)
distance['very close'] = mf.trimf(distance.universe, [0, 0, 10])
distance['close'] = mf.trimf(distance.universe, [5, 13, 20]) 
distance['moderate'] = mf.trimf(distance.universe, [15, 32, 50])
distance['far'] = mf.trimf(distance.universe, [40, 70, 100])
distance['very far'] = mf.trapmf(distance.universe, [80, 100, 110, 110])
distance.view()

# Traffic Activity per hour
traffic_activity['light'] = mf.trimf(traffic_activity.universe, [0, 200, 400])
traffic_activity['moderate'] = mf.trimf(traffic_activity.universe, [200, 400, 600])
traffic_activity['heavy'] = mf.trapmf(traffic_activity.universe, [500, 700, 900, 900])
traffic_activity.view()

# Pedestrian Activity per hour
pedestrian_activity['light'] = mf.trimf(pedestrian_activity.universe, [0, 0, 100])
pedestrian_activity['moderate'] = mf.trimf(pedestrian_activity.universe, [50, 150, 250])
pedestrian_activity['heavy'] = mf.trimf(pedestrian_activity.universe, [200, 500, 500]) # why?
pedestrian_activity.view()

# Visibility
visibility['very_poor'] = mf.trimf(visibility.universe, [0, 25, 100])
visibility['poor'] = mf.trimf(visibility.universe, [50, 125, 350])
visibility['moderate'] = mf.trimf(visibility.universe, [300, 750, 1200])
visibility['clear'] = mf.trimf(visibility.universe, [1000, 1750, 2300])
visibility['excellent'] = mf.trapmf(visibility.universe, [2100, 2300, 2500, 2500])
visibility.view()

# Time of Day
time_of_day['midnight'] = mf.trimf(time_of_day.universe, [0, 1, 4])
time_of_day['dawn'] = mf.trimf(time_of_day.universe, [3, 5.5, 7])
time_of_day['day'] = mf.trimf(time_of_day.universe, [6, 13, 18])
time_of_day['dusk'] = mf.trimf(time_of_day.universe, [17, 19, 21])
time_of_day['night'] = mf.trapmf(time_of_day.universe, [20, 21, 24, 24])
time_of_day.view()

# LED Brightness
brightness['lower'] = mf.trimf(brightness.universe, [0, 1000, 3500])
brightness['low'] = mf.trimf(brightness.universe, [2000, 5000, 8000])
brightness['medium'] = mf.trimf(brightness.universe, [7000, 9500, 12000])
brightness['high'] = mf.trimf(brightness.universe, [11000, 13500, 16000])
brightness['higher'] = mf.trapmf(brightness.universe, [15000, 16500, 18000, 18000])
brightness.view()

# Color Temperature
color_temp['warm glow'] = mf.trimf(color_temp.universe, [0, 1000, 2700])
color_temp['warm white'] = mf.trimf(color_temp.universe, [2500, 3000, 4000])
color_temp['neutral white'] = mf.trimf(color_temp.universe, [3800, 4000, 5200])
color_temp['daylight white'] = mf.trapmf(color_temp.universe, [5000, 5700, 6500, 6500])
color_temp.view()

# plt.show()

# Define fuzzy rules (Include only the 18 most frequently occurring scenarios)

# Morning Commute on Main Roads:
rule1 = ctrl.Rule(ambient_light['dark'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule2 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule3 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule4 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule5 = ctrl.Rule(ambient_light['dark'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule6 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule7 = ctrl.Rule(ambient_light['dark'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule8 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule9 = ctrl.Rule(ambient_light['dark'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule10 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule11 = ctrl.Rule(ambient_light['dark'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule12 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule13 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule14 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule15 = ctrl.Rule(ambient_light['dark'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule16 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule17 = ctrl.Rule(ambient_light['dark'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule18 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule19 = ctrl.Rule(ambient_light['dark'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule20 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule21 = ctrl.Rule(ambient_light['dark'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule22 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule23 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule24 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule25 = ctrl.Rule(ambient_light['dark'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule26 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule27 = ctrl.Rule(ambient_light['dark'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule28 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule29 = ctrl.Rule(ambient_light['dark'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule30 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule31 = ctrl.Rule(ambient_light['dark'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule32 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule33 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule34 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule35 = ctrl.Rule(ambient_light['dark'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule36 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule37 = ctrl.Rule(ambient_light['dark'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule38 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule39 = ctrl.Rule(ambient_light['dark'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule40 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule41 = ctrl.Rule(ambient_light['dark'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule42 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule43 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule44 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule45 = ctrl.Rule(ambient_light['dark'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule46 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule47 = ctrl.Rule(ambient_light['dark'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule48 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule49 = ctrl.Rule(ambient_light['dark'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule50 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule51 = ctrl.Rule(ambient_light['dark'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule52 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule53 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule54 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule55 = ctrl.Rule(ambient_light['dark'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule56 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule57 = ctrl.Rule(ambient_light['dark'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule58 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule59 = ctrl.Rule(ambient_light['dark'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule60 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['moderate'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule61 = ctrl.Rule(ambient_light['dark'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule62 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule63 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule64 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule65 = ctrl.Rule(ambient_light['dark'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule66 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule67 = ctrl.Rule(ambient_light['dark'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule68 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule69 = ctrl.Rule(ambient_light['dark'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule70 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule71 = ctrl.Rule(ambient_light['dark'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule72 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule73 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule74 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule75 = ctrl.Rule(ambient_light['dark'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule76 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule77 = ctrl.Rule(ambient_light['dark'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule78 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule79 = ctrl.Rule(ambient_light['dark'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule80 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))

# School Zone at the Start of School Day:
rule81 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule82 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))

# Morning Exercise in Parks:
rule83 = ctrl.Rule(ambient_light['low'] & distance['very close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule84 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule85 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule86 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule87 = ctrl.Rule(ambient_light['low'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule88 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule89 = ctrl.Rule(ambient_light['low'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule90 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule91 = ctrl.Rule(ambient_light['low'] & distance['very far'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule92 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule93 = ctrl.Rule(ambient_light['low'] & distance['very close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule94 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule95 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule96 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule97 = ctrl.Rule(ambient_light['low'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule98 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule99 = ctrl.Rule(ambient_light['low'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule100 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule101 = ctrl.Rule(ambient_light['low'] & distance['very far'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule102 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule103 = ctrl.Rule(ambient_light['low'] & distance['very close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule104 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule105 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule106 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule107 = ctrl.Rule(ambient_light['low'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule108 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule109 = ctrl.Rule(ambient_light['low'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule110 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule111 = ctrl.Rule(ambient_light['low'] & distance['very far'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule112 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule113 = ctrl.Rule(ambient_light['low'] & distance['very close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule114 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule115 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule116 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule117 = ctrl.Rule(ambient_light['low'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule118 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule119 = ctrl.Rule(ambient_light['low'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule120 = ctrl.Rule(ambient_light['moderate'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule121 = ctrl.Rule(ambient_light['low'] & distance['very far'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule122 = ctrl.Rule(ambient_light['moderate'] & distance['very far'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))

# Morning Market or Street Vendor Area (some conditions is covered by previous scenarios): 
rule123 = ctrl.Rule(ambient_light['low'] & distance['very close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule124 = ctrl.Rule(ambient_light['moderate'] & distance['very close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule125 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule126 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule127 = ctrl.Rule(ambient_light['low'] & distance['moderate'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule128 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))

# Morning Delivery and Commercial Loading Zones (some conditions is covered by previous scenarios):
rule129 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule130 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule131 = ctrl.Rule(ambient_light['low'] & distance['moderate'] & traffic_activity['moderate'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))
rule132 = ctrl.Rule(ambient_light['moderate'] & distance['moderate'] & traffic_activity['moderate'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['medium'], color_temp['neutral white']))

# Outdoor Train or Bus Stations:
rule133 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule134 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['medium'], color_temp['neutral white']))
rule135 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule136 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule137 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule138 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule139 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule140 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dawn'], (brightness['high'], color_temp['neutral white']))
rule141 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule142 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule143 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))
rule144 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['day'], (brightness['high'], color_temp['neutral white']))

# Urban Residential Street at Night:
rule145 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['night'], (brightness['medium'], color_temp['warm white']))

# Urban Main Road During Evening Rush Hour:
rule146 = ctrl.Rule(ambient_light['bright'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dusk'], (brightness['high'], color_temp['neutral white']))
rule147 = ctrl.Rule(ambient_light['bright'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['dusk'], (brightness['high'], color_temp['neutral white']))
rule148 = ctrl.Rule(ambient_light['bright'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dusk'], (brightness['high'], color_temp['neutral white']))
rule149 = ctrl.Rule(ambient_light['bright'] & distance['moderate'] & traffic_activity['heavy'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['dusk'], (brightness['high'], color_temp['neutral white']))

# Commercial District During Evening Shopping:
rule150 = ctrl.Rule(ambient_light['bright'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dusk'], (brightness['high'], color_temp['neutral white']))

# City Park Pathway at Night:
rule151 = ctrl.Rule(ambient_light['dark'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['night'], (brightness['high'], color_temp['warm white']))

# Busy Urban Intersection at Night:
rule152 = ctrl.Rule(ambient_light['very bright'] & distance['close'] & traffic_activity['heavy'] & pedestrian_activity['heavy'] & visibility['excellent'] & time_of_day['night'], (brightness['high'], color_temp['neutral white']))

# Suburban Residential Street at Dusk:
rule153 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['dusk'], (brightness['medium'], color_temp['warm white']))

# Highway Exit Ramp at Night:
rule154 = ctrl.Rule(ambient_light['bright'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['night'], (brightness['medium'], color_temp['neutral white']))
rule155 = ctrl.Rule(ambient_light['bright'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['night'], (brightness['medium'], color_temp['neutral white']))
rule156 = ctrl.Rule(ambient_light['bright'] & distance['far'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['night'], (brightness['medium'], color_temp['neutral white']))
rule154 = ctrl.Rule(ambient_light['bright'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['night'], (brightness['high'], color_temp['neutral white']))
rule155 = ctrl.Rule(ambient_light['bright'] & distance['moderate'] & traffic_activity['moderate'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['night'], (brightness['high'], color_temp['neutral white']))
rule156 = ctrl.Rule(ambient_light['bright'] & distance['far'] & traffic_activity['moderate'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['night'], (brightness['high'], color_temp['neutral white']))

# Pedestrian Bridge at Night:
rule157 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['good'] & time_of_day['night'], (brightness['medium'], color_temp['neutral white']))
rule158 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['good'] & time_of_day['night'], (brightness['medium'], color_temp['warm white']))

# City Square or Plaza During Evening Events:
rule159 = ctrl.Rule(ambient_light['bright'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dusk'], (brightness['high'], color_temp['neutral white']))
rule160 = ctrl.Rule(ambient_light['bright'] & distance['close'] & traffic_activity['moderate'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dusk'], (brightness['high'], color_temp['neutral white']))

# Residential Cul-de-Sac at Night:
rule161 = ctrl.Rule(ambient_light['low'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['night'], (brightness['medium'], color_temp['warm white']))
rule162 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['moderate'] & time_of_day['night'], (brightness['low'], color_temp['warm white']))

# Outdoor Dining Area in the Evening:
rule163 = ctrl.Rule(ambient_light['moderate'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['good'] & time_of_day['dusk'], (brightness['high'], color_temp['neutral white']))

# Sports Field Lighting at Night:
rule164 = ctrl.Rule(ambient_light['very bright'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['execellent'] & time_of_day['dusk'], (brightness['low'], color_temp['daylight white']))
rule165 = ctrl.Rule(ambient_light['very bright'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['execellent'] & time_of_day['dusk'], (brightness['low'], color_temp['daylight white']))
rule166 = ctrl.Rule(ambient_light['very bright'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['execellent'] & time_of_day['dusk'], (brightness['medium'], color_temp['daylight white']))
rule167 = ctrl.Rule(ambient_light['very bright'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['execellent'] & time_of_day['dusk'], (brightness['medium'], color_temp['daylight white']))
rule168 = ctrl.Rule(ambient_light['very bright'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['execellent'] & time_of_day['dusk'], (brightness['high'], color_temp['daylight white']))
rule169 = ctrl.Rule(ambient_light['very bright'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['execellent'] & time_of_day['dusk'], (brightness['high'], color_temp['daylight white']))
rule170 = ctrl.Rule(ambient_light['very bright'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['execellent'] & time_of_day['night'], (brightness['light'], color_temp['daylight white']))
rule171 = ctrl.Rule(ambient_light['very bright'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['light'] & visibility['execellent'] & time_of_day['night'], (brightness['light'], color_temp['daylight white']))
rule172 = ctrl.Rule(ambient_light['very bright'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['execellent'] & time_of_day['night'], (brightness['medium'], color_temp['daylight white']))
rule173 = ctrl.Rule(ambient_light['very bright'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['moderate'] & visibility['execellent'] & time_of_day['night'], (brightness['medium'], color_temp['daylight white']))
rule174 = ctrl.Rule(ambient_light['very bright'] & distance['close'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['execellent'] & time_of_day['night'], (brightness['high'], color_temp['daylight white']))
rule175 = ctrl.Rule(ambient_light['very bright'] & distance['moderate'] & traffic_activity['light'] & pedestrian_activity['heavy'] & visibility['execellent'] & time_of_day['night'], (brightness['high'], color_temp['daylight white']))


rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15,
         rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,rule28, rule29, rule30,
         rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45,
         rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
         rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72, rule73, rule74, rule75, 
         rule76, rule77, rule77, rule78, rule79, rule80, rule81, rule82, rule83, rule84, rule85, rule86, rule87, rule88, rule89, rule90,
         rule91, rule92, rule93, rule94, rule95, rule96, rule97, rule98, rule99, rule100, rule101, rule102, rule103, rule104, rule105,
         rule106, rule107, rule108, rule109, rule110, rule111, rule112, rule113, rule114, rule115, rule116, rule117, rule118,
         rule119, rule120, rule121, rule122, rule123, rule124, rule125, rule126, rule127, rule128, rule129, rule130, rule131, rule132,
         rule133, rule134, rule135, rule136, rule137, rule138, rule139, rule140, rule141, rule142, rule143, rule144, rule145, rule146,
         rule147, rule148, rule149, rule150, rule151, rule152, rule153, rule154, rule155, rule156, rule157, rule158, rule159, rule160,
         rule161, rule162, rule163, rule164, rule165, rule166, rule167, rule168, rule169, rule170, rule171, rule172, rule173, rule174, 
         rule175]






