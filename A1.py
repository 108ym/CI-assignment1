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

def show_3d_graph(first_variable, second_variable):

    fuzzy_variables = {
    'ambient light': ambient_light,
    'distance': distance,
    'traffic activity': traffic_activity,
    'pedestrian activity': pedestrian_activity,
    'visibility': visibility,
    'time of day': time_of_day,
    'brightness': brightness,
    'colour temperature': colour_temp
    }
    
    # Create meshgrid for the two chosen variables
    x, y = np.meshgrid(np.linspace(fuzzy_variables[first_variable].universe.min(), fuzzy_variables[first_variable].universe.max(), 100),
                   np.linspace(fuzzy_variables[second_variable].universe.min(), fuzzy_variables[second_variable].universe.max(), 100))

    # Initialize arrays to hold the outputs
    z_brightness = np.zeros_like(x, dtype=float)
    z_colour_temp = np.zeros_like(x, dtype=float)

    # Constants for other variables (could be adjusted)
    fixed_values = {
        'ambient light': 100,
        'distance': 55,
        'traffic activity': 300,
        'pedestrian activity': 200,
        'visibility': 1000,
        'time of day': 12
    }

    # Loop through grid
    for i, r in enumerate(x):
        for j, c in enumerate(r):
            # Set the chosen input variables
            train.input[first_variable] = x[i, j]
            train.input[second_variable] = y[i, j]

            # Set the constant input variables for non-chosen ones
            for var in fixed_values:
                if var != first_variable and var != second_variable:
                    train.input[var] = fixed_values[var]

            try:
                train.compute()
            except:
                z_brightness[i, j] = float('inf')
                z_colour_temp[i, j] = float('inf')

            z_brightness[i, j] = train.output['brightness']
            z_colour_temp[i, j] = train.output['colour temperature']

    # Function to plot
    def plot3d(x, y, z, label):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', linewidth=0.4, antialiased=True)

        ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
        ax.contourf(x, y, z, zdir='x', offset=x.max()*1.5, cmap='viridis', alpha=0.5)
        ax.contourf(x, y, z, zdir='y', offset=y.max()*1.5, cmap='viridis', alpha=0.5)
        ax.set_xlabel(first_variable)  # Set x-axis label
        ax.set_ylabel(second_variable)  # Set y-axis label
        ax.set_zlabel(label)  # Set z-axis label

        ax.set_title(label)
        ax.view_init(30, 200)

    # Plot the graphs
    plot3d(x, y, z_brightness, "Brightness")
    plot3d(x, y, z_colour_temp, "Colour Temperature")

    plt.show()


def choose_input_variables():
    variables = ['ambient light', 'distance', 'traffic activity', 'pedestrian activity', 'visibility', 'time of day']
    print("\nChoose two input variables to view in the 3D graph:")

    for i, var in enumerate(variables, 1):
        print(f"{i}. {var}")

    print("\n************************************************************************************\n")


    while True:
        try:
            first_choice = int(input("1️⃣ Enter the number for the first variable: "))
            second_choice = int(input("2️⃣ Enter the number for the second variable: "))

            if 1 <= first_choice <= 6 and 1 <= second_choice <= 6 and first_choice != second_choice:
                return variables[first_choice-1], variables[second_choice-1]
            else:
                print("❗️ Please select two different variables from the list. Make sure your choices are between 1 and 6.")
        except ValueError:
            print("❗️ Invalid choice. Please enter the numbers corresponding to the variables.")



def show_graph(train):
    while True:
        print("\nWhat would you like to do next?")
        print("1. View the result graphs (brightness level & colour temperature)")
        print("2. Show control/ output space 3d graph")
        print("3. Quit")
        
        choice = input("Enter your choice (1/3): ")
        print("\n************************************************************************************")

        
        if choice == "1":
            # Viewing the result on the graph based on the values of the inputs
            brightness.view(sim=train)
            colour_temp.view(sim=train)
            plt.show()
        elif choice == "2":
            first_var, second_var = choose_input_variables()
            show_3d_graph(first_var, second_var)
        elif choice == "3":
            print("\nExiting program. Goodbye! 👋")
            exit()
        else:
            print("Invalid choice. Please enter again.")
            continue

        break_if_needed = input("\nDo you want to continue? (y/n): ")
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

def variable_instructions():
    print("************************************************************************************")
    print("                            📜 Variable Instructions 📜                            ")
    print("************************************************************************************")
    
    print("\n💡 Ambient Light Level:")
    print("    - Measured in Lux.")
    print("    - Represents the environmental light conditions.")
    print("    - Range: 0 (like twilight hours) to 200 (like a bright indoor area).")
    
    print("\n📏 Distance from the Street Lamp:")
    print("    - Measured in meters.")
    print("    - Distance between the object and the lamp post.")
    print("    - Range: 0 (directly below the lamp) to 110 (far from the lamp).")
    
    print("\n🚗 Traffic Activity per Hour:")
    print("    - Represents the number of vehicles passing through an area in an hour.")
    print("    - Range: 0 (no vehicles) to 900 (very busy intersection).")
    
    print("\n🚶 Pedestrian Activity per Hour:")
    print("    - Represents the number of people passing through an area in an hour.")
    print("    - Range: 0 (no pedestrians) to 500 (crowded area).")
    
    print("\n👀 Visibility Level:")
    print("    - Measured based on atmospheric conditions such as fog.")
    print("    - Represents how far one can see clearly.")
    print("    - Range: 0 (poor visibility) to 2500 (clear visibility).")
    
    print("\n🕒 Time of Day:")
    print("    - Represents the hour in a 24-hour format.")
    print("    - Range: 0 (midnight) to 24 (end of the day).")
    print("    - Example: 13 for 1 PM.")
    
def output_instructions():
    print("\n************************************************************************************")
    print("                             📜 Output Instructions 📜                            ")
    print("************************************************************************************")
    
    print("\n💡 Brightness Level of the Street Lamp:")
    print("    - Measured in Lumens.")
    print("    - Represents the intensity of light emitted by the street lamp.")
    print("    - Range: 0 (lamp off) to 18000 (maximum brightness).")
    
    print("\n🎨 Colour Temperature of the Street Lamp:")
    print("    - Measured in Kelvin (K).")
    print("    - Describes the warmth or coolness of the light appearance.")
    print("    - Range: 0 (indicating absence of color temperature) to 6500 ")
    print("      (cool, bluish-white daylight).")
    print("    - Typically, warmer temperatures (2500K to 4000K) are used for relaxed settings.")
    print("    - Cooler temperatures (5000K to 6500K) resemble daylight and are used for")
    print("      concentration and focus.")

    
    print("\n************************************************************************************")


def main():
    # Provide a fancy header
    print("************************************************************************************")
    print("                        🌟 Smart Street Lighting Fuzzy System 🌟                      ")
    print("************************************************************************************")

    # Introduce the system
    print("\n👋 Welcome to the Smart Street Lighting Fuzzy System!")
    print("👉 This system is designed to predict the ideal brightness and color temperature")
    print("   for street lamps based on various environmental factors.")
    print("🔹 Factors include ambient light, distance from the streetlamp, traffic activity,")
    print("   pedestrian activity, visibility, and the time of day.")
    print("🔹 Just enter the data as prompted, and the system will do the rest!\n")
    variable_instructions()
    output_instructions()

    # Offer instructions
    print("\n📝 Follow the prompts to input your data.\n")

    print("************************************************************************************\n")


    # Collect data from the user with error handling
    ambient_light_input = get_float_input("💡 Enter the Ambient Light Level (0-200, eg: 90): ", 0, 200)
    distance_input = get_float_input("📏 Enter the Distance from the Street Lamp (0-110, eg: 15): ", 0, 110)
    traffic_activity_input = get_float_input("🚗 Enter the Traffic Activity per Hour (0-900, eg: 200): ", 0, 900)
    pedestrian_activity_input = get_float_input("🚶 Enter the Pedestrian Activity per Hour (0-500, eg: 150): ", 0, 500)
    visibility_input = get_float_input("👀 Enter the Visibility Level (0-2500, eg:750): ", 0, 2500)
    time_of_day_input = get_float_input("🕒 Enter the Time of Day (0-24, eg:21): ", 0, 24)
    
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
