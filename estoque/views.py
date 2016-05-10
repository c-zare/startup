from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from estoque.models import Estoque, Local, Categoria

def index(request):
    estoque_list = Estoque.objects.all()
    paginator = Paginator(estoque_list, 12) # Show 25 contacts per page

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