from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logging out

 
# Signup view
def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if email is already registered
            if User.objects.filter(username=email).exists():
                form.add_error('email', 'Email already registered.')
            else:
                # Create a new user
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                print("Signup successful!")
                # After successful signup, redirect to login page
                return redirect("login")
    else:
        form = signupForm()
    return render(request, "signup.html", {"form": form})

# Login view
def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)  
                print("Login successful!")
                return redirect("index")  
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = loginForm()
    return render(request, "login.html", {"form": form})

@login_required(login_url='/login/')
def index(request):
    houses = add_sellhouse.objects.all()[:3]
    renthouses = add_renthouse.objects.all()[:3]
    
    if request.method == "POST":
        form = sellhouseform(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            print("House successfully added!")
            return redirect('index')  
    else:
        form = sellhouseform()  

    return render(request, "index.html", {
        "user": request.user,
        "houses": houses,
        "form": form,
        "renthouses":renthouses,
    })

@login_required(login_url='/login/')
def complaint(request):
    if request.method == "POST":
        form = complaintform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Product added!")
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = complaintform()
    return render(request,"complaint.html", {'form':form})





@login_required(login_url='/login/')
def sellhouse(request):
    houses = add_sellhouse.objects.all()

    if request.method == 'POST':
        form = sellhouseform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
            return redirect("index")
        else:
            print(form.errors)
    else:
        form = sellhouseform() 

    return render(request, "sellhouse.html", {"form": form, "houses": houses})




@login_required(login_url='/login/')
def renthouse(request):
    houses = add_renthouse.objects.all()
    
    if request.method == 'POST':
        form = renthouseform(request.POST, request.FILES)  
        if form.is_valid():
            form.save() 
            print("Record Inserted!")
            return redirect("index")  
        else:
            print(form.errors)  

    else:
        form = renthouseform()
    return render(request, "renthouse.html", {"form": form, "houses":houses})



@login_required(login_url='/login/')
def contact(request):
    if request.method=='POST':
        form=contectform(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
        else:
            print(form.errors)
    return render(request,'contact.html')


@login_required(login_url='/login/')
def all_sellhouse(request):
    houses = add_sellhouse.objects.all()
    return render(request, "all_sellhouse.html", {'houses': houses})

@login_required(login_url='/login/')
def all_renthouse(request):
    houses = add_renthouse.objects.all()
    return render(request, "all_renthouse.html", {"houses": houses})




