from django.test import TestCase

# Create your tests here.

from datetime import timedelta
from .models import Movie, Seat, Booking
from rest_framework.test import APIClient
from rest_framework import status

#test using my actual movie
class MovieModelTest(TestCase):
    def test_create_movie(self):
        #create a movie 
        movie = Movie.objects.create(
            title="How to Lose a Guy in 10 Days",
            description="A confident magazine writer attempts an experiment on dating while things take a turn.",
            release_date="2003-02-07",
            #timedelta because i was getting an error
            duration=timedelta(hours=1, minutes=56)
        )
        #chek existance
        self.assertEqual(movie.title, "How to Lose a Guy in 10 Days")
        self.assertFalse(movie.id is None)

#test using actual movie i put
class SeatModelTest(TestCase):
    def test_create_seat(self):
        #first we have to create a movie because the seats are linked
        movie = Movie.objects.create(
            title="Clueless",
            description="Cher, a Beverly Hills high schooler, learns about love, friendship, and self-awareness.",
            release_date="1995-07-19",
            duration=timedelta(hours=1, minutes=37)
        )
        #create seat for that movie
        seat = Seat.objects.create(movie=movie, seat_number=1, is_booked=False)
        self.assertEqual(seat.movie, movie)
        self.assertFalse(seat.is_booked)


class BookingModelTest(TestCase):
    def test_create_booking(self):
        movie = Movie.objects.create(
            title="10 Things I Hate About You",
            description="A witty teen rom-com where a rebellious girl meets her match.",
            release_date="1999-03-31",
            duration=timedelta(hours=1, minutes=37)
        )
        seat = Seat.objects.create(movie=movie, seat_number=2, is_booked=False)
        booking = Booking.objects.create(movie=movie, seat=seat)

        self.assertEqual(booking.movie, movie)
        self.assertEqual(booking.seat, seat)

#testing api endpoints, usedc help from chat this is using django rest framework to ensure it works

class MovieAPITest(TestCase):
    def setUp(self):
        #set up a test client
        self.client = APIClient()
        #create sample movie doesnt matter which one but i did use some of the same movies
        self.movie = Movie.objects.create(
            title="Enchanted",
            description="A fairytale princess ends up in New York City.",
            release_date="2007-11-21",
            #timedelta doesnt cause an error
            duration=timedelta(hours=1, minutes=47)
        )

    def test_movie_list_api(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_movie_api(self):
        data = {
            "title": "The Princess Diaries",
            "description": "A teenager in European kingdom.",
            "release_date": "2001-08-03",
            "duration": "02:00:00"
        }
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "The Princess Diaries")
