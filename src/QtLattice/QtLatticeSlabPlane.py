from .lib.MyFloatFormatter import MyFloatFormatter
from .lib.MyFloatEdit import MyFloatEdit
from .lib.MyArrayEdit import MyArrayEdit
from .lib.MyFormWidget import MyFormWidget


class QtLatticeSlabPlane(MyFormWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setTitle("Plane")
        self.setup({
            "Miller index": MyArrayEdit([0, 0, 0], formatter=MyFloatFormatter("4.0f")),
            "Distance (A)": MyFloatEdit(0.),
        })