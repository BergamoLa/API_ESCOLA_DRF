from rest_framework import serializers

from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["name", "general_registration", "document", "birth_date"]


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ["course_code", "description", "level"]

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []



class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source="course.description")
    period = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["course", "period"]
    def get_period(self, obj):
        return obj.get_period_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source="student.name")
    class Meta:
        model = Matricula
        fields = ["student_name"]


