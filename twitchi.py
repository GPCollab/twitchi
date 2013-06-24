import sys
import os
from PyQt4.Qt import *

import urllib.request
import json
from apscheduler.scheduler import Scheduler

#Version 0.05 - scheduler added

class Twitchi(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = Twitchi_MainWindow()
		self.setStyle(QStyleFactory.create("Cleanlooks"))
		self.main.show()

class Twitchi_MainWindow(QMainWindow):
	def __init__(self, *args):
		QMainWindow.__init__(self, *args)
		#Set up window
		self.cw = QWidget(self)
		self.setCentralWidget(self.cw)
		self.setWindowTitle("Twitchi")
		self.setGeometry(100, 100, 390, 200)
		
		# Main label - holds streams status text
		self.label = QLabel("No usernames loaded!", self)
		self.label.move(2, 33)
		self.label.adjustSize()

		# Buttons
		self.btn = QPushButton("Get Streams", self)
		self.btn.move(1, 0)
		self.btn.clicked.connect(self.getTwitchData)

		self.btn = QPushButton("Add Streamer", self)
		self.btn.move(105, 0)
		self.btn.clicked.connect(self.addStreamer)

		self.btn = QPushButton("Remove Streamer", self)
		self.btn.move(209, 0)
		self.btn.clicked.connect(self.removeStreamer)

		self.btn = QPushButton("Toggle Refresh", self)
		self.btn.move(313, 0)
		self.btn.clicked.connect(self.toggleScheduler)

		if not os.path.exists("names"):
			file = open("names", "w+")
			file.close()

		# Initially run a check
		self.getTwitchData()

		# Set up scheduler
		self.refresher = Scheduler()
		self.refresherRunning = True
		self.refresher.start()
		self.refresherInterval = 3 #minutes
		self.refresher.add_interval_job(self.testJob, minutes=self.refresherInterval)


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
						outputString += "{0} is live playing {1}!\nStream title: {2}\n\n".format(jsonData["title"], jsonData["meta_game"], jsonData["status"])
					else:
						outputString += l + " is not live.\n\n"

			file.close()
			self.label.setText(outputString)
			self.label.adjustSize()

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
			self.refresher.unschedule_func(self.testjob)
			self.refresherRunning = False
			print("turning off autorefresh")
		else:
			self.refresher.add_interval_job(self.testJob, minutes=self.refresherInterval)
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