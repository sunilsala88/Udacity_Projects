"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import operator
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
d = {}
for c in calls:
    for p in c[:2]:
        d[p] = d.get(p, 0) + int(c[3])
phone, longest = max(d.items(), key=operator.itemgetter(1))

print(f"{phone} spent the longest time, {longest} seconds, on the phone during September 2016.")

