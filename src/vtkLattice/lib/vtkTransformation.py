import numpy as np
from vtkmodules.vtkCommonMath import vtkMatrix4x4
from vtkmodules.vtkCommonTransforms import vtkTransform


DEFAULT_SCALE = (1.0, 1.0, 1.0)
DEFAULT_TRANSLATION = (0.0, 0.0, 0.0)
DEFAULT_ORIENTATION = vtkMatrix4x4()
DEFAULT_ORIENTATION.Identity()


class vtkTransformation:

    def __init__(self,
                 scale = DEFAULT_SCALE,
                 translation = DEFAULT_TRANSLATION,
                 orientation = DEFAULT_ORIENTATION,
                 ):
        self.scale = scale
        self.translation = translation
        self.orientation = orientation

    def __call__(self):
        transformation = vtkTransform()
        transformation.Translate(self.translation)
        transformation.Concatenate(self.orientation)
        transformation.Scale(self.scale)
        return transformation

    @staticmethod
    def make_orientation(direction, axis):
        direction = direction/np.linalg.norm(direction)
        i, j, k = np.roll([0, 2, 1], axis)
        orientation = np.zeros((3, 3))
        orientation[i] = direction
        for axis in np.identity(3):
            attempt = np.cross(direction, axis)
            modulus = np.linalg.norm(attempt)
            if not np.isclose(modulus, 0.0):
                orientation[j] = attempt/modulus
                break
        orientation[k] = np.cross(orientation[j], orientation[i])
        # Create the direction cosine matrix
        matrix = vtkMatrix4x4()
        matrix.Identity()
        for i in range(0, 3):
            matrix.SetElement(i, 0, orientation[0][i])
            matrix.SetElement(i, 1, orientation[1][i])
            matrix.SetElement(i, 2, orientation[2][i])
        return matrix
