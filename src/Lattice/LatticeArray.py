import numpy as np
from copy import deepcopy


class LatticeArray(np.ndarray):

    def __new__(cls,
                array: list = [],
                basis: np.ndarray = None):
        obj = np.asarray(deepcopy(array)).view(cls)
        obj.basis = basis
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.basis = getattr(obj, 'basis', None)

    def get_attribute(self, attribute):
        value = [getattr(obj, attribute) for i, obj in enumerate(self)]
        return np.array(value)

    def get_method(self, method):
        value = [getattr(obj, method)() for i, obj in enumerate(self)]
        return np.array(value)

    def set_attribute(self, attribute, value):
        for i, obj in enumerate(self):
            setattr(obj, attribute, value[i])
        return self

    def set_method(self, method, value):
        for i, obj in enumerate(self):
            getattr(obj, method)(value[i])
        return self
