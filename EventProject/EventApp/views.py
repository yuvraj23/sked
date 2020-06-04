from django.shortcuts import render,redirect
from EventApp.forms import ChildDetailForm
from EventApp.forms import VolDetailForm
from EventApp.forms import DonDetailForm

# Create your views here.

def index(request):
    return render(request,'EventApp/index.html')

def about(request):
    return render(request,'EventApp/ABOUT.html')

def childdetail(request):
    form = ChildDetailForm
    if request.method=='POST':
        form=ChildDetailForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/thank')
    return render(request,'EventApp/childform.html',{'form':form})


def voldetail(request):
    form = VolDetailForm
    if request.method=='POST':
        form=VolDetailForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/thank')
    return render(request,'EventApp/volfrom.html',{'form':form})



def dondetail(request):
    form = DonDetailForm
    if request.method=='POST':
        form=DonDetailForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/thank')
    return render(request,'EventApp/donfrom.html',{'form':form})


def thank(request):
    return render(request,'EventApp/thank.html')
