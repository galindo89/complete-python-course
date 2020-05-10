from csv import reader
from csv import DictReader
import pandas as pd
from collections import OrderedDict
import csv
#with open("Testeo.csv", "r") as f:
 #       reader = csv.DictReader(f)
  #      print (list (reader))
result_list = []


with open("Testeo.csv") as file_obj:
    reader = csv.DictReader(file_obj, delimiter=",")
    result_list=list(reader)
    #print(result_list)
list=dict(OrderedDict(result_list[0]))

print(list)

"""
# open file in read mode
with open ("Testeo.csv", "r") as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    dict_reader = DictReader (read_obj)
    # get a list of dictionaries from dct_reader
    list_of_dict = list (dict_reader)
    # print list of dict i.e. rows
print (list_of_dict)

"""