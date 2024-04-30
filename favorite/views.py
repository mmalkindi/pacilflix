from itertools import product
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

favorite_shows = [['Parasite', 'rainbowbridge', '2024-01-01 21:18:29'],
    ['The Hunger Games: The Ballad of Songbirds & Snakes', 'rainbowbridge', '2024-01-02 12:50:07'],
    ['Bridgerton', 'kentangnyamekdi', '2024-01-02 21:12:20'],
    ['La La Land', 'cottonthedog', '2024-01-03 22:43:57'],
    ['The Maze Runner', 'cottonthedog', '2024-01-04 15:57:18'],
    ['Pitch Perfect', 'cottonthedog', '2024-01-05 21:18:29'],
    ['Wednesdays', 'kodokronggeng', '2024-01-04 15:26:42'],
    ['The Silent Sea', 'berkelapkelip', '2024-01-05 17:16:15'],
    ['Alice in Borderland', 'berkelapkelip', '2024-01-06 15:26:42'],
    ['A Man Called Otto', 'berkelapkelip', '2024-01-07 18:17:47'],
    ['Dune', 'parahsihtamol', '2024-01-06 18:26:33'],
    ['Bridgerton', 'aizadiguno', '2024-01-07 22:27:29'],
    ['The Greatest Showman', 'aizadiguno', '2024-01-08 22:22:39'],
    ['WandaVision', 'aizadiguno', '2024-01-09 11:31:56'],
    ['Godzilla King of The Monsters', 'kudaponi11', '2024-01-08 21:07:15'],
    ['The Greatest Showman', 'kudaponi11', '2024-01-08 21:07:15']]

def show_main(request):
    context = {
        'favorite_shows': favorite_shows,
    }

    return render(request, "main.html", context)

def show_xml(request):
    data = favorite_shows
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = favorite_shows
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = favorite_shows
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = favorite_shows
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_favorite_show(request, id):
    data = "" # Belum implement

def delete_favorite_show(request, id):
    data = "" # Belum implement