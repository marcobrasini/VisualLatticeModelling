from PyQt5.QtWidgets import QAbstractItemView, QLabel, QSizePolicy
from PyQt5.QtCore import QModelIndex, QObject, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from vtkLattice import vtkWidget, vtkViewer, vtkLattice
from .lib.MyTabWidget import MyTabWidget


class QtViewerTabDefault(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setScaledContents(True)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setPixmap(QPixmap('utils/defaultTitle.png'))
        self.setAlignment(Qt.AlignCenter)
        self.resize(self.pixmap().size())


class QtViewerTab(QAbstractItemView):

    viewerRemoved = pyqtSignal(QObject, int)
    viewerInserted = pyqtSignal(QObject, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = MyTabWidget(self, QtViewerTabDefault)
        self.widget.widgetOpenRequested.connect(
            lambda i: self.widget.insertTab(
                i, vtkWidget(vtkViewer(f"vtkViewer[{i}]")), f"vtkViewer[{i}]"
        ))
        self.widget.widgetCloseRequested.connect(
            lambda i: self.widget.removeTab(i)
        )
        self.setViewport(self.widget)
        self.setAcceptDrops(True)

    def moveCursor(self, cursorAction, modifiers):
        return QModelIndex()

    def setModel(self, model):
        super().setModel(model)
        self.widget.clear()
        self.widget.widgetRemoved.connect(self.emit_viewerRemoved)
        self.widget.widgetInserted.connect(self.emit_viewerInserted)
        for i in range(self.model().rowCount(QModelIndex())):
            viewer = self.model().viewer(i)
            self.insertViewer(viewer, i, False)

    def viewer(self, i):
        return self.widget.widget(i).viewer

    def lattice(self, i, j):
        return self.viewer(i).lattice[j]

    def removeViewer(self, index: int, callback: bool = True):
        if not callback:
            self.widget.widgetRemoved.disconnect()
        self.widget.removeTab(index)
        self.widget.widgetRemoved.connect(self.emit_viewerRemoved)

    def appendViewer(self, index, callback: bool = True):
        widget = vtkWidget(vtkViewer(f"vtkViewer[{index}]"))
        if not callback:
            self.widget.widgetInserted.disconnect()
        self.widget.insertTab(index, widget, widget.name())
        self.widget.widgetInserted.connect(self.emit_viewerInserted)

    def insertViewer(self, viewer: vtkViewer, i: int, callback: bool = True):
        widget = vtkWidget(viewer)
        if not callback:
            self.widget.widgetInserted.disconnect()
        self.widget.insertTab(i, widget, widget.name())
        self.widget.widgetInserted.connect(self.emit_viewerInserted)

    def emit_viewerRemoved(self, index: int):
        self.viewerRemoved.emit(self, index)

    def emit_viewerInserted(self, index):
        self.viewerInserted.emit(self, index)

    def closeEvent(self, event):
        for i in range(self.widget.count()):
            self.widget.widget(i).closeEvent(event)
        return super().closeEvent(event)
