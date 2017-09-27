import math
import MaxPlus


def createCube(length, width, height, position):
    """
    fonction creer un cube.
    la variable obj contient les infos de l'objet geometrique, ici une Box.
    on creer la variable Node qui est notre noeud lie au viewport et le lier a notre obj.
    on definit la longueur de l'objet.
    on definit la largeur de l'objet.
    on definit la hauteur de l'objet.
    on place notre box dans la scene grace a sa position.
    *position represente un ensemble de donnees x, y, z qui sont les coordonnees de l'objet dans la scene.
    la fonction renvoi notre node contenant la box creee au dessus.
    """
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Box)
    obj.ParameterBlock.length.Value = length
    obj.ParameterBlock.width.Value = width
    obj.ParameterBlock.Height.Value = height

    node = MaxPlus.Factory.CreateNode(obj)
    node.Position = MaxPlus.Point3(*position)

    return node


def compute_positions(spacing, width, length):
    """
    fonction de calcule des coordonnees de position de nos futures objets.
    on creer une liste vide qui contiendra nos positions.
    pour chaques lignes en Y en fonction du nombre width.
    on creer une ligne en X en fonction du nombre length.
    la variable x contient la position en x fois un espacement pour pas que les cubes soient les uns sur les autres.
    la variable y contient la position en y fois un espacement pour pas que les cubes soient les uns sur les autres.
    et on range ces infos dans notre liste de coordonnees x y z.
    A noter que Z est a 0 tout le temps car on veut que toutes les boites soit au sol; a 0 en Z donc.
    la fonction renvoi notre liste contenant les positions calculees.
    """
    positions = list()

    for ligne_y in range(width):
        for ligne_x in range(length):
            x = ligne_x * spacing
            y = ligne_y * spacing
            positions.append([x, y, 0.0])

    return positions


def set_height(node, height):
    """
    fonction pour definir/modifier la hauteur de notre box.
    obj recupere les parametres de la box via node.
    initialisation de la nouvelle valeur de hauteur de notre cube.
    """
    obj = node.GetBaseObject()
    obj.ParameterBlock.Height.SetValue(height)


def compute_heights(period, square_count, size_multiplier):
    """
    fonction de calcule des hauteurs pour l'animation.
    calcule de alpha qui correspond au nombre de fois que l'on va creer un point sur notre cerlce.
    pour ce faire, 2pi est multiplie par la periode (rayon du cerle ou les points sont calcules)
    le tout divise par le nombre de carres que l'ont a cree.
    on creer une liste vide qui va acceuille nos donnees de hauteurs.
    boucle qui, pour le nombre de carres (square_count), va calculer la hauteur de chaques point dans le cercle.
    pour obtenir la hauteur du point, il faut calculer sin(Angle * le num du carre).
    je multiplis cette valeur par sizeMultiplier pour agrandir
    les hauteurs car trop petite dans la scene plus de visibilite).
    on ajoute la hauteur dans la liste, les un apres les autres pendant la boucle.
    on renvoi ces infos a celui qui appelera cette fonction.
    """
    alpha = (2 * period * math.pi) / square_count
    heights = list()

    for i in range(0, square_count):
        height = (math.sin(alpha * i)) * size_multiplier
        heights.append(height)

    return heights

	
def animate_Boxes(boxes, period, square_count, frame_count, size_multiplier):
    """
    Fonction pour animer les boites.
    on recupere les hauteurs calculees dans une liste "heights".
    on active "autokey".
    pour chaque frames.
    truc chelou de max car pour lui, il y a 160 trucs ("ticks") dans une frame.
    On doit le mettre sans se poser de questions.
    pour chaques box crees.
    i nous permet d'incrementer de 1 notre lecture de la liste de hauteurs pour que les boites bouches
    (sinon elles sont animees mais la hauteur ne change pas donc inutile
    on defini donc notre nouvelle hauteur a notre box.
    je divise les hauteurs par 10 pour avoir plus de valeurs entre 0 et 1 plutot que entre 0 et 10
    car les valeurs de couleurs vont de 0 a 1.
    j'initialise la nouvelle couleur. ici avec des tons de rouge vers le noir
    """
    heights = compute_heights(period, square_count, size_multiplier)

    MaxPlus.Animation.SetAnimateButtonState(True)

    for frame_number in range(frame_count):

        MaxPlus.Animation.SetTime(frame_number * 160)

        for index, box in enumerate(boxes):
            i = (frame_number + index) % square_count
            set_height(box, heights[i])
            color_ratio = heights[i] / 10
            set_color(box,color_ratio,0,0)

    # on desactive "autokey"
    MaxPlus.Animation.SetAnimateButtonState(False)


def set_color(node, r, g, b):
    """
    fonction pour changer la couleur de l'objet
    changement de la couleur en specifiant notre node
    """
    node.SetWireColor(MaxPlus.Color(r, g, b))
	

if __name__ == '__main__':
    PERIOD = 1              # defini le nombre de fois que l'on va fair le tour du cerle dans le calcule des positions
    FRAME_COUNT = 50        # nombre de frames que l'on veut calculer l'animation
    SIZE_MULTIPLIER = 20    # pour changer de coefficient de hauteur (optionnel mais 10 est une bonne valeur)
    PADDING = 15            # espacement entre nos cubes (doit toujours etre superieur a la largeur du cube a savoir 10)
    BOX_WIDTH_COUNT = 20    # largeur de l'objet
    BOX_HEIGHT_COUNT = 20   # longeur de l'objet


    positions = compute_positions(PADDING, BOX_WIDTH_COUNT, BOX_HEIGHT_COUNT)  # calcule des positions des objets
    all_Boxes = list()  # creation d'une liste vide pour les boites

    for position in positions:  # creation des cubes en fonction des positions calculees precedement

        boxes = createCube(10, 10, 10, position)  # on creer le cube a tel position
        set_color(boxes, 1, 1, 1)  # on initialise la couleur en blanc
        all_Boxes.append(boxes)  # on remplit la liste des boites

    # on lance le calcule de l'animation des boites
    animate_Boxes(all_Boxes, PERIOD, BOX_HEIGHT_COUNT, FRAME_COUNT, SIZE_MULTIPLIER)
