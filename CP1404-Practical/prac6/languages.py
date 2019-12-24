from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # create a list
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")

    # loop through the 3 languages
    for language in languages:
        if language.is_dynamic():

            # print out if its dynamically type
            print(language.name)


if __name__ == '__main__':
    main()
