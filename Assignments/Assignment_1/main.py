from abc import ABC, abstractmethod
from payment_method import (PaymentMethod, RazorpayCardPayment,RazorpayUPIPayment,StripeCardPayment,StripeUPIPayment)
from payment_factories import(FactoryPaymentMethod, StripeFactory, RazorpayFactory)
from aggregators import(Aggregator, RazorpayFactory, StripeFactory)
from aggregator_factory import(AggregatorFactory)
def main():
 try: 
     aggregator_name = input("Enter payment gateway (Stripe/ Razorpay): " ).strip().lower()
     method_type = input("Enter payment method (card/upi): ").lower()
     amount = float(input("Enter amount: "))
        
     if method_type == "card":
         card_number = input("Enter card Number: ")

         details = { "card_number" : card_number}
     elif method_type == "upi":

        upi_id = input("Enter UPI Id: ")
        details = { "upi_id" : upi_id}
     else:
         print("Invalid Payment method")
         return

     aggregator = AggregatorFactory.get_aggregator_object(aggregator_name)
     success = aggregator.call_get_payment_object(method_type,amount,**details)

     if success:
         print("Payment successful")
     else:
         print("Payment failed")

 except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
   main()

