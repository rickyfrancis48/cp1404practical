import prac_06.guitar
from prac_06.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        part = line.strip().split(',')
        guitar = Guitar(part[0], part[1], part[2])
        guitars.append(guitar)
    in_file.close()

    # Loop through and display all languages (using their str method)
    for guitar in guitars:
        print(guitar)


main()
