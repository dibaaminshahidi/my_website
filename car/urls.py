from . import views
from django.urls import path
app_name = 'car'

urlpatterns = [
    path('review',view= views.review,name='Review'),
    path('thanks',view= views.thanks,name='Thanks'),

]