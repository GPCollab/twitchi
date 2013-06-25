import sys
import os
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui

import urllib.request
import json

from mainwindow import Twitchi_MainWindow

class Twitchi(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = Twitchi_MainWindow()
		# self.setStyle(QStyleFactory.create("Plastique"))
		# self.setStyle(QStyleFactory.create("Cleanlooks"))
		self.main.show()

def main(args):
	app = Twitchi(args)
	app.exec_()
if __name__ == "__main__":
	main(sys.argv)