from EyeImage import EyeImage
from Refractive_Defect import Refractive_Defect
from IOP import IOP

class Eye:
    def __init__(self, diagnosis = None, 
                 refractiveDefect: Refractive_Defect = None, 
                 phakic_Pseudophakic = None, 
                 iop: IOP = None, 
                 pachymetry = None, 
                 axialLength = None, 
                 vf_md = None, 
                 fundusImage: EyeImage = None, 
                 imageWithContour: EyeImage = None):
      self._diagnosis = diagnosis
      self._refractiveDefect = refractiveDefect
      self._phakic_Pseudophakic = phakic_Pseudophakic
      self._iop = iop
      self._pachymetry = pachymetry
      self._axialLength = axialLength
      self._vf_md = vf_md
      self._fundusImage = fundusImage
      self._imageWithContour = imageWithContour

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value

    @property
    def refractiveDefect(self) -> Refractive_Defect:
        return self._refractiveDefect

    @refractiveDefect.setter
    def refractiveDefect(self, value: Refractive_Defect):
        self._refractiveDefect = value

    @property
    def phakic_Pseudophakic(self):
        return self._phakic_Pseudophakic

    @phakic_Pseudophakic.setter
    def phakic_Pseudophakic(self, value):
        self._phakic_Pseudophakic = value

    @property
    def iop(self) -> IOP:
        return self._iop

    @iop.setter
    def iop(self, value: IOP):
        self._iop = value

    @property
    def pachymetry(self):
        return self._pachymetry

    @pachymetry.setter
    def pachymetry(self, value):
        self._pachymetry = value

    @property
    def axialLength(self):
        return self._axialLength

    @axialLength.setter
    def axialLength(self, value):
        self._axialLength = value

    @property
    def vf_md(self):
        return self._vf_md

    @vf_md.setter
    def vf_md(self, value):
        self._vf_md = value

    @property
    def fundusImage(self) -> EyeImage:
        return self._fundusImage

    @fundusImage.setter
    def fundusImage(self, value: EyeImage):
        self._fundusImage = value

    @property
    def imageWithContour(self) -> EyeImage:
        return self._imageWithContour

    @imageWithContour.setter
    def imageWithContour(self, value: EyeImage):
        self._imageWithContour = value
