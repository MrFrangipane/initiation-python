import random
import max_


def make_cylinders(row_count, column_count, spacing, cyl_height, cyl_radius):
	cylinders = []

	for row in range(row_count):
		for column in range(column_count):
			
			position = [row * spacing, column * spacing, 0]
			new_cylinder = max_.cylinder(
				cyl_height, 
				cyl_radius, 
				position, 
				segments=5
			)
			
			bend_angle = random.randint(-90, 90)
			max_.bend(
				new_cylinder, 
				bend_angle, 
				collapse=True
			)
			
			rotation = [0, 0, random.randint(0, 360)]
			max_.rotate(new_cylinder, rotation)
			
			cylinders.append(new_cylinder)
	
	return cylinders
