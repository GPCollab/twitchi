import sys
import os
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui

import urllib.request
import json

#Version 0.09 - Timer and autorefresh implemented

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)


class Twitchi(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = Twitchi_MainWindow()
		# self.setStyle(QStyleFactory.create("Plastique"))
		# self.setStyle(QStyleFactory.create("Cleanlooks"))
		self.main.show()

class Twitchi_MainWindow(QMainWindow):

	testSignal = pyqtSignal()

	def __init__(self, *args):
		super()
		QMainWindow.__init__(self, *args)
		#Set up window
		# self.centralwidget = QWidget(self)
		# self.setCentralWidget(self.cw)
		self.setWindowTitle("Twitchi")
		# self.setGeometry(100, 100, 390, 200)
		self.setGeometry(100, 100, 611, 392)
		self.setMaximumSize(QtCore.QSize(611, 392))
		
		# # Main label - holds streams status text
		# self.label = QLabel("No usernames loaded!", self)
		# self.label.move(2, 33)
		# self.label.adjustSize()

		# # Buttons
		# self.btn = QPushButton("Get Streams", self)
		# self.btn.move(1, 0)
		# self.btn.clicked.connect(self.getTwitchData)

		# self.btn = QPushButton("Add Streamer", self)
		# self.btn.move(105, 0)
		# self.btn.clicked.connect(self.addStreamer)

		# self.btn = QPushButton("Remove Streamer", self)
		# self.btn.move(209, 0)
		# self.btn.clicked.connect(self.removeStreamer)

		# self.btn = QPushButton("Toggle Refresh", self)
		# self.btn.move(313, 0)
		# self.btn.clicked.connect(self.toggleScheduler)

		# self.resize(620, 402)
		self.centralwidget = QtGui.QWidget(self)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.groupBox = QtGui.QGroupBox(self.centralwidget)
		self.groupBox.setGeometry(QtCore.QRect(10, 10, 591, 71))
		self.groupBox.setTitle(_fromUtf8(""))
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.layoutWidget = QtGui.QWidget(self.groupBox)
		self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 571, 52))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
		self.gridLayout.setMargin(0)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.addButton = QtGui.QPushButton(self.layoutWidget)
		self.addButton.setMinimumSize(QtCore.QSize(0, 50))
		self.addButton.setAutoFillBackground(False)
		self.addButton.setDefault(False)
		self.addButton.setFlat(False)
		self.addButton.setObjectName(_fromUtf8("addButton"))
		self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
		self.removeButton = QtGui.QPushButton(self.layoutWidget)
		self.removeButton.setMinimumSize(QtCore.QSize(0, 50))
		self.removeButton.setAutoFillBackground(False)
		self.removeButton.setDefault(False)
		self.removeButton.setFlat(False)
		self.removeButton.setObjectName(_fromUtf8("removeButton"))
		self.gridLayout.addWidget(self.removeButton, 0, 3, 1, 1)
		self.toggleButton = QtGui.QPushButton(self.layoutWidget)
		self.toggleButton.setMinimumSize(QtCore.QSize(0, 50))
		self.toggleButton.setAutoFillBackground(False)
		self.toggleButton.setDefault(False)
		self.toggleButton.setFlat(False)
		self.toggleButton.setObjectName(_fromUtf8("toggleButton"))
		self.gridLayout.addWidget(self.toggleButton, 0, 4, 1, 1)
		self.refreshButton = QtGui.QPushButton(self.layoutWidget)
		self.refreshButton.setMinimumSize(QtCore.QSize(0, 50))
		self.refreshButton.setSizeIncrement(QtCore.QSize(0, 0))
		self.refreshButton.setAutoFillBackground(False)
		self.refreshButton.setDefault(False)
		self.refreshButton.setFlat(False)
		self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
		self.gridLayout.addWidget(self.refreshButton, 0, 0, 1, 1)
		self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 591, 251))
		self.groupBox_2.setTitle(_fromUtf8(""))
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.textBrowser = QtGui.QTextBrowser(self.groupBox_2)
		self.textBrowser.setGeometry(QtCore.QRect(10, 10, 571, 231))
		self.textBrowser.setAutoFillBackground(False)
		self.textBrowser.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
		self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
		self.textBrowser.setFrameShadow(QtGui.QFrame.Sunken)
		self.textBrowser.setOpenExternalLinks(True)
		self.textBrowser.setOpenLinks(True)
		self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
		self.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuTest = QtGui.QMenu(self.menubar)
		self.menuTest.setObjectName(_fromUtf8("menuTest"))
		self.menuHelp = QtGui.QMenu(self.menubar)
		self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
		self.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(self)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		self.setStatusBar(self.statusbar)
		self.actionAbout = QtGui.QAction(self)
		self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
		self.actionSettings = QtGui.QAction(self)
		self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
		self.menuTest.addAction(self.actionSettings)
		self.menuHelp.addAction(self.actionAbout)
		self.menubar.addAction(self.menuTest.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.addButton.setStatusTip(_translate("MainWindow", "Add a new stream to check", None))
		self.addButton.setText(_translate("MainWindow", "Add Streamer", None))
		self.removeButton.setStatusTip(_translate("MainWindow", "Remove an existing stream", None))
		self.removeButton.setText(_translate("MainWindow", "Remove Streamer", None))
		self.toggleButton.setStatusTip(_translate("MainWindow", "Toggle auto-refreshing of data", None))
		self.toggleButton.setText(_translate("MainWindow", "Toggle Refresh", None))
		self.refreshButton.setStatusTip(_translate("MainWindow", "Refresh stream data", None))
		self.refreshButton.setText(_translate("MainWindow", "Refresh", None))
		self.menuTest.setTitle(_translate("MainWindow", "Settings", None))
		self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
		self.actionAbout.setText(_translate("MainWindow", "About", None))
		self.actionAbout.setStatusTip(_translate("MainWindow", "About Twitchi", None))
		self.actionSettings.setText(_translate("MainWindow", "Preferences", None))
		self.actionSettings.setStatusTip(_translate("MainWindow", "Application settings", None))

		self.refreshButton.clicked.connect(self.getTwitchData)
		self.addButton.clicked.connect(self.addStreamer)
		self.removeButton.clicked.connect(self.removeStreamer)
		self.toggleButton.clicked.connect(self.toggleTimer)

		if not os.path.exists("names"):
			file = open("names", "w+")
			file.close()

		# Initially run a check
		self.getTwitchData()
		self.timerInterval = 5000

		self.timer = QTimer()
		self.timer.timeout.connect(self.getTwitchData)
		self.timer.start(self.timerInterval)

	def toggleTimer(self):
		if self.timer.isActive():
			self.timer.stop()
			print("stopping timer")
		else:
			self.timer.start(self.timerInterval)
			print("starting timer")

	def getTwitchData(self):
		print("getTwitchData")
		if os.path.getsize("names") > 0:
			file = open("names", "r+")
			outputString = ""
			for l in file.readlines():
				if len(l) > 1:  #to prevent blank lines from being read
					l = l.rstrip()  # strip newline characters
					url = "http://api.justin.tv/api/stream/list.json?channel=" + l

					f = urllib.request.urlopen(url).read()
					if len(f) > 2:
						jsonData = json.loads(f.decode("utf8"))[0]["channel"]
						outputString += "<p><b>{0}</b> is live playing <b>{1}!</b><br/>{2}<br /><a href=\"{3}\">Open Stream</a></p>".format(jsonData["title"], jsonData["meta_game"], jsonData["status"], jsonData["channel_url"])
					else:
						outputString += "<p>" + l + " is not live."

			file.close()
			self.textBrowser.setHtml(_translate("MainWindow", "<html><head></head><body>" + outputString + "</body></html>", None))

	def addStreamer(self):
		text, ok = QInputDialog.getText(self, "Add Username", "Enter twitch username:")
		
		if ok:
			file = open("names", "r")
			streamer_usernames = file.readlines()
			numLines = len(streamer_usernames)
			file.close()

			file = open("names", "a+")
			if numLines is 0:
				file.write(str(text))
			else:
				file.write("\n" + str(text))
			file.close()
			self.getTwitchData()

	def removeStreamer(self):
		self.w = RemoveUserWindow()
		self.w.show()

class RemoveUserWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.setGeometry(120, 120, 261, 191)
		self.setMinimumSize(QtCore.QSize(261, 191))
		self.setMaximumSize(QtCore.QSize(261, 191))
		self.groupBox = QtGui.QGroupBox(self)
		self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 121))
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.listWidget = QtGui.QListWidget(self.groupBox)
		self.listWidget.setGeometry(QtCore.QRect(10, 20, 221, 91))
		self.listWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
		self.listWidget.setTextElideMode(QtCore.Qt.ElideRight)
		self.listWidget.setUniformItemSizes(False)
		self.listWidget.setSelectionRectVisible(False)
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		self.selectAllButton = QtGui.QPushButton(self)
		self.selectAllButton.setGeometry(QtCore.QRect(10, 140, 71, 41))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.selectAllButton.sizePolicy().hasHeightForWidth())
		self.selectAllButton.setSizePolicy(sizePolicy)
		self.selectAllButton.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
		self.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))
		self.removeButton = QtGui.QPushButton(self)
		self.removeButton.setGeometry(QtCore.QRect(90, 140, 161, 41))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
		self.removeButton.setSizePolicy(sizePolicy)
		self.removeButton.setObjectName(_fromUtf8("removeButton"))

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, RemoveStreamer):
		RemoveStreamer.setWindowTitle(_translate("RemoveStreamer", "Remove Streamer", None))
		self.groupBox.setTitle(_translate("RemoveStreamer", "Select stream(s) to remove", None))
		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)

		file = open("names", "r")
		self.streamer_usernames = file.readlines()
		file.close()

		# Add usernames into list widget
		for l in self.streamer_usernames:
			l = l.rstrip()
			self.listWidget.addItem(QtGui.QListWidgetItem(l))

		self.listWidget.setSortingEnabled(__sortingEnabled)
		self.selectAllButton.setText(_translate("RemoveStreamer", "Select All", None))
		self.removeButton.setText(_translate("RemoveStreamer", "Remove Selected", None))

		self.selectAllButton.clicked.connect(self.selectAllNames)
		self.removeButton.clicked.connect(self.onNameChosen)



	def selectAllNames(self):
		for i in range(0, len(self.listWidget)):
			self.listWidget.item(i).setSelected(True)

	def onNameChosen(self):
		numSelected = 0
		selectedNames = []
		for i in range(0, len(self.listWidget)):
			if self.listWidget.item(i).isSelected():
				# print(str(self.listWidget.item(i).text()))
				selectedNames.append(self.listWidget.item(i).text())
				numSelected+=1

		confirmation = QMessageBox.question(self, "Message", "Are you sure you want to remove " + str(numSelected) + " username(s)?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if confirmation == QMessageBox.Yes:
			file = open("names", "w+")
			# for i, l in len(self.listWidget)
			for i, l in enumerate(self.streamer_usernames):
				l = l.rstrip()
				if l not in selectedNames:
					if i == len(self.streamer_usernames)-1:
						file.write(l)
					else:
						file.write(l + "\n")
			file.close()
			self.close()


		# combo = QComboBox(self)

		# file = open("names", "r")
		# self.streamer_usernames = file.readlines()
		# file.close()

		# for l in self.streamer_usernames:
		# 	if len(l) > 1:  #to prevent blank lines from being read
		# 		l = l.rstrip()
		# 		combo.addItem(l)

		# combo.activated[str].connect(self.onNameChosen)





	# def onNameChosenddd(self, name):
	# 	reply = QMessageBox.question(self, "Message", "Are you sure you want to remove this username?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
	# 	if reply == QMessageBox.Yes:
	# 		file = open("names", "w+")
	# 		for i, l in enumerate(self.streamer_usernames):
	# 			l = l.rstrip()
	# 			if l != name and len(l) > 1:
	# 				if i == len(self.streamer_usernames)-1:
	# 					file.write(l)
	# 				else:
	# 					file.write(l + "\n")

	# 		file.close()
	# 		self.close()




def main(args):
	app = Twitchi(args)
	app.exec_()
if __name__ == "__main__":
	main(sys.argv)