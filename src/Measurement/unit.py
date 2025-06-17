from src.Measurement.quantity import Quantity

class Unit:
    def __init__(self, ratioToRelativeUnit=1, relativeUnit=None):
        self._ratioToBaseUnit = ratioToRelativeUnit
        self._baseUnit = self
        if (relativeUnit):
            self._ratioToBaseUnit = self._ratioToBaseUnit * relativeUnit._ratioToBaseUnit
            self._baseUnit = relativeUnit._baseUnit
    
    def amountInUnit(self, amount, otherUnit):
        return amount * self._ratioToBaseUnit / otherUnit._ratioToBaseUnit

    def s(self, amount):
        return Quantity(amount, self)