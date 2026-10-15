from unittest import TestCase
from src.QtLattice.lib.MyTabWidget import MyTabWidget
from . import openqt


class TestMyTabWidget(TestCase):

    @openqt
    def test_MyTabWidget(self):

        from PyQt5.QtWidgets import QWidget

        tab = MyTabWidget()
        tab.widgetInserted.connect(lambda i: print(f"inserted widget {i}"))
        tab.widgetRemoved.connect(lambda i: print(f"removed widget {i}"))
        tab.widgetOpenRequested.connect(lambda i: print(f"open widget {i}"))
        tab.widgetCloseRequested.connect(lambda i: print(f"close widget {i}"))
        tab.insertTab(0, QWidget(), 'widget1')
        tab.insertTab(0, QWidget(), 'widget0')
        tab.insertTab(2, QWidget(), 'widget1')
        tab.removeTab(1)
        return tab