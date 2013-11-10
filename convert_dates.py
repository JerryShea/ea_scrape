# convert EA's date/time format to python's standard format, which is understood by most other tools

import datetime, json, sys

dt_format_from = "%a, %d %b %Y %H:%M:%S"

data = json.load(sys.stdin)

for item in data:
  if item:
    # the below calls automatically correct for DST and convert DST times to non-DST
    item['startDate'] = str(datetime.datetime.strptime(item['startDate'], dt_format_from))
    item['endDate'] = str(datetime.datetime.strptime(item['endDate'], dt_format_from))

print json.dumps(data, indent=2)
