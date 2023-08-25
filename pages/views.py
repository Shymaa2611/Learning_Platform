from django.shortcuts import render,redirect
from .models import Contact
from .forms import contactForm

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/aboutus.html')


def contact(request):
    if request.method=='POST':
        form=contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=contactForm()
    context={
        'form':form
    }
    return render(request,'pages/contact.html',context)
