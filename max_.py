import MaxPlus


def cylinder(height, radius, position, segments=1):
	base_obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
	base_obj.ParameterBlock.Radius.Value = radius
	base_obj.ParameterBlock.Height.Value = height
	base_obj.ParameterBlock.HeightSegs.Value = segments
	
	node = MaxPlus.Factory.CreateNode(base_obj)
	node.Position = MaxPlus.Point3(*position)
	
	return node


def rotate(node, rotation):
	rotation_quat = MaxPlus.Quat()
	rotation_quat.SetEuler(*rotation)
	node.Rotation = rotation_quat
	
	return rotation_quat
	
	
def bend(node, angle, collapse=False):
	modifier = MaxPlus.Factory.CreateObjectModifier(MaxPlus.ClassIds.Bend)
	modifier.ParameterBlock.BendAngle.Value = angle
	node.AddModifier(modifier)
	
	if collapse:
		node.Collapse()
		return node
	
	return modifier
