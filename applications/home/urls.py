#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .handlers import index, books
from .handlers import company

# 其他 URL 通过 acl 获取
urls = [
    # index
    (r"/?(.html)?", index.IndexHandler),
    (r"/about/?(.html)?", index.AboutHandler),
    (r"/shop/?(.html)?", index.ShopHandler),

    (r"/books/?(.html)?", books.BooksHandler),
    (r"/books/list/?(.html)?", books.BooksListHandler),
    (r"/books/query/?(.html)?", books.BooksQueryHandler),


]