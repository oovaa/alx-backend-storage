

from functools import wraps


def do_nothing(f):
    """the dec"""
    @wraps(f)
    def inner(*args, **kwargs):
        """the dec inner"""
        return f(*args, **kwargs)
    return inner


@do_nothing
def alpha(*args, **kwargs):
    """a function that dose nothing"""

    print(f'args {args}')
    print(f'kwargs {kwargs}')


print(alpha.__name__)
print(alpha.__doc__)
