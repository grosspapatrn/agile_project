from django.db import models
from django.core.validators import MinLengthValidator


# creating a model
class Tag(models.Model):
    # creating some fields
    name = models.CharField(max_length=20, validators=[MinLengthValidator(4)])


    def __str__(self):
        return self.name