
'''
Question 1:

Write a function(s) that converts an octal number, represented as a string into its decimal value.
'''

def octalToDecimal(oct):
  # Powers of 8 from right to left
  oct = str(oct)
  decimal = 0
  power = 0
  for digit in reversed(oct):
    decimal += int(digit) * (8**power)
    power += 1
  return decimal


'''
Question 2: 

Write a function(s) that prints out a tree shape (see below). The function should take two arguments: a tree width and a trunk height. For example, the arguments 9 and 4 will print out a tree of width 9 and trunk length 4, as shown below:

    *
   ***
  *****
 *******
*********
   ***
   ***
   ***
   ***

You can assume that the width of the tree will be odd and hence every line will have an odd number of asterisks. The trunk will always have a width of three asterisks.
'''

def printTree(width, trunk):
  # Print Tree
  for row in range((width+1)//2):

    asts = 2 * row + 1
    spaces = (width - asts) // 2

    print(' ' * spaces + '*' * asts)

  # Print Trunk
  left_spaces = (width - 3) // 2
  for row in range(trunk):
    print(' ' * left_spaces + '***')


print(octalToDecimal(52))
printTree(5, 4)