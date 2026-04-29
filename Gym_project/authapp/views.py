from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
# Create your views here.
def Home(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("usernumber")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if len(username) != 10 or not username.isdigit():
            messages.error(request, "Phone number must be 10 digits.")
            return redirect('/signup')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request, "Phone number already exists.")
                return redirect('/signup')
        except User.DoesNotExist:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email already exists.")
                return redirect('/signup')
        except User.DoesNotExist:
            pass

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()
        messages.success(request, "Your account has been successfully created, Login Please.")   
        return redirect('/login')

    return render(request,"signup.html")

def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("usernumber")
        pass1 = request.POST.get("pass1")

        myuser = authenticate(username=username, password=pass1)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('/login')
    return render(request,"handlelogin.html")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/login')