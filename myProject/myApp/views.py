from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    context={}
    return render(request, 'myApp/index.html', context)



def subscribe(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        # Handle the subscription logic here
        return HttpResponse("Thank you for subscribing!")
    return redirect('index')  # Change 'index' to the name of your home page view if different



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you can add functionality to send an email or save the contact message
        return HttpResponse("Thank you for getting in touch!")
    
    # Redirect or render a page if necessary for GET requests
    return redirect('index')  # Change 'index' to the name of your home page view if different
