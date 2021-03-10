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

list_numbers_texts = []

for record in texts:
    list_numbers_texts.append(record[0])
    list_numbers_texts.append(record[1])


list_numbers_calls = []

for record in calls:
    list_numbers_calls.append(record[0])
    list_numbers_calls.append(record[1])

unique_numbers = len(set(list_numbers_texts + list_numbers_calls))

print("There are {} different telephone numbers in the records".format(unique_numbers))

