from django.urls import reverse
from pydoc_data.topics import topics
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

# my_views = {
#     'first' : 'first page',
#     'second' : 'second page',
#     'last' : 'last page'
# }

# def index(request,nth):
#     try:
#         return HttpResponse(my_views[nth])
#     except:
#         raise(Http404('Not found'))
#         # return HttpResponseNotFound()

# def add_result(request,x,y):
#     result = f"{x} + {y} = {x+y}" 
#     return HttpResponse(result)


# def red(request,n):
#     my_views_list = list(my_views.keys())
#     nth = my_views_list[n]
#     print(nth)
#     return HttpResponseRedirect(reverse('first',args= [nth]))

def example_view(request):
    # var = {'user_logged_in' : True , 'num_list' : [1,2,3,4]}
    return render(request,'first_app/example.html')

# def var_view(request):
#     # var = {'user_logged_in' : True , 'num_list' : [1,2,3,4]}
#     return render(request,'first_app/variable.html')

def test(request):
    # var = {'user_logged_in' : True , 'num_list' : [1,2,3,4]}
    return render(request,'first_app/test.html')

