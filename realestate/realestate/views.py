from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from members.models import Members

def home(request):
    return render(request, 'home.html', {})

def terms_and_conditions(request):
    return render(request, 'terms-and-conditions.html', {})


def privacy_policy(request):
    return render(request, 'privacy_policy.html', {})

def invalid(request):
    return render(request, 'invalid.html', {})

def post_property(request):
    if(request.session.get('role')=='Agent'):
      return render(request, 'post_property.html')
    elif(request.session.get('role')=='Customer') :
      return redirect('./../invalid') 
    else :
      return redirect('./../login')


def signup(request):
    return render(request, 'sign-up.html', {})


def aboutus(request):
    return render(request, 'aboutus.html', {})

def services(request):
    return render(request, 'services.html', {})

def login(request):
    return render(request, 'login.html', {})

def changepassword(request):
    return render(request, 'changepassword.html', {})

def forgotpassword(request):
    return render(request, 'forgotpassword.html', {})

def profile(request):
    user = Members.objects.filter(mobile=request.session.get('mobile')).values().first()
    return render(request, 'profile.html', {'user': {"id":user['id'],"name":user['name'], "email":user['email'], "mobile":user['mobile'] }})

def updateprofile(request):
    user = Members.objects.filter(mobile=request.session.get('mobile')).values().first()
    return render(request,'updateprofile.html', {'user': {"id":user['id'],"name":user['name'], "email":user['email'], "mobile":user['mobile'] }})

def logout(request):
    request.session.clear()
    messages.error(request, "You have successfully logged out.")
    return redirect('./login') 

def register(request):
    name = request.POST['name']
    email = request.POST['email']
    password = '123456'
    phone = request.POST['phone']
    role = request.POST['role']
    gender = request.POST['gender']    
    if Members.objects.filter(mobile=phone).exists():
        messages.error(request, "This Phone is already in use. Please choose a different mobile number.")
        return redirect('./signup')
    else:
        user = Members(name=name, email=email, password=password, mobile=phone, role=role, gender=gender)
        user.save()
        messages.success(request, "User is Signed up successfully.")
        return redirect('./signup')
    
def loginaction(request):
    password = request.POST['password']
    phone = request.POST['phone']
    if Members.objects.filter(mobile=phone, password=password).exists():
        user = Members.objects.filter(mobile=phone).values().first()
        # print(user)
        # pdb.set_trace()
        if(user):
            request.session['id'] = user['id']
            request.session['name'] = user['name']
            request.session['email'] = user['email']
            request.session['mobile'] = phone
            request.session['role'] = user['role']
        return redirect('./')
    else:
       messages.error(request, "Login Failed. Invalid Credentials.")
       return redirect('./login')
    
def forgotpass(request):
     phone = request.POST['phone']
     if Members.objects.filter(mobile=phone).exists():
        user = Members.objects.filter(mobile=phone).values().first()
        return render(request, 'forgotpassword.html', { 'password': user['password'] })
     else:
        messages.error(request, "User is not found.")
        return redirect('./forgot-password')  
     
def updatedprofile(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    id = request.POST['id']
    e = Members.objects.get(id=id)
    e.name  = name
    e.email = email
    e.phone = phone
    e.save()
    messages.success(request, "User Updated Successfully.")
    return redirect('./update-profile')