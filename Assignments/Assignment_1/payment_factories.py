from abc import ABC, abstractmethod
from payment_method import PaymentMethod
from payment_method import RazorpayCardPayment
from payment_method import RazorpayUPIPayment
from payment_method import StripeCardPayment
from payment_method import StripeUPIPayment

class FactoryPaymentMethod(ABC):

    factory = {}

    @classmethod
    def get_payment_object(cls, method_type: str, **kwargs) -> PaymentMethod:

        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")

        return cls.factory[method_type](**kwargs)

class RazorpayFactory(FactoryPaymentMethod):
    factory = {
        "card": RazorpayCardPayment,
        "upi": RazorpayUPIPayment
    }

class StripeFactory(FactoryPaymentMethod):
    factory = {
        "card" : StripeCardPayment,
        "upi" : StripeUPIPayment
    }