from itertools import product
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

downloaded_shows = [['Parasite', 'rainbowbridge', '2024-01-01 23:57:28'],
    ['A Man Called Otto', 'rainbowbridge', '2024-01-02 14:13:05'],
    ['Pitch Perfect', 'rainbowbridge', '2024-01-03 19:13:02'],
    ['La La Land', 'rainbowbridge', '2024-01-04 11:10:45'],
    ['The Greatest Showman', 'rainbowbridge', '2024-01-05 20:01:51'],
    ['Jurassic World', 'kentangnyamekdi', '2024-02-01 12:54:22'],
    ['The Hunger Games: The Ballad of Songbirds & Snakes', 'kentangnyamekdi', '2024-03-01 10:40:48'],
    ['The Maze Runner', 'kentangnyamekdi', '2024-01-04 11:10:09'],
    ['Godzilla King of The Monsters', 'kentangnyamekdi', '2024-01-05 21:48:51'],
    ['Dune', 'kentangnyamekdi', '2024-01-06 12:30:58'],
    ['The Silent Sea', 'kentangnyamekdi', '2024-01-07 12:54:27'],
    ['Bridgerton', 'kentangnyamekdi', '2024-01-08 11:40:57'],
    ['WandaVision', 'cottonthedog', '2024-01-03 10:41:53'],
    ['Alice in Borderland', 'kodokronggeng', '2024-01-04 17:04:53'],
    ['Wednesdays', 'kodokronggeng', '2024-01-05 18:45:56'],
    ['Parasite', 'kodokronggeng', '2024-01-06 16:29:33'],
    ['A Man Called Otto', 'berkelapkelip', '2024-01-05 18:51:48'],
    ['Pitch Perfect', 'berkelapkelip', '2024-01-06 14:42:36'],
    ['La La Land', 'berkelapkelip', '2024-01-07 23:55:12'],
    ['The Greatest Showman', 'berkelapkelip', '2024-01-08 15:47:01'],
    ['Jurassic World', 'parahsihtamol', '2024-01-05 21:15:32'],
    ['The Hunger Games: The Ballad of Songbirds & Snakes', 'parahsihtamol', '2024-01-06 20:59:34'],
    ['The Maze Runner', 'parahsihtamol', '2024-01-07 14:36:09'],
    ['Godzilla King of The Monsters', 'aizadiguno', '2024-01-07 13:18:18'],
    ['Dune', 'aizadiguno', '2024-01-08 19:48:30'],
    ['The Silent Sea', 'aizadiguno', '2024-01-09 16:02:19'],
    ['Bridgerton', 'aizadiguno', '2024-01-10 11:27:20'],
    ['WandaVision', 'kudaponi11', '2024-01-08 21:48:37'],
    ['Alice in Borderland', 'kudaponi11', '2024-01-09 10:14:00'],
    ['Wednesdays', 'kudaponi11', '2024-01-10 22:27:53']]

def show_main(request):
    context = {
        'downloaded_shows': downloaded_shows,
    }

    return render(request, "download.html", context)

def show_xml(request):
    data = downloaded_shows
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = downloaded_shows
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = downloaded_shows
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = downloaded_shows
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_downloaded_show(request, id):
    data = "" # Belum implement

def delete_downloaded_show(request, id):
    data = "" # Belum implement