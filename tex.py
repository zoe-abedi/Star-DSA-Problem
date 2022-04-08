# Problem 1:
# Simple pyramid pattern
# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart(n)

Output
* 
* * 
* * * 
* * * * 
* * * * * 

# Problem 2:
Another Approach: 
Using List in Python 3, this could be done in a simpler way

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern
def pypart(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
 
# Driver Code
n = 5
pypart(n)
# Output
# *
# **
# ***
# ****
# *****
# After 180 degree rotation

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern
def pypart2(n):
     
    # number of spaces
    k = 2*n - 2
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 2
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart2(n)
#Output
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 


# Problem 3:
Printing Triangle

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern triangle
def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
triangle(n)
#Output
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 



#Problem 4:
#Number Pattern

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern of numbers
def numpat(n):
     
    # initialising starting number
    num = 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # re assigning num
        num = 1
     
        # inner loop to handle number of columns
            # values changing acc. to outer loop
        for j in range(0, i+1):
         
                # printing number
            print(num, end=" ")
         
            # incrementing number at each column
            num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver code
n = 5
numpat(n)
# Output
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 





# Problem 5:
# Numbers without reassigning

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern of numbers
def contnum(n):
     
    # initializing starting number
    num = 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # not re assigning num
        # num = 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing number
            print(num, end=" ")
         
            # incrementing number at each column
            num = num + 1
     
        # ending line after each row
        print("\r")
 
n = 5
 
# sending 5 as argument
# calling Function
contnum(n)
# Output
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 



# Problem 6:
# Character Pattern

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern of alphabets
def alphapat(n):
     
    # initializing value corresponding to 'A'
    # ASCII value
    num = 65
 
    # outer loop to handle number of rows
    # 5 in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # explicitly converting to char
            ch = chr(num)
         
            # printing char value
            print(ch, end=" ")
     
        # incrementing number
        num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
alphapat(n)
# Output
# A 
# B B 
# C C C 
# D D D D 
# E E E E E





# Problem 7: 
# Continuous Character pattern

# Python code 3.x to demonstrate star pattern
 
# Function to demonstrate printing pattern of alphabets
def  contalpha(n):
     
    # initializing value corresponding to 'A'
    # ASCII value
    num = 65
 
    # outer loop to handle number of rows
-   for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # explicitly converting to char
            ch = chr(num)
         
            # printing char value
            print(ch, end=" ")
         
            # incrementing at each column
            num = num +1
     
     
        # ending line after each row
        print("\r")
 
# Driver code
n = 5
contalpha(n)
# Output:
# A 
# B C 
# D E F 
# G H I J 
# K L M N O
