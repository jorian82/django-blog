from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'basics':['If you want to contact me, please email me','jorge.rivera@ssde.com.mx']})
