class Refractive_Defect:
    def __init__(self, dioptre1 = None, 
                 dioptre2 = None, 
                 astigmatism = None):
        self._dioptre1 = dioptre1
        self._dioptre2 = dioptre2
        self._astigmatism = astigmatism

    @property
    def dioptre1(self):
        return self._dioptre1

    @dioptre1.setter
    def set_dioptre1(self, value):
        self._dioptre1 = value

    @property
    def dioptre2(self):
        return self._dioptre2

    @dioptre2.setter
    def dioptre2(self, value):
        self._dioptre2 = value

    @property
    def astigmatism(self):
        return self._astigmatism

    @astigmatism.setter
    def astigmatism(self, value):
        self._astigmatism = value
