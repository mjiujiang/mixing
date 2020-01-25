#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""URL处理器

[description]
"""
import json
from .common import CommonHandler
from applications.admin.models.mxbooks import Books

class BooksHandler(CommonHandler):
    def get(self, *args, **kwargs):
        """登记册
        """
        params = {

        }

        self.render_html('books.html', **params)


class BooksListHandler(CommonHandler):
    def get(self, *args, **kwargs):
        """登记册
        """
        params = {

        }

        self.render_html('books.html', **params)


class BooksQueryHandler(CommonHandler):
    def get(self, *args, **kwargs):
        lbh = self.get_argument('search', '')
        # 判断是否为空
        if not lbh:
            return self.error('登记号错误！')

        query = Books.Q.filter(Books.lbh == lbh).first()
        if not query:
            return self.error('未查询到相关数据！')

        params = {
            "lbh": query.lbh,
            "name": query.name,
            "xz": query.xz,
            "data": query.data,
            "cj": query.cj,
            "cw": query.cw,
            "sx": query.sx,
            "jn": query.jn,
        }

        return self.show(params)
