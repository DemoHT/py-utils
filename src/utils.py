# -*- coding:utf-8 -*-
import datetime


class DateUtil:
    @classmethod
    def today(cls, fmt="%Y-%m-%d"):
        return datetime.datetime.now().strftime(fmt)

    @classmethod
    def now(cls, fmt='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.now().strftime(fmt)

    @classmethod
    def plus_day(cls, t_str, days_num):
        if " " in t_str:
            fmt = '%Y-%m-%d %H:%M:%S'
        elif "-" in t_str:
            fmt = '%Y-%m-%d'
        else:
            fmt = '%Y%m%d'

        d = datetime.datetime.strptime(t_str, fmt)
        d = d + datetime.timedelta(days=days_num)
        return d.strftime(fmt)

    @classmethod
    def plus(cls, t_str, **timedelta):
        if " " in t_str:
            fmt = '%Y-%m-%d %H:%M:%S'
        elif "-" in t_str:
            fmt = '%Y-%m-%d'
        else:
            fmt = '%Y%m%d'

        d = datetime.datetime.strptime(t_str, fmt)
        d = d + datetime.timedelta(**timedelta)
        return d.strftime(fmt)

    @classmethod
    def range(cls, st_str, ed_str, **timedelta):
        if " " in st_str:
            fmt = '%Y-%m-%d %H:%M:%S'
        elif "-" in st_str:
            fmt = '%Y-%m-%d'
        else:
            fmt = '%Y%m%d'

        list_ = []
        start = datetime.datetime.strptime(st_str, fmt)
        end = datetime.datetime.strptime(ed_str, fmt)
        while start < end:
            list_.append(start.strftime(fmt))
            start = start + datetime.timedelta(**timedelta)
        if start >= end:
            list_.append(end.strftime(fmt))
        return list_

    @classmethod
    def split(cls, st_str, ed_str, **timedelta):
        if " " in st_str:
            fmt = '%Y-%m-%d %H:%M:%S'
        elif "-" in st_str:
            fmt = '%Y-%m-%d'
        else:
            fmt = '%Y%m%d'

        list_ = []
        start = datetime.datetime.strptime(st_str, fmt)
        end = datetime.datetime.strptime(ed_str, fmt)
        while start <= end:
            tmp = start + datetime.timedelta(**timedelta)
            if tmp < end:
                list_.append((start.strftime(fmt), tmp.strftime(fmt)))
            else:
                list_.append((start.strftime(fmt), end.strftime(fmt)))
            start = tmp
        return list_


class Logger:

    @classmethod
    def getLogger(cls, path):
        import logging
        # 配置日志信息
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s [%(name)-6s] [%(levelname)s] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename=path,
                            filemode='w')
        # 定义一个Handler打印INFO及以上级别的日志到sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        # 设置日志打印格式
        formatter = logging.Formatter('%(asctime)s [%(name)-6s] [%(levelname)s] %(message)s')
        console.setFormatter(formatter)
        # 将定义好的console日志handler添加到root logger
        logging.getLogger('').addHandler(console)
        return logging


class Http:
    """
    Http get / post
    @:param data : use dict or tuple pair list
    """

    @classmethod
    def get(cls, url, data=None):
        import urllib
        import urllib2
        if data:
            data = urllib.urlencode(data)
            url = url + data
        response = urllib2.urlopen(url)
        return response.read()

    @classmethod
    def post(cls, url, data):
        import urllib
        import urllib2
        data = urllib.urlencode(data)
        response = urllib2.urlopen(url, data)
        return response.read()


def md5(content):
    import hashlib
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()
