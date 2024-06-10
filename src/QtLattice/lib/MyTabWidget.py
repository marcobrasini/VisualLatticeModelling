from PyQt5.QtWidgets import QTabWidget, QWidget, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from .MyTabBar import MyTabBar


class MyTabWidget(QTabWidget):

    class MyTabDefault(QLabel):

        def __init__(self, parent=None):
            super().__init__(parent=parent)
            self.setScaledContents(True)
            self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            self.setPixmap(QPixmap('utils/defaultTitle.png'))
            self.setAlignment(Qt.AlignCenter)
            self.resize(self.pixmap().size())

    def __init__(self, parent=None, tabWidget=QWidget):
        super().__init__(parent=parent)
        self.tabWidget = tabWidget
        self.setAcceptDrops(True)
        self.setTabBar(MyTabBar(self))
        self.defaultTab(MyTabWidget.MyTabDefault())

    def defaultTab(self, widget):
        self.addTab(widget, None)
        self.tabBar().defaultTab()

    def appendTab(self):
        index = self.count() - 1
        super().insertTab(index, self.tabWidget(), None)
        self.tabBar().insertTab(index, None)
        self.setCurrentIndex(index)

    def removeTab(self, index):
        if index != self.count() - 1:
            self.widget(index).close()
            self.tabBar().removeTab(index)
            super().removeTab(index)
