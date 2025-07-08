from django.db import models
from datetime import date

# Create your models here.
class Tarefas(models.Model):
    title = models.CharField(max_length=100, null=False,blank=False, verbose_name='Título')
    created_date = models.DateField(auto_now_add=True, null=False,blank=False)
    deadline = models.DateField(null=False,blank=False, verbose_name='Data de entrega')
    finished_date = models.DateField(null=True, blank=False)

    class Meta:
        ordering = ["deadline"]
    
    def mark_has_complete(self):
        if not self.finished_date:
            self.finished_date = date.today()
            self.save()
