from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^goals/$', views.goals, name="goals"),
]
