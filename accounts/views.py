from django.contrib.auth.models import User,auth
from .models import *
from django.shortcuts import redirect, render
from django.contrib import messages

def register(request):
    if request.method =='POST':
        Username = request.POST["username"]
        Firstname = request.POST["firstname"]
        Lastname = request.POST["lastname"]
        mail = request.POST["email"]
        Passwd1 = request.POST["password1"]
        Passwd2 = request.POST["password2"]

        if Passwd1 == Passwd2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"Username Exists!")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"Email already taken!")
                return redirect('register')
            else:
                obj = User.objects.create_user(username=Username,first_name=Firstname,last_name=Lastname,email=mail,password=Passwd1)
                obj.save()
                return redirect('login')
        else:
            messages.info(request,"Passwords does not match!")
            return redirect('/')
    else:
        return render(request,'register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['userName']
        passwd = request.POST['passWord']
        user = auth.authenticate(username=username,password=passwd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Username or Password")
            return('login')
    else:
        return render(request, 'login.html')
    
def userLogout(request):
    auth.logout(request)
    return redirect('/')

# Getting Session Data

# def getSession_AccData(request,key):
#     if request.user.is_authenticated():
#         username = request.user.username
#         try:
#             record = Acc_Data.objects.get(username=username, key=key)
#             return record.value
#         except :
#             return None

#     elif key in request.session.keys():
#         return request.session[key]
#     else:
#         return None

# def setSession_AccData(request, key, value):
#     if request.user.is_authenticated():
#         username = request.user.username
#         try:
#             record = Acc_Data.objects.get(username=username, key=key)
#             record.value = value
#             record.save()
#         except Acc_Data.DoesNotExist:
#             record = Acc_Data(username=username, key=key, value=value)
#             record.save()

#     else:
#         request.session[key] = value

# def deleteSessionOrAccountData(request, key):
#     if request.user.is_authenticated():
#         username = request.user.username
#         Acc_Data.objects.filter(username=username).filter(key=key).delete()
#     else:
#         del request.session[key]


# # save all existing session data to new user account
    
#     for key in request.session.keys():
#         record = Acc_Data(username=request.POST['username'], key=key, value=str(request.session[key]))
#         record.save()
