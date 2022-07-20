from django.urls import path
from . import views

app_name = 'first_app'
urlpatterns = [
    # # path('index',view= views.index), #static routing
    # path('<str:nth>/',view= views.index , name= 'first'), # dynamic routing
    # path('<int:n>',view= views.red), #redirect
    # path('<int:x>/<int:y>',view= views.add_result) # dynamic(more param) routing
    path('',views.example_view,name='example'), #domain.com/first_app
    # path('variable',views.var_view,name='variable'),
    path('test',views.test,name='test')

     #domain.com/first_app

]