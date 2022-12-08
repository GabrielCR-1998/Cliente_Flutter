from django.urls import path


from .views import obtenerCarreras
from .views import obtenerCursos
from .views import obtenerGrupos
from .views import obtenerMatricula
from .views import registrarMatricula

urlpatterns = [
    path('obtenerCarreras/', obtenerCarreras),
    path('obtenerCursos/<str:codigo_carrera>/',obtenerCursos),
    path('obtenerGrupos/<str:codigo_curso>/',obtenerGrupos),
    path('registrarMatricula/',registrarMatricula),
    

    
]