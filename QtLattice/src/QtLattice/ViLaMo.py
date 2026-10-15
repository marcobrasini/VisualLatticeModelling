import sys
import logging
import traceback
import faulthandler
from PyQt5.QtWidgets import QApplication, QMainWindow
from .QtViewer import QtViewer


def excepthook(exc_type, exc, tb):
    # PyQt5 con l'excepthook di default chiama qFatal() su ogni eccezione
    # non gestita dentro uno slot: il programma "crasha" senza spiegazioni.
    # Con un excepthook personalizzato l'errore viene loggato e l'app continua.
    msg = ''.join(traceback.format_exception(exc_type, exc, tb))
    logging.getLogger('qt').error("Eccezione non gestita:\n" + msg)
    sys.__excepthook__(exc_type, exc, tb)


class QtMain(QMainWindow):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('qt')
        self.logger.setLevel(logging.DEBUG)
        self.viewer = QtViewer()
        self.viewer.setup([])
        self.setCentralWidget(self.viewer)
        self.showMaximized()

    def closeEvent(self, event):
        self.viewer.closeEvent(event)
        super().closeEvent(event)


# Per via dell'import relativo va lanciato come modulo:
#   python -m <nome_pacchetto>.ViLaMo
if __name__ == '__main__':

    faulthandler.enable()   # stampa lo stack anche in caso di segfault (VTK/Qt C++)
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    main = QtMain()
    sys.exit(app.exec_())
