# Création d'interfaces avec PySide

## Exemple Classes

```Python
# Vehicule
class Vehicule(object):
    
    def __init__(self):
        self.est_demarre = False
        self.kilometre_parcouru = 0
    
    def demarrer(self):
        self.est_demarre = True

    def rouler(self, nombre_kilometre):
        if self.est_demarre:
            self.kilometre_parcouru += nombre_kilometre

# Moto
class Moto(Vehicule):

    def __init__(self):
        # Super init
        Vehicule.__init__(self)
        # Moto specific attribute
        self.casque_mis = False
    
    def mettre_son_casque(self):
        self.casque_mis = True
        
    def rouler(self, nombre_kilometre):
        if self.casque_mis:
            Vehicule.rouler(self, nombre_kilometre)

moto = Moto()
moto.mettre_son_casque()
moto.demarrer()
moto.rouler(5)
print moto.kilometre_parcouru
```
