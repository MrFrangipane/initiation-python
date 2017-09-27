# actionMan.executeAction 0 "40021";delete $; python.ExecuteFile @"F:\_DD_WORK\IIM\exo_python\pythonmax_ExoSquare.py"
# 09.2017
# Yoann Andre IIM A5 3D
# EXO PYTHON - 3DSMAX 2016


import random
import MaxPlus


#
## 3DS MAX
def cylinder(radius,height):
    """creation d'un cylinder"""
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
    node = MaxPlus.Factory.CreateNode(obj)
    obj.ParameterBlock.Radius.Value = radius
    obj.ParameterBlock.Height.Value = height
    return node


def colorize(node, color):
    node.SetWireColor(MaxPlus.Color(*color))


def move(node, position):
    """Positionner le cylinder"""
    node.Position = MaxPlus.Point3(*position)


def set_height(node, height):
    obj = node.GetBaseObject()
    obj.ParameterBlock.Height.SetValue(height)


#
## CALCULS
def compute_random_heights(count,height_min, height_max): 
    random_heights = list()
	
    for i in range(0,count):
        random_height = random.randint(height_min,height_max)
        random_heights.append(random_height)

    return random_heights   # renvoi d'une liste avec des valeurs random


def padding(count, radius):
    """pas entre les cylinders"""
    padding_list = list()

    if radius <= 1: radius += 1

    for i in range(0,count):
        padding_list.append(i * radius * 3)

    return padding_list  # renvoi du "pas" entre les objets
	

def compute_position(count,radius):
    positions = list()
    for x in radius:
        for y in radius:
            positions.append([x,y,0])
	
    return positions  # renvoi d'une liste de position


def compute_color(base_color1, base_color2, count):
    color = list()
    for x in range(0,count):
        for y in range(0,count):
            if y % 2:  # si [y] est divisible par 2 alors mets la color 1
                color.append(base_color1)
            else:  # sinon mets la 2
                color.append(base_color2)

    return color  # liste avec une ligne sur 2 base_color1 et base_color2


#
## CHEF
def cylinder_square (cylinder_radius, cylinder_height, square_count, base_color1, base_color2):
    """Chef"""
    cylinders = list()
    radiuses = padding(square_count, cylinder_radius)
    cylinder_positions = compute_position(square_count, radiuses)
    cylinder_color = compute_color(base_color1, base_color2, square_count)
	
    for index in range(square_count * square_count):
        new_cylinder = cylinder(cylinder_radius, cylinder_height)

        move(new_cylinder, cylinder_positions[index])
        colorize(new_cylinder, cylinder_color[index])
        cylinders.append(new_cylinder)

    return cylinders

#
## CHEF ANIMATION
def animate_cylinders(cylinders, frame_count, height_min, height_max):
    heights = compute_random_heights(frame_count, height_min, height_max)
	
    MaxPlus.Animation.SetAnimateButtonState(True)
	
    for frame_number in range(frame_count):
        MaxPlus.Animation.SetTime(frame_number * 160)
		
        for index, cylinder in enumerate(cylinders):
            i = (frame_number + index) % frame_count
            set_height(cylinder, heights[i])
			
    MaxPlus.Animation.SetAnimateButtonState(False)


#
# Main
if __name__ == '__main__':
    all_objects = list()
	
    cylinders = cylinder_square(
		cylinder_radius = 3.0,
		cylinder_height = 5.0,
		square_count = 5,
		base_color1 = [0.5,0.5,0], 
		base_color2 = [1,0,0.5]

	)
    all_objects += cylinders
	
    animate_cylinders(all_objects, frame_count=60, height_min=1, height_max=10)
