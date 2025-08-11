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
            evento = Eventos.objects.create(
                nombre=request.POST.get('nombre'),
                descripcion=request.POST.get('descripcion'),
                localizacion=request.POST.get('localizacion'),
                organizador=request.POST.get('organizador'),
                disciplina=request.POST.get('disciplina'),
                data=datetime.strptime(request.POST.get('data'), '%Y-%m-%d').date(),
                usuario_id=1  # Cambiar por el ID del usuario logueado
            )
            messages.success(request, f'Evento "{evento.nombre}" creado exitosamente!')
            return redirect('pagina_eventos')  # Redireccionar a la misma página
        except Exception as e:
            messages.error(request, f'Error al crear el evento: {str(e)}')
            return redirect('pagina_eventos')