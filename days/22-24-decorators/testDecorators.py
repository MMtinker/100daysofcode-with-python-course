import time
from functools import wraps

def timeit(func):
    ''' Decorator to time the function '''
    #@wraps (func)
    def wrapper(*args, **kwargs):
        # before calling the decorated function
        print('Starting timer...')
        start = time.time()

        # Call the decorated function
        func(*args, **kwargs)

        # After calling the decorated function
        end = time.time()
        print(f'== {func.__name__} took {int(end-start)} seconds to complete ')

    return wrapper


@timeit
def myLoop(x):
    for i in range(x):
        print(f'i={i}')


# x = input('Please enter range: ')
#
# myLoop(int(x))


def make_html(arg1):
    def wrap(func):
        def wrapper(*args):
            return f'<{arg1}>{func(*args)}</{arg1}>'
        return wrapper
    return wrap



@make_html('p')
@make_html('strong')
def get_text(text):
    return text
    #pass


myText = get_text('I code with PiBytes')

print(myText)