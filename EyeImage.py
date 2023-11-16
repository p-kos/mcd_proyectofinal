import os
import cv2 as cv
from matplotlib import pyplot as plt

class EyeImage:
    def __init__(self, id, fileName, format, width, height, path):
      self._id = id
      self._fileName = fileName
      self._format = format
      self._width = width
      self._height = height
      self._path = path

    @staticmethod
    def fromPath(fullPath):
        ext = fullPath[-3:]
        if (ext in ['png', 'jpg', 'bmp']):
          file_name = os.path.basename(fullPath)
          path = os.path.dirname(fullPath)
          id = int(file_name[-9:-6])
          im = cv.imread(fullPath)
          return EyeImage(id, 
                          fileName = file_name, 
                          format = ext, 
                          width = im.shape[0], 
                          height = im.shape[1], 
                          path = path)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def fileName(self) -> str:
        return self._fileName

    @fileName.setter
    def fileName(self, value):
        self._fileName = value

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def fullpath(self):
      return os.path.join(self._path, self._fileName)

    def display(self):
        img = cv.imread(self.fullpath)
        plt.title(self._fileName)
        plt.imshow(img)
