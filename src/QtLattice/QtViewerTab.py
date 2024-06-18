from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDropEvent
from vtkLattice import vtkWidget, vtkViewer, vtkLattice
from .lib.MyTabWidget import MyTabWidget
from .QtViewerModel import QtViewerModel


class QtViewerTabDefault(QLabel):
    def __init__(self, parent: QObject = None):
        super().__init__(parent=parent)
        self.setScaledContents(True)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setPixmap(QPixmap('utils/defaultTitle.png'))
        self.setAlignment(Qt.AlignCenter)
        self.resize(self.pixmap().size())


class QtViewerTab(MyTabWidget):

    viewerSelectRequested = pyqtSignal(int)
    viewerInsertRequested = pyqtSignal(int, str)
    viewerRenameRequested = pyqtSignal(int, str)
    viewerRemoveRequested = pyqtSignal(int)
    latticeSelectRequested = pyqtSignal(int, int)       #
    latticeInsertRequested = pyqtSignal(int, int, str)  #
    latticeRenameRequested = pyqtSignal(int, int, str)  #
    latticeRemoveRequested = pyqtSignal(int, int)       #

    def __init__(self, model: QtViewerModel = None, parent: QObject = None):
        super().__init__(parent, QtViewerTabDefault)
        self.model = model
        self.setAcceptDrops(True)
        self.widgetOpenRequested.connect(self.request_viewerInsert)
        self.widgetCloseRequested.connect(self.request_viewerRemove)
        self.widgetRenameRequested.connect(self.request_viewerRename)
        self.currentChanged.connect(self.request_viewerSelect)

    def setup(self):
        self.clear()
        for i in range(self.model.viewerCount()):
            self.insertViewer(i)

    def viewer(self, i: int) -> vtkViewer:
        return self.widget(i).viewer

    def lattice(self, i: int, j: int) -> vtkLattice:
        return self.viewer(i).lattice[j]

    ###########################################################################
    def selectViewer(self, i: int):
        self.setCurrentIndex(i)

    def insertViewer(self, i: int):
        widget = vtkWidget(self.model.viewer(i)).render()
        self.insertTab(i, widget, widget.name())

    def renameViewer(self, i: int):
        name = self.model.viewer(i).name
        self.tabBar().labels[i].setText(name)

    def removeViewer(self, i: int):
        self.removeTab(i)

    def selectLattice(self, i: int, j: int):
        self.setCurrentIndex(i)

    def insertLattice(self, i: int, j: int):
        lattice = self.model.lattice(i, j)
        self.widget(i).insertLattice(lattice, j)

    def renameLattice(self, i: int, j: int):
        pass

    def removeLattice(self, i: int, j: int):
        self.widget(i).removeLattice(j)

    def updateLattice(self, i: int, j: int):
        self.widget(i).refresh()

    ###########################################################################
    def request_viewerSelect(self, i: int):
        if i < self.count() - 1:
            self.viewerSelectRequested.emit(i)

    def request_viewerAppend(self, viewer = ""):
        viewer = viewer if viewer else f"vtkViewer[{self.count() - 1}]"
        self.viewerInsertRequested.emit(self.count()-1, viewer)

    def request_viewerInsert(self, i: int, viewer = ""):
        viewer = viewer if viewer else f"vtkViewer[{i}]"
        self.viewerInsertRequested.emit(i, viewer)

    def request_viewerRename(self, i: int, name: str):
        self.viewerRenameRequested.emit(i, name)

    def request_viewerRemove(self, i: int):
        self.viewerRemoveRequested.emit(i)

    def request_latticeSelect(self, i: int, j: int):
        self.latticeSelectRequested.emit(i, j)

    def request_latticeAppend(self, i: int, lattice = ""):
        self.latticeInsertRequested.emit(i, len(self.viewer(i)), lattice)

    def request_latticeInsert(self, i: int, j: int, lattice = ""):
        self.latticeInsertRequested.emit(i, j, lattice)

    def request_latticeRename(self, i: int, j: int, name: str):
        self.latticeRenameRequested.emit(i, j, name)

    def request_latticeRemove(self, i: int, j: int):
        self.latticeRemoveRequested.emit(i, j)

    ###########################################################################
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
            if self.count() > 1:
                self.request_latticeAppend(self.currentIndex(), poscar)
            else:
                self.request_viewerAppend()
                self.request_latticeAppend(self.count() - 1, poscar)
