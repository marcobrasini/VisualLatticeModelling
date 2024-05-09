from PyQt5.QtWidgets import QMainWindow, QFrame, QVBoxLayout
from vtkViewer import vtkViewer


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.viewer = vtkViewer()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.viewer)
        self.frame = QFrame()
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)


if __name__ == "__main__":

    import sys
    from PyQt5.Qt import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
