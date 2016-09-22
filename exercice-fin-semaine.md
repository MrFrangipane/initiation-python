# Outil Teapot

Creer deux modules Python pour fabriquer un outil de création de Teapot dans 3dsMax

L'interface doit ressembler à ceci

![Interface](/exo_interface.png)

## Evalutation

Vous serez évalués sur 

- Nommage des variables clair et concis
- Respect des conventions, espaces, tabulations, ... référez-vous au [PEP8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)
- Bonne séparation des modues d'interface et de creation d'objets
- Création de fonctions autonomes et courtes, au besoin

Aides 

- [Tutoriel sur les `Layouts`](http://zetcode.com/gui/pysidetutorial/layoutmanagement/)
- [Aide de la `QSpinBox`](https://srinikom.github.io/pyside-docs/PySide/QtGui/QSpinBox.html)
- [Aide du `QLabel`](https://srinikom.github.io/pyside-docs/PySide/QtGui/QLabel.html)

## Module `teapot.py`

Squelette du module

```Python
import MaxPlus


def create_teapot(position, rotation):
  pass


def create_teapot_circle(count, radius):
  pass
```

## Module `teapot_gui.py`

Squelette du module

```Python
from PySide import QtGui
import maxhelper
import teapot


class _GarbageCollectorProtector(object):
    protected_widgets = list()


class TeapotTool(maxhelper.MaxWidget):

    def __init__(self):
        # Initialise Classe Parente
        maxhelper.MaxWidget.__init__(self)
        # Initialise les elements d'interface
        self.init_ui()

    def init_ui(self):
        pass
      
    def button_pressed(self):
        pass

def main():
    # Creation du widget
    teapot_tool = TeapotTool()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(teapot_tool)
    # Affichage
    teapot_tool.show()


if __name__ == '__main__':
    main()
```

