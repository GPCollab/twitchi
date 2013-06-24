import sys
import os
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui

import urllib.request
import json
from apscheduler.scheduler import Scheduler

#Version 0.06 - New UI layout, largely unfinished

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
		self.setStyle(QStyleFactory.create("Plastique"))
		# self.setStyle(QStyleFactory.create("Cleanlooks"))
		self.main.show()

class Twitchi_MainWindow(QMainWindow):
	def __init__(self, *args):
		QMainWindow.__init__(self, *args)
		#Set up window
		# self.centralwidget = QWidget(self)
		# self.setCentralWidget(self.cw)
		self.setWindowTitle("Twitchi")
		# self.setGeometry(100, 100, 390, 200)
		self.setGeometry(100, 100, 620, 402)
		
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
		self.centralwidget = QWidget(self)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.groupBox = QGroupBox(self.centralwidget)
		self.groupBox.setGeometry(QtCore.QRect(10, 10, 591, 61))
		self.groupBox.setTitle(_fromUtf8(""))
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.layoutWidget = QWidget(self.groupBox)
		self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 551, 42))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.gridLayout = QGridLayout(self.layoutWidget)
		self.gridLayout.setMargin(0)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.removeButton = QPushButton(self.layoutWidget)
		self.removeButton.setMinimumSize(QtCore.QSize(0, 40))
		self.removeButton.setAutoFillBackground(False)
		self.removeButton.setDefault(False)
		self.removeButton.setFlat(False)
		self.removeButton.setObjectName(_fromUtf8("removeButton"))
		self.gridLayout.addWidget(self.removeButton, 0, 3, 1, 1)
		self.refreshButton = QPushButton(self.layoutWidget)
		self.refreshButton.setMinimumSize(QtCore.QSize(0, 40))
		self.refreshButton.setAutoFillBackground(False)
		self.refreshButton.setDefault(False)
		self.refreshButton.setFlat(False)
		self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
		self.gridLayout.addWidget(self.refreshButton, 0, 0, 1, 1)
		self.toggleButton = QPushButton(self.layoutWidget)
		self.toggleButton.setMinimumSize(QtCore.QSize(0, 40))
		self.toggleButton.setAutoFillBackground(False)
		self.toggleButton.setDefault(False)
		self.toggleButton.setFlat(False)
		self.toggleButton.setObjectName(_fromUtf8("toggleButton"))
		self.gridLayout.addWidget(self.toggleButton, 0, 4, 1, 1)
		self.addButton = QPushButton(self.layoutWidget)
		self.addButton.setMinimumSize(QtCore.QSize(0, 40))
		self.addButton.setAutoFillBackground(False)
		self.addButton.setDefault(False)
		self.addButton.setFlat(False)
		self.addButton.setObjectName(_fromUtf8("addButton"))
		self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
		self.groupBox_2 = QGroupBox(self.centralwidget)
		self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 591, 281))
		self.groupBox_2.setTitle(_fromUtf8(""))
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.textBrowser = QTextBrowser(self.groupBox_2)
		self.textBrowser.setGeometry(QtCore.QRect(10, 10, 571, 261))
		self.textBrowser.setAutoFillBackground(False)
		self.textBrowser.setFrameShape(QFrame.NoFrame)
		self.textBrowser.setFrameShadow(QFrame.Sunken)
		self.textBrowser.setOpenExternalLinks(True)
		self.textBrowser.setOpenLinks(True)
		self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
		self.setCentralWidget(self.centralwidget)
		self.menubar = QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(self)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		self.setStatusBar(self.statusbar)

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		
		self.refreshButton.setText(_translate("MainWindow", "Refresh", None))
		self.refreshButton.clicked.connect(self.getTwitchData)

		self.addButton.setText(_translate("MainWindow", "Add Streamer", None))
		self.addButton.clicked.connect(self.addStreamer)
		
		self.removeButton.setText(_translate("MainWindow", "Remove Streamer", None))
		self.removeButton.clicked.connect(self.removeStreamer)

		self.toggleButton.setText(_translate("MainWindow", "Toggle Refresh", None))
		self.toggleButton.clicked.connect(self.toggleScheduler)
		# self.textBrowser.setHtml(_translate("MainWindow", "<html><head></head><body><p><b>iso</b> is live playing <b>Portal 2!</b><br/>Portal 2 Segment Attempts<br /><a href=\"http://www.justin.tv/isolitic\">Open Stream</a></p>	<p><b>sullyjhf</b> is live playing <b>Mirror's Edge!</b><br/>Mirrors edge sub 1 attempts sdf sdafsdf asdfasdfd<br /><a href=\"http://www.justin.tv/sullyjhf\">Open Stream</a></p></body></html>", None))



		if not os.path.exists("names"):
			file = open("names", "w+")
			file.close()

		# Initially run a check
		# self.getTwitchData()

		# Set up scheduler
		self.refresher = Scheduler()
		self.refresherRunning = False
		# self.refresher.start()
		self.refresherInterval = 10 #minutes
		self.refresher.add_interval_job(self.getTwitchData, seconds=self.refresherInterval)


	def testJob(self):
		print("TESTING SCHEDULER")
		self.getTwitchData()

	def getTwitchData(self):
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
					# else:
						# outputString += "<p>" + l + " is not live."

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
		self.w = MyPopup()
		self.w.setGeometry(QRect(100, 100, 100, 100))
		self.w.show()

	def toggleScheduler(self):
		if self.refresherRunning:
			self.refresher.unschedule_func(self.getTwitchData)
			self.refresherRunning = False
			print("turning off autorefresh")
		else:
			self.refresher.add_interval_job(self.getTwitchData, seconds=self.refresherInterval)
			self.refresherRunning = True
			print("turning on autorefresh")

class MyPopup(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		combo = QComboBox(self)

		file = open("names", "r")
		self.streamer_usernames = file.readlines()
		file.close()

		for l in self.streamer_usernames:
			if len(l) > 1:  #to prevent blank lines from being read
				l = l.rstrip()
				combo.addItem(l)

		combo.activated[str].connect(self.onNameChosen)

	def onNameChosen(self, name):
		reply = QMessageBox.question(self, "Message", "Are you sure you want to remove this username?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			file = open("names", "w+")
			for i, l in enumerate(self.streamer_usernames):
				l = l.rstrip()
				if l != name and len(l) > 1:
					if i == len(self.streamer_usernames)-1:
						file.write(l)
					else:
						file.write(l + "\n")

			file.close()
			self.close()

def main(args):
	app = Twitchi(args)
	app.exec_()
if __name__ == "__main__":
	main(sys.argv)