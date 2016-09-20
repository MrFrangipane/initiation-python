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
make_teapot(radius=20.0, segments=10, position=[0.0, 0.0, 5.0])
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
		angle_z = math.pi * (index % 2) + current_angle
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
