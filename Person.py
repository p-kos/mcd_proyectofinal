import pandas as pd
import cv2 as cv
from matplotlib import pyplot as plt
from Eye import Eye

class Person:
    def __init__(self, 
                 id = None, 
                 age: int = None, 
                 gender = None, 
                 odEye: Eye = None, 
                 osEye: Eye = None):
        self._id = id
        self._age = age
        self._gender = gender
        self._odEye = odEye
        self._osEye = osEye

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def odEye(self) -> Eye:
        return self._odEye

    @odEye.setter
    def odEye(self, value: Eye):
        self._odEye = value

    @property
    def osEye(self) -> Eye:
        return self._osEye

    @osEye.setter
    def osEye(self, value: Eye):
        self._osEye = value

    def __str__(self):
        return f'Person:{str(self._id)}; Age:{self.age}; Gender: {self.gender}'

    def display(self):
      print("Person: ", end="")
      if self._id == None:
         print('N/A')
      else:
        print(self._id)
      print(f" ├─Age: {self.age}")
      print(f" ├─Gender: {self.gender}")
      if (self._odEye != None):
        print(f" ├─Od Eye: ")
        print(f" |   ├─Diagnosis {self.odEye.diagnosis}")
        print(f" |   ├─Refractive:")
        print(f" |   |  ├─Defect Dioptre 1: {self.odEye.refractiveDefect.dioptre1}")
        print(f" |   |  ├─Defect Dioptre 2: {self.odEye.refractiveDefect.dioptre2}")
        print(f" |   |  └─Defect Astigmatism: {self.odEye.refractiveDefect.astigmatism}")
        print(f" |   ├─Phakic Pseudophakic: {self.odEye.phakic_Pseudophakic}")
        print(f" |   ├─IOP:")
        print(f" |   |  ├─Pneumatic: {self.odEye.iop.pneumatic}")
        print(f" |   |  └─Perkins: {self.odEye.iop.perkins}")
        print(f" |   ├─Pachymetry: {self.odEye.pachymetry}")
        print(f" |   ├─Axial Length: {self.odEye.axialLength}")
        print(f" |   └─VF/MD: {self.odEye.vf_md}")
      if self._osEye != None:
        print(f" └─Os Eye: ")
        print(f"     ├─Diagnosis {self.osEye.diagnosis}")
        print(f"     ├─Refractive:")
        print(f"     |  ├─Defect Dioptre 1: {self.osEye.refractiveDefect.dioptre1}")
        print(f"     |  ├─Defect Dioptre 2: {self.osEye.refractiveDefect.dioptre2}")
        print(f"     |  └─Defect Astigmatism: {self.osEye.refractiveDefect.astigmatism}")
        print(f"     ├─Phakic Pseudophakic: {self.osEye.phakic_Pseudophakic}")
        print(f"     ├─IOP:")
        print(f"     |  ├─Pneumatic: {self.osEye.iop.pneumatic}")
        print(f"     |  └─Perkins: {self.osEye.iop.perkins}")
        print(f"     ├─Pachymetry: {self.osEye.pachymetry}")
        print(f"     ├─Axial Length: {self.osEye.axialLength}")
        print(f"     └─VF/MD: {self.osEye.vf_md}")

      plt.rcParams["figure.figsize"] = (15,8)
      if self.odEye != None \
        and self.odEye.fundusImage != None\
        and self.odEye.fundusImage.fullpath != None:
        img1 = cv.imread(self.odEye.fundusImage.fullpath)
        plt.subplot(2, 2, 1)
        plt.imshow(img1)
        plt.title("Od Eye Fundus Image")
      if self.odEye != None \
        and self.odEye.imageWithContour != None\
        and self.odEye.imageWithContour.fullpath != None:
        img2 = cv.imread(self.odEye.imageWithContour.fullpath)
        plt.subplot(2, 2, 2)
        plt.imshow(img2)
        plt.title("Od Eye image with Contour")
      if self.osEye != None \
        and self.osEye.fundusImage != None\
        and self.osEye.fundusImage.fullpath != None:
        img3 = cv.imread(self.osEye.fundusImage.fullpath)
        plt.subplot(2, 2, 3)
        plt.imshow(img3)
        plt.title("Os Eye Fundus Image")
      if self.osEye != None \
        and self.osEye.imageWithContour != None\
        and self.osEye.imageWithContour.fullpath != None:
        img4 = cv.imread(self.osEye.imageWithContour.fullpath)
        plt.subplot(2, 2, 4)
        plt.imshow(img4)
        plt.title("Od Eye image with Contour")

