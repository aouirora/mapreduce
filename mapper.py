#!/usr/bin/env python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 6:
        raise ValueError("Expected 6 fields, got {0}".format(len(data)))

    date, time, item, category, sales, payment = data
    sys.stdout.write("{0}\t{1}\n".format(category, sales))
