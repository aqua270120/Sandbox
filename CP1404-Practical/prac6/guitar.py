NOW_YEAR = 2019
AGE_VINTAGE = 50

class Guitar:
    """Storing guitar details"""
    def __init__(self, name="",  year=0, cost=0):
        """Initialise a Guitar"""
        self.name= name
        self.year= year
        self.cost= cost

    def __str__(self):
        """return a String"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age"""
        return NOW_YEAR - self.year

    def is_vintage(self):
        """check if the guitar is vintage or not"""
        return self.get_age() > AGE_VINTAGE