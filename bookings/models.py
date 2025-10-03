# bookings/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.DurationField()

    def __str__(self):
        return self.title


class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.IntegerField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"{self.movie.title} - Seat {self.seat_number} ({status})"


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.movie.title} - Seat {self.seat.seat_number}"