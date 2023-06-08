from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from form_app.models import Account

from form_app.EmailBackend import EmailBackEnd

# Create your views here.
def test(request):
    return render(request,"test.html")

def main(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def dashboard(request):
    return render(request,'dashboard.html')

def bms_home(request):
    return render(request,'bms-apply/bms-home.html')

def basic_form(request):
    return render(request,'bms-apply/fy_bms_form.html')

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponseRedirect("/home")
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def register_check(request):
    return render(request,"register_check.html")

def register_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        middle_name=request.POST.get("middle_name")
        last_name=request.POST.get("last_name")
        inhouse = request.POST.get('category') == '1'
        mobile_number=request.POST.get("mobile_number")
        address=request.POST.get("address")
        email=request.POST.get("email")
        username=request.POST.get("username")
        mother_first_name=request.POST.get("mother_first_name")
        father_first_name=request.POST.get("father_first_name")
        date=request.POST.get("date")
        date_object = datetime.strptime(date, "%d %B %Y")
        formatted_date = date_object.strftime("%Y-%m-%d")
        password=request.POST.get("password")
       
        user=Account.objects.create_user(first_name=first_name,middle_name=middle_name,last_name=last_name,inhouse=inhouse,mobile_number=mobile_number,address=address,email=email,username=username,mother_first_name=mother_first_name,father_first_name=father_first_name,dob=formatted_date,password=password)
        user.save()
        messages.success(request,"Account Created Successfully")
        return HttpResponseRedirect("/register_check")
        
            #messages.error(request,"Failed to create Account")
            #return HttpResponseRedirect("/register_check")
