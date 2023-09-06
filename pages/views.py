from django.shortcuts import render,redirect
from .models import Contact,Blog
from .forms import contactForm
from .google_bard import get_response
from django.http import JsonResponse


def google_bard_response(request):
    response = get_response(request.GET.get('prompt'))
    return JsonResponse({'message': response})

def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/aboutus.html')

def chat(request):
    return render(request,'pages/chat.html')

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