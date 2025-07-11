from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def payment(self,amount):
        pass
class UPI(PaymentMethod):
    def payment(self,amount):
        print(f"paid:{amount} via UPI")

upi = UPI()
upi.payment(100)


