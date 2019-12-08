
def main():
    for i in range(1, 21, 2):
        print(i, end=" ")
    print()
    print()
    for i in reversed(range(1, 21)):
        print(i, end=" ")
    print()
    for i in range(1, 11):
        print(i*10, end=" ")
    print()
    star = int(input("Choose a number you like"))

    for i in range(1,star+1):
        print("*", end="")
    print()
    for i in range(1, star+1):
        print()
        for j in range(1, i+1):
            print("*", end="")


main()