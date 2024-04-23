from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# This function is defined/named 'main'
# The function takes in a request
# The function returns a HttpResponse which contains
# The string ("hello")
def main(request):
    return HttpResponse("<h1>Hello</h1>")
