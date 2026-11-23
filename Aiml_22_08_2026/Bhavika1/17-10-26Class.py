import time
import cProfile
from functools import wraps
import inspect

#decorator to calculate the time taken by a function to execute
def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

@time_decorator
def complex_calculator(n: int, multiplier: float = 1.5) -> float:
    '''Performs heavy maths computations in a large pool of data.'''
    total = 0.0
    for i in range(int(1_000_000)):
        total += (i ** 0.5) * multiplier

    return total

#signature of the function
# Check the signature and docstring
print("==== FUNCTION SIGNATURE & METADATA ====")
print(f"Function Name: {complex_calculator.__name__}")
print(f"Signature:     {inspect.signature(complex_calculator)}")
print(f"Docstring:     {complex_calculator.__doc__}\n")
    