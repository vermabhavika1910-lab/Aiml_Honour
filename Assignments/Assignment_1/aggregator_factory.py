from aggregators import (StripeFactory,  StripeAggregator, RazorpayFactory,  RazorpayAggregator, Aggregator)
class AggregatorFactory:

    factory = {
        "stripe" : StripeAggregator,
        "razorpay" : RazorpayAggregator
    }

    @classmethod
    def get_aggregator_object(cls, aggregator_name: str) ->Aggregator:
        if aggregator_name not in cls.factory:
            raise ValueError("Invalid Aggregator")
        return cls.factory[aggregator_name]()