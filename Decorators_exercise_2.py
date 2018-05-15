# Nice, when I reviewed the first decorator function I wrote 5 days ago, I came to the point that there should be something wrong there.
# Atfer some time of meditation over decorators, I came to the same code :-)

from functools import wraps

def glupaci(deco_arg): # my deco function that reads the deco argument
    def func_deco(undeco_func): # my decorator function that reads the function to be decorated
        @wraps(undeco_func) # this one keep the '__name__' and '__doc__' to be the ones of the originally called function. Otherwise they turn to the most internal decorators ones.
        def wrapper_f(*argv): # My wropping function that reads the arguments from the function that is to be decorated.
            print('And who are the musketeers?') # Decorating the initial function ( something before it )

            argv = [deco_arg + 'The Fucking '+x for x in argv ] # modifying the imput data
            undeco_func(*argv) # callng the initial function wiht modified (decorated) imput data.

            print('These were all the musketeers.') # Decorating the initial function ( something after it )

        return wrapper_f
    return func_deco




@glupaci('Is it possible that ') # we can also give a deco argument
def story(*args):
    for arg in args:
        print('{} is a musketeer.'.format(arg))



if __name__ == '__main__':
    story('Atos', 'Portos', 'Aramis')
    print('____')
    print(story.__name__)
