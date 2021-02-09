from django.contrib import admin
from dota2App.models import Heroi, Item

class Herois(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Heroi, Herois)

class Itens(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    list_per_page = 20

admin.site.register(Item, Itens)