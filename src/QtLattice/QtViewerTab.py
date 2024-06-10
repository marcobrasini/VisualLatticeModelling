from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QModelIndex
from vtkLattice import vtkWidget
from .lib.MyTabWidget import MyTabWidget


class QtViewerTab(QAbstractItemView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = MyTabWidget(self, vtkWidget)
        self.setViewport(self.widget)
        self.setAcceptDrops(True)

    def setModel(self, model):
        super().setModel(model)
        self.widget.clear()
        for viewer in range(self.model().rowCount(QModelIndex())):
            index = self.model().index(viewer, 0)
            widget = vtkWidget(index.internalPointer().vtk())
            self.insertViewer(index, widget)

    def insertViewer(self, index, widget):
        self.widget.insertTab(index.row(), widget, widget.name())

    def removeViewer(self, index):
        self.widget.removeTab(index)

    def closeEvent(self, event):
        for i in range(self.widget.count()):
            self.widget.widget(i).closeEvent(event)
        return super().closeEvent(event)

