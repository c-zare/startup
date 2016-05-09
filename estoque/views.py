from django.shortcuts import render
from estoque.models import Estoque, Local

def index(request):
	return render(request, 'estoque_index.html', { 'estoques' : Estoque.objects.all() } )
