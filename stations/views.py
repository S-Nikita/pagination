from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def read_data():
    bus_station_data = []
    with open('data-398-2018-08-30.csv', encoding='utf-8', newline='',) as f:
        reader = csv.DictReader(f)
        for row in reader:
            bus_station_dict = {}
            bus_station_dict['Name'] = row['Name']
            bus_station_dict['Street'] = row['Street']
            bus_station_dict['District'] = row['District']
            bus_station_data.append(bus_station_dict)
    return bus_station_data

CONTENT = read_data()

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 20)
    bus_stations = paginator.get_page(page_number)
    context = {
        'bus_stations': bus_stations,
        'page': bus_stations
    }
    return render(request, 'stations/index.html', context)
