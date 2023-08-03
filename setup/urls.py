from django.contrib import admin
from django.urls import path, include
from escola.views import (
    AlunosViewSet,
    CursosViewSet,
    ListaAlunosMatriculados,
    MatriculasViewSet,
    ListaMatriculasAlunos,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matriculas", MatriculasViewSet, basename="matriculas")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("aluno/<int:pk>/matriculas/", ListaMatriculasAlunos.as_view()),
    path("curso/<int:pk>/matriculas/", ListaAlunosMatriculados.as_view()),
]
