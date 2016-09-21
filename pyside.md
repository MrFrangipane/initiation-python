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

## Exemple PySide

### Base

```Python
import sys
from PySide import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))        
    
        self.show()


def main():
    
    application = QtGui.QApplication(sys.argv)
    example_1 = Example()
    example_2 = Example()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()

```

### Avec Bouton

```Pyhton
import sys
from PySide import QtGui

class Example(QtGui.QWidget):
    def __init__(self, titre="Titre"):
        QtGui.QWidget.__init__(self)
        self.titre = titre
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(self.titre)
        self.setWindowIcon(QtGui.QIcon('web.png'))        
        
        self.le_bouton = QtGui.QPushButton("le bouton", parent=self)
        self.le_bouton.move(10, 25)
        self.le_bouton.pressed.connect(self.bouton_presse)
        
        self.show()

    def bouton_presse(self):
        print "SALUT ! je suis {titre}".format(titre=self.titre)

        
def main():
    application = QtGui.QApplication(sys.argv)
    example_1 = Example("Example 1")
    example_2 = Example("Exemple 2")
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
```
