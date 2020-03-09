from django.db import models


class Consultorio(models.Model):
    nombre = models.CharField(max_length=30, help_text='Nombre del consultorio')

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre

        super(Consultorio, self).save()

    class Meta:
        verbose_name_plural = "Consultorios"
