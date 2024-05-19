from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("Hello, Duniyaaa!")
    return render(request,'website/index.html')

def About(request):
    return HttpResponse("kunal patil")


def Contact(request):
    return HttpResponse("9892885090")