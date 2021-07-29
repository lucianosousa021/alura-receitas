from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Alura_receita


# Create your views here.
def index(request):
    receitas = Receitas.objects.order_by('-data').filter(publicada=True)
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    receita_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_exibir)


def buscar(request):
    listas_receitas = Receitas.objects.order_by('-data').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if buscar:
            listas_receitas = listas_receitas.filter(
                nome_receita__icontains=nome_buscar)

    dados = {
        'receitas': listas_receitas
    }
    return render(request, 'buscar.html', dados)
