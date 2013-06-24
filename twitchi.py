import sys
from PyQt4 import QtGui

import sys
import urllib.request
import json

#Version 0.03 - Handles not live streams, breaks if names file does not exist - remove name not implemented

class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

        self.setGeometry(100, 100, 390, 200)
        self.setWindowTitle('Twitcher')


        # Main Label
        self.label = QtGui.QLabel("", self)
        self.label.move(2, 23)


        # Buttons
        self.btn = QtGui.QPushButton('Get Streams', self)
        self.btn.move(1, 0)
        self.btn.clicked.connect(self.getTwitchData)

        self.btn = QtGui.QPushButton('Add Stream', self)
        self.btn.move(85, 0)
        self.btn.clicked.connect(self.addUsername)

        self.btn = QtGui.QPushButton('Remove Name', self)
        self.btn.move(170, 0)
        
        self.show()

    def addUsername(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Add Username', 'Enter twitch username:')
        
        if ok:
            file = open('names', 'a+')
            file.write('\n' + str(text))
            file.close()
            self.getTwitchData()

    def getTwitchData(self):
        file = open('names', 'r+')
        outputString = ''

        for l in file.readlines():
            l = l.rstrip()
            url = 'http://api.justin.tv/api/stream/list.json?channel=' + l

            f = urllib.request.urlopen(url).read()
            if len(f) > 2:
                jsonData = json.loads(f.decode("utf8"))[0]['channel']
                outputString += '{0} is live playing {1}!\nStream title: {2}\n\n'.format(jsonData['title'], jsonData['meta_game'], jsonData['status'])
            else:
                outputString += l + ' is not live.\n\n'

        file.close()

        self.label.setText(outputString)
        self.label.adjustSize()

class App(QtGui.QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = MainWindow()
        self.main.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()