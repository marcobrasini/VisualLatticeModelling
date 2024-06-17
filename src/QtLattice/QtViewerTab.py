from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import QModelIndex, QObject, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDropEvent
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


class QtViewerTab(MyTabWidget):

    viewerSelected = pyqtSignal(int)
    viewerRenamed = pyqtSignal(QObject, int, str)
    viewerRemoved = pyqtSignal(QObject, int)
    viewerInserted = pyqtSignal(QObject, int)
    latticeRemoved = pyqtSignal(QObject, int, int)
    latticeInserted = pyqtSignal(QObject, int, int)

    def __init__(self, parent=None):
        super().__init__(parent, QtViewerTabDefault)
        self.setAcceptDrops(True)
        self.currentChanged.connect(self.selectViewer)
        self.widgetOpenRequested.connect(self.openViewer)
        self.widgetCloseRequested.connect(self.closeViewer)
        self.widgetInserted.connect(self.emit_viewerInserted)
        self.widgetRemoved.connect(self.emit_viewerRemoved)
        self.widgetRenamed.connect(self.emit_viewerRenamed)

    def setModel(self, model):
        self.clear()
        for i in range(model.rowCount(QModelIndex())):
            viewer = model.viewer(i)
            self.insertViewer(viewer, i, False)

    def viewer(self, i) -> vtkViewer:
        return self.widget(i).viewer

    def lattice(self, i, j) -> vtkLattice:
        return self.viewer(i).lattice[j]

    def openViewer(self, index: int):
        widget = vtkWidget(vtkViewer(f"vtkViewer[{index}]"))
        self.insertTab(index, widget, widget.name())

    def closeViewer(self, index: int):
        self.removeTab(index)

    def insertViewer(self, viewer: vtkViewer, i: int, callback: bool = True):
        widget = vtkWidget(viewer)
        widget.render()
        if not callback:
            self.widgetInserted.disconnect()
        self.insertTab(i, widget, widget.name())
        self.widgetInserted.connect(self.emit_viewerInserted)

    def removeViewer(self, index: int, callback: bool = True):
        if not callback:
            self.widgetRemoved.disconnect()
        self.removeTab(index)
        self.widgetRemoved.connect(self.emit_viewerRemoved)

    def renameViewer(self, i: int, name: str, callback: bool = True):
        self.tabBar().labels[i].setText(name)

    def appendLattice(self, lattice: vtkLattice, i: int, callback: bool = True):
        self.widget(i).appendLattice(lattice)
        if callback:
            self.emit_latticeInserted(i, len(self.viewer(i))-1)

    def insertLattice(self, lattice: vtkLattice, i: int, j: int, callback: bool = True):
        self.widget(i).insertLattice(lattice, j)
        if callback:
            self.emit_latticeInserted(i, j)

    def removeLattice(self, i: int, j: int, callback: bool = True):
        self.widget(i).removeLattice(j)
        if callback:
            self.emit_latticeInserted(i, j)

    def selectViewer(self, i: int, callback: bool = True):
        self.setCurrentIndex(i)
        if callback:
            self.emit_viewerSelected(i)

    def selectLattice(self, i: int, j: int):
        self.setCurrentIndex(i)

    def emit_viewerInserted(self, i: int):
        self.viewerInserted.emit(self, i)

    def emit_viewerRemoved(self, i: int):
        self.viewerRemoved.emit(self, i)

    def emit_latticeInserted(self, i: int, j: int):
        self.latticeInserted.emit(self, i, j)

    def emit_viewerRenamed(self, i: int, name: str):
        self.viewerRenamed.emit(self, i, name)

    def emit_viewerSelected(self, i: int):
        self.viewerSelected.emit(i)

    def closeEvent(self, event):
        for i in range(self.count()):
            self.widget(i).closeEvent(event)
        return super().closeEvent(event)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        for poscar in event.mimeData().text().splitlines():
            poscar = poscar.strip().split('///')[1].replace('\\', '/')
            index = self.currentIndex()
            lattice = vtkLattice.load_poscar(poscar)
            if self.count() > 1:
                self.appendLattice(lattice, index)
            else:
                self.openViewer(index)
                self.appendLattice(lattice, index)
