# Python appliqué à 3Ds Max

3Ds Max embarque un interpréteur Python, et les fonctionnalités de manipulation des objets 3D sont exposées dans
le module `MaxPlus`

[Documentation Autodesk](http://docs.autodesk.com/3DSMAX/16/ENU/3ds-Max-Python-API-Documentation/index.html)

## Création d'objet

### Exemple

[Exemple Autodesk](http://docs.autodesk.com/3DSMAX/16/ENU/3ds-Max-Python-API-Documentation/index.html?url=files/GUID-1AC35645-91D7-4DBE-9714-681C8CC8700F.htm,topicNumber=d30e920)

### Exercice

Créer une fonction qui créé une `teapot`

```Python
make_teapot(position=[0.0, 0.0, 5.0], rotation=[0.0, 0.0, 0.0])
```

Puis une fonction qui créé un cercle de `teapots`

```Python
teapot_circle(radius=20, count=7)
```

### Correction

```Python
import math
import MaxPlus

def create_teapot(position, rotation):
	# Create Geometry
	teapot_geometry = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Teapot)
	teapot_geometry.ParameterBlock.Radius.Value = 10.0
	teapot_geometry.ParameterBlock.Segs.Value = 4
	# Create Node
	teapot_node = MaxPlus.Factory.CreateNode(teapot_geometry)
	teapot_node.Position = MaxPlus.Point3(*position)
	# Set transform
	rotation_quat = MaxPlus.Quat()
	rotation_quat.SetEuler(*rotation)
	teapot_node.Rotation = rotation_quat
	# Return
	return teapot_node
	

def teapot_circle(radius, count):
	# Distribution Angle
	distribution_angle = 2 * math.pi / count
	# Each teapot
	for teapot_index in range(count):
		# Compute Angles
		current_angle = distribution_angle * teapot_index
		angle_z = math.pi * (teapot_index % 2) + current_angle
		# Compute position
		position_x = radius * math.cos(current_angle)
		position_y = radius * math.sin(current_angle)
		# New Teapot
		new_teapot = create_teapot([position_x, position_y, 0], [0, 0, angle_z])
		# Set Other Params
		new_teapot.SetName("Teapot_{index:03d}".format(index=teapot_index))
		new_teapot.SetWireColor(MaxPlus.Color(255 / count * teapot_index))

teapot_circle(radius=30, count=15)
```

## Intégration widget PySide

Pré-requis : Chapitre PySide

Exemple

```Python
import sys
from PySide import QtGui
import MaxPlus


class _GarbageCollectorProtector(object):
    protected_widgets = list()


class Example(QtGui.QWidget):

    def __init__(self):
        # Initialise Classe Parente
        QtGui.QWidget.__init__(self)
        # mouseMoveEvent meme si aucun bouton presse
        self.setMouseTracking(True)
        # Initialise les elements d'interface
        self.init_ui()

    def init_ui(self):
        # Place et taille
        self.setGeometry(300, 300, 250, 150)
        # Line
        self.line = QtGui.QLineEdit(parent=self)
        self.line.move(10, 10)
        # Button
        self.button = QtGui.QPushButton("Click me", parent=self)
        self.button.move(10, 40)
        self.button.pressed.connect(self.button_pressed)
        # Titre
        self.setWindowTitle('Example')

    def mouseMoveEvent(self, event):
        # Disable keyboard
        MaxPlus.CUI.DisableAccelerators()
        # Forward to parent class
        QtGui.QWidget.mouseMoveEvent(self, event)

    def button_pressed(self):
        print self.line.text()
        

def main():
    # Creation d'un widget
    example = Example()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(example)
    # Affichage
    example.show()


if __name__ == '__main__':
    main()
```
