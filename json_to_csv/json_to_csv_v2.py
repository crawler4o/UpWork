"""
A command line tool that will take any json input and output a flat csv file.
"""

import json
import csv
import os


def write(parsed_list):
    parsed_json_list = parsed_list[0]
    names_list = parsed_list[1]

    for ent in range(len(names_list)):

        parsed_json = parsed_json_list[ent]
        fieldnames = []
        for x in parsed_json:
            a = 0
            while a + 1 < len(parsed_json[x]):
                for y in parsed_json[x][a]:
                    if y not in fieldnames:
                        fieldnames.append(y)
                a += 1

        with open(f'{names_list[ent][:-5]}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for x in parsed_json:
                a = 0
                while a + 1 < len(parsed_json[x]):
                    writer.writerow(parsed_json[x][a])
                    a += 1


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

            print(parsed_json)
            z = 0
            for _ in parsed_json:
                writer.writerow(parsed_json[z])
                z += 1


def parse():
    parsed_json_list = []
    names_list = []
    for file in os.listdir('./input/'):
        names_list.append(file)
        file_path = f'./input/{file}'
        with open(file_path, 'r', encoding='utf-8') as f:
            parsed_json = json.load(f)
        parsed_json_list.append(parsed_json)

    return [parsed_json_list, names_list]


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


def flatten(x, name=''):
    if type(x) is dict:
        for a in x:
            flatten(x[a], name + a + '_')
    elif type(x) is list:
        i = 0
        for a in x:
            flatten(a, name + str(i) + '_')
            i += 1
    else:
        out[name[:-1]] = x

    return out


def flatten3(x, name=''):
    if type(x) is dict:
        shifted = False
        for a in x:
            if type(x[a]) is not dict and type(x[a]) is not list:
                if not shifted:
                    out.insert(0, {a: x[a]})
                    shifted = True
                else:
                    out[0][a] = x[a]
            else:
                flatten3(x[a], name + a + '_')
    elif type(x) is list:
        for a in x:
            flatten3(a, name)#  + str(i) + '_')
    #else:
     #   out.append[name[:-1]] = x

    return out


def flatten2(x, name=''):
    if type(x) is dict:
        for a in x:
            flatten(x[a])
    elif type(x) is list:
        for a in x:
            flatten(a)
    else:
        out[name[:-1]] = x

    return out


if __name__ == '__main__':
    write2(parse2())
