import math
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

	
def cylinder(height=1.0, radius=1.0):
	obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
	node = MaxPlus.Factory.CreateNode(obj)
	obj.ParameterBlock.Radius.Value = radius
	obj.ParameterBlock.Height.Value = height
	
	return node
	

def move(node, position):
	node.Position = MaxPlus.Point3(*position)


def rotate(node, rotation):
	rotation_quat = MaxPlus.Quat()
	rotation_quat.SetEuler(*rotation)
	node.Rotation = rotation_quat

	
def cylinder_circle(circle_radius, cylinder_count, cylinder_height, cylinder_radius):
	cylinders = list()
	cylinder_positions = compute_positions(circle_radius, cylinder_count)
	cylinder_rotations = compute_rotations(cylinder_count)
	
	for index, cylinder_position in enumerate(cylinder_positions):
		new_cylinder = cylinder(cylinder_height, cylinder_radius)
		move(new_cylinder, cylinder_position)
		rotate(new_cylinder, cylinder_rotations[index])
		cylinders.append(new_cylinder)

	return cylinders


for i in range(1, 6):
	cylinders = cylinder_circle(
		circle_radius=i * 5.0, 
		cylinder_count=i * 7,
		cylinder_height=i * 3,
		cylinder_radius=i * 0.5
)
