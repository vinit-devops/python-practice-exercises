# Solution 1

import sys

print("Python version:")
version = sys.version.split()
print(version[0])


# Solution 2
def trackRecords(n, scores):
    if not (1 <= n <= 1000):
        raise ValueError("n must be between 1 and 1000")
    if any(not (0 <= s <= 10**8) for s in scores):
        raise ValueError("Each score must be between 0 and 10^8")
    if len(scores) != n:
        raise ValueError("Length of scores must be equal to n")
    
    result = [0, 0]
    high = low = scores[0]

    for score in scores[1:]:
        if score > high:
            result[0] += 1
            high = score
        elif score < low:
            result[1] += 1
            low = score
            
    return result
#scores = [6, 18, 4, 22, 3, 8, 7, 12, 19, 9]
#n=len(scores)
#result = trackRecords(n, scores)
#print(result)


# Solution 3

from datetime import datetime

date1 = datetime.strptime("2022-08-15", "%Y-%m-%d").date()
date2 = datetime.strptime("04/12/20", "%d/%m/%y").date()
date3 = datetime.strptime("March 3, 2005", "%B %d, %Y").date()

print(date1)
print(date2)
print(date3)


# Solution 4

from datetime import datetime
from dateutil import parser

user_input = input("Enter a date in any format: ")

try:
    parsed_date = parser.parse(user_input)
    formatted_date = parsed_date.strftime("%Y-%m-%d")
    print("Formatted Date:", formatted_date)
except ValueError:
    print("Invalid date format.")
# Note: There should be distinction between date and month while passing input else program may misbehave
