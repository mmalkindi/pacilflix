from django.shortcuts import render

# Create your views here.

contributors = [['nabila', 'penulis skenario', 'perempuan', 'indonesia'], ['aulia', 'penulis skenario', 'laki-laki', 'indonesia'], ['zainina', 'penulis skenario', 'perempuan', 'indonesia'], 
                ['jessica', 'pemain, sutradara',  'perempuan', 'indonesia'], ['reza', 'penulis skenario, pemain, sutradara', 'laki-laki', 'indonesia']
]

def show_main(request):
    context = {
        'contributors': contributors,
    }

    return render(request, "contributor.html", context)
