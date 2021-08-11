
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
# Create your views here.
from django.contrib.auth import authenticate, login, update_session_auth_hash,get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm,CustomUserChangeForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})
    # 들여쓰기 매우 중요합니다.




def password_change(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user,request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
    else:
        form = PasswordChangeForm(request.user)
        context ={
            "form":form
        }
        return render(request,"",context)

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('common:user', request.user.username)
    
    else:
	    form = CustomUserChangeForm(instance = request.user)
    
    return render(request, 'common/user_change.html', {'form':form})


@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            # 추가된 부분
            user = form.save()
            update_session_auth_hash(request, user)
            # 끝 
            return redirect('common:user', request.user.username)
    
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/password.html',{'form':form})

@login_required
def delete(request,id):
    user = get_object_or_404(User, pk = id)
    user.delete()
    return redirect('home')  


def user(request, username):
   
    user = get_object_or_404(get_user_model(), username = username)
    return render(request, 'common/user.html', {'user':user})
