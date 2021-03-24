import math

# Create functions for 2 equations and print option
def sphere(radius):
    r = float(radius)
    sphere_volume = 12.56/3 * r ** 3
    sphere_sa = 12.56 * r ** 2
    sphere_volume = round(sphere_volume, 2)
    results = {'Radius':r, 'Volume':sphere_volume, 'Surface Area':sphere_sa}
    print(results)
    return sphere_volume, sphere_sa

def r_prism(x_length, y_width, z_height):
    x = float(x_length)
    y = float(y_width)
    z = float(z_height)
    prism_volume = x * y * z
    prism_sa = (2 * x) + (2 * y) + (2 * z)
    results = {'Length':r, 'Volume':sphere_volume, 'Surface Area':sphere_sa}
    return prism_volume, prism_sa

def log_results():
    test_value = 'Got it'
    with open("5d_results.txt", "a") as file:
        file.write(test_value+'\n')

# Ask user to select from equation options
# Easier for people to visualize - use spherical equation or a rectangular prism
# Should I ask user to stick to integers?
print ("This application will output 5 different sets of changes in the size of a 3 dimensional object over time.")
print ("You will be able to choose between an equation for a sphere of varying radius or a rectangular prism of varying dimensions.")
print ("These equations will vary over time based off the options chosen for the change in time and dimension(s).\n")

# Add in loop to allow user to quit at any time.
print ("You may continue as long as you wish or enter 'q' to quit the application.\n")

# Ask user to input initial value.
equation = input("Would you prefer to use an equation for a sphere(1), an equation for a rectangular prism(2), or would you like to quit(q)?\nPlease enter a 1, 2, or q only.  ").lower()

if equation != "q":
    time = input("And what value would you like to use for delta t (change in time) in these equations?  ")

    if equation == "1":
        radius = input("Please enter the initial radius you would like to use.  ")
        radius = float(radius)
        d_radius = input("Please enter the amount you would like the radius to change each time.  ")
        d_radius = float(d_radius)
        sphere(radius)
        # print (sphere_volume)
        # print (sphere_ra)
        

    elif equation == "2":
        print ("For a rectangular prism, please choose the intial value of each side (x, y, z) and the change of each of these values.")
        x_length = input("What is the initial length (x) for the prism?  ")
        dx = input("What is the change in x (delta x) after each iteration?  ")
        y_width = input("What is the initial width (y) for the prism?  ")
        dy = input("What is the change in y (delta y) after each iteration?  ")
        z_height = input("What is the initial height (z) for the prism?  ")
        dz = input("What is the change in z (delta z) after each iteration?  ")
        r_prism(x_length, y_width, z_height)
        

# Calculate 5 successive iterations for the value.
# Will call functions 5 times and output the equations as a list.

# Output the successive iterations.
