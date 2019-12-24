class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """construct from a given values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """String format of output"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                           self.reflection, self.year)

    def is_dynamic(self):
        """determine if language is dynamic"""
        if self.typing == "Dynamic":
            return True

