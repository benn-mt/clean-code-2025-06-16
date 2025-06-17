class Quantity:
    def __init__(self, amount: float, unit):
        self._amount = amount
        self._unit = unit

    def __eq__(self, other):
        return self._amount == other._amountInUnit(self._unit)
    
    def _amountInUnit(self, otherUnit):
       return self._unit.amountInUnit(self._amount, otherUnit)
    
    def add(self, other):
       return Quantity(self._amount + other._amountInUnit(self._unit), self._unit)
    
    def __repr__(self):
     return f"Quantity({self._amount} {self._unit}) "