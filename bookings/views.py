from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# -----------------------
# DRF ViewSets (API)
# -----------------------

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# -----------------------
# Regular Django Views (HTML + forms)
# -----------------------

def movie_list(request):
    """Show all movies in an HTML template."""
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    """Handle seat selection & booking for a specific movie."""
    movie = get_object_or_404(Movie, id=movie_id)
    available_seats = Seat.objects.filter(movie=movie, is_booked=False)

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seats')
        for seat_id in selected_seats:
            seat = Seat.objects.get(id=seat_id)
            if not seat.is_booked:
                seat.is_booked = True
                seat.save()
                Booking.objects.create(movie=movie, seat=seat)

        return redirect('/booking-history/')

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': available_seats,
    })


def booking_history(request):
    """Show a list of all bookings."""
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})