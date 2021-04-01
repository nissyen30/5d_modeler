import math
import json


def sphere(radius, d_radius):
    j = 1
    r = float(radius)
    dr = float(d_radius)

    while j < 4:
        r1 = ("Radius " + str(j))
        v1 = ("Volume " + str(j))
        s1 = ("Surface Area " + str(j))
        sphere_volume = round((12.56/3 * r ** 3), 2)
        sphere_sa = round((12.56 * r ** 2), 2)
        sphere_dict[r1] = r
        sphere_dict[v1] = sphere_volume
        sphere_dict[s1] = sphere_sa
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
        x2 = ("Length " + str(k))
        y2 = ("Width " + str(k))
        z2 = ("Height " + str(k))
        v2 = ("Volume " + str(k))
        s2 = ("Surface Area " + str(k))
        prism_volume = round((x * y * z), 2)
        prism_sa = round(((2 * x * y) + (2 * x * z) + (2 * y * z)), 3)
        prism_dict[x2] = x
        prism_dict[y2] = y
        prism_dict[z2] = z
        prism_dict[v2] = prism_volume
        prism_dict[s2] = prism_sa
        x += dx
        y += dy
        z += dz
        k += 1

def prt_log(my_list):
    # print log to 5d_modeler.txt
    with open("5d_results.txt", "a") as file:
        file.write(json.dumps(my_list))

# Ask user to select from equation options
print ("This application will output 3 different sets of changes in the size of a 3-dimensional object over time.\nYou will be able to choose between an equation for a sphere or a rectangular prism and choose both their intial dimensions and their rate of change from one iteration to the next.\nEach of the 3 iterations for that chosen shape will provide a different set of 4-D data with multiple sets comprising a fifth dimension.\nThese values are reported without unit as the math remains the same no matter which unit is assigned to it.\nFeel free to assign whatever units you wish keeping in mind that Surface Area will be that unit squared and Volume will be that unit cubed.\n")

# Add in loop to allow user to quit at any time.
print ("You may continue as long as you wish or enter 'q' to quit the application.\n")

# Ask user to input initial value.
while True:
    equation = input("Would you prefer to model a sphere(1), a rectangular prism(2), or would you like to quit(q)?\nPlease enter a 1, 2, or q only.  ").lower()

    if equation == "q":
        print("\nThanks for testing my app!")
        break

    elif equation == "1":
        i = 1
        while i < 4:
            radius = input("\nPlease enter the initial radius you would like to use.  ")
            d_radius = input("\nPlease enter the amount you would like the radius to change each time.  ")
            # sphere_list = list()
            sphere_dict = {}
            try:
                sphere(radius, d_radius)
            except ValueError:
                print("\nPlease enter numeric (integer or float) values only.")
                continue
            prt_log(sphere_dict)
            print("\n")
            print(sphere_dict)
            print("\nYou will also see these results in the file '5d_results.txt' in your folder where they have been saved for future use.\nNew results will be appended to the end of the file each time you run this loop.\n")
            i += 1
        
    elif equation == "2":
        i = 1
        while i < 4:
            print ("\nFor a rectangular prism, please choose the intial value of each side (x, y, z) and the change of each of these values.")
            x_length = input("\nWhat is the initial length (x) for the prism?  ")
            dx = input("\nWhat is the change in x (delta x) after each iteration?  ")
            y_width = input("\nWhat is the initial width (y) for the prism?  ")
            dy = input("\nWhat is the change in y (delta y) after each iteration?  ")
            z_height = input("\nWhat is the initial height (z) for the prism?  ")
            dz = input("\nWhat is the change in z (delta z) after each iteration?  ")
            prism_dict = {}
            try:
                r_prism(x_length, dx, y_width, dy, z_height, dz)
            except ValueError:
                print("\nPlease enter numeric (integer or float) values only.")
                continue
            prt_log(prism_dict)
            print("\n")
            print(prism_dict)
            print("\nYou will also see these results in the file '5d_results.txt' in your folder where they have been saved for future use.\nNew results will be appended to the end of the file each time you run this loop.\n")
            i += 1
