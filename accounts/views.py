from django.shortcuts import render,redirect
from .forms import authenticationForm,profileForm,LoginForm
from .models import User,Profile

def authentications(request):
    login_form = LoginForm(request.POST or None)
    signup_form = authenticationForm(request.POST or None)
    if request.method == 'POST':
       if 'login_submit' in request.POST and login_form.is_valid():
            email = login_form.cleaned_data['email']
            request.session['email'] = email
            if User.objects.filter(email=email).exists():
                return redirect('profile')
            else:
                return redirect('signUp')
         
       elif 'signup_submit' in request.POST and signup_form.is_valid():
            signup_form.save()
            return redirect('signUp')
 

    context = {
        'form1': login_form,
        'form2': signup_form
    }
    return render(request, 'authentication/signUp.html', context)

def profile(request):
    email = request.session.get('email', None)
    if email:
        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()  
            profile = Profile.objects.filter(user=user)

            return render(request, 'profiles/profile.html', {'user': profile.first()})
        else:
           print("Error")
    
    return render(request, 'profiles/profile.html', {'user': None})

def settings(request):
    email = request.session.get('email', None)
    user = User.objects.get(email=email)  
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=user)
        if form.is_valid() :
            form.save()
            return redirect('profile') 
        else:
            print("not valid")
    else:
        form = profileForm(instance=user)
    return render(request, 'profiles/settings.html', {'form': form,'user':user})




