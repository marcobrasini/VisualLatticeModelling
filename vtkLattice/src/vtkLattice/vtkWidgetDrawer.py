from .lib.vtkEntityPolyline import vtkEntityPolyline
from .lib.vtkEntityPolygon import vtkEntityPolygon
from .lib.vtkEntityPoly import vtkEntityPoly
from .vtkDrawer import vtkDrawer


class vtkDrawerPolyline(vtkDrawer):

    def __init__(self, widget):
        super().__init__(widget)
        self.entity = vtkEntityPolyline()


class vtkDrawerPolygon(vtkDrawer):

    def __init__(self, widget):
        super().__init__(widget)
        self.entity = vtkEntityPolygon()


class vtkDrawerPoly(vtkDrawer):

    def __init__(self, widget):
        super().__init__(widget)
        self.entity = vtkEntityPoly()


class vtkWidgetDrawer:

    def __init__(self, widget):
        self.widget = widget
        self.entities = {
            'polyline': [],
            'polygon': [],
            'poly': [],
        }

    def drawing_polyline(self):
        self.drawer = vtkDrawerPolyline(self.widget)
        self.entities['polyline'].append(self.drawer.entity)

    def drawing_polygon(self):
        self.drawer = vtkDrawerPolygon(self.widget)
        self.entities['polygon'].append(self.drawer.entity)

    def drawing_poly(self):
        self.drawer = vtkDrawerPoly(self.widget)
        self.entities['poly'].append(self.drawer.entity)
