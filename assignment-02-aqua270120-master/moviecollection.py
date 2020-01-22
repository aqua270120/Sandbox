from operator import attrgetter

from movie import Movie
import csv


class MovieCollection:
    def __init__(self):
        super().__init__()
        # create a list to contain movies
        movies = []
        self.movies = movies

    def add_movie(self, movie):
        # append new movie
        self.movies.append(movie)

    def get_number_watch_movies(self):
        # count number of watch movies
        unwatch_count = 0
        for movie in self.movies:
            if movie.is_watched:
                unwatch_count += 1
        return unwatch_count

    def get_number_unwatch_movies(self):
        # count number of unwatch movies
        watch_count = 0
        for movie in self.movies:
            if not movie.is_watched:
                watch_count += 1
        return watch_count

    def load_movies(self, file_name):
        # load movies from the csv file
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            list_movies = list(reader)
            for movie in list_movies:
                self.movies.append(Movie(title=movie[0], year=int(movie[1]), category=movie[2]
                                         , is_watch="w" in movie[3]))

    def save_movies(self, file_name):
        # save movies
        with open(file_name, "w", newline="") as csv_file:
            list_movies = csv.writer(csv_file)
            for movie in self.movies:
                list_movies.writerow([movie.title, movie.year, movie.category, "w" if movie.is_watched else "u"])

    def sort(self, key):
        # sort movie by key
        self.movies.sort(key=attrgetter(key))

    def __str__(self):
        # display movies
        for movie in self.movies:
            print(movie)
        return ""
