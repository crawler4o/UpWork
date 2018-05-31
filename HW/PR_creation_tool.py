"""
This tool parses Detailed designs and outputs PRs export to be imported.

"""

import os
import shutil
from xlrd import open_workbook
from datetime import datetime


export_template = 'Some template in some format'


class RanHardware:
    """ The equipment - blank dictionaries containing all possible equipment """

    def __init__(self):
        self.cabinets = {'BTS3900': 0,
                         'BTS3900L': 0,
                         }

        self.rectifiers = {'Benning V1': 0,
                           'Benning V2': 0,
                           }

        self.boards = {}


class Survey:
    """ The survey data - blank dictionary containing all possible survey data """

    def __init__(self):
        self.antenna = {'Space_Available': False,
                        }


class Pr:
    """ The PR data - blank dictionary containing all possible PR items """

    def __init__(self):
        self.materials = {'Space_Available': False,
                          }

        self.services = {'Installation_of_something': 0,
                         }

        self.ew_standard = {'Pole_support': 0,
                            }

        self.ew_special = {}  # dic in format {'name':[eCor number, 'description']}


class Job:
    """ The complete job data """

    def __init__(self, j_id):
        self.existing = RanHardware
        self.target = RanHardware
        self.survey = Survey
        self.pr = Pr
        self.job_id = j_id

    def parse_design(self, detailed_design_file):
        """ Update the existing, target and survey objects """

    def evaluate_design(self):  # to update the pr object
        """ To update the pr object """

    def add_to_pr_export(self, exp_template):
        """ Adding the pr object contents to the pr export """


if __name__ == '__main__':
    output_file = '{}_PR_Export'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
    shutil.copyfile(export_template, output_file)
    for file in os.listdir('./input/'):
        job = Job(file[:10])
        job.parse_design('./input/'+file)
        job.evaluate_design()
        job.add_to_pr_export(output_file)
        del job
