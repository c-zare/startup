from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^core/', include('core.urls'), name='core'),
    url(r'^estoque/', include('estoque.urls'), name='estoque'),
]