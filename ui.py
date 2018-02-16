from PySide.QtGui import *
import max_
import square


class CylinderMaker(QWidget):
	
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setWindowTitle("Cylinder Maker")
		
		layout = QGridLayout(self)
		
		self.spin_rows = QSpinBox()
		layout.addWidget(QLabel("Row count"), 0, 0)
		layout.addWidget(self.spin_rows, 0, 1)
		
		self.spin_columns = QSpinBox()
		layout.addWidget(QLabel("Column count"), 1, 0)
		layout.addWidget(self.spin_columns, 1, 1)
		
		self.button_make = QPushButton("Make")
		layout.addWidget(self.button_make, 2, 0, 1, 2)
		self.button_make.clicked.connect(self.button_clicked)
	
	def button_clicked(self):
		square.make_cylinders(
			row_count=self.spin_rows.value(), 
			column_count=self.spin_columns.value(), 
			spacing=10, 
			cyl_height=5, 
			cyl_radius=2
		)


cylinder = CylinderMaker()
cylinder.show()
max_.attach_widget(cylinder)
