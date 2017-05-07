from django.conf.urls import url
from footballers_app import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()),
	url(r'^list/$', views.ListFootballers.as_view()),
	url(r'^list/(?P<player>\d+)$', views.FootballerDetails.as_view())
]