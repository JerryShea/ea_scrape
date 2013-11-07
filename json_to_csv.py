# thanks to http://stackoverflow.com/questions/1871524/convert-from-json-to-csv-using-python

import csv, json, sys

input = open(sys.argv[1])
data = json.load(input)
input.close()

output = csv.writer(sys.stdout)

# header row
output.writerow(data[0].keys())

for row in data:
  if row.values():
    output.writerow(row.values())
