"""
This is not a meaningful script, but my notes from
Ned Batchelder's PyCon 2013 presentation
"""

import re
import os
import lorem
import itertools as itt


def pattern_gen():
    ipsum = lorem.paragraph()
    for match in re.finditer('ol', ipsum):
        print(match)


def walk_os():
    for root, dirs, files in os.walk(r'd:\GoogleDrive'):
        print(f'{root}___{dirs}___{files}')


def inf_stream_integers():
    """ This is a never ending one :-) """
    for num in itt.count():
        print(num)


def itertools_cool_tools():
    """ This is a never ending one :-) """
    seq = itt.chain(itt.repeat(7, 3), itt.cycle(range(4)))
    for num in seq:
        print(num)


def cool_zip():
    names = ['Eiffel Tower', 'Empire State', 'Sears Tower']
    heights = [324, 381, 442]
    for building, height in zip(names, heights):
        print(f'The building is: {building} and it is {height}m high')


def list_en_ex():
    my_list = ['asd', 'qwe', 'erty']
    for i, v in enumerate(my_list):
        print(f'The intex in {i} and the value is {v}')


def dict_cool():
    tall_buildings = {
        'Empire State': 381, 'Sears Tower': 442,
        'Burj Khalifa': 828, 'Taipei 101': 509,
        }

    print(max(tall_buildings.values()))
    print('______________')
    print(max(tall_buildings.items(), key=lambda b: b[1]))
    print('______________')
    print(max(tall_buildings, key=tall_buildings.get))
    print('______________')


def own_con():
    nums = [11, 12, 23, 34, 34, 564, 65, 765, 876]

    def evens(stream):
        them = []
        for x in stream:
            if x % 2 == 0:
                them.append(x)
        return them

    for n in evens(nums):
        print(n)


if __name__ == '__main__':

    #  pattern_gen()
    #  walk_os()
    #  inf_stream_integers()
    #  itertools_cool_tools()
    #  list_en_ex()
    #  cool_zip()
    #  dict_cool()
    own_con()
