from django.shortcuts import render
from .models import Goal

# Create your views here.

def goals(request):
	context = {}
	l = Goal.objects.get(owner=request.user)
	context['goalList'] = l
	return render(request, "goalTracker/goals.html", context)
