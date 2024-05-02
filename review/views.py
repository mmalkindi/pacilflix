from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Jason',
    }
    return render(request, "main_review.html", context)

def show_ulasan(request):
    return render(request, "ulasan.html")