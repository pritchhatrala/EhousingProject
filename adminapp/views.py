from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from myapp.models import *
from .models import *
from myapp.forms import *
from .forms import *


# Admin Logout
def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def admin_login(request):
    # ✅ Step 1: Check & Create predefined admin if not exists
    admin_email = 'admin@ehousing.com'
    admin_username = 'ehousingadmin'
    admin_password = 'admin123'

    if not User.objects.filter(username=admin_username).exists():
        User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password
        )

    # ✅ Step 2: Normal login process
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            users = User.objects.filter(email=email)

            if users.count() > 1:
                messages.error(request, "Multiple users found with this email address. Please use a unique email.")
                return render(request, 'adminapp/admin_login.html')

            user = users.first()

            if user and user.check_password(password) and user.is_staff:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid credentials or you are not an admin.")
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")

    return render(request, 'adminapp/admin_login.html')


@login_required(login_url='/admin_login/')
def admin_dashboard(request):
    return render(request, 'adminapp/admin_dashboard.html')

@login_required(login_url='/admin_login/')
def view_sellhouses(request):
    sellhouses = add_sellhouse.objects.all()
    return render(request, 'adminapp/view_sellhouses.html', {'sellhouses': sellhouses})

@login_required(login_url='/admin_login/')
def view_renthouses(request):
    renthouses = add_renthouse.objects.all()
    return render(request, 'adminapp/view_renthouses.html', {'renthouses': renthouses})

@login_required(login_url='/admin_login/')
def view_complaints(request):
    complaints = complaint.objects.all()
    return render(request, 'adminapp/view_complaints.html', {'complaints': complaints})


# all Delete View here 
def deletedata(request, id):
    stid = add_sellhouse.objects.get(id=id)
    stid.delete()
    return redirect("view_sellhouse")


def deleteRentdata(request,id):
    stid = add_renthouse.objects.get(id=id)
    stid.delete()
    return redirect("view_renthouse")

def deletecomplaint(request,id):
    stid = complaint.objects.get(id=id)
    stid.delete()
    return redirect("view_complaint")



# all update view here 
def updateSelldata(request, id):
    stid = add_sellhouse.objects.get(id=id)
    if request.method == "POST":
        form = updatesellForm(request.POST, request.FILES, instance=stid)
        if form.is_valid():
            form.save()
            print("Record Updated!")
            return redirect("view_sellhouse")
        else:
            print(form.errors)
    return render(request, "adminapp/update_sellhouse.html", {"house": stid})



def updateRentdata(request, id):
    stid = add_renthouse.objects.get(id=id)
    if request.method == "POST":
        form = updaterentForm(request.POST, request.FILES, instance=stid)
        if form.is_valid():
            form.save()
            print("Record Updated!")
            return redirect("view_renthouse")
        else:
            print(form.errors)
    return render(request, "adminapp/update_renthouse.html", {"house": stid})


def updateComplaintdata(request, id):
    stid = complaint.objects.get(id=id)
    if request.method == "POST":
        form = updateComplaintForm(request.POST, request.FILES, instance=stid)
        if form.is_valid():
            form.save()
            print("Record Updated!")
            return redirect("view_complaints")
        else:
            print(form.errors)
    return render(request, "adminapp/update_complaintdata.html", {"house": stid})




