# Python appliqué à 3Ds Max

3Ds Max embarque un interpréteur Python, et les fonctionnalités de manipulation des objets 3D sont exposées dans
le module `MaxPlus`

[Documentation Autodesk](http://docs.autodesk.com/3DSMAX/16/ENU/3ds-Max-Python-API-Documentation/index.html)

## Création d'objet

[Exemple Autodesk](http://docs.autodesk.com/3DSMAX/16/ENU/3ds-Max-Python-API-Documentation/index.html)

## Exemple : Fonction `make_teapot`

```Python
# Import de MaxPlus (qui permet d'interagir avec 3dsMax)
import MaxPlus


# Fonction pour creer une teapot
def make_teapot(radius=20.0, segments=10, position=[0.0, 0.0, 0.0]):
    # Nouvelle Teapot
    teapot_geo = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Teapot)
    # Defini les attributs
    teapot_geo.ParameterBlock.Radius.Value = radius
    teapot_geo.ParameterBlock.Segs.Value = segments
    # Creer la node dans la scene
    teapot_node = MaxPlus.Factory.CreateNode(teapot_geo)
    # Deplace dans la scene
    teapot_node.Position = MaxPlus.Point3(position[0], position[1], position[2])
    # Renvoie la node
    return teapot_node

# Test la fonction
make_teapot()
```
