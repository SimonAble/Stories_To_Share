from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#<<------------------LOGIN PAGE------------------>>
def login(request):

    return render(request, 'mainApp/login.html')


#<<------------------HOME PAGE------------------>>
def index(request):
    
    return render(request, 'mainApp/home.html')


#<<------------------WRITE PAGE------------------>>
def write(request):

    response = "Write Page"

    return HttpResponse(response)


#<<------------------EXPLORE PAGE------------------>>
def explore(request):

    response = "Explore Page"

    return HttpResponse(response)


#<<------------------PROFILE PAGE------------------>>
def profile(request):

    response = "Profile Page"

    return HttpResponse(response)





