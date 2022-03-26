from django.shortcuts import render,redirect
# authentication.
from django.contrib.auth import authenticate,login,logout

from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_logins(request):
    return render(request,'all_logins.html')

def donor_login(request):
    if request.method == "POST":
       u =  request.POST['emailid']
       p =  request.POST['password']
       user = authenticate(username=u,password=p)
       if user:
           login(request,user)
           error = "no"
       else:
           error = "yes"

    return render(request,'donor_login.html',locals())

def ngo_login(request):
    return render(request,'ngo_login.html')

def admin_login(request):
    return render(request,'admin_login.html')

def volunteer_login(request):
    return render(request,'volunteer_login.html')



def donor_reg(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        cnt = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        address = request.POST['address']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            Donor.objects.create(user=user,contact=cnt,userpic=userpic,address=address)
            error = "no"
        except:
            error = "yes"

    return render(request,'donor_reg.html')

def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request,'donor_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')

    user = request.user
    donor = Donor.objects.get(user=user)
    # if request.method == "POST":
    #     donationname = request.POST['donationname']
    #     donationpic  = request.FILES['donationpic']
    #     collectionloc = request.POST['collectionloc']
    #     description   = request.POST['description']
    #     try:
    #         Donation.objects.create(donor=donor)

    return render(request,'donate_now.html')