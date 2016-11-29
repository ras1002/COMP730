from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^goals/$', views.goals, name="goals"),
    url(r'^add_goal/$', views.add_goal, name="add_goal"),
    url(r'^add_to_piggbank/(?P<goal_id>[\d]+)/$', views.add_to_piggybank, name="add_to_piggybank"),
    url(r'^edit_goal/(?P<goal_id>[\d]+)/$', views.edit_goal, name="edit_goal"),
]
