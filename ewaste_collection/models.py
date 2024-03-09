# models.py

from django.db import models

class EWasteCollection(models.Model):
    waste_image = models.ImageField(upload_to='ewaste_images/')
    waste_type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    visible = models.BooleanField(default=False)  # Field to indicate visibility
    date_submitted = models.DateTimeField(auto_now_add=True)  # Field to store submission date

    def __str__(self):
        return f"{self.waste_type}"    

class ElectronicWasteType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name