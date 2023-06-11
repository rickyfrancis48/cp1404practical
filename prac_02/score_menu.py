from random import random


def main():
    """score menu"""
    score = int()
    menu = """    (G)et a valid score
    (P)rint result 
    (S)how stars
    (Q)uit"""
    choice = display_menu(menu)
    while choice != "Q":
        if choice == "G":
            score = get_score(score)
        elif choice == "P":
            score = check_score(score)
            print(score)
        elif choice == "S":
            score = check_score(score)
            print_stars(score)
        else:
            print("Invalid response")
        choice = display_menu(menu)


def check_score(score):
    """checks if score has been selected"""
    if score == int():
        print("Please choose score")
        score = get_score(score)
    return score


def get_score(score):
    """Gets score from input"""
    score = int(input("Score: "))
    return score


def print_stars(score):
    """prints stars for score number"""
    print('*' * score)


def display_menu(menu):
    """displays menu and choice selection"""
    print(menu)
    choice = (input(">>> ").upper())
    return choice


main()
