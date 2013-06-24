import sys
from PyQt4 import QtGui

import sys
import urllib.request
import json


#Version 0.02 - Only handles streams that are live

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      
        self.label = QtGui.QLabel("No Username Chosen", self)
        self.label.move(2, 23)

        self.btn = QtGui.QPushButton('Pick Username', self)
        self.btn.move(1, 0)
        self.btn.clicked.connect(self.showDialog)

        self.setGeometry(100, 100, 390, 80)
        self.setWindowTitle('Input dialog')
        self.show()
        
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        
        if ok:
            self.getTwitchData(str(text))
            self.label.adjustSize()
        
    def getTwitchData(self, streamUsername):
        url = 'http://api.justin.tv/api/stream/list.json?channel=' + streamUsername
        f = urllib.request.urlopen(url)
        jsonData = json.loads(f.read().decode("utf8"))[0]['channel']
        self.label.setText('{0} is live playing {1}!\nStream title: {2}'.format(jsonData['title'], jsonData['meta_game'], jsonData['status']))

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()