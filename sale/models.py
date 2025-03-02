from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commandes")
    produits = models.ManyToManyField(Produit, through="CommandeProduit")
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=[("en cours", "En cours"), ("livré", "Livré")], default="en cours")

    def __str__(self):
        return f"Commande {self.id} - {self.utilisateur.username}"

class CommandeProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite} (Commande {self.commande.id})"
