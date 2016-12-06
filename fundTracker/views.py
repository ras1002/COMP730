from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Fund, Transaction

# Create your views here.

@login_required
def deposit(request):
    context = {}
    f = Fund.objects.get(owner=request.user)
    if request.method == 'POST':
        post_deposit = float(request.POST.get("deposit"))
        post_date = request.POST.get("date")
        post_comment = request.POST.get("comment")
        if f.deposit(post_deposit):
            context['success'] = True
        else:
            context['error'] = True
    context['fund'] = f
    return render(request,"fundTracker/deposit.html",context)
		
@login_required
def add_transaction(request):
    context = {}
    f = Fund.objects.get(owner=request.user)
    context['fund'] = f
    if request.method =='POST':
        try:
            post_amount = float(request.POST.get("amount"))
        except ValueError:
            print("ValueError with post value ", request.POST.get("amount"))
            context['error'] = True
            return render(request, 'fundTracker/add_transaction.html', context)
        post_date = request.POST.get("date")
        post_category = request.POST.get("category")
        t = Transaction(amount=post_amount, date=post_date, category=post_category, fund=f)
        if t.process():
            context['success'] = True
            t.save()
        else:
            context['error'] = True
    return render(request, 'fundTracker/add_transaction.html', context)
	
@login_required
def trackFund(request):
    f = Fund.objects.get(owner=request.user)
    t = f.transaction_set.all().order_by('-date')
    return render(request,"fundTracker/trackFund.html",{'fund':f, 'transaction_list':t})

@login_required
def history(request):
	return render(request,"fundTracker/history.html",{})

@login_required
def fund_account(request):
    return render(request, 'fundTracker/fund_account.html', {})
	

