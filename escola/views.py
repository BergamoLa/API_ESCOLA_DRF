from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import (
    AlunoSerializer,
    CursoSerializer,
    ListaAlunosMatriculadosSerializer,
    ListaMatriculasAlunoSerializer,
    MatriculaSerializer,
)


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as Matriculas"""

    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAlunos(generics.ListAPIView):
    """Listando as matriculas de um aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(student_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos Matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(course_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
