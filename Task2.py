"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
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

time_spent_on_phone_dict = {}

for record in calls:
    if record[0] in time_spent_on_phone_dict:
        time_spent_on_phone_dict[record[0]] += int(record[3])
    else:
        time_spent_on_phone_dict[record[0]] = int(record[3])
    if record[1] in time_spent_on_phone_dict:
        time_spent_on_phone_dict[record[1]] += int(record[3])
    else:
        time_spent_on_phone_dict[record[1]] = int(record[3])

max_caller_nr = max(time_spent_on_phone_dict,key=time_spent_on_phone_dict.get)
max_caller_duration = time_spent_on_phone_dict[max_caller_nr]

print(
    "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(max_caller_nr, max_caller_duration)
)