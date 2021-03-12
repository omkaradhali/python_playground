# -*- coding: utf-8 -*-
"""
Your company built an in-house calendar tool called HiCal.
You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting.
In Hi-Cal, a meeting is stored as tuple of integers (start_time, end_time).
These integers represent the number of 30-minute blocks past 9:00am.

For example:
(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges
and returns a list of condensed ranges.

For example, given:
[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:
[(0, 1), (3, 8), (9, 12)]
"""


def merge_ranges(meetings):
    
    sorted_meetings = sorted(meetings)
    
    current_start, current_end = sorted_meetings[0]
    
    result = []
    
    for item in sorted_meetings:
        if current_end >= item[0] :
            if result:
                result.pop()
            result.append((current_start, item[1]))
            current_end = item[1]
        else:
            result.append(item)
            current_start = item[0]
            current_end = item[1]
 
    print(result)
    
    

merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])