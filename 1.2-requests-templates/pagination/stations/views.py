import csv

from django.contrib.admin.templatetags.admin_list import pagination
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))





def bus_stations(request):

    # получите текущую страницу и передайте ее в контекст
    file = open(settings.BUS_STATION_CSV, mode='r', encoding="UTF-8")
    csv_reader = csv.DictReader(file)

    content = []


    for el in csv_reader:
        pattern_dict = {
            "Name": el.get("Name"),
            "Street": el.get("Street"),
            "District": el.get("District")
        }
        content.append(pattern_dict)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page
    }

    return render(request, 'stations/index.html', context)
