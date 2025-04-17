from django.shortcuts import render , redirect
from .models import Product, Category
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm
from django import forms

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request , 'home.html', {'products': products})

def about(request):
    return render(request , 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request, ("Please Check the Credintials Again!!"))
            return redirect('login')
    else:
        return render(request , 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have be Logged Out "))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login User
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, ("You have Registered Sucessfully, WELCOME !! "))
            return redirect('home')
        else:
            messages.success(request, ("OOPS!! , Please Try again with The Registration "))
            return redirect('register')
    else:
        return render(request , 'register.html', {'form':form})


def update_password(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        #Did they Fill out The Form
        if request.method == 'POST':
            #Do stuff
            form = ChangePasswordForm(current_user,request.POST)
            # Is the Form Valid
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password Has Been Updated...")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('home')

   
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        
        if user_form.is_valid():
            user_form.save()
            
            login(request, current_user)
            messages.success(request, "User Has Been Updated!!")
            return redirect('home')
        return render(request, "update_user.html", {'user_form':user_form})
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('home')

    
    
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request , 'product.html', {'product': product})

""" def category(request , foo):
    # replace spaces with hyphens
    foo = foo.replace('-',' ')
    print(f"Category lookup for: {foo}")
    # Grab the Category from the url
    try:
        # Look Up for The Category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html',{'products':products, 'category':category})
        
    except:
        messages.success(request, ("OOPS!! , That Category Doen't Exists...... "))
        return redirect('home') """
    
def category(request, foo):
    try:
        category = Category.objects.get(name__iexact=foo.replace('-', ' '))
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        messages.error(request, "OOPS!! That Category Doesn't Exist...")
        return redirect('home')
    
def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html' , {"categories":categories})

    