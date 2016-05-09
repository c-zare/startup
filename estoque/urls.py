from django.conf.urls import url, include
from estoque import views

urlpatterns = [
	url(r'^$', views.index, name='index')
]