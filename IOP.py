class IOP:
    def __init__(self, pneumatic = None, perkins = None):
      self._pneumatic = pneumatic
      self._perkins = perkins

    @property
    def pneumatic(self):
        return self._pneumatic

    @pneumatic.setter
    def pneumatic(self, value):
        self._pneumatic = value

    @property
    def perkins(self):
        return self._perkins

    @perkins.setter
    def perkins(self, value):
        self._perkins = value
