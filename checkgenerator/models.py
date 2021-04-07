from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
CHECK_TYPES = (
    ('kitchen',),
    ('client'),
)

STATUS = (
    ('new'),
    ('rendered'),
    ('printed'),
)

class Printer(models.Model):
    name = models.CharField('Имя', max_length=128)
    api_key = models.CharField('API Ключ', max_length=32, unique=True)
    check_type = models.CharField('Тип чека', choices=CHECK_TYPES, max_length=7)
    point_id = models.IntegerField('Точка')

    def __str__(self):
        return self.name

class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField('Тип чека', choices=CHECK_TYPES, max_length=7)
    order = JSONField('Заказ')
    status = models.CharField('Статус', choices=STATUS, max_length=8)
    pdf_file = models.FileField('PDF файл')

    def __str__(self):
        return self.printer_id