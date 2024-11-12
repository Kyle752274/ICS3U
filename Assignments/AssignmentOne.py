"""
Author : Kyle 
   Revison date : 24 september 2024
   Program : Three part python output
   Description : A program that determines the Area of a rectangle, Circle,
   SA and Volume of a cylinder, and the pendlumum period.
   VARIABLE DICTIONARY :
   PartL1(The length for Part one)
   PartL1 (int)
   PartW1 = The width for part one
   PartW1 (int)
   Area = The area equation/answer for part one
   Area (string)
   PartR2 = The radius for part two
   PartR2 (int)
   Area2 = The area equation/answer for part two
   Area2 (string)
   PartR3 = The radius for part three
   PartR3 (int)
   PartH1 = The height for part three
   PartH1 (int)
   Volume = The equation/answer for part 3
   Volume (string)
   SurfaceA = The second equation/answer for part 3
   SurfaceA (string)
   PartL1 = The length for part 4
   PartL1 (int)
   g = The gravity for part 4
   g (float)
   PendulumP = The pendulum Period equation for part 4
   PendulumP (string)
    
"""
import math
#Variables for part 1
PartL1 = input("Please input length ")
#converts length to integer
PartL1 = int(PartL1)
PartW1 = input("please input width ")
#converts width to integer
PartW1 = int(PartW1)
#calculates area
Area = int(PartL1*PartW1)
#prints the answer 
print("the area is",(Area))
print("-----------------------------------------------------------")

#variables for part 2
PartR2 = input("Please input radius ")
#converts radius to integer
PartR2 = int(PartR2)

Area2 = math.pi*math.pow(PartR2,2)
#prints and rounds to 2nd decimal place
print("The area of the cylinder is %.2f" % Area2)
print("-----------------------------------------------------------")

#Variables for part 3
PartR3 = input("Please input radius ")
#converts radius to integer
PartR3 = int(PartR3)
PartH1 = input("Please input height ")
#converts height to integer
PartH1 = int(PartR3)
#Equation for volume
Volume = (math.pi*math.pow(PartR3, 2)*PartH1)
#prints and rounds to the 2nd decimal place
print("the volume of the cylinder is %.2f" %Volume)
SurfaceA = 2*math.pi*PartR3*PartH1+2*math.pi*math.pow(PartR3, 2)
#prints and rounds to the 2nd decimal place  
print("the surface area of the cylinder is %.2f" %SurfaceA)
print("-----------------------------------------------------------")

#Variables for part 4 
PartL1 = input("Please input Length ")
#converts length to float
PartL1 = int(PartL1)
#convers length to float
g:float =float(9.8)
#calculates the pendulum period 
PendulumP = 2*math.pi*(math.sqrt(PartL1/g))
#prints and rounds to the 2nd decimal place
print("the Pendulum Period is %.2f" %PendulumP)
print("-----------------------------------------------------------")


 
