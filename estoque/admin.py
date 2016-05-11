from django.contrib import admin

# Register your models here.
from estoque.models import Local, Categoria, Estoque

admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Estoque)