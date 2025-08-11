from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.shortcuts import render, redirect
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Eventos, Usuarios
from datetime import datetime

from django.shortcuts import render

# Create your views here.
class EventosView(View):
    @method_decorator(csrf_exempt, name='dispatch')
    def get (self, request):
        eventos = Eventos.objects.all().values()
        return JsonResponse(list(eventos), safe=False)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            eventos = Eventos.objects.create(
                nombre=data["nombre"],
                descripcion=data["descripcion"],
                localizacion=data["localizacion"],
                organizador=data["organizador"],
                disciplina=data["disciplina"],
                usuario_id=data["usuario"], 
                data=data["data"]
            )
            return JsonResponse({"mensaje": "Evento creado correctamente", "id": eventos.id})
        except Exception as e:
            return HttpResponseBadRequest("Error al crear el evento")

class paginaView(View):
    @method_decorator(csrf_exempt, name='dispatch')
    def get(self, request):
        eventos = Eventos.objects.all().values()
        return render(request, 'eventos/index.html', {'eventos': eventos})
    
    def post(self, request):
        try:
            data = request.POST
            evento = Eventos.objects.create(
                nombre=data["nombre"],
                descripcion=data["descripcion"],
                localizacion=data["localizacion"],
                organizador=data["organizador"],
                disciplina=data["disciplina"],
                usuario_id=data["usuario"], 
                data=datetime.strptime(data["data"], '%Y-%m-%d %H:%M:%S')
            )
            return redirect('pagina')
        except Exception as e:
            return HttpResponseBadRequest("Error al crear el evento")
    
