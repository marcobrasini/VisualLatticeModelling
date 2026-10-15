import logging
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPlainTextEdit


class _RecorderHandler(logging.Handler):
    """Handler di logging che inoltra i record tramite un segnale Qt.

    Il segnale rende l'append thread-safe: se il log arriva da un thread
    diverso da quello della GUI, Qt accoda la chiamata nel thread principale.
    """

    def __init__(self, signal):
        super().__init__()
        self._signal = signal

    def emit(self, record):
        try:
            self._signal.emit(self.format(record))
        except RuntimeError:
            pass  # widget già distrutto (es. log durante lo shutdown)
        except Exception:
            self.handleError(record)


class QtTerminalRecorder(QPlainTextEdit):
    # Composizione invece di ereditarietà multipla Handler + QPlainTextEdit:
    # prima Handler.close() mascherava QWidget.close() e l'append avveniva
    # direttamente dal thread del logger.

    recordReceived = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.document().setDocumentMargin(0)
        self.setReadOnly(True)
        self.handler = _RecorderHandler(self.recordReceived)
        self.recordReceived.connect(self.appendPlainText)
