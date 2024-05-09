import numpy as np


class LatticeBasis(np.ndarray):

    def __new__(cls,
                array: np.ndarray = np.identity(3),
                parameter: float = 1.0):
        obj = np.asarray(array * parameter).view(cls)
        obj.parameter = parameter
        return obj

    def __array_finalize__(self, obj = None):
        if obj is None: return
        self.parameter = getattr(obj, 'parameter', 1.0)

    def a(self) -> float:
        return np.linalg.norm(self.__getitem__(0))

    def b(self) -> float:
        return np.linalg.norm(self.__getitem__(1))

    def c(self) -> float:
        return np.linalg.norm(self.__getitem__(2))

    def alpha(self) -> float:
        u = self.__getitem__(1) / self.b()
        v = self.__getitem__(2) / self.c()
        return np.arccos(u @ v) * 180/np.pi

    def beta(self) -> float:
        u = self.__getitem__(2) / self.c()
        v = self.__getitem__(0) / self.a()
        return np.arccos(u @ v) * 180 / np.pi

    def gamma(self) -> float:
        u = self.__getitem__(0) / self.a()
        v = self.__getitem__(1) / self.b()
        return np.arccos(u @ v) * 180 / np.pi

    def volume(self) -> float:
        return np.linalg.det(self)
