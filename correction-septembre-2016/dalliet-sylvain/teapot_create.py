""" MODULE PYTHON SYLVAIN DALLIT IIM """
""" Teapot Creation Functions """

import MaxPlus
import math
import random

def make_teapot(rad, seg, pos):
    # node geometry parameters
    teapot_geometry = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Teapot)
    teapot_geometry.ParameterBlock.Radius.Value = rad
    teapot_geometry.ParameterBlock.Segs.Value = seg
    
    # node creation
    teapot_node = MaxPlus.Factory.CreateNode(teapot_geometry)
    
    # Transform
    teapot_node.Position = MaxPlus.Point3(*pos)
    
    # return
    return teapot_node


def loop_teapot(rad, seg, teapot_count, thename):
    teapot_posx = 0
    
    # fix for the first teapot posx
    first_teapot = make_teapot(1.0, 10, [teapot_posx, 0, 0])
    first_teapot.SetName("{teapot_name}_000".format(teapot_name=thename))
    first_teapot.SetWireColor(MaxPlus.Color(255/teapot_count))
    
    for teapot_index in range(1,teapot_count):
        # position offset
        teapot_posx += 10

        # call teapot creation
        new_teapot = make_teapot(1.0, 10, [teapot_posx, 0, 0])

        # Set Teapot(s) name(s) and color(s)        
        new_teapot.SetName("{teapot_name}_{index:03d}".format(
            teapot_name = thename,
            index=teapot_index
            ))
        new_teapot.SetWireColor(MaxPlus.Color(255 / teapot_count * (teapot_index+1)))

    
def unique_name_fix(teapot_count2, thename2):
    # fix for non unique names
    sceneObjs = [obj for obj in MaxPlus.Core.GetRootNode().Children]
    checkname_list = []
    check_name = thename2
    
    # filter the geometry and make sure we collect the one we actually need using the base name
    for obj in sceneObjs:
        if check_name in obj.Name:
            checkname_list.append(obj)

    # now we process all checked objects   
    total_teapot_count = int(len(checkname_list))
    instance_number = 0
    posx_offset = 0
    # rename process
    for obj_checked in checkname_list:
        obj_checked.SetName("{teapot_name2}_{index2:03d}".format(
            teapot_name2 = thename2,
            index2=instance_number
            ))
        # color process
        obj_checked.SetWireColor(MaxPlus.Color(255 / total_teapot_count * (instance_number+1)))
        # position process
        obj_checked.Position = MaxPlus.Point3(posx_offset, 0, 0)
        instance_number += 1
        posx_offset += 50
        # add parameters for more fun
        # random scale
        rand_scale_value = random.randint(1,2)
        obj_checked.Scaling = MaxPlus.Point3(rand_scale_value, rand_scale_value, rand_scale_value)

        # random rotation
        rand_rotation_value = random.randint(0,360)
        rotation_quat = MaxPlus.Quat()
        rotation_quat.SetEuler(0, 0, rand_rotation_value)
        obj_checked.Rotation = rotation_quat
    

    """
    #debug
    print len(checkname_list)    
    print total_teapot_count
    """
