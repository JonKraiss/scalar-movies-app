from django.test import TestCase

from moviesapp.movies.models import Movie, Rating


class TestMovieRatings(TestCase):
    fixtures = ['movie.json']

    def setUp(self):
        self.movie = Movie.objects.get(pk=1)
        self.movie.rating_set.create(review='boring', score=1)
        self.movie.rating_set.create(review='great', score=5)
        self.movie.rating_set.create(review='okay', score=2)

    def test_rating_average(self):
        self.assertEqual(self.movie.get_average_rating(), 2.7)
