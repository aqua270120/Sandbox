
def main():
    total = 0
    items = int(input("Number of items: "))
    for items in range(1, items+1):
        price = float(input("Price of item:  "))
        total = total+price
    print("Total price of {} is {}".format(items, total))
main()