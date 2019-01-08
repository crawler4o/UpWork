"""
This is not a meaningful script, but my notes from
Ned Batchelder's PyCon 2013 presentation
"""

import re
import os
import lorem
import itertools as itt
from timeit import timeit


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

    print('_________________')
    print(dict(zip(names, heights)))


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
        for x in stream:
            if x % 2 == 0:
                yield x

    for n in evens(nums):
        print(n)


def simple_gen():
    def simple_gen_in():
        yield 'Hello'
        yield 'World'

    for x in simple_gen_in():
        print(x)


def range_scan_2d():
    """This one is just an example - it won't run :-)"""
    def range_2d(width, height):
        """Produces a stream of 2d coordinates."""
        for y in range(height):
            for x in range(width):
                yield x, y

    for col, row in range_2d(10,15):
        value = spreadsheet.get_value(col,row)
        do_something(value)

        if this_is_my_value(value):
            break

def get_cell():
    """ The better way to get a cell. This also won't run."""
    for cell in spreadsheet.cells():
        value = cell.get_value()
        do_something(value)

        if this_is_my_value(value):
            break



def some_file_things():
    """ Cool example for abstraction"""

    def interesting_lines(f):
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            if not line:
                continue
            yield line

    with open('my_file.ini') as f:
        for line in interesting_lines(f):
            do_something(line)


def iterable_and_iterator_diff():
    iterable = 'asdfgh'
    iterator = iter(iterable)
    value = next(iterator)
    print(value)
    value = next(iterator)
    print(value)


def helpful_open_file():
    with open('asd.dat') as f:
        # Read the first line
        try:
            header_line = next(f)
        except StopIteration:
            print('The file is empty. Stop iteration error risen on line 146')

        # Read the rest
        for data in f:
            do_something()


def own_iterable():
    class ToDoList(object):
        def __init__(self):
            self.tasks = []

        #  def __iter__(self):
        #      return iter(self.tasks)

        def __iter__(self):  # or even better to be a generator
            for task in self.tasts:
                if not task.done:
                    yield task

        def all(self):
            return iter(self.tasks)

        def done(self):
            """
            A generator expression.
            Again returns a generator, just the oposite of the one in __iter__.
            """
            return (t for t in self.tasks if t.done)

    todo = ToDoList()
    # ...
    for task in todo:
        print('a')
        # ...


if __name__ == '__main__':

    #  pattern_gen()
    #  walk_os()
    #  inf_stream_integers()
    #  itertools_cool_tools()
    #  list_en_ex()
    #  cool_zip()
    #  dict_cool()
    #  own_con()
    #  print(timeit('own_con()', setup='from __main__ import own_con', number=50))
    #  simple_gen()
    iterable_and_iterator_diff()
