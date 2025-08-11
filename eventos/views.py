from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
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
        eventos = Eventos.objects.all()
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
    
    def put(self, request):
        try:
            # Obtener datos del cuerpo de la petición PUT
            body = json.loads(request.body.decode('utf-8'))
            
            # Obtener el ID del evento a actualizar
            evento_id = body.get('id')
            if not evento_id:
                return HttpResponseBadRequest("ID del evento es requerido")
            
            # Buscar el evento
            evento = get_object_or_404(Eventos, id=evento_id)
            
            # Actualizar los campos
            evento.nombre = body.get("nombre", evento.nombre)
            evento.descripcion = body.get("descripcion", evento.descripcion)
            evento.localizacion = body.get("localizacion", evento.localizacion)
            evento.organizador = body.get("organizador", evento.organizador)
            evento.disciplina = body.get("disciplina", evento.disciplina)
            
            # Actualizar usuario si se proporciona
            if "usuario" in body:
                evento.usuario_id = body["usuario"]
            
            # Actualizar fecha si se proporciona
            if "data" in body:
                evento.data = datetime.strptime(body["data"], '%Y-%m-%d %H:%M:%S')
            
            evento.save()
            
            return JsonResponse({
                'success': True,
                'message': 'Evento actualizado correctamente',
                'evento_id': evento.id
            })
            
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Formato JSON inválido")
        except ValueError as e:
            return HttpResponseBadRequest(f"Error en formato de fecha: {str(e)}")
        except Exception as e:
            return HttpResponseBadRequest(f"Error al actualizar el evento: {str(e)}")
    
    def delete(self, request):
        try:
            # Obtener datos del cuerpo de la petición DELETE
            body = json.loads(request.body.decode('utf-8'))
            
            # Obtener el ID del evento a eliminar
            evento_id = body.get('id')
            if not evento_id:
                return HttpResponseBadRequest("ID del evento es requerido")
            
            # Buscar y eliminar el evento
            evento = get_object_or_404(Eventos, id=evento_id)
            evento_nombre = evento.nombre  # Guardar el nombre para la respuesta
            evento.delete()
            
            return JsonResponse({
                'success': True,
                'message': f'Evento "{evento_nombre}" eliminado correctamente',
                'evento_id': evento_id
            })
            
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Formato JSON inválido")
        except Exception as e:
            return HttpResponseBadRequest(f"Error al eliminar el evento: {str(e)}")
    
