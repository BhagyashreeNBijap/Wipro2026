from abc import ABC, abstractmethod
class BANK(ABC):
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass

class SBI(BANK):
    def interest(self):
        print("Interest is 12%")
    def loan(self):
        print("Loan is available")

s=SBI
s.interest()
s.loan()
