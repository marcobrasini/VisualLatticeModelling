import logging
from textwrap import dedent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSplitter
from .QtTerminalRecorder import QtTerminalRecorder
from .QtTerminalConsole import QtTerminalConsole


class QtTerminal(QSplitter):

    def __init__(self, parent=None):
        super().__init__(Qt.Horizontal, parent=parent)
        self.console = QtTerminalConsole(self)
        self.recorder = QtTerminalRecorder(self)
        self.addWidget(self.console)
        self.addWidget(self.recorder)
        # Logger
        self.logger = logging.getLogger('qt')
        self.logger.addHandler(self.recorder)
        self.init_environment()

    def add_local(self, name, value):
        self.console.push_local_ns(name, value)
        self.logger.info("    {} : {} = {}".format(name, type(value), value))


    def init_environment(self):

        import numpy as np
        from Lattice import Lattice
        from vtkLattice import vtkLattice

        self.logger.info(dedent("""
            QtLattice environment initialization
            ... imported logging module
            ... imported numpy module as np
            ... imported Lattice class
            ... imported vtkLattice class
        """))
        self.console.push_local_ns('logging', logging)
        self.console.push_local_ns('np', np)
        self.console.push_local_ns('Lattice', Lattice)
        self.console.push_local_ns('vtkLattice', vtkLattice)
        self.logger.info("Global variable added:")
        self.add_local('model', getattr(self.parent(), 'model', None))
        self.add_local('logger', getattr(self.parent(), 'logger', None))
        self.logger.info("")
