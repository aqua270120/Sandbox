from prac8.taxi import Taxi


class SilverServiceTaxis(Taxi):
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Calling the __str__ from the parent class """
        return "{} plus flag_fall of ${}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Calling the get_fare from the parent class plus with he plag_fall"""
        return self.flag_fall + super().get_fare()
