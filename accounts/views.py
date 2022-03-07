from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('homepage')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, "login.html")

# Signup
def register_view(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if request.POST['password'] == request.POST['confirm-password']:
            create_user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname,
            )
            create_user.save()
            return redirect('login')
        else:
            messages.info(
                request, 'Password and Confirm Password did not match')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Listing available users
@login_required(login_url="/login")
def userList(request):
    users = User.objects.all()
    context = {'user_list': users}
    return render(request, "users.html", context)

# Create users
@login_required(login_url="/login")
def createUser(request):
    if request.method == 'GET':
        return render(request, "add_user.html")
    else:
        firstname = request.POST['first-name-in']
        lastname = request.POST['last-name-in']
        username = request.POST['user-name-in']
        email = request.POST['email-in']
        password = request.POST['password']
        is_staff_in = request.POST.getlist('is_staff-in')
        is_staff_ad = str(is_staff_in[0])
        print(is_staff_ad)
        if is_staff_ad == "is_staff":
            create_user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname,
                is_staff=True,
            )
            create_user.save()
        else:
            create_user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname,
            )
    return render(request, "add_user.html")

# Update user
@login_required(login_url="/login")
def updateUser(request, id):
    if request.method == "POST":
        user = User.objects.get(id=id)
        firstname = request.POST['first-name-in']
        lastname = request.POST['last-name-in']
        username = request.POST['user-name-in']
        email = request.POST['email-in']
        user.first_name = firstname
        user.last_name = lastname
        user.username = username
        user.email = email
        user.save()
        messages.info(request, 'One User Updated Successfully.')
        return redirect('/users/list')
    else:
        userObj = User.objects.get(id=id)
        context = {"userObj": userObj}
        return render(request, "update_user.html", context)

# Delete user
@login_required(login_url="/login")
def deleteUser(request, id):
    user = user = User.objects.get(id=id)
    user.delete()
    messages.info(request, 'One User Updated Successfully.')
    return redirect('/users/list')
