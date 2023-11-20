from django.shortcuts import render

# Create your views here.

def forloop(request):
    d={'name':'gnaneswari'}
    return render(request,'forloop.html',d)


def blocklevel(request):
    d={'name':'gnaneswari'}
    return render(request,'blocklevel.html',d)
