#import the necessary libraries
import sys
import math
import argparse
import numpy as np
import matplotlib.pyplot as mpl 

print("Program to calculate Braking distance:")

# User input for mass of car
m = int(input("Enter the mass of the car in kg: "))

# User input for velocity of car
v = int(input("Enter the speed of the car in km/h: "))

g = 9.8  # acceleration due to gravity in earth

# Options given to user to choose appropriate road type
print("Select Road type:")
print("1 for Concrete")
print("2 for Ice")
print("3 for Water")
print("4 for Gravel")
print("5 for Sand")
num = int(input())

if num == 1:
    print("Select road condition:")
    print("6 for Dry")
    print("7 for Wet")
    n = int(input())  # user can choose concrete road condition
    if n == 6:
        mu = 0.5  # coefficient of friction dry
    else:
        mu = 0.35  # coefficient of friction wet
elif num == 2:
    print("Select road condition:")
    print("6 for Dry")
    print("7 for Wet")
    n = int(input())  # user can choose ice road condition
    if n == 6:
        mu = 0.15  # coefficient of friction dry
    else:
        mu = 0.08  # coefficient of friction wet
elif num == 3:
    mu = 0.05  # coefficient of friction water road
elif num == 4:
    mu = 0.35  # coefficient of friction gravel road
else:
    mu = 0.3  # coefficient of friction sand road

rd = (v*0.01)  # Normal reaction time in human is 0.01, reaction distance = velocity of car * reaction time
vn = v/3.6  # This formula converts the velocity of car from km/h to m/s.
bd = (0.051*pow(vn,2))/mu  # the 0.051 is a constant - (1/2g). Actual formula for braking distance is pow(vn,2)/2*mu*g
sd = (bd + rd)  # Actual stopping distance of car is breaking distance plus reaction distance

print("The braking distance is "+str(sd)+" m")
bt = sd/vn  # breaking time is stopping distance divided by velocity
a = -((pow(vn,2))/(2*sd))  # derived from formula s=ut + 0.5*a*pow(t,2) where u=0, a is deceleration hence negative
taxis = np.arange(0, bt, bt/2000)  # plotting of time in a resolution of 1/2000
vaxis = vn + (a * taxis) 
daxis = vn * taxis + (0.5 * a * pow(a, 2))

mpl.subplot(2,1,1)
mpl.plot(taxis, daxis)
mpl.xlabel('Time (s)') # adding x-axis label for distance vs time
mpl.ylabel('Distance (m)') # adding y-axis label for distance vs time

mpl.subplot(2,1,2)
mpl.plot(taxis, vaxis)
mpl.xlabel('Time (s)') # adding x-axis label for velocity vs time
mpl.ylabel('Velocity (m/s)') # adding y-axis label for velocity vs time

mpl.show()
