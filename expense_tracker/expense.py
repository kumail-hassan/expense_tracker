from dataclasses import dataclass

@dataclass
class Expense :
    name: str
    category: str
    amount: float

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"
        

    