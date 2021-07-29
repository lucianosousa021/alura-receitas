from django.contrib import admin
from .models import Alura_receita

# Register your models here.

#Alterar visulização no Django Admin
class ListandoReceitas(admin.ModelAdmin):
    #Adiciona colunas
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    #Permite que as colunas virem link
    list_display_links = ('id', 'nome_receita', 'categoria', 'tempo_preparo')
    #campo de buscas
    search_fields = ('nome_receita',)
    #lista de categorias
    list_filter = ('categoria',)
    #10 receitas por pagina
    list_per_page = 10
    #editar na tabela
    list_editable = ('publicada',)

admin.site.register(Alura_receita, ListandoReceitas)