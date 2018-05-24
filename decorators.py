"""This is the doc string of the decorators.py module .
And we use triple quoting, because it allows the string to contain line breaks"""

from functools import wraps


def first_decorator_txt(deco_txt):
    def first_decorator(func):
        @wraps(func)
        def wrapper_func(var):
            return 'Nqkakva {0} kaza : {1}'.format(deco_txt, func(var))
        return wrapper_func
    return first_decorator


@first_decorator_txt('patka')
def double_text(text_to_print):
    """This is the documentation string of the double_text function """
    return text_to_print + text_to_print


print(double_text('edno_'))
print(double_text.__name__)
print(double_text.__doc__)
print(__doc__)
