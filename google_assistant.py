import manager
from PyQt5.QtWidgets import *
from PyQt5.uic import *
import sys

Manager = manager.Manager()
GoogleAssistant = QApplication(sys.argv)
Window = loadUi('')
Window.show()
sys.exit(GoogleAssistant.exec_())
