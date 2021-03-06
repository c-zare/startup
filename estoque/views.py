from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from estoque.models import Estoque, Local, Categoria


def editar(request,estoque_id):
    estoque = Estoque.objects.get(id=estoque_id)
    return render(request, 'estoque_editar.html', { 'estoque' : estoque })

def exibir(request,estoque_id):
    estoque = Estoque.objects.get(id=estoque_id)
    return render(request, 'estoque_exibir.html', { 'estoque' : estoque })

def index(request, pesquisa_nome=''):
    estoque_list = Estoque.objects.filter(nome__contains=pesquisa_nome)
    paginator = Paginator(estoque_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        estoques = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        estoques = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        estoques = paginator.page(paginator.num_pages)

    return render(request, 'estoque_index.html', { 'estoques': estoques })

def novo(request):
    return render(request, 'estoque_novo.html')    