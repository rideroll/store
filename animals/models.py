from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Animal(models.Model):
    KIND_CHOICES = (
        ('D', 'Dog'),
        ('C', 'Cat'),
    )

    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=20)
    image_url = models.URLField()
    description = models.TextField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f'{self.name} and I am {self.age}'