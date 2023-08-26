from django.shortcuts import render,redirect
from .models import Contact,Blog
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

def blog(request):
    bl=Blog.objects.all()
    return render(request,'pages/blog.html',{'blogs':bl})