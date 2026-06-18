#!/usr/bin/env python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, item, category, sales, payment = data
    sys.stdout.write("{0}\t{1}\n".format(category, sales))
