from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    return render(request,'mine/index.html',{})



def contact(request):

    if request.method == 'POST':
        print("It worked!!!!")

    return render(request,'mine/contact.html',{})

