# coding: utf-8

#
# Flatten JSON and output as CSV
#
# Invoke with the path to the JSON file as an argument, e.g.
#
#   python json2csv.py data.json
#
# Outputs to a CSV file in the working directory
#
# JSON flattening function from: http://goo.gl/z0mzsH
#

from collections import OrderedDict
import csv
import json
import sys

# infile = sys.argv[1]
infile = 'test.json'
outfile = open("output.csv", "w")

writer = csv.writer(outfile, delimiter=",")

data = json.load(open(infile), object_pairs_hook=OrderedDict)

# Recursively flatten JSON
def flatten(structure, key="", path="", flattened=None): 
    if flattened is None:
        flattened = OrderedDict()    
    if type(structure) not in(OrderedDict, list):
        flattened[((path + "_") if path else "") + key] = structure    
    elif isinstance(structure, list):
        for i, item in enumerate(structure):
            flatten(item, "", path + "_" + key, flattened)    
    else:
        for new_key, value in structure.items():
            flatten(value, new_key, path + "_" + key, flattened)    
    return flattened

# Write fields
fields = []
for result in data["results"]:
    flattened = flatten(data["results"][0])
    for k, v in flattened.iteritems():
        if k not in fields:
            fields.append(k)
writer.writerow(fields)

# Write values
for result in data["results"]:
    flattened = flatten(result)
    row = []
    for field in fields:
        if field in flattened.iterkeys():
            row.append(flattened[field])
        else:
            row.append("")
    writer.writerow(row)
