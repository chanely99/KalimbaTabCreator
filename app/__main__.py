from fbs_runtime.application_context.PyQt5 import ApplicationContext
from qtpy import QtWidgets
from app import MainWindow
import sys

appctxt = ApplicationContext()
#app = QtWidgets.QApplication(['ELFIN Planner'])
appctxt.app.mw = MainWindow()
appctxt.app.mw.show()
sys.exit(appctxt.app.exec_())
#app.exec_()
