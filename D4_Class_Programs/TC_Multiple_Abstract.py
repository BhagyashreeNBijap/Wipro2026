from abc import ABC,abstractmethod
class BANK(ABC):
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass

class SBI(BANK):
    def interest(self):
        print("interest is 6%")
    def loan(self):
        print("loan is available")

s=SBI()
s.interest()
s.loan()
