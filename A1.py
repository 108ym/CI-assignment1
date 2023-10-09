import numpy as np
from skfuzzy import control as ctrl
from skfuzzy import membership as mf
import matplotlib.pyplot as plt

visibility = ctrl.Antecedent(np.arange(0, 2500, 1), 'visibility')
time_of_day = ctrl.Antecedent(np.arange(0, 24, 0.1), 'time_of_day')
brightness = ctrl.Consequent(np.arange(0, 18000, 1), 'brightness')
color_temp = ctrl.Consequent(np.arange(0, 6500, 1), 'color_temp')


visibility['very_poor'] = mf.trimf(visibility.universe, [0, 0, 60])
visibility['poor'] = mf.trimf(visibility.universe, [50, 150, 250])
visibility['moderate'] = mf.trimf(visibility.universe, [150, 350, 550])
visibility['clear'] = mf.trimf(visibility.universe, [500, 1250, 2000])
visibility['excellent'] = mf.trapmf(visibility.universe, [1800, 2200, 2500, 2500])

visibility.view()

time_of_day['midnight'] = mf.trimf(time_of_day.universe, [0, 0, 7])
time_of_day['dawn'] = mf.trimf(time_of_day.universe, [5, 6.5, 8])
time_of_day['day'] = mf.trimf(time_of_day.universe, [6.5, 12.5, 18])
time_of_day['dusk'] = mf.trimf(time_of_day.universe, [17, 18.5, 20])
time_of_day['night'] = mf.trapmf(time_of_day.universe, [18.5, 20.5, 24, 24])

time_of_day.view()


brightness['no'] = mf.trimf(brightness.universe, [0, 0, 2])
brightness['low'] = mf.trimf(brightness.universe, [10, 1300, 2800])
brightness['medium'] = mf.trimf(brightness.universe, [2500, 4000, 5500])
brightness['high'] = mf.trimf(brightness.universe, [4000, 6000, 8000])
brightness['higher'] = mf.trapmf(brightness.universe, [7000, 12000, 18000,18000])

brightness.view()

color_temp['soft_white'] = mf.trimf(color_temp.universe, [0, 0, 2800])
color_temp['warm_white'] = mf.trimf(color_temp.universe, [2700, 3000, 3300])
color_temp['natural_white'] = mf.trimf(color_temp.universe, [3200, 3700, 4200])
color_temp['daylight_white'] = mf.trapmf(color_temp.universe, [4100, 5000, 6500,6500])

color_temp.view()
plt.show()


