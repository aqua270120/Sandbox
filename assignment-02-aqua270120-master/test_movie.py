"""(Incomplete) Tests for Movie class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    # TODO: Write tests to show this initialisation works
    print(initial_movie)
    assert initial_movie.title == "Thor: Ragnarok"
    assert initial_movie.category == "Comedy"
    assert initial_movie.year == 2017
    assert initial_movie.is_watched
    # TODO: Add more tests, as appropriate, for each method
    # Test check-unwatched:
    print("Test check unwatched:")
    print(initial_movie)
    initial_movie.check_unwatch()
    assert not initial_movie.is_watched
    print(initial_movie.is_watched)
    # Test check-watch
    print("Test check watched")
    initial_movie.check_watch()
    assert initial_movie.is_watched
    print(initial_movie.is_watched)
    print(initial_movie)


run_tests()
