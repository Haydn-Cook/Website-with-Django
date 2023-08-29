from django.shortcuts import render

# Create your views here.

def Homepage(request):
    '''
    displays hompage.html
    '''
    return render(request,'Homepage/Homepage.html')
