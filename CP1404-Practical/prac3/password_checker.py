MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
SPECIAL_CHARS_REQUIRED = True

def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")

    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input(">  ")
    while not(is_valid_password(password)):
        print("Invalid password")
        password = input(">  ")
    print("Your " + str(len(password)) + " character password is valid: " + password)

def is_valid_password(password):
    #determine whether the length of password is valid or not
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    lower = 0
    upper = 0
    number = 0
    special = 0
    for char in password:
        #count number, Uppercase,Lowercase and special character in password
        if char.isdigit():
            number += 1
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if char in SPECIAL_CHARACTERS:
            special += 1
    # if there is no lowercase, uppercase or number.Return false
    if lower == 0 or upper == 0 or number == 0:
        return False
    #if password requires special character but there is none of them.Return flase
    if SPECIAL_CHARS_REQUIRED:
        if special == 0:
            return False
    #valid password willl be print if the programme gets here
    return True


main()