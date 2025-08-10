from django.contrib import admin
from .models import Eventos, Usuarios

# Register your models here.
@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'localizacion', 'organizador', 'disciplina', 'data')
    

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'disciplina')
    