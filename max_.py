import ctypes
from PySide import QtCore, QtGui
import MaxPlus


GWL_HWNDPARENT = -8
SetWindowLongPtr = ctypes.windll.user32.SetWindowLongPtrW


class FocusFilter(QtCore.QObject):
    def eventFilter(self, obj, event):
        MaxPlus.CUI.DisableAccelerators()
	return False

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

def get_hwnd(widget):
	ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
	ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
	wdgt_ptr = ctypes.pythonapi.PyCObject_AsVoidPtr(widget.winId())
	return wdgt_ptr
	
def attach_widget(widget):
	parent_hwnd = MaxPlus.Win32.GetMAXHWnd()
	hwnd = get_hwnd(widget)
	SetWindowLongPtr(hwnd, GWL_HWNDPARENT, parent_hwnd)
	app = QtGui.QApplication.instance()
	widget._focus_filter = FocusFilter()
	widget.event_filter = app.installEventFilter(widget._focus_filter)
