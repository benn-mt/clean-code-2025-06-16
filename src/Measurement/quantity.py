class Quantity:
    def __init__(self, amount: float, unit):
        self._amount = amount
        self._unit = unit

    def __eq__(self, other):
        return self._unit.isCompatibleWith(other._unit) and self._amount == other._amountInUnit(self._unit)
    
    def add(self, other):
       if not self._unit.isCompatibleWith(other._unit):
          raise Exception("Units are not compatible")
       return Quantity(self._amount + other._amountInUnit(self._unit), self._unit)
    
    def _amountInUnit(self, otherUnit):
       return self._unit.amountInUnit(self._amount, otherUnit)
     
    def __repr__(self):
     return f"Quantity({self._amount} {self._unit}) "