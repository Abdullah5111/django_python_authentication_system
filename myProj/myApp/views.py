from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    return render(request, "myApp/index.html")

def signup(request):
    if(request.method == "POST"):
        username = request.POST.get('username', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')


        myUser = User.objects.create_user(username, email, password1)
        myUser.first_name = fname
        myUser.last_name = lname

        myUser.save()

        messages.success(request, "Account created successfully")
        
        return redirect('signin')


    return render(request, "myApp/signup.html")


def signin(request):
    if(request.method == "POST"):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '') 

        user = authenticate(username = username, password = password)

        if user is not None:
             login(request, user)
             fname = user.first_name
             messages.success(request, "Logged in successfully")
             return render (request, "myApp/index.html", {"fname": fname})
            
        else:
            messages.error(request, "Account not found")
            return redirect("home")

    return render(request, "myApp/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")