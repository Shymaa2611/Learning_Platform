from django.shortcuts import render,redirect
from .forms import authenticationForm,profileForm,LoginForm
from .models import User



""" def signup(request):
    if request.method == 'POST':
        form =authenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['username'] = form.cleaned_data['username']
            request.session['email'] = form.cleaned_data['email']
            request.session['password'] = form.cleaned_data['password']
            return redirect('settings')
    else:
        form = authenticationForm
    return render(request, 'authentication/signUp.html', {'form': form})
 """

def authentications(request):
    login_form = LoginForm(request.POST or None)
    signup_form = authenticationForm(request.POST or None)
    
    if request.method == 'POST':
        if 'login_submit' in request.POST and login_form.is_valid():
            email = login_form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                return redirect('profile')
            else:
                return redirect('signUp')
           
        elif 'signup_submit' in request.POST and signup_form.is_valid():
            signup_form.save()
            request.session['username'] = signup_form.cleaned_data['username']
            request.session['email'] = signup_form.cleaned_data['email']
            request.session['password'] = signup_form.cleaned_data['password']
            return redirect('profile')  

    context = {
        'form1': login_form,
        'form2': signup_form
    }
    return render(request, 'authentication/signUp.html', context)

def profile(request):
    username = request.session.get('username', None)
    email = request.session.get('email', None)
    password= request.session.get('password', None)
    return render(request,'profiles/profile.html',{'username':username,'password':password,'email':email})

def settings(request):
    username = request.session.get('username', None)
    email = request.session.get('email', None)
    password= request.session.get('password', None)
    if request.method=='POST':
        form=profileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=profileForm()
    return render(request,'profiles/settings.html',{'form':form,'username':username,'password':password,'email':email})