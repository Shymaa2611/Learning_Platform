from django.shortcuts import render,redirect
from .forms import authenticationForm


def signup(request):
    if request.method == 'POST':
        form =authenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('profile')
    else:
        form = authenticationForm
    return render(request, 'authentication/signUp.html', {'form': form})


def profile(request):
    return render(request,'profiles/profile.html')