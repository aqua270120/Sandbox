from prac8.taxi import Taxi
from prac8.silver_service_taxi import SilverServiceTaxis

taxis = [Taxi("Prius", 100), SilverServiceTaxis("Limo", 100, 2), SilverServiceTaxis("Hummer", 200, 4)]


def print_taxi(taxis):
    """Print taxis"""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def taxi_choice():
    """taxis validation"""
    global current_taxi
    try:
        choose_taxi = int(input("Choose taxi:"))
        if choose_taxi > 2:
            print("Invalid choice.Please try again")
            taxi_choice()
        elif choose_taxi < 0:
            print("No car exist")
            taxi_choice()
        else:
            current_taxi = taxis[choose_taxi]
            print(current_taxi)
    except ValueError:
        print("Oops! That was no valid number. Try again...")
        taxi_choice()


def drive_car():
    """Calculate trip cost """
    try:
        global trip_cost
        current_taxi.start_fare()
        distance_driven = float(input("Drive how far?"))
        current_taxi.drive(distance_driven)
        trip_cost = current_taxi.get_fare()
        print("Your {} trip cost you ${}".format(current_taxi.name, trip_cost))
    except ValueError:
        print("Oops! That was no valid number. Try again...")


def main():
    print("Let's drive!")
    total = 0
    while True:
        print("-----Menu-----")
        print("(C)- Choose taxi")
        print("(D)- Drive")
        print("(Q)- Quit")
        choice = input(">>> ").upper()
        if choice == "Q":
            print("Total trip cost: ${:.2f}".format(total))
            print("Taxis are now:")
            print_taxi(taxis)
            break
        elif choice == "C":
            print("Taxis available:")
            print_taxi(taxis)
            taxi_choice()
        elif choice == "D":
            drive_car()
            total += trip_cost
        else:
            print("Invalid menu choice! Please try again")
        print("Bill to date: ${:.2f}".format(total))


main()
