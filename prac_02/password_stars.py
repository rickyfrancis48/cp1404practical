minimum_char: int = 8
password = str(input("Enter Password: "))
char_length = len(password)
while char_length < minimum_char:
    print("Invalid input. Try again.")
    password = input("Enter Password: ")
print('*' * char_length)
