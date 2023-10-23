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
colour_temp = ctrl.Consequent(np.arange(0, 6500, 1), 'colour temperature')

# Create fuzzy sets/membership functions 
ambient_light['very dark'] = mf.trimf(ambient_light.universe, [0, 10, 20]) #candlelight lit room
ambient_light['dark'] = mf.trimf(ambient_light.universe, [10, 20, 30]) #room lit by a device screen
ambient_light['moderate'] = mf.trimf(ambient_light.universe, [20, 85, 150]) #room with curtains drawn on a cloudy day
ambient_light['bright'] = mf.trimf(ambient_light.universe, [100, 150, 200]) #well-lit indoor enviroment that provides decent visibility
ambient_light['very bright'] = mf.trapmf(ambient_light.universe, [150, 175, 200, 200]) #bright (office lighting)
# ambient_light.view()

# Distance from the street lamp (meters)
distance['very close'] = mf.trimf(distance.universe, [0, 0, 10])
distance['close'] = mf.trimf(distance.universe, [5, 13, 20]) 
distance['moderate'] = mf.trimf(distance.universe, [15, 32, 50])
distance['far'] = mf.trimf(distance.universe, [40, 70, 100])
distance['very far'] = mf.trapmf(distance.universe, [80, 100, 110, 110])
# distance.view()

# Traffic Activity per hour
traffic_activity['light'] = mf.trimf(traffic_activity.universe, [0, 200, 400])
traffic_activity['moderate'] = mf.trimf(traffic_activity.universe, [200, 400, 600])
traffic_activity['heavy'] = mf.trapmf(traffic_activity.universe, [500, 700, 900, 900])
# traffic_activity.view()

# Pedestrian Activity per hour
pedestrian_activity['light'] = mf.trimf(pedestrian_activity.universe, [0, 0, 100])
pedestrian_activity['moderate'] = mf.trimf(pedestrian_activity.universe, [50, 150, 250])
pedestrian_activity['heavy'] = mf.trimf(pedestrian_activity.universe, [200, 500, 500]) # why?
# pedestrian_activity.view()

# Visibility
visibility['very_poor'] = mf.trimf(visibility.universe, [0, 25, 100])
visibility['poor'] = mf.trimf(visibility.universe, [50, 125, 350])
visibility['moderate'] = mf.trimf(visibility.universe, [300, 750, 1200])
visibility['clear'] = mf.trimf(visibility.universe, [1000, 1750, 2300])
visibility['excellent'] = mf.trapmf(visibility.universe, [2100, 2300, 2500, 2500])
# visibility.view()

# Time of Day
time_of_day['midnight'] = mf.trimf(time_of_day.universe, [0, 1, 4])
time_of_day['dawn'] = mf.trimf(time_of_day.universe, [3, 5.5, 7])
time_of_day['day'] = mf.trimf(time_of_day.universe, [6, 13, 18])
time_of_day['dusk'] = mf.trimf(time_of_day.universe, [17, 19, 21])
time_of_day['night'] = mf.trapmf(time_of_day.universe, [20, 21, 24, 24])
# time_of_day.view()

# LED Brightness
brightness['lower'] = mf.trimf(brightness.universe, [0, 1000, 3500])
brightness['low'] = mf.trimf(brightness.universe, [2000, 5000, 8000])
brightness['medium'] = mf.trimf(brightness.universe, [7000, 9500, 12000])
brightness['high'] = mf.trimf(brightness.universe, [11000, 13500, 16000])
brightness['higher'] = mf.trapmf(brightness.universe, [15000, 16500, 18000, 18000])
# brightness.view()

# colour Temperature
colour_temp['warm glow'] = mf.trimf(colour_temp.universe, [0, 1000, 2700])
colour_temp['warm white'] = mf.trimf(colour_temp.universe, [2500, 3000, 4000])
colour_temp['neutral white'] = mf.trimf(colour_temp.universe, [3800, 4000, 5200])
colour_temp['daylight white'] = mf.trapmf(colour_temp.universe, [5000, 5700, 6500, 6500])
# colour_temp.view()


# Define fuzzy rules (Include only the 18 most frequently occurring scenarios)

# Morning Commute on Main Roads, School Zone at the Start of School Day, Morning Market or Street Vendor Area and Outdoor Train or Bus Stations:

rule1 = ctrl.Rule((ambient_light['dark'] | ambient_light['moderate']) & 
                  (distance['very close'] | distance['close'] | distance['moderate'] | distance['far'] | distance['very far']) & 
                  (traffic_activity['heavy'] & pedestrian_activity['heavy']) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['dawn'] | time_of_day['day']), 
                  (brightness['higher'], colour_temp['neutral white']))

rule2 = ctrl.Rule((ambient_light['dark'] | ambient_light['moderate']) & 
                  (distance['very close'] | distance['close'] | distance['moderate'] | distance['far'] | distance['very far']) & 
                  (traffic_activity['heavy'] | pedestrian_activity['heavy']) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['dawn'] | time_of_day['day']), 
                  (brightness['high'], colour_temp['neutral white']))

# Morning Exercise in Parks:
rule3 = ctrl.Rule((ambient_light['dark'] | ambient_light['moderate']) & 
                  (distance['very close'] | distance['close'] | distance['moderate']) & 
                  (traffic_activity['light'] & pedestrian_activity['heavy']) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['dawn'] | time_of_day['day']), 
                  (brightness['high'], colour_temp['neutral white']))

rule4 = ctrl.Rule((ambient_light['dark'] | ambient_light['moderate']) & 
                  (distance['very close'] | distance['close'] | distance['moderate']) & 
                  (traffic_activity['light'] & (pedestrian_activity['light'] | pedestrian_activity['moderate'])) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['dawn'] | time_of_day['day']), 
                  (brightness['medium'], colour_temp['neutral white']))

# Morning Delivery and Commercial Loading Zones (some conditions is covered by previous scenarios):
rule5 = ctrl.Rule((ambient_light['dark'] | ambient_light['moderate']) & 
                  (distance['very close'] | distance['close'] | distance['moderate']) & 
                  (traffic_activity['moderate'] & pedestrian_activity['moderate']) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['dawn'] | time_of_day['day']), 
                  (brightness['medium'], colour_temp['neutral white']))

# Urban Residential Street and City Park Pathway at Night:
rule6 = ctrl.Rule((ambient_light['moderate']) & 
                  (distance['very close'] | distance['close']) & 
                  (traffic_activity['light'] & (pedestrian_activity['light'] | pedestrian_activity['moderate'])) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['night']), 
                  (brightness['higher'], colour_temp['warm white']))

# Urban Main Road During Evening Rush Hour:
rule7 = ctrl.Rule((ambient_light['bright']) & 
                  (distance['close'] | distance['moderate'] | distance['far']) & 
                  (traffic_activity['heavy'] & (pedestrian_activity['light'] | pedestrian_activity['moderate'])) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['dusk'] | time_of_day['night']), 
                  (brightness['high'], colour_temp['neutral white']))

# Commercial District During Evening Shopping and City Square or Plaza During Evening Events:
rule8 = ctrl.Rule((ambient_light['bright']) & 
                  (distance['very close'] | distance['close'] | distance['moderate']) & 
                  ((traffic_activity['light'] | traffic_activity['moderate']) & (pedestrian_activity['heavy'])) & 
                  (visibility['moderate'] | visibility['clear'] | visibility['excellent']) & 
                  (time_of_day['dusk'] | time_of_day['night']), 
                  (brightness['high'], colour_temp['neutral white']))

# Busy Urban Intersection at Night:
rule9 = ctrl.Rule((ambient_light['very bright']) & 
                  (distance['very close'] | distance['close'] | distance['moderate']) & 
                  ((traffic_activity['heavy']) & (pedestrian_activity['heavy'])) & 
                  (visibility['moderate'] | visibility['clear'] | visibility['excellent']) & 
                  (time_of_day['night']), 
                  (brightness['higher'], colour_temp['neutral white']))

# Suburban Residential Street at Dusk, Pedestrian Bridge and Residential Cul-de-Sac at Night:
rule10 = ctrl.Rule((ambient_light['moderate']) & 
                  (distance['very close'] | distance['close']) & 
                  (traffic_activity['light'] & pedestrian_activity['light']) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['dusk'] | time_of_day['night'] | time_of_day['midnight']), 
                  (brightness['medium'], colour_temp['warm white']))

# Highway Exit Ramp at Night:
rule11 = ctrl.Rule((ambient_light['bright']) & 
                  (distance['close'] | distance['moderate'] | distance['far']) & 
                  (traffic_activity['light'] | traffic_activity['moderate']) & (pedestrian_activity['light']) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['night'] | time_of_day['midnight']), 
                  (brightness['medium'], colour_temp['neutral white']))

# Outdoor Dining Area in the Evening:
rule12 = ctrl.Rule((ambient_light['moderate']) & 
                  (distance['very close'] | distance['close']) & 
                  (traffic_activity['light'] & pedestrian_activity['heavy']) & 
                  (visibility['moderate'] | visibility['clear']) & 
                  (time_of_day['dusk'] | time_of_day['night']), 
                  (brightness['high'], colour_temp['neutral white']))

# Sports Field Lighting at Night:
rule13 = ctrl.Rule((ambient_light['very bright']) & 
                  (distance['close'] | distance['moderate']) & 
                  (traffic_activity['light'] & pedestrian_activity['light']) & 
                  (visibility['clear'] | visibility['excellent']) & 
                  (time_of_day['dusk'] | time_of_day['night']), 
                  (brightness['low'], colour_temp['daylight white']))

rule14 = ctrl.Rule((ambient_light['very bright']) & 
                  (distance['close'] | distance['moderate']) & 
                  (traffic_activity['light'] & pedestrian_activity['moderate']) & 
                  (visibility['clear'] | visibility['excellent']) & 
                  (time_of_day['dusk'] | time_of_day['night']), 
                  (brightness['medium'], colour_temp['daylight white']))

rule15 = ctrl.Rule((ambient_light['very bright']) & 
                  (distance['close'] | distance['moderate']) & 
                  (traffic_activity['light'] & pedestrian_activity['heavy']) & 
                  (visibility['clear'] | visibility['excellent']) & 
                  (time_of_day['dusk'] | time_of_day['night']), 
                  (brightness['high'], colour_temp['daylight white']))

rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15]

train_ctrl = ctrl.ControlSystem(rules=rules)
train = ctrl.ControlSystemSimulation(control_system=train_ctrl)

# Define the values for the inputs
train.input['ambient light'] = 170
train.input['distance'] = 20
train.input['traffic activity'] = 20
train.input['pedestrian activity'] = 480
train.input['visibility'] = 2200
train.input['time of day'] = 20

# Compute the outputs
train.compute()

# Print the output values
print(train.output)

# To extract the outputs
print(train.output['brightness'])
print(train.output['colour temperature'])

# # Viewing the result on the graph based on the values of the inputs
# brightness.view(sim=train)
# colour_temp.view(sim=train)

# # View control/ output space
# x, y = np.meshgrid(np.linspace(ambient_light.universe.min(), ambient_light.universe.max(), 100),
#                    np.linspace(distance.universe.min(), distance.universe.max(), 100))
# z_brigtness = np.zeros_like(x, dtype=float)
# z_colour_temp = np.zeros_like(x, dtype=float)


# # Create meshgrid for ambient_light and distance
# x, y = np.meshgrid(np.linspace(ambient_light.universe.min(), ambient_light.universe.max(), 100),
#                    np.linspace(distance.universe.min(), distance.universe.max(), 100))

# # Initialize arrays to hold the outputs
# z_brightness = np.zeros_like(x, dtype=float)
# z_colour_temp = np.zeros_like(x, dtype=float)

# # Constants for other variables
# # fixed_ambient_light = 
# # fixed_distance = 
# fixed_traffic_activity = 300
# fixed_pedestrian_activity = 200
# fixed_visibility = 1000
# fixed_time_of_day = 12

# # Loop through grid
# for i, r in enumerate(x):
#     for j, c in enumerate(r):
#         # Set the inputs
#         train.input['ambient light'] = x[i, j]
#         train.input['distance'] = y[i, j]

#         # Set the constant input variables
#         train.input['traffic activity'] = fixed_traffic_activity
#         train.input['pedestrian activity'] = fixed_pedestrian_activity
#         train.input['visibility'] = fixed_visibility
#         train.input['time of day'] = fixed_time_of_day

#         try:
#             train.compute()
#         except:
#             z_brightness[i, j] = float('inf')
#             z_colour_temp[i, j] = float('inf')

#         z_brightness[i, j] = train.output['brightness']
#         z_colour_temp[i, j] = train.output['colour temperature']


# # Function to plot
# def plot3d(x, y, z, label):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', linewidth=0.4, antialiased=True)

#     ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
#     ax.contourf(x, y, z, zdir='x', offset=x.max()*1.5, cmap='viridis', alpha=0.5)
#     ax.contourf(x, y, z, zdir='y', offset=y.max()*1.5, cmap='viridis', alpha=0.5)
#     ax.set_title(label)
#     ax.view_init(30, 200)

# # Plot the graphs
# plot3d(x, y, z_brightness, "Brightness")
# plot3d(x, y, z_colour_temp, "Colour Temperature")

# plt.show()


# Allow the user input and output 
# Initialize the control system

def show_graph(train):
    while True:
        print("\nWhat would you like to do next?")
        print("1. View the graphs")
        print("2. Quit")
        
        choice = input("Enter your choice (1/2): ")
        print("************************************************************************************")

        
        if choice == "1":
            # Viewing the result on the graph based on the values of the inputs
            brightness.view(sim=train)
            colour_temp.view(sim=train)
            plt.show()
        elif choice == "2":
            print("\nExiting program. Goodbye! 👋")
            exit()
        else:
            print("Invalid choice. Please enter again.")
            continue

        break_if_needed = input("Do you want to continue? (y/n): ")
        if break_if_needed.lower() == 'n':
            print("\nExiting program. Goodbye! 👋")
            exit()

def get_float_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"❗️ Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("❗️ Invalid input. Please enter a numerical value.")

def main():
    # Provide a fancy header
    print("************************************************************************************")
    print("                    🌟 Smart Street Lighting Fuzzy System 🌟                        ")
    print("************************************************************************************")

    # Introduce the system
    print("\n👋 Welcome to the Smart Street Lighting Fuzzy System!")
    print("👉 This system is designed to predict the ideal brightness and color temperature")
    print("   for street lamps based on various environmental factors.")
    print("🔹 Factors include ambient light, distance from the streetlamp, traffic activity,")
    print("   pedestrian activity, visibility, and the time of day.")
    print("🔹 Just enter the data as prompted, and the system will do the rest!\n")
    print("************************************************************************************")


    # Offer instructions
    print("\n📝 Follow the prompts to input your data.\n")

    print("************************************************************************************")


    # Collect data from the user with error handling
    ambient_light_input = get_float_input("💡 Enter the Ambient Light Level (0-200): ", 0, 200)
    distance_input = get_float_input("📏 Enter the Distance from the Street Lamp (0-110): ", 0, 110)
    traffic_activity_input = get_float_input("🚗 Enter the Traffic Activity per Hour (0-900): ", 0, 900)
    pedestrian_activity_input = get_float_input("🚶 Enter the Pedestrian Activity per Hour (0-500): ", 0, 500)
    visibility_input = get_float_input("👀 Enter the Visibility Level (0-2500): ", 0, 2500)
    time_of_day_input = get_float_input("🕒 Enter the Time of Day (0-24): ", 0, 24)
    
    print("\n🔍 Computing the ideal light settings...\n")
    print("************************************************************************************")


    # Define the values for the inputs
    train.input['ambient light'] = ambient_light_input
    train.input['distance'] = distance_input
    train.input['traffic activity'] = traffic_activity_input
    train.input['pedestrian activity'] = pedestrian_activity_input
    train.input['visibility'] = visibility_input
    train.input['time of day'] = time_of_day_input
    
    # Compute the outputs
    train.compute()
    
    # Print the output values
    print("\n🎉 Predicted Output Values:")
    print(f"💡 Brightness Level: {train.output['brightness']}")
    print(f"🌈 Colour Temperature: {train.output['colour temperature']} \n")
    print("************************************************************************************")

    show_graph(train)

if __name__ == '__main__':
    main()
