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

def update_profile(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.id)
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'prof_form': prof_form
    }

    return render(request, 'user/update_profile.html', context )