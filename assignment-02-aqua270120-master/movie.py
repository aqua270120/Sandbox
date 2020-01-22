"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """..."""

    def __init__(self, title="", year=0, category="", is_watch=False):
        self.title = title
        self.category = category
        self.year = year
        self.is_watched = is_watch

    def __str__(self):
        return "{} - {} ({}) ({})".format(self.title, self.year, self.category,
                                          self.check_watch())

    def check_watch(self):
        """Changing movie to watch"""
        if self.is_watched:
            return "watched"
        return "unwatched"
