from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Goal
from .forms import GoalForm

import time
import decimal

# Create your views here.

@login_required
def goals(request):
	context = {}
	l = request.user.goal_set.all()
	context['goal_list'] = l
	return render(request, "goalTracker/goals.html", context)

@login_required
def add_goal(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.owner = request.user
            goal.save()
            return HttpResponseRedirect(reverse("goalTracker:goals"))
    else:
        form = GoalForm(user=request.user)
    context = {'form':form}
    return render(request, "goalTracker/add_goal.html", context)

@login_required
def edit_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if('delete' in request.POST):
            goal.delete()
            return HttpResponseRedirect(reverse("goalTracker:goals"))
        if form.is_valid():
            goal = form.save(commit=False)
            goal.owner = request.user
            goal.save()
            return HttpResponseRedirect(reverse("goalTracker:goals"))
    else:
        form = GoalForm(instance=goal, user=request.user)
    context= {'form':form}
    return render(request, "goalTracker/edit_goal.html", context)

@login_required
def add_to_piggybank(request, goal_id):
    context = {}
    goal = Goal.objects.get(id=goal_id)
    if request.method == "POST":
        post_amount = decimal.Decimal(request.POST.get("amount"))
        print("--------------------{}".format(post_amount))
        result = goal.add_savings(request.user, post_amount)
        if result:
            goal.save()
            return HttpResponseRedirect(reverse("goalTracker:goals"))
        else:
            context['error'] = True
    context['goal'] = goal
    return render(request, "goalTracker/add_to_piggybank.html", context)

