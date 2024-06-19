import sys
import logging
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QMainWindow
from .QtViewer import QtViewer


class QtMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.logger = logging.getLogger('qt')
        self.logger.setLevel(logging.DEBUG)
        self.viewer = QtViewer()
        self.viewer.setup([])
        self.setCentralWidget(self.viewer)
        self.showMaximized()

    def closeEvent(self, event):
        self.viewer.closeEvent(event)
        super().closeEvent(event)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QtMain()
    main.show()
    sys.exit(app.exec_())
