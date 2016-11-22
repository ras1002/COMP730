from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Fund

# Create your views here.

@login_required
def deposit(request):
    if request.method == 'POST':
        post_deposit = float(request.POST.get("deposit"))
        post_date = request.POST.get("date")
        post_comment = request.POST.get("comment")
        f = Fund.objects.get(owner=request.user)
        f.deposit(post_deposit)
    return render(request,"fundTracker/deposit.html",{})

@login_required
def trackFund(request):
    u = request.user
    f = Fund.objects.get(owner=u)
    t = f.transaction_set.all()
    return render(request,"fundTracker/trackFund.html",{'fund':f, 'transaction_list':t})

@login_required
def history(request):
	return render(request,"fundTracker/history.html",{})

@login_required
def fund_account(request):
    return render(request, 'fundTracker/fund_account.html', {})
