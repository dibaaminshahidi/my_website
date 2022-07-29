from tkinter.tix import Form
from django import forms

class Review_form(forms.Form):
    first_name = forms.CharField(label = 'first-name', max_length= 100)
    last_name = forms.CharField(label = 'last-name', max_length= 100)
    email = forms.CharField(label = 'Email')
    review = forms.CharField(label = 'Write your Review')
