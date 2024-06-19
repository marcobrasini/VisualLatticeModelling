from unittest import TestCase
from src.QtLattice.lib.MyFloatFormatter import MyFloatFormatter
from . import qt


class Test_MyFloatFormatter(TestCase):

    @qt
    def test_QFloatFormatter_setPrecision(self):
        qFloat = MyFloatFormatter(format="+16.10f").setPrecision()
        self.assertTrue(qFloat.precision == 0.0000000001)
        qFloat = MyFloatFormatter(format="+16.8f").setPrecision()
        self.assertTrue(qFloat.precision == 0.00000001)
        qFloat = MyFloatFormatter(format="+12.8f").setPrecision()
        self.assertTrue(qFloat.precision == 0.00000001)

    @qt
    def test_QFloatFormatter_setLimitation(self):
        qFloat = MyFloatFormatter(format="+16.10f").setLimitation()
        self.assertTrue(qFloat.limitation == 9999.9999999999)
        qFloat = MyFloatFormatter(format="+16.8f").setLimitation()
        self.assertTrue(qFloat.limitation == 999999.99999999)
        qFloat = MyFloatFormatter(format="+12.8f").setLimitation()
        self.assertTrue(qFloat.limitation == 99.99999999)

    @qt
    def test_QFloatFormatter_float_to_string(self):
        Widget = MyFloatFormatter(format="+12.8f")
        self.assertTrue(Widget.float_to_string(1.1286139) == " +1.12861390")
        self.assertTrue(Widget.float_to_string(61.1286139) == "+61.12861390")
        self.assertTrue(Widget.float_to_string(-61.1286139) == "-61.12861390")
        self.assertTrue(Widget.float_to_string(61.1286139999) == "+61.12861400")
        self.assertTrue(Widget.float_to_string(+361.1286139) == "+99.99999999")
        self.assertTrue(Widget.float_to_string(-361.1286139) == "-99.99999999")

    @qt
    def test_QFloatFormatter_string_to_float(self):
        Widget = MyFloatFormatter(format="+12.8f")
        self.assertTrue(Widget.string_to_float("61.1286139") == 61.12861390)
        self.assertTrue(Widget.string_to_float(" 61.1286139") == 61.12861390)
        self.assertTrue(Widget.string_to_float("+61.1286139") == 61.12861390)
        self.assertTrue(Widget.string_to_float("-61.1286139") == -61.12861390)
        self.assertTrue(Widget.string_to_float("61.1286139999") == 61.12861400)
        self.assertTrue(Widget.string_to_float(" 361.1286139") == +99.99999999)
        self.assertTrue(Widget.string_to_float("-361.1286139") == -99.99999999)

