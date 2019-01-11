def dec_fun(dec_argu):
    def dec_fun_(re_func):
        def dec_fun__(in_int):
            print('alabala')
            print(f'The decorator argument is : {dec_argu}')
            re_func(in_int)
            print('portokala')
        return dec_fun__
    return dec_fun_


@dec_fun('Sample Decorator argument')
def ext_fun(in_int):
    print('This is the function')
    print(f'The in integer is : {in_int}')


if __name__ == '__main__':
    ext_fun(5)
