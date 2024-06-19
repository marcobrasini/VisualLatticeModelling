from logging import Handler
from PyQt5.QtWidgets import QPlainTextEdit


class QtTerminalRecorder(Handler, QPlainTextEdit):

    def __init__(self, parent=None):
        Handler.__init__(self)
        QPlainTextEdit.__init__(self, parent=parent)
        self.document().setDocumentMargin(0)
        self.setReadOnly(True)
        self.flushOnClose = False

    def emit(self, record):
        self.appendPlainText(self.format(record))
