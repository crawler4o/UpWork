""" A tool that will parse the DD file and output PR items """

from os import listdir
from xlrd import open_workbook


class Job:
    def __init__(self, open_file_name):
        dd_wb = open_workbook(filename = './input/{}'.format(open_file_name))
        dd_sheet = dd_wb.sheet_by_name('Site solution')
        self.existing = {}  # existing hardware
        self.target = {}  # target hardware
        self.to_add = {}  # hardware to be installed
        self.to_del = {}  # hardware to be removed
        self.job_id = open_file_name[:10]
        if dd_sheet.cell_value(2, 4) == 'Position':  # define the solution version
            lines_total = 97  # how many lines is the template
            cols = [2, 5, 9, 12]  # in which columns is the party
        else:
            lines_total = 84
            cols = [2, 4, 7, 9]

        for x in range(4, lines_total):  # parsing row by row
            self.existing = self.parse_column(self.existing, x, cols[0], dd_sheet)
            self.existing = self.parse_column(self.existing, x, cols[1], dd_sheet)
            self.target = self.parse_column(self.target, x, cols[2], dd_sheet)
            self.target = self.parse_column(self.target, x, cols[3], dd_sheet)

        self.existing = self.feeder_name(self.existing)  # updating the feeders in existing
        self.target = self.feeder_name(self.target)  # updating the feeders in target
		
        self.to_install()
        self.to_remove()


    @staticmethod
    def parse_column(dict, x, y, dd_sheet):
        if dd_sheet.cell_value(x, y) and dd_sheet.cell_value(x, y+1):
            item = str(dd_sheet.cell_value(x, y))
            qty = int(dd_sheet.cell_value(x, y+1))
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
        n_dict = {}
        for x in dict:
            for y in feeders:
                if y[0] in x:
                    if y[1] in n_dict.keys():
                        n_dict[y[1]] += dict[x]
                        to_del.append(x)
                    else:
                        n_dict[y[1]] = dict[x]
                        to_del.append(x)

        for x in to_del:
            dict.pop(x)
			
        for x in n_dict:
            dict[x] = n_dict[x]
        
		#  To add the feeder lengths. The successful regex so far for feeder length is re.search('(?<![1])\d{1,2,3}(?![/]', a).group(). Anyway, this would match the 1 in 1 5/8 )
		
        return dict


    def to_install(self):  #filling the self.to_add dictionary	
        for x in self.target:
            if x in self.existing.keys(): 
                if self.target[x] > self.existing[x]:
                    self.to_add[x] = self.target[x] - self.existing[x]
                else:
                    pass
            else:
                self.to_add[x] = self.target[x]
        # to add exception for rectifiers as 2 are in the initial package and PSU upgrade		


    def to_remove(self):  #filling the self.to_del dictionary
        for x in self.existing:
            if x in self.target.keys():
                if self.existing[x] > self.target[x]:
                    self.to_del[x] = self.existing[x] - self.target[x]
                else:
                    pass
            else:
                self.to_del[x] = self.existing[x]



def create_obj_lst():  # created a list of objects - object per file in the input folder
    jobs = []
    for file in listdir('./input/'):
        jobs.append(Job(file))	
	
    return jobs

	
if __name__ == '__main__':
		
    for job in create_obj_lst():
        print('\n\nThe job is {}'.format(job.job_id))
        
        print('The existing HW is:')
        for x in job.existing:
            print('{}:{}'.format(x, job.existing[x]))
        
        print(' \nThe target HW is:')
        for x in job.target:
            print('{}:{}'.format(x, job.target[x]))
        print('')
        
        print(' \nThe HW to be installed is:')
        for x in job.to_add:
            print('{}:{}'.format(x, job.to_add[x]))
        print('')
        
        print(' \nThe HW to be removed is:')
        for x in job.to_del:
            print('{}:{}'.format(x, job.to_del[x]))
        print('')
		
