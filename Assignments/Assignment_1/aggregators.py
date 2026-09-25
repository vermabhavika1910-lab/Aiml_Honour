from abc import ABC, abstractmethod
from payment_factories  import FactoryPaymentMethod
from payment_factories import RazorpayFactory
from payment_factories import StripeFactory

class Aggregator(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def call_get_payment_object(self, method_type:str, amount: float, **kwargs) -> bool:
        pass

class RazorpayAggregator(Aggregator):

    def __init__(self):
        super().__init__("Razorpay")
        self.processing_fee = 2.0

    def call_get_payment_object(self, method_type: str, amount: float, **kwargs) -> bool:
        payment = RazorpayFactory.get_payment_object(method_type, **kwargs)
        return payment.pay(amount)

class StripeAggregator(Aggregator):

    def __init__(self):          
        super().__init__("Stripe")
        self.processing_fee = 2.9

    def call_get_payment_object(self, method_type: str, amount: float, **kwargs) -> bool:
        payment = StripeFactory.get_payment_object(method_type, **kwargs)
        return payment.pay(amount)