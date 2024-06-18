from PyQt5.QtWidgets import QMenu


class QtMenuEdit(QMenu):

    def __init__(self, parent=None):
        super().__init__('Edit', parent=parent)

    def model(self):
        return self.parent().model
