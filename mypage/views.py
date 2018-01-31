from django.shortcuts import render
from mypage.forms import VistorForm

# Create your views here.
def firstpage(request):
    form = VistorForm()

    if request.method == "POST":
        form = VistorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'mypage.html', {'form':form})
        else:
            print('ERROR FORM INVALID')
    return render(request, 'mypage.html', {'form':form})
