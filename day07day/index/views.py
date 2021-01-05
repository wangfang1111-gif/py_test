from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
     #return  render(request,'myfirst.html')
    # return HttpResponse('hello world')

    return redirect('https://mail.iwhalecloud.com/')
