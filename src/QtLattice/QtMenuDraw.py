from PyQt5.QtWidgets import QMenu, QAction


class QtMenuDraw(QMenu):

    def __init__(self, parent=None):
        super().__init__('Draw', parent=parent)

        self.polyline = QAction('Polyline')
        self.addAction(self.polyline)

        self.convex = QAction('Convex hull')
        self.addAction(self.convex)


    def model(self):
        return self.parent().model
