from django.shortcuts import render
from .forms import User, UserForm, Userbase
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'home.html')

# @login_required
# def logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('home'))


def register(request):
    registered = False
    if request.method == 'POST':
        # get info from both forms
        user_form = Userbase(data=request.POST)
        profile_form = UserForm(data=request.POST)

        # check if forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            # hash password
            user.set_password(user.password)
            user.save()

            # deal with the custom fields
            profile = profile_form.save(commit=False)
            # sets one to one rship btn UserBase and Userform
            profile.user = user

            # manipulation
            if 'picture' in request.FILES:
                # stores the image in the media file FILES contains a dictionary of media DIRS
                # same thing is done for files
                profile.picture = request.FILES['profile_pics']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    # if it was not HTTP post, render the forms as blanks
    else:
        user_form = Userbase()
        profile_form = UserForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def logout(request):
    logout(request)
    return render(request,'home.html')


def login(request):
    if request.method == 'POST':
        # grabbing the fields
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate
        user = authenticate(username=username, password=password)
        # if user is in db
        if user:
            if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Your account is not active')
        else:
            return HttpResponse('Invalod login details')
    else:
        return render(request, 'login.html')
