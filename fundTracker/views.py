from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Fund

# Create your views here.
def deposit(request):
	return render(request,"fundTracker/deposit.html",{})
	
def trackFund(request):
    u = request.user
    f = Fund.objects.get(owner=u)
    t = f.transaction_set.all()
    return render(request,"fundTracker/trackFund.html",{'fund':f, 'transaction_list':t})

def history(request):
	return render(request,"fundTracker/history.html",{})

def fund_account(request):
    u = request.user
    return render(request, 'fundTracker/fund_account.html', {})
