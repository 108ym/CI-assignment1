import numpy as np
from skfuzzy import control as ctrl
from skfuzzy import membership as mf
import matplotlib.pyplot as plt

#initialise fuzzy variables
ambient_light = ctrl.Antecedent(np.arange(0, 200, 0.1), 'ambient_light')
motion = ctrl.Antecedent(np.arange(0, 10, 0.1), 'motion')
traffic_activity = ctrl.Antecedent(np.arange(0, 900, 1), 'traffic_activity')
pedestrian_activity = ctrl.Antecedent(np.arange(0, 500, 1), 'pedestrian_activity')
visibility = ctrl.Antecedent(np.arange(0, 2500, 1), 'visibility')
time_of_day = ctrl.Antecedent(np.arange(0, 24, 0.1), 'time_of_day')
brightness = ctrl.Consequent(np.arange(0, 18000, 1), 'brightness')
color_temp = ctrl.Consequent(np.arange(0, 6500, 1), 'color_temp')

#create fuzzy sets/membership functions 
ambient_light['very dark'] = mf.trimf(ambient_light.universe, [0, 10, 20]) #candlelight lit room
ambient_light['dark'] = mf.trimf(ambient_light.universe, [10, 20, 30]) #room lit by a device screen
ambient_light['moderate'] = mf.trimf(ambient_light.universe, [20, 85, 150]) #room with curtains drawn on a cloudy day
ambient_light['bright'] = mf.trimf(ambient_light.universe, [100, 150, 200]) #well-lit indoor enviroment that provides decent visibility
ambient_light['very bright'] = mf.trapmf(ambient_light.universe, [150, 175, 200, 200]) #bright (office lighting)
ambient_light.view()

# Motion
motion['yes'] = mf.trapmf(motion.universe, [0, 0, 8, 10])
motion['no'] = mf.trimf(motion.universe, [8, 10, 10]) #distance beyond the detection of sensor
motion.view()

# Traffic Activity per hour
traffic_activity['light'] = mf.trimf(traffic_activity.universe, [0, 200, 400])
traffic_activity['moderate'] = mf.trimf(traffic_activity.universe, [200, 400, 600])
traffic_activity['heavy'] = mf.trapmf(traffic_activity.universe, [500, 700, 900, 900])
traffic_activity.view()

# Pedestrian Activity per hour
pedestrian_activity['light'] = mf.trimf(pedestrian_activity.universe, [0, 0, 100])
pedestrian_activity['moderate'] = mf.trimf(pedestrian_activity.universe, [50, 150, 250])
pedestrian_activity['heavy'] = mf.trimf(pedestrian_activity.universe, [200, 500, 500])
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
color_temp['warm_glow'] = mf.trimf(color_temp.universe, [0, 1000, 2700])
color_temp['warm_white'] = mf.trimf(color_temp.universe, [2500, 3000, 4000])
color_temp['neutral_white'] = mf.trimf(color_temp.universe, [3800, 4000, 5200])
color_temp['daylight_white'] = mf.trapmf(color_temp.universe, [5000, 5700, 6500, 6500])
color_temp.view()

plt.show()


