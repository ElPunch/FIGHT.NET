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
        except:
            return HttpResponseBadRequest("Error al crear el evento")

class paginaView(View):
    def get(self, request):
        eventos = Eventos.objects.all().values()
        return render(request, 'eventos/index.html', {'eventos': eventos})
    
    
    def post(self, request):
    try:
        # Handle form data from HTML form submission
        eventos = Eventos.objects.create(
            nombre=request.POST.get("nombre"),
            descripcion=request.POST.get("descripcion", ""),
            localizacion=request.POST.get("localizacion"),
            organizador=request.POST.get("organizador"),
            disciplina=request.POST.get("disciplina"),
            usuario_id=1,  # You'll need to handle user authentication
            data=request.POST.get("data")
        )
        # Redirect to avoid form resubmission
        return redirect('/pagina/')
    except Exception as e:
        print(f"Error creating event: {str(e)}")  # For debugging
        eventos = Eventos.objects.all()
        return render(request, 'eventos/index.html', {'eventos': eventos})
    
