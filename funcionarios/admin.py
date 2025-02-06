from django.contrib import admin
from .models import Funcionario
from django.db import models
from django.forms import TextInput
from django.utils.safestring import mark_safe  # Para exibir a imagem

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'funcao', 'status', 'departamento', 'admissao', 'foto_preview')
    search_fields = ('nome', 'cpf', 'rg')
    list_filter = ('status', 'departamento')

    # Personalizar os campos do formulário do Django Admin
    formfield_overrides = {
        models.CharField: {'widget': admin.widgets.AdminTextInputWidget(attrs={'size': '30'})},
    }

    # Método para exibir a foto no admin
    def foto_preview(self, obj):
        if obj.foto:
            return mark_safe(f'<img src="{obj.foto.url}" width="50" height="50" style="border-radius: 50%;" />')
        return "Sem Foto"

    foto_preview.short_description = "Foto"
