""" A tool that will parse the DD file and output PR items """
from os import listdir
from xlrd import open_workbook


class Job:
    def __init__(self, open_file):
        dd_wb = open_workbook(filename=open_file)
        dd_sheet = dd_wb.sheet_by_name('Site solution')
        self.existing = {}
        self.target = {}
        self.to_add = {}
        self.to_rem = {}
        self.job_id = open_file.name[:10]
        if dd_sheet.cell_value(3, 5) == 'Position':
            cols = [3, 6, 10, 13]
        else:
            cols = [3, 5, 8, 10]

        for x in range(5, 99):  # parsing row by row
            self.existing = self.parse_column(self.existing, x, cols[0], dd_sheet)
            self.existing = self.parse_column(self.existing, x, cols[1], dd_sheet)
            self.target = self.parse_column(self.target, x, cols[2], dd_sheet)
            self.target = self.parse_column(self.target, x, cols[3], dd_sheet)

        self.existing = self.feeder_name(self.existing)  # updating the feeders in existing
        self.target = self.feeder_name(self.target)  # updating the feeders in target

    @staticmethod
    def parse_column(dict, x, y, dd_sheet):
        if dd_sheet.cell_value(x, y) and dd_sheet.cell_value(x, y+1):
            item = dd_sheet.cell_value(x, y)
            qty = dd_sheet.cell_value(x, y+1)
            if item in dict.keys():
                dict[item] += qty
            else:
                dict[item] = qty
        return dict

    @staticmethod
    def feeder_name(dict):  # unifies the feeder records
        feeders = [['1/2', '1/2 Feeder'],
                   ['7/8', '7/8 Feeder'],
                   ['5/4', '5/4 Feeder'],
                   ['1/4', '5/4 Feeder'],
                   ['5/8', '13/8 Feeder']
                   ]

        to_del = []
        for x in dict.keys():
            for y in feeders:
                if y[0] in x:
                    if dict[y[1]]:
                        dict[y[1]] += dict[x]
                        to_del.append(x)
                    else:
                        dict[y[1]] = dict.pop(x)

        for x in to_del:
            dict.pop(x)

        return dict
