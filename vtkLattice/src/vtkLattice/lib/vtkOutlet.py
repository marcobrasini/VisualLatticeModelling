from abc import ABC, abstractmethod


class vtkOutlet(ABC):

    @abstractmethod
    def translate(self, displacement):
        pass

    @abstractmethod
    def rotate(self, angle, axis):
        pass

    @abstractmethod
    def rescale(self, factor):
        pass
