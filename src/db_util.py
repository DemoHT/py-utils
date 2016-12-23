#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import MySQLdb


reload(sys)
sys.setdefaultencoding('utf8');


class MySQL:
    """
    use with statement to auto close connection, like:
    with MySQL(**conf) as mysql:
        data = mysql.execute(sql)
        print data

    otherwise must execute close() function to release connection
    """

    def __init__(self, host, user, passwd, db, port=3306, charset='utf8'):
        self._db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset=charset)
        self._cursor = self._db.cursor()
        self._print_sql = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def execute(self, sql, args=None):
        if self._print_sql:
            print "sql:", sql
            print "params:", args
        self._cursor.execute(sql, args)
        return self._cursor.fetchall()

    def column_name(self):
        return tuple(x[0] for x in self._cursor.description)

    def print_sql(self, boolean):
        self._print_sql = boolean

    def close(self):
        print 'close mysql connection'
        self._cursor.close()
        self._db.close()


localhost = {
    "host": "127.0.0.1", "user": "root", "passwd": "qwe123", "db": "test"
}
