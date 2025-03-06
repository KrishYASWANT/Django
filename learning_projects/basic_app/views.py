from django.shortcuts import render, redirect
from basic_app.form import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse  # Updated import
from basic_app.models import UserProfileInfo
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

# Added welcome
def welcome(request):
    return render(request  ,'basic_app/welcome.html', {'user': request.user})

@login_required
def update_profile_pic(request):
    if request.method == "POST" and request.FILES.get('profile_pic'):
        user_profile = UserProfileInfo.objects.get(user=request.user)  # ✅ Correct: Using the Model
        user_profile.profile_pic = request.FILES['profile_pic']
        user_profile.save()
        return redirect('basic_app:welcome')  # Redirect back to welcome page
    
    return redirect('basic_app:welcome')  # If no file is uploaded, stay on the same page

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) 

def registed(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form= UserForm()
        profile_form = UserProfileInfoForm()
    return render(request ,'basic_app/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})
    
def user_login(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('basic_app:welcome'))

                #return HttpResponseRedirect(reverse('welcome'))  #index -> welcome
            else:
                HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username : {} and Password : {}".format(username,password))
            return HttpResponse("Invalid Login Details Supplied")
    else:
        return render(request, 'basic_app/login.html',{})



            