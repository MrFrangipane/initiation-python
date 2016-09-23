""" MODULE PYTHON SYLVAIN DALLIET IIM"""
""" Teapot Creation Interface """

from PySide import QtGui
import maxhelper
import MaxPlus
import teapot_create


reload(maxhelper)
reload(teapot_create)


class _GarbageCollectorProtector(object):
    protected_widgets = list()


class Example(maxhelper.MaxWidget):

    def __init__(self):
        # Initialise Classe Parente
        maxhelper.MaxWidget.__init__(self)
        # Initialise les elements d'interface
        self.init_ui()


    def init_ui(self):
        # Place et taille
        self.setGeometry(300, 300, 450, 200)
        
        # Name Area
        self.name_area_label = QtGui.QLabel('Base Name : ')
        self.name_area = QtGui.QLineEdit('MagicTeapot')

        # Segments Area
        self.segments_area_label = QtGui.QLabel('Nbr. Segments :')
        self.segments_area = QtGui.QSpinBox()
        self.segments_area.setMinimum(1)
        
        # Radius Area
        self.radius_area_label = QtGui.QLabel('Radius :')
        self.radius_area = QtGui.QDoubleSpinBox()
        self.radius_area.setMinimum(5.000)
        self.radius_area.setDecimals(3)
        self.radius_area.setSingleStep(0.01)
        self.radius_area.setAccelerated(True)

        # Quantity Area
        self.quantity_area_label = QtGui.QLabel('Nbr. Teapot :')
        self.quantity_area = QtGui.QSpinBox()
        self.quantity_area.setMinimum(1)
        
        # Button creation
        self.button = QtGui.QPushButton("Shazam")
        self.button.pressed.connect(self.button_pressed)

        # Button fix unique name and some fun
        self.button_fix = QtGui.QPushButton("Fix unique name")
        self.button_fix.pressed.connect(self.button_fix_pressed)

        # Layout
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.name_area_label, 0, 0)
        layout.addWidget(self.name_area, 0, 1)
        layout.addWidget(self.segments_area_label, 1, 0)
        layout.addWidget(self.segments_area, 1, 1)
        layout.addWidget(self.radius_area_label, 2, 0)
        layout.addWidget(self.radius_area, 2, 1)
        layout.addWidget(self.quantity_area_label, 3, 0)
        layout.addWidget(self.quantity_area, 3, 1)
        layout.addWidget(self.button, 4, 2)
        layout.addWidget(self.button_fix, 5, 2)

        # Title
        self.setWindowTitle('The Teapot Magic Maker')


    def button_pressed(self):

        # Print a sentence using all inputs        
        print "You created a {quantity} Teapot(s) with the base name \"{name}\" with {nbr_segments} segments and a radius of {radius_value}".format(
            quantity=self.quantity_area.text(),
            name=self.name_area.text(),
            nbr_segments=self.segments_area.text(),
            radius_value=self.radius_area.text()
            )
        
        # Create X teapot
        quantity_teapot = int(self.quantity_area.text())
        #print quantity_teapot
		# get teapot name
        custom_name = self.name_area.text()
        # Loop Teapot Function
        teapot_create.loop_teapot(1.0, 10, quantity_teapot, custom_name)


    def button_fix_pressed(self):
        # get teapot quantity
        quantity_teapot2 = int(self.quantity_area.text())
        #print quantity_teapot
		# get teapot name
        custom_name2 = self.name_area.text()
		# call the fix function
        teapot_create.unique_name_fix(quantity_teapot2, custom_name2)

      
def main():
    # Creation d'un widget
    example = Example()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(example)
    # Affichage
    example.show()


if __name__ == '__main__':
    main()
