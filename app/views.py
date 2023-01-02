from django.shortcuts import render

def loops(request):
    d={'name':'ashu'}
    return render(request,'loops.html',d)
