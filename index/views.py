from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login,logout
from .models import itemmodel
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from . import forms
from datetime import datetime
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index:home')
    else:
        form = UserCreationForm()
    return render(request,'index/signuppage.html',{'form':form})
@login_required
def home(request,user_id):
    data =itemmodel.objects.filter(userid=user_id).order_by('date')
    # print(request)
    return render(request,'index/homepage.html', {"data" : data})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            current_user = request.user
            current_user = current_user.id
            return redirect('index:home',user_id = current_user)
    else:
        form = AuthenticationForm()
    return render(request,'index/loginpage.html',{'form':form})
def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('index:login')
@login_required
def additem_view(request):
    print(request)
    if request.method == 'POST' :
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        date = request.POST.get('date')
        userid = request.user.id
        new = itemmodel(
              userid = userid,
              name = name,
              quantity = quantity,
              date = date,
              status = status,
        )
        new.save()
        messages.success(request,'Your order has been placed.')
        # return redirect('index:home',user_id = userid)
    return render(request,'index/additem.html')
@login_required
def update_view(request,item_id):
    data= itemmodel.objects.get(id=item_id)
    form = forms.CreateItem(request.POST)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.userid = request.user.id
            # print(instance.status)
            instance.save()
            data.delete()
            return redirect('index:home',user_id = request.user.id)
    print(form.is_valid())
    return render(request,'index/update.html',{'data':data})

def filter_view(request):
    # print(request.POST)
    id=request.POST.get('date')
    print(id)
    if id:
        data = itemmodel.objects.filter(date=id,userid = request.user.id)
        return render(request, 'index/homepage.html' , {"data" : data})
    else :
        return redirect('index:home',user_id = request.user.id)
def delete_view(request,item_id):
    data = itemmodel.objects.get(id=item_id)
    data.delete()
    return redirect('index:home',user_id=request.user.id)
def edit(request,item_id):
    data= itemmodel.objects.get(id=item_id)
    print(data.date)
    data.date = data.date.strftime("%Y-%m-%d")
    print(data.date)
    return render(request, 'index/update.html', { 'data': data })
