import math
import json

# Create functions for 2 equations and print option
def sphere(radius, d_radius):
    j = 1
    r = float(radius)
    dr = float(d_radius)

    while j < 4:
        sphere_volume = 12.56/3 * r ** 3
        sphere_sa = 12.56 * r ** 2
        sphere_volume = round(sphere_volume, 2)
        sphere_dict.update({'Radius':r, 'Volume':sphere_volume, 'Surface Area':sphere_sa})
        sphere_list.append(sphere_dict)
        prt_log(sphere_dict)
        r += dr
        j += 1

def r_prism(x_length, dx, y_width, dy, z_height, dz):
    k = 1
    x = float(x_length)
    dx = float(dx)
    y = float(y_width)
    dy = float(dy)
    z = float(z_height)
    dz = float(dz)

    while k < 4:
        prism_volume = x * y * z
        prism_sa = (2 * x * y) + (2 * x * z) + (2 * y * z)
        prism_dict.update({'Length':x, 'Width':y, 'Height':z, 'Volume':prism_volume, 'Surface Area':prism_sa})
        prism_list.append(prism_dict)
        prt_log(prism_dict)
        print (prism_list)
        x += dx
        y += dy
        z += dz
        k += 1


def prt_log(my_list):
    # print log after each loop
    with open("5d_results.txt", "a") as file:
        file.write(json.dumps(my_list))

# Ask user to select from equation options
# Easier for people to visualize - use spherical equation or a rectangular prism
# Should I ask user to stick to integers?
print ("This application will output 5 different sets of changes in the size of a 3 dimensional object over time.")
print ("You will be able to choose between an equation for a sphere of varying radius or a rectangular prism of varying dimensions.")
print ("These equations will vary over time based off the options chosen for the change in time and dimension(s).\n")

# Add in loop to allow user to quit at any time.
print ("You may continue as long as you wish or enter 'q' to quit the application.\n")

# Ask user to input initial value.
while True:
    equation = input("Would you prefer to use an equation for a sphere(1), an equation for a rectangular prism(2), or would you like to quit(q)?\nPlease enter a 1, 2, or q only.  ").lower()

    if equation == "q":
        print("Thanks for testing my app!")
        break

    while equation == "1" or equation =="2":
        # time = input("\nAnd what value would you like to use for delta t (change in time) in these equations?  ")
        # time = float(time)

        if equation == "1":
            i = 1
            while i < 3:
                radius = input("\nPlease enter the initial radius you would like to use.  ")
                d_radius = input("\nPlease enter the amount you would like the radius to change each time.  ")
                sphere_list = list()
                sphere_dict = {}
                sphere(radius, d_radius)
                i += 1
            else:
                print("\nPlease check your results in the file '5d_results.py' in your folder.\nNew results will be appended to the end of the file each time you run this.\n")
                break
            
        elif equation == "2":
            i = 1
            while i < 2:
                print ("\nFor a rectangular prism, please choose the intial value of each side (x, y, z) and the change of each of these values.")
                x_length = input("\nWhat is the initial length (x) for the prism?  ")
                dx = input("\nWhat is the change in x (delta x) after each iteration?  ")
                y_width = input("\nWhat is the initial width (y) for the prism?  ")
                dy = input("\nWhat is the change in y (delta y) after each iteration?  ")
                z_height = input("\nWhat is the initial height (z) for the prism?  ")
                dz = input("\nWhat is the change in z (delta z) after each iteration?  ")
                prism_list = list()
                prism_dict = {}
                r_prism(x_length, dx, y_width, dy, z_height, dz)
                i += 1
            else:
                break
