from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile.user=user
            profile.save()
        return redirect('login')
    else:
        form= UserRegisterForm()
        
    params={
        'form':form,

    }
    return render(request, 'django_registration/registration_form.html', params)

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {'title':'index'})


def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'user/userprofile.html', params)

def profile(request, user_id):

    profiles = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'user/userprofile.html',{"profiles":profiles})

