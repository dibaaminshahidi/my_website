from cProfile import label
from distutils.log import error
from tkinter.tix import Form
from xml.parsers.expat import model
from django import forms
from pyrsistent import field
from .models import Review
from django.forms import ModelForm


# class Review_form(forms.Form):
#     first_name = forms.CharField(label = 'first-name', max_length= 100)
#     last_name = forms.CharField(label = 'last-name', max_length= 100)
#     email = forms.CharField(label = 'Email')
#     review = forms.CharField(label = 'Write your Review',
#                                                 widget = forms.Textarea(attrs={'class':'my_form'}))
    
class Review_form(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name','stars']        
        labels = {'first_name' : "your firstname"}
        error_messages = { 
            'stars' : {'min_value':'min error',
                        'max_value':'max error'}
        }
        # fields = '__all__'