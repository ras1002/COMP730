from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Goal
from .forms import GoalForm

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
