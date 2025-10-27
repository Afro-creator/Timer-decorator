Python Timer Decorator

A lightweight and reusable **Python decorator** that measures and reports the execution time of any function it wraps.
This is a handy utility for performance testing, debugging, and learning how decorators work in Python.

Features

Measures precise function execution time using `time.perf_counter()`.
Works with **any function** (with or without arguments).
Simple, reusable, and dependency-free.
Can be easily extended for logging, saving results, or profiling code blocks.

What Is a Decorator?

A decorator is a Python function that wraps another function to modify or extend its behavior without changing the original code.
Decorators are often used for logging, authorization, caching, or timing — like this project.

Code Example

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()      # Start timer
        result = func(*args, **kwargs)   # Run the original function
        end = time.perf_counter()        # End timer
        print(f"Finished '{func.__name__}' in {end - start:.4f} seconds")
        return result
    return wrapper
```

Usage

1. Decorate your function with `@timer`

```python
@timer
def process_data():
    print("Processing data...")
    time.sleep(2)  # Simulate a delay
    return "Done"

@timer
def add_numbers(a, b):
    time.sleep(1)
    return a + b

process_data()
result = add_numbers(10, 20)
print("Result:", result)
```

Output

```
Processing data...
Finished 'process_data' in 2.0018 seconds
Finished 'add_numbers' in 1.0011 seconds
Result: 30
```

How It Works

1. The `@timer` decorator takes a function as input.
2. It defines an inner `wrapper` function that:

   * Records the start time (`time.perf_counter()`)
   * Runs the original function
   * Records the end time
   * Prints how long it took to execute
3. It returns the `wrapper`, replacing the original function with the timed version.

Example Extension — Logging to File

You can extend the decorator to **log timings** to a file:

```python
def timer_log(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        with open("timelog.txt", "a") as f:
            f.write(f"{func.__name__} executed in {elapsed:.4f} seconds\n")
        return result
    return wrapper
```

Possible Use Cases

* Profiling slow parts of your code
* Measuring performance of functions in data processing or APIs
* Tracking runtime for machine learning model training
* Benchmarking different algorithms

---

Project Structure

```
timer_decorator/
│
├── timer.py          # The timer decorator code
├── example.py        # Example usage
└── README.md         # Documentation (this file)
```

Learning Goals

This project helps you understand:

* How **Python decorators** work internally
* How to use **`*args` and `**kwargs`** to handle flexible arguments
* How to measure **execution time** precisely
* How to build **reusable utilities** for code performance tracking

Next Steps

* Add unit tests for your decorator.
* Integrate with the `logging` module instead of `print()`.
* Create a parameterized decorator that toggles verbose mode or logging output.
* Use decorators to measure API response times or database query speeds.

License

This project is open-source and available under the **MIT License**.
Feel free to use, modify, and share.

