'''
The process involves calculating the time taken before the operation starts, and then measuring how much time was consumed while performing the operation. This can be achieved using a decorator that tracks the execution time of the process.

Specifically:
Capture the start time before the operation begins.
Measure the time taken to perform the operation.
Output the total time taken for the process using a decorator.
-------------------------------------------------------------
# Simulated execution time tracking using a counter
step_counter = 0  # Global counter to simulate time

# Decorator that simulates tracking time
def fake_time_tracker(func):
    def wrapper(*args, **kwargs):
        global step_counter
        print("\n[Simulating start of operation]")
        start = step_counter  # Capture "start time"
       
        result = func(*args, **kwargs)
       
        step_counter += 1  # Simulate time passing
        end = step_counter  # Capture "end time"

        duration = end - start
        print(f"[Simulated Time Taken by '{func.__name__}']: {duration} units")
        return result
    return wrapper

# Example function to simulate a task
@fake_time_tracker
def fake_operation():
    print("Performing some steps...")
    for i in range(3):
        print("Step ",i+1)

# Run the function
fake_operation()
fake_operation()

# Decorator that simulates tracking time
def fake_time_tracker(func):
    def wrapper(*args, **kwargs):
        global step_counter
        print("\n[Simulating start of operation]")
        start = step_counter  # Capture "start time"
       
        result = func(*args, **kwargs)
       
        step_counter += 1  # Simulate time passing
        end = step_counter  # Capture "end time"

        duration = end - start
        print("[Simulated Time Taken by " + func.__name__ + "]: " + duration + "units")
        return result
    return wrapper

# Example function to simulate a task
@fake_time_tracker
def fake_operation():
    print("Performing some steps...")
    for i in range(3):
        print("Step ",i+1 )

# Run the function
fake_operation()
fake_operation()'''
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Function ",func.__name__ , f"took {(end_time - start_time):.4f}seconds")
        return result
    return wrapper

@time_it
def my_function():
    time.sleep(2)
    
my_function()
