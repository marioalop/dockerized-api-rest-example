from django.db import models


# Create your models here.
class Efemeride(models.Model):
    dia = models.DateField()
    cita = models.CharField(max_length=250, null=True, blank=True)

    @property
    def hoy(self):
        return self.cita

    @property
    def mes(self):
        month_data = Efemeride.objects.filter(dia__month=self.dia.month).order_by("dia__day")
        # return {i.dia.strftime("%d"): i.cita for i in month_data}
        data = {}
        for i in month_data:
            key = i.dia.strftime("%d")
            try:
                data[key] = data[key] + " // " + i.cita
            except KeyError:
                data[key] = i.cita
        return data




