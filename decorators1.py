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
