import math

'''
Question 1: 
 
 Adapt the “HelloWorld” code below to produce a program that defines a variable capable of holding an integer of your choice. The program should add 3 to that number, multiply the result by 2, subtract 4, subtract twice the original number, add 3, then print the result and a new line.
'''
 
def printHelloWorld(x):
  x = int(x) # Ensures x is an int
  print((x+3)*2-4-2*x+3)

'''
Question 2: 
 
 Complete the function below so that it prints every integer from x to x + 10.  Do not use loops. 
 
 Call this function from the main to test your program.
'''

def printXTenTimes(x):
  x = int(x) # Ensures x is an int
  print(x)
  print(x+1)
  print(x+2)
  print(x+3)
  print(x+4)
  print(x+5)
  print(x+6)
  print(x+7)
  print(x+8)
  print(x+9)
  print(x+10)

'''
Question 3: 
 
 Complete the function below so that it converts the height of a person from centimetres to feet and inches. Use integer division (rounding down is acceptable, which is the default for integer division). 
 
 Hint: 254 cm is exactly 100 inches and 12 inches is exactly 1 foot. 
 
 Call this function from the main to test your program.  For example you could test your program with the follow five values, where "?" replaced with the true value.

 101 cm is 3 feet 3 inches to the nearest inch.
 3 cm is 0 feet 1 inches to the nearest inch.
 15 cm is ? feet ? inches to the nearest inch.
 192 cm is ? feet ? inches to the nearest inch.
 124 cm is ? feet ? inches to the nearest inch.
'''

def convertMetricToImperialHeights(height):
  feet = height/12
  inches = height%12
  cm_to_inch_ratio = 254/100
  imperialheight_totalinches = height/cm_to_inch_ratio
  imperialheight_feet = math.floor(imperialheight_totalinches/12)
  inches_extra = math.floor(imperialheight_totalinches%12)
  print(str(101) + " is " + str(imperialheight_feet) + " feet " + str(inches_extra) + " inches to the nearest inch.");

'''
Question 4: 
 
 Complete the function below so that it uses three variables (current, previous, next) to calculate and print out the first ten numbers of the Fibonacci sequence, each on a new line: i.e. the first four lines should be as follows:

 0 
 1 
 1 
 2
 
'''

def fibonacci():
  count = 2

  previous = 0
  print(previous)
  current = 1
  print(current)
  next = previous + current

  while count <= 10:
    previous = current
    current = next
    next = previous + current
    print (current)
    count += 1
  

'''
 Question 5: 
 
 Complete the function below so that it uses two variables: height and radius. Use these two variables and print to the screen, the volume of a cylinder. 

 Call this function from the main to test your program.  For example, you could test your program with the following values, 

 height 7.0cm and radius 4.0cm
 height 20.0cm and radius 3.0cm
 height 14.7cm and radius 5.2cm
 
 Which prints out, 
 
 the cylinder with height 7.0cm and radius 4.0cm has a volume of 351.86cm^3
'''

def volumeOfACylinder(height, radius):
  volume = math.pi * radius**2 * height
  volume = '{0:.2f}'.format(volume)
  print("the cylinder with height " + str(height) + "cm and radius " + str(radius)+  "cm has a volume of " + str(volume) + "cm^3")


print("Question 1\n");
printHelloWorld(5);

print("\nQuestion 2\n");
printXTenTimes(5);

print("\nQuestion 3\n");
convertMetricToImperialHeights(101);

print("\nQuestion 4\n");
fibonacci();

print("\nQuestion 5\n");
volumeOfACylinder(5, 10);
