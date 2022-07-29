import django
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import Review_form
# Create your views here.
def review(request):
    if request.method == 'POST':
        form = Review_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('car:Thanks'))
    else:
        form = Review_form()
    
    return render(request,'car/review.html',context = {'form':form})

def thanks(request):
    return render(request,'car/thanks.html')