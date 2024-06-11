from PyQt5.QtWidgets import QTabBar, QLineEdit, QToolButton
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent


class MyTabBarAdder(QToolButton):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QToolButton {
                border-image: url("utils/icons/iconPlus.png");
            }
            QToolButton:hover {
                border-image: url("utils/icons/iconPlus_hover.png");
            }
        """)


class MyTabBarLabel(QLineEdit):

    def __init__(self, text: str = ""):
        super().__init__()
        self.setText(text)
        self.renamed()
        self.editingFinished.connect(self.renamed)

    def renamed(self):
        self.setFrame(False)
        self.setEnabled(False)

    def renaming(self):
        self.setFrame(True)
        self.setEnabled(True)
        self.selectAll()


class MyTabBar(QTabBar):

    tabOpenRequested = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setUpdatesEnabled(True)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.labels = []
        self.appendTab = MyTabBarAdder()
        self.appendTab.clicked.connect(self.emit_tabOpenRequested)
        self.tabBarDoubleClicked.connect(self.renameTab)
        self.currentChanged.connect(self.changeTab)
        self.tabMoved.connect(self.movedTab)
        self.setSelectionBehaviorOnRemove(QTabBar.SelectLeftTab)
        self.setStyleSheet("""
            QTabBar::close-button {
                image: url("utils/icons/iconCross.png")
            }
            QTabBar::close-button:hover {
                image: url("utils/icons/iconCross_hover.png")
            }
            """)

    def defaultTab(self):
        self.setTabButton(0, QTabBar.RightSide, self.appendTab)
        self.setTabEnabled(0, False)

    def insertTab(self, index, text):
        self.labels.insert(index, MyTabBarLabel(text))
        self.setTabButton(index, QTabBar.LeftSide, self.labels[index])

    def removeTab(self, index):
        del self.labels[index]

    def renameTab(self, index):
        if index < self.count() - 1:
            self.labels[index].renaming()

    def changeTab(self):
        for label in self.labels:
            label.renamed()

    def movedTab(self, from_index, to_index):
        label = self.labels.pop(from_index)
        self.labels.insert(to_index, label)

    def emit_tabOpenRequested(self):
        self.tabOpenRequested.emit(self.count() - 1)

    def mousePressEvent(self, event: QMouseEvent):
        if self.isMovable():
            self.pos0 = event.pos()
            self.dragRect = super().tabRect(super().tabAt(event.pos()))
            self.lastRect = super().tabRect(self.count()-1)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.isMovable():
            dragging = event.pos().x() - self.pos0.x()
            if self.dragRect.right() + dragging < self.lastRect.left():
                super().mouseMoveEvent(event)
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)
