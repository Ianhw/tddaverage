
"""
Program: average_scores.py
Author: ian Waddell
Last date modified: 01/27/20

This program takes the average score of a person then output it.
"""

def average():
    # Get input for scores
    # declare variables, use score1, score2, score3 in calculation
    global average
    average = int(one) + int(two) + int(three)
    average = average/3
    average = str(round(average, 2))
    print(average)
    return average



if __name__ == '__main__':
    print('Enter first name:')
    fn = input()
    print('Enter last name:')
    ln = input()
    print('Enter age:')
    age = input()
    print('Enter first score:')
    one = input()
    int(one)
    print('Enter second score:')
    two = input()
    int(two)
    print('Enter third score:')
    three = input()
    int(three)

    average()

    print(ln, ", ", fn, " age: ", age, " average grade: ", average)