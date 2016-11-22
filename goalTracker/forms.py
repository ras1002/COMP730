from django.forms import ModelForm
from .models import Goal

class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['title','goal_amount','description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(GoalForm, self).__init__(*args, **kwargs)

