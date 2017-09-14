import math
import random
import MaxPlus

def compute_positions(radius, count):
	positions = list()
	alpha = (2 * math.pi) / count
	
	for element in range(count):
		x = radius * math.cos(alpha * element)
		y = radius * math.sin(alpha * element)
		positions.append([x, y, 0.0])
	
	return positions


def compute_rotations(count):
	alpha = (2 * math.pi) / count
	rotations = list()
	
	for i in range(count):
		rotations.append([0.0, 0.0, i * alpha])

	return rotations

	
def compute_colors(base_color, count, factor=3):
	colors = list()
	alpha = (2 * math.pi) / count
	
	for i in range(count):
		value = (1.0 + math.cos(i * alpha * factor)) / 2.0
		
		color = (
			base_color[0] * value,
			base_color[1] * value,
			base_color[2] * value,
		)
		colors.append(color)
	
	return colors


def random_color():
	return random.random(), random.random(), random.random()
	
	
	
def cylinder(height=1.0, radius=1.0):
	obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
	node = MaxPlus.Factory.CreateNode(obj)
	obj.ParameterBlock.Radius.Value = radius
	obj.ParameterBlock.Height.Value = height
	
	return node
	

def move(node, position):
	node.Position = MaxPlus.Point3(*position)


def colorize(node, color):
	node.SetWireColor(MaxPlus.Color(*color))
	

def rotate(node, rotation):
	rotation_quat = MaxPlus.Quat()
	rotation_quat.SetEuler(*rotation)
	node.Rotation = rotation_quat

	
def cylinder_circle(circle_radius, cylinder_count, cylinder_height, cylinder_radius, base_color):
	cylinders = list()
	cylinder_positions = compute_positions(circle_radius, cylinder_count)
	cylinder_rotations = compute_rotations(cylinder_count)
	cylinder_colors = compute_colors(base_color, cylinder_count)
	
	for index in range(cylinder_count):
		new_cylinder = cylinder(cylinder_height, cylinder_radius)
		
		move(new_cylinder, cylinder_positions[index])
		rotate(new_cylinder, cylinder_rotations[index])
		colorize(new_cylinder, cylinder_colors[index])
		
		cylinders.append(new_cylinder)

	return cylinders

colors = compute_colors([0, 1, 0], 60)

	
for i in range(1, 60):
	cylinders = cylinder_circle(
		circle_radius=i * 7, 
		cylinder_count=i * 5,
		cylinder_height=i * 1.1,
		cylinder_radius=2,
		base_color=colors[i]
)