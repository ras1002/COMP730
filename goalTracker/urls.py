from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^goals/$', views.goals, name="goals"),
    url(r'^add_goal/$', views.add_goal, name="add_goal"),
]
