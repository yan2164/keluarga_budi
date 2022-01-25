from django.db import models

# Create your models here.
class Person(models.Model):

    class JenisKelamin(models.TextChoices):
        L = 'laki-laki'
        P = 'perempuan'

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(choices=JenisKelamin.choices, max_length=9)

    def __str__(self) -> str:
        return super().__str__()