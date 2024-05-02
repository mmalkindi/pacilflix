from django.shortcuts import render

# Create your views here.

contributors = [['nabila', ' '], ['aulia', ' '], ['zainina', ' '], ['fikri', ' '], ['gilang', ' '], ['karina', ' '], ['haikal', ' '], 
                ['hilmi', ' '], ['rastanti', ' '], ['kent', ' '], ['dinda', ' '], ['kelvin', ' '], ['adiguno', ' '], ['kirana', ' '], 
                ['rafif', ' '], ['khairunnisa', ' '], ['aiza', ' '], ['bonaparte', ' '], ['firmansyah', ' '], ['deriysana', ' '], 
                ['elizabeth', ' '], ['apriano', ' '], ['millian', ' '], ['amanda', ' '], ['alkindi', ' '], ['jessica', ' '], ['reza', ' '],
                ['roger', ' '], ['calista', ' '], ['sekar', ' '], ['prawira', ' '], ['nisrina', ' '], ['jason', ' '], ['florence', ' '], 
                ['elena', ' '], ['winata', ' '], ['moreno', ' '], ['amira', ' '], ['natanael', ' '], ['diego', ' '], ['akhyaari', ' '], 
                ['nabil', ' '], ['tiara', ' '], ['caesar', ' '], ['sofia', ' '], ['saputra', ' '], ['ester', ' '], ['kezia', ' '], 
                ['diva', ' '], ['brian', ' '], ['michelle', ' '], ['aaron', ' '], ['zidan', ' '], ['carissa', ' '], ['daffa', ' '], 
                ['davin', ' '], ['kilau', ' '], ['dimas', ' '], ['steven', ' '], ['fadhil', ' '], ['rumintang', ' '], 
                ['fathur', ' '], ['minji', ' '], ['iqbal', ' '], ['ramadhan', ' ']]

def show_main(request):
    context = {
        'contributors': contributors,
    }

    return render(request, "contributor.html", context)
