"""
Emails
Estimate: 60 minutes
Actual:   90 minutes
"""


def main():
    emails = {}
    abort = False
    while not abort:
        email = input("Email: ")
        if email == "":
            abort = True
        else:
            split_names = get_name(email)
            joiner = " "
            full_name = joiner.join(split_names)
            answer = input(f"Is your name {full_name}? (Y/N) ")
            if answer == "y" or answer == "":
                name = full_name
            elif answer == "n":
                name = input("Name: ")
            else:
                print("Invalid response")
            emails.update({email: name})

    for person in emails:
        print(f"{emails[person]} ({person})")


def get_name(email):
    email_name = email.split("@")
    split_names = email_name[0].split(".")
    return split_names


main()
