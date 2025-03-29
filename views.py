from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth_login(request,new_user)
            return redirect('user:dashboard')
        else:
            return render(request,'user/register.html',{'form': form})
       
    else: 
        form = UserCreationForm()
        return render(request, 'user/register.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            new_user = form.get_user()
            auth_login(request,new_user)
            return redirect('user:dashboard') 
        else:
            return render(request,'user/login.html',{'form':form})

    form = AuthenticationForm()
    return render(request,'user/login.html',{'form': form})  

    
@login_required   
def dashboard_view(request):
    #if request.method =='POST':
     return render(request,'user/dashboard.html')   




def logout(request):
    auth_logout(request)
    return redirect('user:login')





def home(request):
    return render(request, 'home.html')



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user:dashboard')
        else:       
            messages.error(request, 'There was a problem changing your password.')    
            return render(request, 'user/change-password.html', {'form': form})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'user/change-password.html', {'form': form})
        



def test_email(request):
    send_mail(
        'Test Email from Django',
        'Hello! This is a test email sent from Django using Mailchimp SMTP.',
        'yadavbhumika98@gmail.com',
        ['yadavbhumika98@gmail.com'],  # Replace with recipient's email
        fail_silently=False,
    )
    return HttpResponse('Test email sent successfully!')