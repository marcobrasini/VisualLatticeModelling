from unittest import TestCase
from PyQt5.QtWidgets import QLineEdit, QSpinBox, QLabel
from src.QtLattice.lib.MyFormWidget import MyFormWidget
from . import openqt, qt


class TestMyFormWidget(TestCase):

    def items(self):
        return [
            ('First name:', QLineEdit("Donald")),
            ('Last name:', QLineEdit("Duck")),
            ('Age:', QSpinBox()),
        ]

    @openqt
    def test_MyFormWidget(self):
        form = MyFormWidget(self.items())
        return form

    @openqt
    def test_MyFormWidget_clean(self):
        form = MyFormWidget(self.items())
        form.clean()
        assert form.count() == 0
        return form

    @qt
    def test_MyFormWidget_append(self):
        form = MyFormWidget(self.items())
        assert form.count() == 3

    @openqt
    def test_MyFormWidget_append(self):
        form = MyFormWidget(self.items())
        form.append(self.items()[2])
        assert form.count() == 4
        return form

    @openqt
    def test_MyFormWidget_insert(self):
        form = MyFormWidget(self.items())
        form.insert(self.items()[2], 0)
        assert form.count() == 4
        return form

    @openqt
    def test_MyFormWidget_remove(self):
        form = MyFormWidget(self.items())
        form.remove(0)
        assert form.count() == 2
        return form

    @qt
    def test_MyFormWidget_label(self):
        form = MyFormWidget(self.items())
        assert isinstance(form.label(0), QLabel)
        assert form.label(0).text() == 'First name:'
        assert isinstance(form.label(1), QLabel)
        assert form.label(1).text() == 'Last name:'
        assert isinstance(form.label(2), QLabel)
        assert form.label(2).text() == 'Age:'

    @qt
    def test_MyFormWidget_field(self):
        form = MyFormWidget(self.items())
        assert isinstance(form.field(0), QLineEdit)
        assert form.field(0).text() == 'Donald'
        assert isinstance(form.field(1), QLineEdit)
        assert form.field(1).text() == 'Duck'
        assert isinstance(form.field(2), QSpinBox)
        assert form.field(2).value() == 0

    @openqt
    def test_MyFormWidget_setLabel(self):
        form = MyFormWidget(self.items())
        form.label(0).setText('new First Name')
        form.label(1).setText('new Last Name')
        form.label(2).setText('new Age')
        assert form.label(0).text() == 'new First Name'
        assert form.label(1).text() == 'new Last Name'
        assert form.label(2).text() == 'new Age'
        return form

    @openqt
    def test_MyFormWidget_setField(self):
        form = MyFormWidget(self.items())
        form.field(0).setText('Mickey')
        form.field(1).setText('Mouse')
        assert form.field(0).text() == 'Mickey'
        assert form.field(1).text() == 'Mouse'
        return form
