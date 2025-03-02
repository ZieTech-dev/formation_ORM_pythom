# formation_ORM_pythom

# Guide Complet sur Django ORM

## 1. Utilisation de `related_name` en Django ORM

Le paramètre `related_name` permet de définir un nom personnalisé pour accéder aux objets liés dans une relation `ForeignKey` ou `ManyToManyField`.

### **Exemple :**
```python
from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')
```

Dans cet exemple, `related_name="likes"` permet d'accéder à tous les likes d'un article avec `article.likes.all()`.

---

## 2. Explication de `__gt` dans Django ORM

`__gt` est un lookup qui signifie "greater than" (strictement supérieur à).

### **Exemple :**
```python
produits_disponibles = Produit.objects.filter(stock__gt=0)
```
**SQL équivalent :**
```sql
SELECT * FROM produit WHERE stock > 0;
```

### **Autres lookups courants :**
| Lookup | Signification | Exemple Django ORM | Équivalent SQL |
|---------|--------------|-------------------|---------------|
| `__gt` | Supérieur à (`>`) | `stock__gt=10` | `WHERE stock > 10` |
| `__gte` | Supérieur ou égal (`>=`) | `stock__gte=10` | `WHERE stock >= 10` |
| `__lt` | Inférieur à (`<`) | `stock__lt=5` | `WHERE stock < 5` |
| `__lte` | Inférieur ou égal (`<=`) | `stock__lte=5` | `WHERE stock <= 5` |

---

## 3. Tri des objets avec `order_by()`

La méthode `order_by()` permet de trier les résultats d'une requête ORM.

### **Exemple :**
```python
commandes_triees = Commande.objects.order_by("-date_commande")
```
- `"date_commande"` : tri par ordre croissant.
- `"-date_commande"` : tri par ordre décroissant.

**SQL équivalent :**
```sql
SELECT * FROM commande ORDER BY date_commande DESC;
```

### **Autres exemples :**
```python
# Trier les produits par prix croissant
produits = Produit.objects.order_by("prix")

# Trier les produits par prix décroissant
produits = Produit.objects.order_by("-prix")
```

---

## 4. Utilisation de `annotate()` pour ajouter des champs calculés

La méthode `annotate()` permet d'ajouter des valeurs calculées à chaque objet d'une requête.

### **Exemple : Compter le nombre de commandes par utilisateur**
```python
from django.db.models import Count

utilisateurs_commandes = User.objects.annotate(nombre_commandes=Count("commandes"))
```

**SQL équivalent :**
```sql
SELECT user.*, COUNT(commande.id) AS nombre_commandes
FROM user
LEFT JOIN commande ON commande.utilisateur_id = user.id
GROUP BY user.id;
```

### **Affichage des résultats :**
```python
for utilisateur in utilisateurs_commandes:
    print(f"{utilisateur.username} a passé {utilisateur.nombre_commandes} commande(s).")
```

### **Autres cas d'utilisation de `annotate()` :**
```python
# Nombre de produits commandés par chaque utilisateur
utilisateurs_produits = User.objects.annotate(nombre_produits=Count("commandes__produits"))

# Nombre de commandes pour chaque produit
produits_commandes = Produit.objects.annotate(nombre_commandes=Count("commandeproduit"))

# Nombre total de produits commandés par commande
commandes = Commande.objects.annotate(total_produits=Count("produits"))
```

---

## **Conclusion**
- `related_name` permet d'accéder à des objets liés de manière plus intuitive.
- `__gt`, `__lt`, `__contains`, etc. sont des **lookups** pour filtrer les requêtes Django ORM.
- `order_by()` permet de **trier** les objets.
- `annotate()` permet d'ajouter des **champs calculés** à une requête.

**Tu veux un exercice pour pratiquer ces concepts ? 🚀**

