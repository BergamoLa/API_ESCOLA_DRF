from django.db import models


class Aluno(models.Model):
    name = models.CharField(max_length=30)
    general_registration = models.CharField(max_length=9)
    document = models.CharField(max_length=11)
    birth_date = models.DateField(max_length=30)

    def __str__(self):
        return self.name


class Curso(models.Model):
    LEVEL = (("B", "Basic"), ("M", "Mid"), ("A", "Advance"))

    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1, choices=LEVEL, blank=False, null=False, default="B"
    )

    def __str__(self):
        return self.description


class Matricula(models.Model):
    PERIOD = (("M", "Morning"), ("E", "Evening"), ("N", "Nocturnal"))
    student = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    period = models.CharField(
        max_length=1, choices=PERIOD, blank=False, null=False, default="M"
    )
