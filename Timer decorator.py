import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()      # Start timer
        result = func(*args, **kwargs)   # Execute the target function
        end = time.perf_counter()        # End timer
        print(f"Finished '{func.__name__}' in {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def process_data():
    print("Processing data...")
    time.sleep(2)  # simulate a delay
    return "Done"

@timer
def add_numbers(a, b):
    time.sleep(1)
    return a + b

process_data()
result = add_numbers(10, 20)
print("Result:", result)
