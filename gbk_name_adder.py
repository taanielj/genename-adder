#!/usr/bin/env python

import os
import sys
import csv
#sublime text!

gbkfiles_list = []
for f in os.listdir('./'):
    if f.endswith('.gbk'):
        gbkfiles_list.append(f)

if len(gbkfiles_list) == 0:
	sys.exit("No genbank files!")
else:
	print(gbkfiles_list)


gbkfile = raw_input("Type the genbank file name: ")
fileRows = []
with open(gbkfile, 'r+') as fd:
   for line in fd:
      fileRows.append(line)



pegfiles_list = []

for f in os.listdir('./'):
    if f.endswith('.csv'):
        pegfiles_list.append(f)

if len(gbkfiles_list) == 0:
	sys.exit("peg-name file must be csvdd!")
else:
	print(pegfiles_list)


pegfile = raw_input("Choose the peg to name file: ")

with open(pegfile, mode='r') as infile:
    reader = csv.reader(infile)
    myDict = {rows[0]:rows[1] for rows in reader}



for key, value in myDict.items():
    for i, j in enumerate(fileRows):
        if key in j:
            fileRows.insert(i+1,'                     /gene="%s" \n' %myDict[key])
print("Done!")


outfile = open("output.gbk", "w")
for item in fileRows:
  outfile.write("%s" % item)

print('Saved output as "output.gbk"!')

