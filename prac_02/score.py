"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """grades score"""
    score = get_score()
    if score < 0 or score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")
    print(random.randint(0, 100))


def get_score():
    """Gets score for main function"""
    score = float(input("Enter score: "))
    return score


main()
