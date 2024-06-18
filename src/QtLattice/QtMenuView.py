from PyQt5.QtWidgets import QMenu


class QtMenuView(QMenu):

    def __init__(self, parent=None):
        super().__init__('View', parent=parent)

    def model(self):
        return self.parent().model
