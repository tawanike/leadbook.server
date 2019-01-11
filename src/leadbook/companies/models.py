from django.db import models

class Company(models.Model):
    name: models.T
    address:
    phone:

    def __str__(self):
        return self.name
