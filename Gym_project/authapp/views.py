from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Attendence, Contact, Membership, Enrollment, Trainer, Gallery, Attendence

 
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
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('/login')
    return render(request,"handlelogin.html")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/login')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phonenumber")
        description = request.POST.get("description")

        contact = Contact(name=name, email=email, phonenumber=phonenumber, description=description)
        contact.save()
        messages.info(request, "Your message has been sent successfully.")
        return redirect('/contact')

    return render(request,"contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to enroll.")
        return redirect('/login')
    Memberships = Membership.objects.all()
    Trainers = Trainer.objects.all()
    context={
        'Memberships': Memberships,
        'Trainers': Trainers,
    }
    if request.method == "POST":
        # selected_plan_id = request.POST.get("member")
        # membership = Membership.objects.get(id=selected_plan_id)
        # price = membership.price
        # plan_name = membership.plan

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        phonenumber = request.POST.get("phonenumber")       
        dob = request.POST.get("dob")   
        selected_trainer = request.POST.get("trainer")
        address = request.POST.get("address")  
        selected_plan = request.POST.get("member")  
        enrollment = Enrollment(fullname=fullname, email=email, gender=gender,phonenumber=phonenumber, dob=dob, 
                                selected_plan=selected_plan, selected_trainer=selected_trainer, 
                                address=address, )  
        enrollment.save()
        messages.info(request, "You have been enrolled successfully. Please wait for confirmation.")
        return redirect('/enroll')




    
    return render(request,"enroll.html",context)



def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to view your profile.")
        return redirect('/login')

    user_phone = request.user.username

    enrollments = Enrollment.objects.filter(phonenumber=user_phone)
    attendences = Attendence.objects.filter(phonenumber=user_phone).order_by('-selectdate')

    context = {
        'enrollments': enrollments,
        'attendences': attendences,
    }

    return render(request, "profile.html", context)

def gallery(request):
    images = Gallery.objects.all().order_by('-timestamp')
    context = {
        'images': images,
    }
    return render(request, "gallery.html", context)

from .models import Attendence, Trainer

def attendence(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in.")
        return redirect('/login')

    Trainers = Trainer.objects.all()

    if request.method == "POST":
        phonenumber = request.POST.get("phonenumber")
        trainer = request.POST.get("trainer")
        workout = request.POST.get("workout")
        login_time = request.POST.get("login")
        logout_time = request.POST.get("logout")

        Attendence.objects.create(
            phonenumber=phonenumber,
            trainedby=trainer,
            selectworkout=workout,
            login=login_time,
            logout=logout_time
        )

        messages.success(request, "Attendance marked successfully!")
        return redirect('/attendence')

    context = {
        "Trainers": Trainers
    }

    return render(request, "attendence.html", context)