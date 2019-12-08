def main():
    #create a while loop to ask input again if conditions given are not fullfilled
    while True:
        try:
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            if denominator > 0:
                fraction = numerator / denominator
                print(fraction)
            else:
                print("Your denominator must > 0, please try again")
        except ValueError:
            print("Your numerator must be a number ")
            continue
main()
