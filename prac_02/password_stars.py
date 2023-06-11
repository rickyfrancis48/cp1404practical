def main():
    minimum_char: int = 4
    char_length = get_password(minimum_char)
    hide_password(char_length)


def hide_password(char_length):
    print('*' * char_length)


def get_password(minimum_char):
    password = str(input("Enter Password: "))
    char_length = len(password)
    while char_length < minimum_char:
        print("Invalid input. Try again.")
        password = input("Enter Password: ")
        char_length = len(password)
    return char_length


main()
