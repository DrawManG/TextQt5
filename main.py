from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
#hook


sys.exit(app.exec_())