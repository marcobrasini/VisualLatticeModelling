import sys
import logging
import traceback
import faulthandler
from PyQt5.QtWidgets import QApplication
from QtLattice.ViLaMo import QtMain


def excepthook(exc_type, exc, tb):
    # PyQt5 con l'excepthook di default chiama qFatal() su ogni eccezione
    # non gestita dentro uno slot: il programma "crasha" senza spiegazioni.
    # Con un excepthook personalizzato l'errore viene loggato e l'app continua.
    msg = ''.join(traceback.format_exception(exc_type, exc, tb))
    logging.getLogger('qt').error("Eccezione non gestita:\n" + msg)
    sys.__excepthook__(exc_type, exc, tb)


if __name__ == '__main__':
    faulthandler.enable()
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    main = QtMain()
    sys.exit(app.exec_())
