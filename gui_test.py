#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This program centers a window 
on the screen. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore 

class Communicate(QtCore.QObject):
    closeApp = QtCore.pyqtSignal() 

#class Example(QtGui.QWidget):
class Example(QtGui.QMainWindow):
    
    def __init__(self):

        super(Example, self).__init__()
        self.form_widget = FormWidget() 
        self.setCentralWidget(self.form_widget) 
        """
        """
        self.initUI()
        
    def initUI(self): 

        '''
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)     
        '''

        """Positioning a label at a specific location"""
        '''
        lbl1 = QtGui.QLabel('ZetCode', self)
        lbl1.move(115, 100)         
        '''

        """Text edit""" 
        '''
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)            
        '''

        """Defining exit action"""
        exitAction = QtGui.QAction(QtGui.QIcon('images/exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        """Defining open file action"""
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        """Adding toolbar"""
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        '''

        """Don't know what it is?
        self.statusBar()
        '''

        """Adding menu items"""
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(openFile)

        """Adding buttons"""
        """
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QtGui.QPushButton('Button', self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50) 
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QPushButton</b> widget')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)   
        """

        """Some more buttons"""
        """
        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        self.statusBar()
        """

        """Dialog box+line edit"""
        '''
        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        '''

        """Using the class Communicate"""
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        
        """Checkbox"""
        cb = QtGui.QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        """Buttons with color"""
        self.col = QtGui.QColor(0, 0, 0)       

        redb = QtGui.QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(100, 50)

        redb.clicked[bool].connect(self.setColor)

        greenb = QtGui.QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(100, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QtGui.QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(100, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(500, 200, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %self.col.name())

        """Progress bar"""
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(130, 140, 200, 25)

        self.btn = QtGui.QPushButton('Start', self)
        self.btn.move(140, 180)
        self.btn.clicked.connect(self.doAction)

        self.timer = QtCore.QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 50, 280, 170)
        self.setWindowTitle('QtGui.QProgressBar')
        self.show()

        """Split the gui into frames""" 
        #hbox = QtGui.QHBoxLayout(self)

        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)
 
        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        """
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        """
     
        """Setting up the main gui"""
        """This section should be by the end of this function.\
        Otherwise the sections after this will be ignored"""  
        self.setGeometry(600, 600, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('images/chat.png'))          
        self.show() 

    def timerEvent(self, e):
        """Timer for progress bar""" 
        if self.step >= 100:
        
            self.timer.stop()
            self.btn.setText('Finished')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        """Buttons status in the progress bar"""
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')     

    def setColor(self, pressed):
        source = self.sender()        
        if pressed:
            val = 255
        else: val = 0                        
        if source.text() == "Red":
            self.col.setRed(val)                
        elif source.text() == "Green":
            self.col.setGreen(val)             
        else:
            self.col.setBlue(val)             
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name()) 

    def changeTitle(self, state):
        """Change window title according to the status of checkbox"""
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')  
    
    def buttonClicked(self):

        """Define what to do on button click"""
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def closeEvent(self, event):
    
        """Asking for confirmation before quitting"""
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes | 
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()         
    
    def keyPressEvent(self, e):
       
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
    
    def showDialog(self):
    
        """Open file action"""
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','/home/Documents')        
        f = open(fname, 'r')
        with f:        
            data = f.read()
            #self.textEdit.setText(data)   
    def printText(self):
        self.textEdit.setText("test data")
        
    '''
    def mousePressEvent(self, event):
        self.c.closeApp.emit()
        self.statusBar().showMessage('Oops!! Did you just press the mouse button?')
        '''    
#class FormWidget(QtGui.QWidget):
class FormWidget(QtGui.QMainWindow):
    def __init__(self):
        super(FormWidget, self).__init__()
        '''
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
        '''
        self.statusBar().showMessage('Oops!! Did you just press the mouse button?')
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    #ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main() 
