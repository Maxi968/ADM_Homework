#!/bin/python3

from datetime import datetime

def time_delta(t1, t2):
    format_time='%a %d %b %Y %H:%M:%S %z'

    t1tm = datetime.strptime(t1,format_time)
    t2tm = datetime.strptime(t2,format_time)
  
    return str(round(abs((t1tm-t2tm).total_seconds())))

T = int(input())

for i in range(T):
    t1 = input()
    t2 = input()
    print(time_delta(t1,t2))
