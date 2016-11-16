from django.shortcuts import render

# Create your views here.
def deposit(request):
	return render(request,"fundTracker/deposit.html",{})
	
def trackFund(request):
	return render(request,"fundTracker/trackFund.html",{})
	
def history(request):
	return render(request,"fundTracker/history.html",{})