from django.contrib import admin

from escola.models import Aluno, Curso, Matricula


class Alunos(admin.ModelAdmin):
    list_display = ("id", "name", "general_registration", "document", "birth_date")
    list_display_links = ("id", "name")
    search_fields = ("document",)
    list_per_page = 20


admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ("id", "course_code", "description", "level")
    list_display_links = ("id", "course_code")
    search_fields = ("course_code",)
    list_per_page = 20


admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ("id", "student", "course", "period")
    list_display_links = ("id",)
    list_per_page = 20


admin.site.register(Matricula, Matriculas)
