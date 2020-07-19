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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def count(text, call):
    record = []

    for t in (text):
        record.extend([t[0], t[1]] )
    
    for c in (call):
        record.extend([c[0], c[1]])

    return len(set(record))


answer = count(texts, calls)
print(f"There are {answer} different telephone numbers in the records.")

