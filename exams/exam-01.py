# dependencies
import math

# array printing method
def printArr(arr):
    [print(row) for row in arr]
    print()

# point class used for triangle class
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, other):
        return(math.hypot(self.x - other.x, self.y - other.y))

# Q1:
# A triangle is defined by the three vertices. Write the following functions of the Triangle class
# assuming that the Point class has already been written for you. You may add helper functions as needed.
class Triangle(object):

    # default constructor assigning (0, 0), (1, 0), and (0, 1) as vertices unless specified 
    def __init__(self, v1_x=0, v1_y=0, v2_x=1, v2_y=0, v3_x=0, v3_y=1):
        self.v1 = Point(v1_x, v1_y)
        self.v2 = Point(v2_x, v2_y)
        self.v3 = Point(v3_x, v3_y)

    # calculate and return the area of the triangle
    def area(self):
        a = self.v1.dist(self.v2)
        b = self.v1.dist(self.v3)
        return(a * b * 0.5)

    # return True if the triangle is an isosceles right angled triangle
    def isRight(self):
        return(-1)

    # calculate the return the perimeter of the triangle
    def perimeter(self):
        return(-1)
    
    # return True if a Point p is strictly inside the triangle or False otherwise
    def pointInside(self, p):
        return(-1)
    
# Q2:
# Given a 2D list filled with 0s and 1s, write the function largestRectangle() that finds the largest
# rectangle made up of only 1s and returns the area of this rectangle. You may solve this problem 
# iteratively.
# Example: 
# rect is a 2D list that is filled with 0s and 1s
# return an integer of the largest area of 1s
# rect = [
#   [0, 0, 0, 0, 0],
#   [0, 0, 1, 1, 0],
#   [0, 1, 1, 1, 0]
# ]
# largestRectangle(rect) => 4
def largestRectangle(grid):
    # get maximum area of histogram
    def maxAreaInHistogram(hist):
        stack = []
        largest = 0
        for index, height in enumerate(hist):
            last = None
            while(stack and stack[-1][1] > height):
                last = stack.pop()
                largest = max(largest, (index - last[0]) * last[1])
            if last is not None:
                stack.append((last[0], height))
            else:
                stack.append((index, height))
        index = len(hist)
        while stack:
            last = stack.pop()
            largest = max(largest, (index - last[0]) * last[1])
        return(largest)

    # convert grid into histogram
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == 1):
                grid[i][j] = grid[i - 1][j] + 1

    # find maximum area of each row of new histogram grid
    maxArea = max([maxAreaInHistogram(row) for row in grid])
    return(maxArea)


# Q3:
# Given n, it is easy to get the factorial of n. It might be a big number, but you can still compute it.
# However, the inverse problem is difficult. Given some largest number, n, write the function, 
# inverseFactorial(n), find x such that x! is equal to n. In other words 
# abs(x! - n) < abs((x - 1)! - n) and abs(x! - n) < abs((x + 1)! - n). You may use Python's 
# math.factorial() in your algorithm. Assume that n is a positive integer.
# inverseFactorial(40320) => 8
# inverseFactorial(115) => 5
def inverseFactorial(n):
    if(n == 1 or n == 2):
        return(n)
    lo = 0
    hi = n // 2
    while(lo < hi):
        x = (lo + hi) // 2
        xF = math.factorial(x)
        if(xF == n):
            return(x)
        elif(xF > n):
            hi = x
        else:
            lo = x
    return(-1)

# Q4:
# Given a string, s, return the length of the longest palindrome that is a substring of s. There could
# be two or more substrings that are the longest palindromes in s, then just return the length of any
# one. There are two edge cases that your function must be able to handle - the string s itself is a 
# palindrome or there is no substring of length 2 or greater that is a palindrome. The string s will
# only be lowercase letters.
# longestPalindrome("radar") => 5
# longestPalindrome("abcde") => 1
# longestPalindrome("babad") => 3
def longestPalindrome(string):
    # helper method to determine if string is a palindrome
    def isPalindrome(string):
        if(len(string) % 2 == 0):
            return(False)
        left = right = len(string) // 2
        while(left >= 0 and right < len(string)):
            if(string[left] != string[right]):
                return(False)
            left -= 1
            right += 1
        return(True)

    string = string.replace(" ", "")
    if(isPalindrome(string)):
        return(string)
    maxPalindrome = ""
    for Len in range(1, len(string)):
        for i in range(len(string) - Len + 1):
            j = i + Len - 1
            tempString = ""
            for k in range(i, j + 1):
                tempString += string[k]
            if(isPalindrome(tempString) and len(tempString) > len(maxPalindrome)):
                maxPalindrome = tempString
    return(maxPalindrome)

# Q5 :
# A group of friends wants to do a secret santa with each friend being assigned to another and no
# friend can be assigned to themselves (this is called derangement). The friends are named A, E, I,
# O, U, and Y. Additionally, E does not like Y and A does not like E and each will get bad gifts for
# the other if they have the opportunity to do so. Write the pairings() function that returns a list
# with all the assignments that do not assign any of the friends to themselves, nor pair E to Y or
# A to E. You may add helper functions as needed.
# Match the friends for secret santa
# friends = ["A", "E", "I", "O", "U", "Y"]
# pairings(friends) => ["E:I", "I:O", "O:U", "U:Y", "Y:A"]
def findPairings():
    print(f"Q5: Fix me\n")
    return(-1)

# EC:
# Trace Ackermann's function
# if m = 0,           f(m, n) => n + 1
# if m > 0 and n = 0, f(m, n) => f(m - 1, 1)
# if m > 0 and n > 0, f(m, n) => f(m - 1, f(m, n - 1))
def ackermann(m, n):
    if(m == 0):
        return(n + 1)
    else:
        if(n == 0):
            return(ackermann(m - 1, 1))
        else:
            return(ackermann(m - 1, ackermann(m, n - 1)))

def main():
    # Q1 - Python classes
    myTriangle = Triangle(0, 0, 2, 0, 0, 2)
    print(f"Q1: Fix me\n")

    # Q2 - Largest rectangle of 1s
    myArr = [
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1]
    ]
    print(f"Q2: The largest rectangle is {largestRectangle([[num for num in row] for row in myArr])} units\n")
    printArr(myArr)

    # Q3 - Longest palindrome in string
    myString = "asdaibohphobia"
    print(f"Q3: The longest palindrome in \"{myString}\" is \"{longestPalindrome(myString)}\"\n")

    # Q4 - Inverse factorial of integer
    n = 4
    n = math.factorial(n)
    print(f"Q4: The inverse factorial of {n} is {inverseFactorial(n)}\n")

    # Q5 - Subset problem
    print(f"{findPairings()}")

    # EC - Ackermann's function trace (n = 3)
    n = 4
    myGrid = [[ackermann(i, j) for j in range(n)] for i in range(n)]
    print(f"EC: The Ackermann function traced up to n = {n}\n")
    printArr(myGrid)

main()