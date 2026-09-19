import time

def add (*args):
    """Add all the numbers in args."""
    time.sleep(1)  # Simulate a delay
    return sum(args)

print (add(1, 2, 3))

def display_info(name, age):
    for i in range(3):
        time.sleep(1)  # Simulate a delay
        print("running display_info()")
        print(f"Name: {name}, Age: {age}")

display_info("Alice", 30)        