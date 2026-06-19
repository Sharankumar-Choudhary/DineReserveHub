from django.shortcuts import render
from datetime import date

from users.models import User
from reservations.models import Reservation
from restaurants.models import TableModel


def dashboard(request):

    total_diners = User.objects.filter(
        role='DINER'
    ).count()

    total_reservations_today = Reservation.objects.filter(
        reservation_time__date=date.today()
    ).count()

    available_tables = TableModel.objects.filter(
        is_active=True
    ).count()

    context = {
        'total_diners': total_diners,
        'total_reservations_today': total_reservations_today,
        'available_tables': available_tables,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )