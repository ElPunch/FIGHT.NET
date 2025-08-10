from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Eventos, Usuarios

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
            eventos = Eventos.object.create(
                nombre=data["nombre"],
                descripcion=data["descripcion"],
                localizacion=data["localizacion"],
                organizador=data["organizador"],
                disciplina=data["disciplina"],
                usuario_id=data["usuario"], 
                data=data["data"]
            )
            return JsonResponse({"mensaje": "Evento creado correctamente", "id": eventos.id})
        except:
            return HttpResponseBadRequest("Error al crear el evento")


    """
    def get(self, request):
        data = {"respuesta": "hola mundo"}
        return JsonResponse(data)
    
    def post(self, request):
        try:
            body = json.loads(request.body)
        except:
            return HttpResponseBadRequest("Formato invalido")
        
        data = {
            "nombre": body.get("nombre"),
            "descripcion": body.get("descripcion"),
            "localizacion": body.get("localizacion"),
            "organizador": body.get("organizador"),
            "disciplina": body.get("disciplina"),
            "usuario": body.get("usuario"),
            "data": body.get("data")
        }

        return JsonResponse(data)
    """

class paginaView(View):
    def get(self, request):
        eventos = Eventos.objects.all().values()
        return render(request, 'eventos/index.html', {'eventos': eventos})