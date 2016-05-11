from django.conf.urls import url, include
from estoque import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^exibir/(?P<estoque_id>\d+$)', views.exibir, name='exibir'),
	url(r'^editar/(?P<estoque_id>\d+$)', views.editar, name='editar'),
	url(r'^novo/', views.novo, name='novo'),
]