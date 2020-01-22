"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from moviecollection import MovieCollection
from movie import Movie


class MoviesToWatchApp(App):
    """..."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movise = []

    def build(self):
        self.title = "Movies to watch 2.0 by Nguyen Le Huy Bao"
        self.root = Builder.load_file("app.kv")
        self.print_movies()
        return self.root

    def on_start(self):
        # start the program by loading movies from the csv file
        self.movie_collection.load_movies("movies.csv")
        # display movies list
        self.print_movies()
        # get the number of watch and unwatch movies
        self.count_unwatch_watch_movies()
        # set movie list sorted by title by default
        self.sort_list("title")

    def sort_list(self, key):
        self.movie_collection.sort(key)
        # update the movie list again everytime the list is sorted
        self.update_movie()

    def count_unwatch_watch_movies(self):
        # get number of watch and unwatch movies
        self.root.ids.movie_status.text = "To watch: " + str(self.movie_collection.get_number_unwatch_movies()) \
                                          + ".Watched: " + str(self.movie_collection.get_number_watch_movies())

    def print_movies(self):
        self.movise = self.movie_collection.movies
        # add button for each movie
        for movie in self.movise:
            if movie.is_watched:
                movie_button = Button(text="{} ({} from {}) watched".format(movie.title, movie.category, movie.year))
                # set background color for watched movies
                movie_button.background_color = (1, 2, 3, 3)
            else:
                movie_button = Button(text="{} ({} from {}) ".format(movie.title, movie.category, movie.year))
                # set background for unwatch movies
                movie_button.background_color = (0.5, 1.5, 2.5, 3.5)
            # create an button and assign movie to the btn
            movie_button.movie = movie
            # call the watch_movie function when the button is pressed
            movie_button.bind(on_press=self.watch_movie)
            # add button to the entry box id
            self.root.ids.entry_box.add_widget(movie_button)

    def title_validation(self, input_title):
        # if length of title = 0: display message error
        if not input_title.strip():
            self.pop_up_message("Your title must not be blank")
        else:
            return input_title

    def year_validation(self):
        try:
            current_year = 2020
            year = int(self.root.ids.input_year.text)
            # year = int(input_year)
            if year < 0:
                # self.pop_up_message("Year must be > 0")
                raise ValueError
            elif year > current_year:
                raise ValueError
            return int(year)
        except ValueError:
            self.pop_up_message("Not a valid year input. Please try again!")

    def genre_validation(self):
        category = self.root.ids.input_category.text
        if category in ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]:
            return category
        else:
            self.pop_up_message("Invalid genre.Please try again")

    def add_movie(self, title, category, year):
        # only add when all fields are provided
        if title and category and year:
            # title validation
            title_check = self.title_validation(title)
            # category validation
            category_check = self.genre_validation()
            # year validation
            year_check = self.year_validation()
            if title_check and category_check and year_check:
                # Format movie title
                separator = " "
                pretty_title_before = separator.join(title_check.split())
                pretty_title_after = pretty_title_before.title()
                # add new movie to movie list
                self.movie_collection.add_movie(Movie(pretty_title_after, year_check, category_check))
                # reload the list
                self.print_movies()
                # show a pop up message every time you successfully added a new movie
                self.pop_up_message("{} has been added to movie list".format(pretty_title_after))
                # clear text input
                self.clear_add_movie()
                # update movie list
                self.update_movie()
                # update count
                self.count_unwatch_watch_movies()
        else:
            self.pop_up_message("You need to fill in all the fields")

    def watch_movie(self, instance):
        right_now_movie = instance.movie
        # display a message at the bottom indicates the status of a movie
        if right_now_movie.is_watched:
            self.root.ids.output_message.text = "You need to watch {}".format(right_now_movie.title)
        else:
            self.root.ids.output_message.text = "You have unwatch {}".format(right_now_movie.title)
        # change between watch and unwatch
        right_now_movie.is_watched = not right_now_movie.is_watched
        # count again the number of watch and unwatch movies every time a movie is clicked
        self.count_unwatch_watch_movies()
        # change the background color of the movie
        self.update_movie()

    def update_movie(self):
        """Change the background color every time a movie is clicked"""
        self.root.ids.entry_box.clear_widgets()
        self.print_movies()

    def pop_up_message(self, text):
        """display a pop up message"""
        self.root.ids.show_message.text = text
        self.root.ids.popup.open()

    def close_pop_up_message(self):
        """Dismiss the pop up message"""
        self.root.ids.show_message.text = " "
        self.root.ids.popup.dismiss()

    def clear_add_movie(self):
        """Clear the text input"""
        self.root.ids.input_title.text = ""
        self.root.ids.input_year.text = ""
        self.root.ids.input_category.text = ""

    def on_stop(self):
        """End the GUI and save movies to movies.csv"""
        self.movie_collection.save_movies("movies.csv")


if __name__ == '__main__':
    MoviesToWatchApp().run()
