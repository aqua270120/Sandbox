"""..."""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class


from movie import Movie
from moviecollection import MovieCollection
import csv

"""
Replace the contents of this module docstring with your own details
Name:Nguyen le huy bao
Date started:29/11/2019
GitHub URL:https://github.com/JCUS-CP1404/assignment-01-aqua270120
"""


def print_list(my_collection):
    movies_watch = my_collection.get_number_watch_movies()
    movies_unwatch = my_collection.get_number_unwatch_movies()
    for i, movie_data in enumerate(my_collection.movies):
        if movie_data.is_watched:
            print(
                "{}. * {:<50s}   -{:5s}  ({})".format(i, movie_data.title, str(movie_data.year), movie_data.category))
        else:
            print(
                "{}.   {:<50s}   -{:5s}  ({})".format(i, movie_data.title, str(movie_data.year), movie_data.category))
    print("\t" + "{} movies watched, {} movies still to watch".format(movies_watch, movies_unwatch))


# title validation
def title_validation():
    title = input("Title: ")
    if title.isdigit() is True:
        print("Not a valid title input. Title can not be a number")
        print("Please try again!")
        return title_validation()
    elif len(title) == 0:
        print("Not a valid title input. Title can not be blanked")
        print("Please try again!")
        return title_validation()
    else:
        print(title.strip())
    return title.strip()


# year validation
def year_validation():
    current_year = 2020
    while True:
        try:
            year = int(input("Year:"))
        except ValueError:
            print("Not a valid year input. Please try again!")
            continue
        if year < 0:
            print("Not a valid year input. Year must be >= 0")
            print("Please try again!")
            continue
        elif year > current_year:
            print("Invalid year input. Movie's year can not exceed 2020")
            print("Please try again!")
            continue
        else:
            print(year)
            break
    return int(year)


# genre validation
def genre_validation():
    while True:
        genre = input("Category: ").capitalize()
        if genre not in ("Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"):
            print("Not a valid genre input.Please try again! ")
        else:
            print(genre)
            break
    return genre


# append new movie to the movie_list and sort by year
def append_movie(my_collection):
    title = title_validation()
    year = year_validation()
    genre = genre_validation()
    print("{} ({} from {}) added to movies list ".format(title, genre, year))
    my_collection.add_movie(Movie(title, year, genre, is_watch=False))


# check if there are movies to watch or not
def check_movie(my_collection):
    for movie in my_collection.movies:
        if not movie.is_watched:
            return False
    return True


# movies number validation
def movies_number(my_collection):
    while True:
        try:
            watch = int(input(">>>"))
        except ValueError:
            print("Invalid input. Enter a valid number")
            continue
        if watch < 0:
            print("Number must be >= 0")
            continue
        elif watch >= len(my_collection.movies):
            print("Invalid movie number")
        else:
            break
    return watch


# check if movie is watched or not
def watch_movie(my_collection):
    if check_movie(my_collection):
        print("No movies to watch")
    else:
        print("Enter the number of movie to mark as watched")
        watch = movies_number(my_collection)
        movie = my_collection.movies[watch]
        if movie.is_watched:
            print("You have already watch {}".format(movie.title))
        else:
            movie.is_watched = True
            print("{} from {} watched".format(movie.title, movie.year))


def main():
    print("Movies To Watch 2.0 - by Nguyen Le Huy Bao")
    movie_collection = MovieCollection()
    movie_collection.load_movies("movies.csv")
    print()
    while True:
        print("\t-----Menu-----")
        print("(L)- List movies ")
        print("(A)- Add new movies ")
        print("(W)- Watch a movie ")
        print("(Q)- Quit ")
        # ask user to choose to play or instructions or quit
        choice = input(">>> ").upper()
        if choice == "L":
            movie_collection.sort("title")
            print_list(movie_collection)
        elif choice == "A":
            append_movie(movie_collection)
        elif choice == "W":
            check_movie(movie_collection)
            watch_movie(movie_collection)
        elif choice == "Q":
            movie_collection.save_movies("movies.csv")
            print("{} movies saved to movies.csv".format(len(movie_collection.movies)))
            print("Thank you")
            break
        else:
            print("Invalid menu choice. Please try a again ")

    # write movies_list to the movies and also to reset movies file
    # with open("movies_backup.csv", "w") as movie_backup:
    #     movies_writer = csv.writer(movie_backup)
    #     for movies_data in movie_collection.movies:
    #         movies_writer.writerow(movies_data)


main()
