#######################################################################
#                                                                     #
# David Fuller                                                        #
#                                                                     #
# Project Euler: Problem 5.                                           #
#                                                                     #
# 11/12/2016                                                          #
#                                                                     #
#######################################################################

#######################################################################
#                                                                     #
#                          IMPORT STATEMENTS                          #
#                                                                     #
#######################################################################

from tkinter import *   # For GUI
import time             # For keeping track of elapsed time

#######################################################################
#                                                                     #
#                              CONSTANTS                              #
#                                                                     #
#######################################################################

TITLE               = "Project Euler: Problem 2"   # GUI Title.
GEOMETRY            = "300x163"                    # GUI screen size.

#######################################################################
#                                                                     #
#                             EULER CLASS                             #
#                                                                     #
#######################################################################

class Euler:
    # Function finds greatest common divisor, recursively
    def gcd(self, x, y):
        if (y == 0):
            return x
        else:
            return self.gcd(y, x % y)

    # Function find leasc common multiple
    def lcm(self, x, y):
        return x * y / self.gcd(x, y)

    # Method finds solution to Project Euler: Problem 5
    def findSolution(self):
        # Store 1 as answer
        answer = 1

        # Loop through the range of numbers 2 through 20
        # and find the lcm of current answer and the number
        # in the range
        for i in range(2, 21):
            answer = self.lcm(i, answer)

        # Return answer
        return int(answer)

#######################################################################
#                                                                     #
#                              GUI CLASS                              #
#                                                                     #
#######################################################################

class EulerForm:
    def __init__(self, parent, msg):
        # Set up GUI
        self.parent = parent
        self.parent.title(TITLE)
        self.parent.geometry(GEOMETRY)

        # Create solution StringVar
        self.solution = StringVar()
        self.solution.set("")

        # Create GUI Widgets
        self.descriptionMessage = Message(parent, \
                                          text = msg, \
                                          width = 280)
        self.solutionButton = Button(parent, \
                                     text = "Find Solution", \
                                     command = self.findSolution)
        self.solutionLabel = Label(parent, \
                                   textvariable = self.solution)

        # Place GUI Widgets
        self.descriptionMessage.pack()
        self.solutionButton.pack()
        self.solutionLabel.pack()

    # Method finds and displays solution and elapsed time
    def findSolution(self):
        # Store start time
        start = time.time()

        # Project Euler object
        euler = Euler()
        solution = euler.findSolution()

        # Calculate elapsed time, rounded to 2 decimals
        elapsed = ("%.2f" % (time.time() - start))

        # Display the sum, as well as elapsed time
        solution = str(solution) + \
                   " found in " + \
                   str(elapsed) + \
                   " seconds."
        self.solution.set(solution)

#######################################################################
#                                                                     #
#                                DRIVER                               #
#                                                                     #
#######################################################################

# Method sets up Problem description
def createDescription():
    description = "2520 is the smallest number that can be divided" + \
                  " by each of the numbers from 1 to 10 without " + \
                  "remainder.\n\n" + \
                  "What is the smallest positive number that is " + \
                  "evenly divisble by all of the numbers from 1 " + \
                  "to 20?"
    return description

# Define main - app driver
def main():
    # Initialize GUI
    root = Tk()

    # Call function to set up Problem description
    description = createDescription()

    # Set up EulerForm
    euler = EulerForm(root, description)

    # Keep app running
    root.mainloop()

# Begin app
main()
