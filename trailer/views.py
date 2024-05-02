from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Jason',
    }
    return render(request, "main_trailer.html", context)

def show_trailer(request):
    return render(request, "trailer.html")

def show_trailer_old(request):
    return render(request, "trailer_previous.html")
