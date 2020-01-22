"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False
    print("Test loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True
    #
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("AB", 1998, "Cartoon", False))
    print(movie_collection)
    #
    print("Test sorting - is_watch:")
    movie_collection.sort("title")
    print(movie_collection)

    # #
    print("Test saving movie:")
    movie_collection.save_movies("movies.csv")
    #
    print("Test unwatched count:")
    print(movie_collection.get_number_unwatch_movies())

    print("Test watched count:")
    print(movie_collection.get_number_watch_movies())


run_tests()
