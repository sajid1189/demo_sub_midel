from django.db import models

# Create your models here.
class Base(models.Model):
    first = models.CharField(max_length=10)


class SubModel(Base):
    last = models.CharField(max_length=10)