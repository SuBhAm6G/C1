# Define a function that calculates the time taken to execute another function. Apply this decorator to a function that performs a complex calculation. Test the decorated function with different inputs.
import time
def calc_time(func):
    def timer(*args,**kwargs):
        start_time=time.perf_counter()
        result=func(*args,**kwargs)
        end_time=time.perf_counter()
        runtime=end_time-start_time
        print(f"{func.__name__} ran in {runtime:.5f}")
        return result
    return timer

@calc_time
def waste_time(num):
    return [i**5 for i in range(num)]
waste_time(50_000)
waste_time(100_000)
waste_time(150_000)
