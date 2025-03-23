from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Téléphone")
    adresse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse")

    def __str__(self):
        return self.username
    
    
class Article(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    quantite_stock = models.IntegerField(("Quantité en stock"))
    prix = models.FloatField(("Prix (FCFA)"))
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="Image de l'article")

    def __str__(self):
        return f"{self.nom} - {self.prix} XAF"
    