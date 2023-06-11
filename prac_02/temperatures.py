"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """Temperature conversion calculator"""
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            get_fahrenheit()
        elif choice == "F":
            get_celsius()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_fahrenheit():
    """Calculates fahrenheit from celsius """
    celsius_input = float(input("Celsius: "))
    fahrenheit = celsius_input * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def get_celsius():
    """Calculates celsius from fahrenheit"""
    fahrenheit_input = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit_input - 32)
    print(f"Result: {celsius: .2f} C")


main()
