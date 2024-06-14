from django.db import models

# Create your models here.

class Industry(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Industries'


class Company(models.Model):
    name = models.CharField(max_length=150)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Person(models.Model):
    name = models.CharField(max_length=100)
    companies = models.ManyToManyField(Company)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Person'
