"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

call_s = set([data[0] for data in calls])
call_r = set([data[1] for data in calls])
message_s = set([data[0] for data in texts])
message_r = set([data[1] for data in texts])

answer = []

for i in call_s:
    if (i not in call_r and i not in message_s and i not in message_r):
        answer.append(i)

answer.sort()

print("\n These numbers could be telemarketers:")
#print(len(answer))
for i in answer:
    print(i)