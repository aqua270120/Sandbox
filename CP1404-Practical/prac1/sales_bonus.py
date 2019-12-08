def main():
    """
    Program to calculate and display a user's bonus based on sales.
    If sales are under $1,000, the user gets a 10% bonus.
    If sales are $1,000 or over, the bonus is 15%.
    """

    while True:
        sales = float(input("Enter sales: $"))
        if sales < 1000:
            bonus = (sales * 10)/100
            print(" Your bonus is: $", round(bonus))
        if sales >= 1000:
            bonus = (sales*15)/100
            print(" Your bonus is: $", round(bonus))
        if sales <= 0:
            print("Invalid sales")
            break
main()