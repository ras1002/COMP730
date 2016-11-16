from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^deposit/', views.deposit, name="deposit"),
	url(r'^trackFund/', views.trackFund, name="trackFund"),
	url(r'^history/', views.history, name="history"),
]
