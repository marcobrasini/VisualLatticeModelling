from PyQt5.QtWidgets import QTabWidget, QWidget
from PyQt5.QtCore import pyqtSignal
from .MyTabBar import MyTabBar


class MyTabWidget(QTabWidget):

    widgetRemoved = pyqtSignal(int)
    widgetInserted = pyqtSignal(int)
    widgetOpenRequested = pyqtSignal(int)
    widgetRenameRequested = pyqtSignal(int, str)
    widgetCloseRequested = pyqtSignal(int)

    def __init__(self, parent=None, addWidget=QWidget):
        super().__init__(parent=parent)
        self.setTabBar(MyTabBar(self))
        self.defaultTab(addWidget())
        self.widgetOpenRequested = self.tabBar().tabOpenRequested
        self.widgetRenameRequested = self.tabBar().tabRenameRequested
        self.widgetCloseRequested = self.tabBar().tabCloseRequested

    def defaultTab(self, widget):
        self.addTab(widget, None)
        self.tabBar().defaultTab()

    def insertTab(self, index: int, widget: QWidget, name: str = None):
        super().insertTab(index, widget, None)
        self.tabBar().insertTab(index, name)
        self.setCurrentIndex(index)
        self.widgetInserted.emit(index)

    def renameTab(self, index: int, name: str):
        self.tabBar().labels[index].setText(name)

    def removeTab(self, index: int):
        if index != self.count() - 1:
            self.widget(index).close()
            self.tabBar().removeTab(index)
            super().removeTab(index)
            self.widgetRemoved.emit(index)

    def clear(self):
        for i in range(self.count() - 1):
            self.removeTab(0)
