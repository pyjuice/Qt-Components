import sys
import os
import subprocess

from RadialBar import RadialBar

from PyQt5.QtCore import QUrl, Qt, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QGuiApplication, QCursor
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import qmlRegisterType
from OpenGL import GLU

class App(QGuiApplication):
	def __init__(self, argv):
		super(App, self).__init__(argv)

if __name__ == '__main__':
	try:
		app = App(sys.argv)

		# qmlRegisterType(Info, 'SDK', 1, 0, 'Info')
		# qmlRegisterType(Updater, 'SDK', 1, 0, 'Updater')
		qmlRegisterType(RadialBar, "SDK", 1,0, "RadialBar")

		if os.uname()[4][:3] == 'arm':
			app.setOverrideCursor( QCursor( Qt.BlankCursor) )
		
		view = QQuickView()
		ctxt = view.rootContext()
		# ctxt.setContextProperty('MFV', mfv)
		# ctxt.setContextProperty('Config', config)
		# ctxt.setContextProperty('App', app)

		view.setSource(QUrl("main.qml"))
		view.show()
		ret = app.exec_()

	except Exception as e:
		print e
	