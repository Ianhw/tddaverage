import sys
"""
Program: average_scores.py
Author: ian Waddell
Last date modified: 01/27/20

This program takes the average score of a person then output it.
"""

def average():
    # Get input for scores
    # declare variables, use score1, score2, score3 in calculation

    print('Enter first score:')
    one = input()

    print('Enter second score:')
    two = input()

    print('Enter third score:')
    three = input()

    numone = int(one)
    if (numone < 0):
        print("Bad input, good-bye!")
        raise ValueError
        return ValueError
    try:
        numone < 0
    except :
        print("Do not enter a negative")
        raise ValueError


    numtwo = int(two)
    if (numtwo < 0):
        print("Bad input, good-bye!")
        raise ValueError
    try:
        numtwo < 0
    except :
        print("Do not enter a negative")
        raise ValueError
    numthree = int(three)
    if (numthree < 0):
        print("Bad input, good-bye!")
        raise ValueError
    try:
        numthree < 0
    except:
        print("Do not enter a negative")
        raise ValueError
    global average
    average = int(numone) + int(numtwo) + int(numthree)
    average = average/3
    average = int(average)
    print(average)
    return average



if __name__ == '__main__':


    print('Enter first name:')
    fn = input()
    print('Enter last name:')
    ln = input()
    print('Enter age:')
    age = input()

    average()

    print(ln, ", ", fn, " age: ", age, " average grade: ", average)