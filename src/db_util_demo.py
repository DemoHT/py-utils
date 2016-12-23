#!/usr/bin/env python
# -*- coding:utf-8 -*-

from my_util.db_util import MySQL
from my_util.db_util import localhost

with MySQL(**localhost) as mysql:
    data = mysql.execute("select %s, %s from luodayou.piao_log limit 1", ('seat', 'nickname'))
    for line in data:
        print "\t".join(line)
    print mysql.column_name()
