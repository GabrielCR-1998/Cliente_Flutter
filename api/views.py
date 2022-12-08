from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#modelos
from .models import Usuarios
from .models import Carreras
from .models import Cursos
from .models import Periodos
from .models import Grupos
from .models import Matricula


from .serializers import CarrerasSerializer


import json

@api_view(['GET'])
def obtenerCarreras(request):
    serializer = CarrerasSerializer(
        Carreras.objects.all(),
        many=True
    )
    
    return Response(
        serializer.data,status=status.HTTP_200_OK
    )

@api_view(['GET'])
def obtenerCursos(request,codigo_carrera):
    curso = list(Cursos.objects.filter(codigo_carrera_id=codigo_carrera).values())
    return JsonResponse(
        {
            'Cursos':curso
        }
    )
 
@api_view(['GET'])
def obtenerGrupos(request,codigo_curso): 
   grupos = list(Grupos.objects.filter(codigo_curso=codigo_curso).values())
   return Response(
        grupos,status=status.HTTP_200_OK
    )


#! depricated
@api_view(['GET'])
def obtenerMatricula(request,id):
   matricula = Matricula.objects.get(estudiante=id)
   carrera = model_to_dict(matricula.carrera)
   curso = model_to_dict(matricula.curso)
   grupo = model_to_dict(matricula.grupo)
   
   return JsonResponse(
    {
        'carrera':carrera,
        'curso':curso,
        'grupos':grupo
    }
   )
   
@api_view(['POST'])
def registrarMatricula(request):    
    datos = json.loads(request.body)
    grupo = Grupos.objects.get(idgrupo=datos['grupo_id'])
    carrera = Carreras.objects.get(codigo=datos['carrera_id'])
    curso = Cursos.objects.get(codigo=datos['curso_id'])
    estudiante = Usuarios.objects.get(identificacion=datos['estudiante_id'])

    Matricula.objects.create(
        grupo=grupo,
        carrera=carrera,
        curso=curso,
        estudiante=estudiante,
        tipomatricula=datos['tipomatricula']
    )

    return Response(Matricula.objects.all().values(),status=status.HTTP_201_CREATED)       

   


