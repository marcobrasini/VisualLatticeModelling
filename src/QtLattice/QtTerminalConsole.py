from pyqtconsole.console import PythonConsole


class QtTerminalConsole(PythonConsole):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.eval_in_thread()
