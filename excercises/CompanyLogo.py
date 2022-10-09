#!/bin/python3

import math
import os
import random
import re
import sys

s = input()
diz={}

for c in s:
    if c in diz:
        diz[c]+=1
    else:
        diz[c]=1

diz_sort = sorted(diz, key=lambda x: (-diz[x],x))

for c in diz_sort[:3]:
    print(c, diz[c])

