class Chance:
    __CERTAIN_LIKELIHOOD = 1.0
    __THRESHOLD = 0.000001

    def __init__(self, likelihood):
        self._likelihood = likelihood

    # override == operator
    def __eq__(self, other):
        return abs(self._likelihood - other._likelihood) < self.__THRESHOLD

    def not_(self):
        return Chance(self.__CERTAIN_LIKELIHOOD - self._likelihood)
    
    def and_(self, other):
        return Chance(self._likelihood * other._likelihood)
    
    def or_(self, other):
        return Chance(self._likelihood + other._likelihood - (self.and_(other)._likelihood))
    
    def __repr__(self):
     return "Chance(%.10f)" % self._likelihood