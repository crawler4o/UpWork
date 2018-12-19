"""
A command line tool that will take any json input and output a flat csv file.
"""

import json
import csv
import os


def write2(parsed_list):
    parsed_json_list = parsed_list[0]
    names_list = parsed_list[1]

    for ent in range(len(names_list)):
        fieldnames = []
        parsed_json = parsed_json_list[ent]
        n = 0
        for _ in parsed_json:
            while n < len(parsed_json):
                for i in parsed_json[n].keys():
                    if i not in fieldnames:
                        fieldnames.append(i)
                n += 1

        with open(f'{names_list[ent][:-5]}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            z = 0
            for _ in parsed_json:
                writer.writerow(parsed_json[z])
                z += 1


def parse2():
    parsed_json_list = []
    names_list = []
    for file in os.listdir('./input/'):
        names_list.append(file)
        file_path = f'./input/{file}'
        with open(file_path, 'r', encoding='utf-8') as f:
            parsed_json = json.load(f)
        global out
        out = []
        parsed_json = flatten3(parsed_json)
        parsed_json_list.append(parsed_json)

    return [parsed_json_list, names_list]


def flatten3(x, name=''):
    if type(x) is dict:
        shifted = False
        for a in x:
            if type(x[a]) is not dict and type(x[a]) is not list:
                if not shifted:
                    out.insert(0, {name + a: x[a]})
                    shifted = True
                else:
                    out[0][name + a] = x[a]
            else:
                flatten3(x[a], name + a + '_')
    elif type(x) is list:
        for a in x:
            flatten3(a, name)

    return out


if __name__ == '__main__':
    write2(parse2())
