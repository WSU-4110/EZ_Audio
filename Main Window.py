from PyQt5 import QtCore, QtGui, QtWidgets
from downloadlibrary import Ui_DownloadLibrary

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.defaultError="Welcome to EZ Audio! Expand your audio library by entering a valid Youtube URL above."
        self.defaultURL="Enter URL Here..."
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 442)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.URLBox = QtWidgets.QLineEdit(self.centralwidget)
        self.URLBox.setGeometry(QtCore.QRect(30, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        self.URLBox.setFont(font)
        self.URLBox.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.URLBox.setObjectName("URLBox")
        self.EZAudioLogo = QtWidgets.QLabel(self.centralwidget)
        self.EZAudioLogo.setGeometry(QtCore.QRect(30, 20, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.EZAudioLogo.setFont(font)
        self.EZAudioLogo.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.EZAudioLogo.setObjectName("EZAudioLogo")
        self.LibraryButton = QtWidgets.QPushButton(self.centralwidget)
        self.LibraryButton.setGeometry(QtCore.QRect(300, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.LibraryButton.setFont(font)
        self.LibraryButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(103, 103, 103);")
        self.LibraryButton.setObjectName("LibraryButton")
        self.ConvertButton = QtWidgets.QToolButton(self.centralwidget)
        self.ConvertButton.setGeometry(QtCore.QRect(290, 140, 101, 31))
        self.ConvertButton.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(10)
        font.setUnderline(False)
        self.ConvertButton.setFont(font)
        self.ConvertButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(103, 103, 103);")
        self.ConvertButton.setObjectName("ConvertButton")
        self.CreditsLabel = QtWidgets.QLabel(self.centralwidget)
        self.CreditsLabel.setGeometry(QtCore.QRect(30, 70, 201, 20))
        self.CreditsLabel.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.CreditsLabel.setObjectName("CreditsLabel")
        self.ErrorBox = QtWidgets.QLabel(self.centralwidget)
        self.ErrorBox.setGeometry(QtCore.QRect(30, 220, 361, 61))
        self.ErrorBox.setMinimumSize(QtCore.QSize(361, 61))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        self.ErrorBox.setFont(font)
        self.ErrorBox.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.ErrorBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ErrorBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ErrorBox.setLineWidth(0)
        self.ErrorBox.setMidLineWidth(0)
        self.ErrorBox.setTextFormat(QtCore.Qt.AutoText)
        self.ErrorBox.setScaledContents(False)
        self.ErrorBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ErrorBox.setWordWrap(True)
        self.ErrorBox.setObjectName("ErrorBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def changeError(self):
        self.currentError="You haven't entered a URL yet!"
        if self.defaultURL!="Enter URL Here...":
            self.currentError = "Wrong URL!"
        _translate = QtCore.QCoreApplication.translate
        self.ErrorBox.setText(_translate("MainWindow", self.currentError))

    def openLibrary(self):
        self.window=QtWidgets.QMainWindow()
        self.libUI=Ui_DownloadLibrary()
        self.libUI.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EZ Audio"))
        self.URLBox.setText(_translate("MainWindow", self.defaultURL))
        self.EZAudioLogo.setText(_translate("MainWindow", "EZ Audio"))
        self.LibraryButton.setText(_translate("MainWindow", "Library"))
        self.ConvertButton.setText(_translate("MainWindow", "Convert"))
        self.CreditsLabel.setText(_translate("MainWindow", " Made by Yousif, Omar, Jack, and Khaled"))
        self.ErrorBox.setText(_translate("MainWindow", self.defaultError))
        self.ConvertButton.clicked.connect(self.changeError)
        self.LibraryButton.clicked.connect(self.openLibrary)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())