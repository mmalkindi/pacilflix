from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Jason',
    }
    return render(request, "main_show.html", context)

def show_tayangan(request):
    return render(request, "tayangan.html")

def show_series(request):
    return render(request, "series.html")

def show_film(request):
    return render(request, "film.html")

def show_episode(request):
    return render(request, "episode.html")