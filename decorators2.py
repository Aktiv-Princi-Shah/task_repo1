'''
Implementing pattern printing with the use of double decorators.
---------------------------------------------------------------'''
def pattern_logger(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print("Pattern Print Call ",count)
        print("Executing pattern function:")
        return func(*args, **kwargs)
    return wrapper
    
def border_decorator(func):
    def wrapper(*args, **kwargs):
        print("-"*10)
        result = func(*args, **kwargs)
        print("-"*10)
        return result
    return wrapper
    
@border_decorator
@pattern_logger
def print_pattern(rows=5):
    for i in range(1, rows+1):
        print("*"*i)
        
print_pattern(5)
print_pattern(3)
