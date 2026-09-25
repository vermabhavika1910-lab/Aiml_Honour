from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self)->str:
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class RazorpayCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self) -> str:
        return f"RazorPay Card: {self.card_number}"

    def pay(self, amount: float) -> bool:
        print(f"Processing Razourpay caed Payment of ${amount}")
        return True

class RazorpayUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self) -> str:
        return f"RazorPay UPI: {self.upi_id}"

    def pay(self, amount: float) -> bool:
        print(f"Processing Razourpay UPI Payment of ${amount}")
        return True

class StripeCardPayment(PaymentMethod):

    def __init__(self, card_number): 
        self.card_number = card_number

    def get_details(self) -> str:
        return f"Stripe Card : {self.card_number}"

    def pay(self, amount: float) -> bool:
        print(f"Processing Stripe card payment of ${amount}")
        return True
    
class StripeUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self) -> str:
        return f"Stripe UPI: {self.upi_id}"

    def pay(self, amount: float) -> bool:
        print(f"Processing Stripe UPI payment of ${amount}")
        return True