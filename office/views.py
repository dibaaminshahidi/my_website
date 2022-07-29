# Create your views here.
from django.urls import reverse
from pydoc_data.topics import topics
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from matplotlib.style import context
from . import models
# Create your views here.
def list_patients(request):
    # var = {'user_logged_in' : True , 'num_list' : [1,2,3,4]}
    all_patients = models.Patient.objects.all()
    context_list = {'Patients':all_patients}
    return render(request,'office/index.html',context= context_list)
