from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from store.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import login as Login_process ,logout,authenticate


from django.contrib import messages
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('store')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                x=User.objects.filter(username=username)[0]
                x=Customer(user=x)
                x.save()
                messages.success(request, f'Your account has been created ! You are now able to login ')
                return redirect('login')

    context={'form':form}
    return render(request,'user/register.html',context)


def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            Login_process(request, user)
            return redirect('store')
        else:
             messages.info(request, 'Username OR password is incorrect')

    context={}
    return render(request,'user/login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('store')