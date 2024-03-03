from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 != pass2:
            return redirect('signup')
        # myuser = User.objects.get(username=username)
        # if myuser is None:
        #     return redirect('signup')
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()
        return redirect('signin')
    return render(request, 'register/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password1']
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            return redirect('posts')
        else:
            return redirect('signin')
    return render(request, 'register/signin.html')

def signout(request):
    logout(request)
    return redirect('home')
def update(request):
    current_user = request.user
    data = {
        'username': current_user.username,
        'email': current_user.email,
    }
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        myuser = User.objects.get(pk=current_user.pk)
        myuser.username = username
        myuser.email = email
        myuser.save()
        return redirect('signin')


    return render(request, 'register/update.html', data)