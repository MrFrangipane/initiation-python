import math
import random
import MaxPlus

def createCube(length, width, height, position):					#fonction créer un cube.
	obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Box) 	#la variable obj contient les infos de l'objet géometrique, ici une Box.
	node = MaxPlus.Factory.CreateNode(obj)							#on créer la variable Node qui est notre noeud lié au viewport et le lier a notre obj.
	obj.ParameterBlock.length.Value = length						#on définit la longueur de l'objet.
	obj.ParameterBlock.width.Value = width							#on définit la largeur de l'objet.
	obj.ParameterBlock.Height.Value = height						#on définit la hauteur de l'objet.
	node.Position = MaxPlus.Point3(*position)						#on place notre box dans la scene grace a sa position. *position représente un ensemble de données x, y, z qui sont les coordonnées de l'objet dans la scene.
	return node														#la fonction renvoi notre node contenant la box créer au dessus.
	
def compute_positions(espacement, width, length):	#fonction de calcule des coordonnées de position de nos futures objets.
	positions = list()								#on créer une liste vide qui contiendra nos positions.
	for ligneY in range(width):						#pour chaques lignes en Y en fonction du nombre width.
		for ligneX in range(length):				#on créer une ligne en X en fonction du nombre length.
			x = ligneX*espacement					#la variable x contient la position en x fois un espacement pour pas que les cubes soient les uns sur les autres.
			y = ligneY*espacement					#la variable y contient la position en y fois un espacement pour pas que les cubes soient les uns sur les autres.
			positions.append([x, y, 0.0])			#et on range ces infos dans notre liste de coordonnées x y z. A noter que Z est a 0 tout le temps car on veut que toutes les boites soit au sol; à 0 en Z donc.
	return positions								#la fonction renvoi notre liste contenant les positions calculées.

def set_height(node, height):					#fonction pour définir/modifier la hauteur de notre box.
	obj = node.GetBaseObject()					#obj récupere les parametres de la box via node.
	obj.ParameterBlock.Height.SetValue(height)	#initialisation de la nouvelle valeur de hauteur de notre cube.
	
def compute_heights(period,countCarres,sizeMultiplier):	#fonction de calcule des hauteurs pour l'animation.
	alpha = (2*period*math.pi) / countCarres			#calcule de alpha qui correspond au nombre de fois que l'on va créer un point sur notre cerlce. pour ce faire, 2pi est multiplié par la periode (rayon du cerle où les points sont calculés) le tout divisé par le nombre de carrés que l'ont a créé.
	heights = list()									#on créer une liste vide qui va acceuille nos données de hauteurs.
	for i in range(0,countCarres):						#boucle qui, pour le nombre de carrés (countCarres), va calculer la hauteur de chaques point dans le cercle.
		height = (math.sin(alpha * i))*sizeMultiplier	#pour obtenir la hauteur du point, il faut calculer sin(Angle * le num du carré). je multiplis cette valeur par sizeMultiplier pour agrandir les hauteurs car trop petite dans la scene plus de visibilité).
		heights.append(height)							#on ajoute la hauteur dans la liste, les un apres les autres pendant la boucle.
	return heights										#on renvoi ces infos à celui qui appelera cette fonction.

	
def animate_Boxes(Boxes, period, count_carres,frame_count,size_multiplier):	#Fonction pour animer les boites.
	heights = compute_heights(period, count_carres,size_multiplier)			#on récupere les hauteurs calculées dans une liste "heights".
	MaxPlus.Animation.SetAnimateButtonState(True)							#on active "autokey".
	for frame_number in range(frame_count):									#pour chaque frames.
		MaxPlus.Animation.SetTime(frame_number * 160)						#truc chelou de max car pour lui, il y a 160 trucs dans une frame. On doit le mettre sans se poser de questions.
		for index, Box in enumerate(Boxes):									#pour chaques box crées.
			i = (frame_number + index) % count_carres						#i nous permet d'incrémenter de 1 notre lecture de la liste de hauteurs pour que les boites bouches (sinon elles sont animé mais la hauteur ne change pas donc inutile
			set_height(Box, heights[i])										#on défini donc notre nouvelle hauteur à notre box.
			Color_Ratio = heights[i] / 10									#je divise les hauteurs par 10 pour avoir plus de valeurs entre 0 et 1 plutot que entre 0 et 10 car les valeurs de couleurs vont de 0 à 1.
			set_color(Box,Color_Ratio,0,0)									#j'initialise la nouvelle couleur. ici avec des tons de rouge vers le noir
			
	MaxPlus.Animation.SetAnimateButtonState(False)							#on désactive "autokey"

def set_color(node, R, G, B):					#fonction pour changer la couleur de l'objet
	node.SetWireColor(MaxPlus.Color(R,G,B))		#changement de la couleur en spécifiant notre node
	

period = 1				#défini le nombre de fois que l'on va fair le tour du cerle dans le calcule des positions
nb_Frames = 50			#nombre de frames que l'on veut calculer l'animation
size_multiplier=20		#pour changer de coefficient de hauteur (optionnel mais 10 est une bonne valeur) 
padding = 15			#espacement entre nos cubes (doit toujours etre supérieur à la largeur du cube à savoir 10)
nb_Box_width=20			#largeur de l'objet
nb_Box_length=20		#longeur de l'objet


list_position = compute_positions(padding, nb_Box_width, nb_Box_length)	#calcule des positions des objets
all_Boxes=list()														#création d'une liste vide pour les boites

for position in list_position:											#création des cubes en fonction des positions calculées précédement
	
	Boxes=createCube(10,10,10,position)									#on créer le cube à tel position
	set_color(Boxes,1,1,1)												#on initialise la couleur en blanc
	all_Boxes.append(Boxes)												#on remplit la liste des boites
	

animate_Boxes(all_Boxes,period,nb_Box_length,nb_Frames,size_multiplier)	#on lance le calcule de l'animation des boites
	

	
	
	

	


	
