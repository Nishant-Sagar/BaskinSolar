from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'baskin/index.html')

def form(requests):
    return render(requests, 'baskin/form.html')
