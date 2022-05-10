import time
from functools import wraps

def timer(func):
    """ A decorator that prints how long a function took to run

        Args:
            func (callabe): The function being decorated.
        
        Returns:
            callable: The decorated function;
    """

    @wraps(func)
    def wrapper(*args,**kwargs):
        # When wrapper() is called, get the current time.
        t_start = time.time()
        # Call the decorated function and store the result.
        result = func(*args,**kwargs)
        # Get the total it took to run, and print it.
        t_total = time.time() - t_start
        print('{} took {}'.format(func.__name__,t_total))
        return result
    return wrapper

@timer
def sleep_n_seconds(n=10):
    """ Pause processing for n seconds
    
    Args:
        n (int): The number of seconds to pause for.
    """
    time.sleep(n)


print(sleep_n_seconds.__doc__)
print(sleep_n_seconds.__wrapped__)