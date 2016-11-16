from django.shortcuts import render

def home(request):
	return render(request, 'home1.html', {})
	
def piggybank(request):
	return render(request, 'piggybank.html', {})
	
def piggybankFundAccount(request):
	return render(request, 'piggybankFundAccount.html', {})
