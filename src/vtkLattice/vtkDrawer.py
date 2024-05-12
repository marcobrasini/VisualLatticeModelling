from .lib.vtkEntityPolyline import vtkEntityPolyline
from .lib.vtkEntityPolygon import vtkEntityPolygon
from .lib.vtkEntityPoly import vtkEntityPoly


class vtkDrawer:

    def __init__(self, parent):
        self.parent = parent
        self.renderer = self.parent.GetCurrentRenderer
        self.entities = {
            'polyline': [],
            'polygon': [],
            'poly': [],
        }

    def init_polyline(self):
        polyline = vtkEntityPolyline()
        self.entities['polyline'].append(polyline)

    def init_polygon(self):
        polygon = vtkEntityPolygon()
        self.entities['polygon'].append(polygon)

    def init_poly(self):
        poly = vtkEntityPoly()
        self.entities['poly'].append(poly)

    def draw_polyline(self, points):
        polyline = self.entities['polyline'][-1]
        self.renderer().RemoveActor(polyline.actor)
        polyline.set_points(points)
        polyline.render(self.renderer())

    def draw_polygon(self, points):
        polygon = self.entities['polygon'][-1]
        self.renderer().RemoveActor(polygon.actor)
        polygon.set_points(points)
        polygon.render(self.renderer())

    def draw_poly(self, points):
        poly = self.entities['poly'][-1]
        self.renderer().RemoveActor(poly.actor)
        poly.set_points(points)
        poly.render(self.renderer())
