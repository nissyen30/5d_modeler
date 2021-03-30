This is my Python class project. It is a basic 5d Modeler. This is also the precursor for a version that will output the resulting values in a graphic form, but this was not a requirement for this class and it would have taken more time than was available to develop a graphical output. However, I have included the necessary output to a json file which can later be used to develop a graphical output. This output will be saved in a file (called 5d_modeler.txt) in the same folder from which the user runs this app.

The idea is to offer the user a choice to model either a sphere or rectangular prism (or to quit). Then the user will choose the starting values for the chosen shape and the amount of change from the starting value over three iterations. The values will be printed in the console and save in the text file mentioned previously.

Each time the user chooses to run a particular shape, they are modeling one specific reality where the chosen object increases in size based on the user's initial input. The data created each time the user runs through a loop and chooses a new shape or new values creates the multiple sets of objects changing over time (a fifth dimensional set).

The requirements that will be met are:
	1. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
	2. Implement a log that records errors, invalid inputs, or other important events and writes them to a text file
	3. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code.
	4. Build a conversion tool that converts user input to another type and displays it.

The user only needs to have Python installed to run this (it is a python console app). The log that is created with all the data will be generated and updated in whatever folder the user runs the app from.
