import logging
from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDragMoveEvent, QDropEvent
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

    logger = logging.getLogger('qt')

    viewerSelectRequested = pyqtSignal(int)
    viewerInsertRequested = pyqtSignal(int, str)
    viewerRenameRequested = pyqtSignal(int, str)
    viewerRemoveRequested = pyqtSignal(int)
    latticeSelectRequested = pyqtSignal(int, int)
    latticeInsertRequested = pyqtSignal(int, int, str)
    latticeRenameRequested = pyqtSignal(int, int, str)
    latticeRemoveRequested = pyqtSignal(int, int)

    def __init__(self, model: QtViewerModel = None, parent: QObject = None):
        super().__init__(parent, QtViewerTabDefault)
        self.model = model
        self.setAcceptDrops(True)
        self.widgetOpenRequested.connect(self.request_viewerInsert)
        self.widgetCloseRequested.connect(self.request_viewerRemove)
        self.widgetRenameRequested.connect(self.request_viewerRename)
        self.tabBarClicked.connect(self.request_viewerSelect)

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
        self.logger.debug(
            f"  tab.viewer[{i}] selected.")

    def insertViewer(self, i: int):
        widget = vtkWidget(self.model.viewer(i)).render()
        self.insertTab(i, widget, widget.name())
        self.logger.debug(
            f"  tab.viewer[{i}] inserted.")

    def renameViewer(self, i: int):
        name = self.model.viewer(i).name
        self.tabBar().labels[i].setText(name)
        self.logger.debug(
            f"  tab.viewer[{i}] renamed {name}.")

    def removeViewer(self, i: int):
        self.removeTab(i)
        self.logger.debug(
            f"  tab.viewer[{i}] removed.")

    def selectLattice(self, i: int, j: int):
        self.setCurrentIndex(i)
        self.logger.debug(
            f"  tab.viewer[{i}].lattice[{j}] selected.")

    def insertLattice(self, i: int, j: int):
        lattice = self.model.lattice(i, j)
        self.widget(i).insertLattice(lattice, j)
        self.logger.debug(
            f"  tab.viewer[{i}].lattice[{j}] inserted.")

    def renameLattice(self, i: int, j: int):
        name = self.model.lattice(i, j).name
        self.logger.debug(
            f"  tab.viewer[{i}].lattice[{j}] renamed {name}.")

    def removeLattice(self, i: int, j: int):
        self.widget(i).removeLattice(j)
        self.logger.debug(
            f"  tab.viewer[{i}].lattice[{j}] removed.")

    def updateLattice(self, i: int, j: int):
        self.widget(i).refresh()
        self.logger.debug(
            f"  tab.viewer[{i}].lattice[{j}] updated.")

    ###########################################################################
    def request_viewerSelect(self, i: int):
        self.logger.debug(
            f"  requesting tab.viewer[{i}] selection.")
        if i < self.count() - 1:
            self.viewerSelectRequested.emit(i)

    def request_viewerAppend(self, viewer=""):
        self.logger.debug(
            f"  requesting tab.viewer[-1] appending.")
        viewer = viewer if viewer else f"vtkViewer[{self.count() - 1}]"
        self.viewerInsertRequested.emit(self.count() - 1, viewer)

    def request_viewerInsert(self, i: int, viewer=""):
        self.logger.debug(
            f"  requesting tab.viewer[{i}] insertion.")
        viewer = viewer if viewer else f"vtkViewer[{i}]"
        self.viewerInsertRequested.emit(i, viewer)

    def request_viewerRename(self, i: int, name: str):
        self.logger.debug(
            f"  requesting tab.viewer[{i}] renaming.")
        self.viewerRenameRequested.emit(i, name)

    def request_viewerRemove(self, i: int):
        self.logger.debug(
            f"  requesting tab.viewer[{i}] removal.")
        self.viewerRemoveRequested.emit(i)

    def request_latticeSelect(self, i: int, j: int):
        self.logger.debug(
            f"  requesting tab.viewer[{i}].lattice[{j}] selection.")
        self.latticeSelectRequested.emit(i, j)

    def request_latticeAppend(self, i: int, lattice=""):
        self.logger.debug(
            f"  requesting tab.viewer[{i}].lattice[-1] appending.")
        self.latticeInsertRequested.emit(i, len(self.viewer(i)), lattice)

    def request_latticeInsert(self, i: int, j: int, lattice=""):
        self.logger.debug(
            f"  requesting tab.viewer[{i}].lattice[{j}] insertion.")
        self.latticeInsertRequested.emit(i, j, lattice)

    def request_latticeRename(self, i: int, j: int, name: str):
        self.logger.debug(
            f"  requesting tab.viewer[{i}].lattice[{j}] renaming.")
        self.latticeRenameRequested.emit(i, j, name)

    def request_latticeRemove(self, i: int, j: int):
        self.logger.debug(
            f"  requesting tab.viewer[{i}].lattice[{j}] removal.")
        self.latticeRemoveRequested.emit(i, j)

    ###########################################################################
    def closeEvent(self, event):
        for i in range(self.count()):
            self.widget(i).closeEvent(event)
        return super().closeEvent(event)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        # urls()/toLocalFile() invece di split('///'): su Linux/macOS
        # "file:///home/..." diventava "home/..." (senza "/" iniziale).
        files = [url.toLocalFile() for url in event.mimeData().urls()
                 if url.isLocalFile()]
        for poscar in files:
            if self.count() - 1 > 0:
                # se è selezionato il tab di default (l'ultimo) usa l'ultimo viewer
                i = min(self.currentIndex(), self.count() - 2)
                self.logger.info(
                    "\nLoading lattice from POSCAR file\n" + poscar)
                self.request_latticeAppend(i, poscar)
                self.logger.info(
                    "Loaded lattice.\n")
            else:
                self.logger.info(
                    "\nOpening lattice from POSCAR file\n" + poscar)
                self.request_viewerAppend()
                self.logger.info(
                    "Opened new viewer.")
                self.request_latticeAppend(self.count() - 2, poscar)
                self.logger.info(
                    "Opened lattice.\n")
        event.acceptProposedAction()
