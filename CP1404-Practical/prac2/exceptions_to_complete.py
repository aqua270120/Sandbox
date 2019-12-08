def main():
    finished = False
    result = 0
    while not finished:
        try:
            result=int(input("Please enter a integer"))
            print("Valid result is:", result)
            break;
        except ValueError:
            print("Please enter a valid integer.")

main()