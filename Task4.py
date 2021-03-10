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

set_outgoing_calls = set()
no_telemarket = set()

for records in calls:
    set_outgoing_calls.add(records[0])
    no_telemarket.add(records[1])

for records in texts:
    no_telemarket.add(records[0])
    no_telemarket.add(records[1])

list_telemarketers = sorted(list(set_outgoing_calls - no_telemarket))

print("These numbers could be telemarketers: ", list_telemarketers)