def run_three_times(func):
    def wrapper(*args,**kwargs):
        for i in range(3):
            func(*args,**kwargs)
    return wrapper

@run_three_times
def print_sum(a,b):
    print(a + b)

print_sum(3,5)

def run_n_times(n):
    """ Define and return a decorator"""
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator

run_two_times = run_n_times(2)

# 1
@run_two_times
def print_sum_n(a,b):
    print(a + b)

# 2
@run_n_times(2)
def print_sum_n(a,b):
    print(a + b)

print_sum_n(4,6)

# 3
print = run_n_times(20)(print)

print('What is happening?!?!')