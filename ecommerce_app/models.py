from django.db import models

# Create your models here.
class Article(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    quantite_stock = models.IntegerField(("Quantité en stock"))
    prix = models.FloatField(("Prix (FCFA)"))
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="Image de l'article")

    def __str__(self):
        return f"{self.nom} - {self.prix} XAF"