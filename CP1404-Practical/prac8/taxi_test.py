from prac8.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi.price_per_km)
    print(taxi)
    print(taxi.get_fare())
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print(taxi.get_fare())


main()