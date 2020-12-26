#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

tup = (3,30,2019,9,25)

res = datetime.datetime(tup[2], tup[3], tup[4], tup[0], tup[1])
res = res.strftime("%m/%d/%Y %H:%M")
print(res)