from pyqtconsole.console import PythonConsole


class QtTerminalConsole(PythonConsole):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # eval_in_thread() eseguiva i comandi in un thread separato: ogni
        # comando che tocca model/widget Qt (es. model.appendViewer(...))
        # agiva sulla GUI fuori dal thread principale -> crash casuali.
        # eval_queued() esegue nel thread della GUI.
        self.eval_queued()
