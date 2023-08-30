from django.shortcuts import render,redirect
from .forms import authenticationForm,profileForm


def signup(request):
    if request.method == 'POST':
        form =authenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('settings')
    else:
        form = authenticationForm
    return render(request, 'authentication/signUp.html', {'form': form})


def profile(request):
    return render(request,'profiles/profile.html')

def settings(request):
    if request.method=='POST':
        form=profileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=profileForm()
    return render(request,'profiles/settings.html',{'form':form})