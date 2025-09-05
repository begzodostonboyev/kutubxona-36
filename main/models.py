from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=255)
    kurs = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])
    kitobi_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    jinsi = models.CharField(max_length=255, choices=(('erkak','erkak'),('ayol','ayol')))
    tugulgan_sana = models.DateField(null=True, blank=True)
    kitob_soni = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=255)
    sahifa = models.IntegerField(null=True, blank=True)
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Admin(models.Model):
    ism = models.CharField(max_length=255)
    ish_boshlash = models.TimeField(blank=True, null=True)
    ish_tugashi = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.ism

class Record(models.Model):
    talabalar = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True)
    kitoblar = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True)
    adminlar = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    olingan_sana = models.DateTimeField(null=True, blank=True)
    berilgan_sana = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.talabalar} - {self.kitoblar} - {self.adminlar}"
