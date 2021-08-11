from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render
from .models import *

import random

def main(request):
    user = request.user
    ctx = {
        'user': user
    }
    return render(request, 'main.html', ctx)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            ctx = {
                'form': form,
                'error': 'username or password is incorrect'
            }
            return render(request, 'login.html', ctx)

    else:
        form = AuthenticationForm()
        ctx = {
            'form': form
        }
        return render(request, 'login.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            new_profile = Profile()
            new_profile.user = user
            new_profile.save()
            login(request, user)
            return redirect('/')
        else:
            form = RegisterForm()
            ctx = {
                'form': form,
                'error': 'username or password is incorrect'
            }
            return render(request, 'signup.html', ctx)

    else:
        form = RegisterForm()
        ctx = {
            'form': form
        }
        return render(request, 'signup.html', ctx)

def find(request):
    user = request.user
    userlist = list(User.objects.all())
    userlist.remove(user)
    
    randomuser = random.choice(userlist)

    ctx = {
        'randomuser': randomuser
    }

    return render(request, 'randomuser.html', ctx)

def follow(request, pk):
    user = request.user
    randomuser = User.objects.get(id = pk)
    randprofile = Profile.objects.get(user = randomuser)
    randprofile.notyet.add(user)
    randprofile.save()

    return redirect('/')

def mypage(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    notyetlist = list(profile.notyet.all())
    followers = list(profile.follower.all())
    followings = list(profile.following.all())
    cards = list(Player.objects.filter(user = user))
    ctx = {
        'profile' : profile, 
        'notyetlist': notyetlist,
        'followers': followers, 
        'followings': followings, 
        'cards': cards,
    }

    return render(request, 'mypage.html', ctx)

def accept(request, pk):
    user = request.user
    profile = Profile.objects.get(user = user)
    
    others = User.objects.get(id= pk)
    others_profile = Profile.objects.get(user = others)
    
    profile.follower.add(others)
    profile.notyet.remove(others)
    profile.save()

    others_profile.following.add(user)
    others_profile.save()
    return redirect('/')

def reject(request, pk):
    user = request.user
    profile = Profile.objects.get(user = user)
    
    others = User.objects.get(id= pk)
    others_profile = Profile.objects.get(user = others)
    
    profile.notyet.remove(others)
    profile.save()

    return redirect('/')


def find_card(request):
    user = request.user
    players = list(Player.objects.filter(user = None))
    player = random.choice(players)

    ctx = {
        'player': player
    }    

    return render(request, 'randomcard.html', ctx)


def get(request, pk):
    user = request.user
    card = Player.objects.get(id = pk)
    card.user = user
    card.save()

    return redirect('/')

def page(request, my_id, other_id):
    me = request.user
    other = User.objects.get(id = other_id)
    other_profile = Profile.objects.get(user = other)
    cards = list(Player.objects.filter(user = other))
    ctx = {
        'me': me, 
        'other' : other,
        'cards' : cards,

    }
    return render(request, "page.html", ctx)
    
def trade (request, pk):
    user = request.user
    tradeuser = User.objects.get(id = pk)
    tradecard = Player.objects.get(user = tradeuser)
    tradecard.trade.add(user)
    tradecard.save()

    return redirect ('/')

def tradepage (request):
    user = request.user
    cards = list(Player.objects.filter(user = user))
    ctx = {
        'cards': cards
    }

    return render (request, 'trade.html', ctx)