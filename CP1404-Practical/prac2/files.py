def main():
    OUTPUT_FILE = "name.txt"
    #program 1
    name = input("What is your name")
    out_file = open(OUTPUT_FILE, "w")
    print(name, file=out_file)
    out_file.close()

    #program 2
    in_file = open(OUTPUT_FILE, "r")
    name = in_file.read().strip()
    in_file.close()
    print("Your name is ", name)

    #program 3
    in_file = open("number.txt", "r+")
    total = 0
    for line in in_file:
        number = int(line)
        total += number

    in_file.close()
    print(total)
main()