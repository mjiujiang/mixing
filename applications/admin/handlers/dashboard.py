#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""URL处理器

[description]
"""
import tornado

from applications.admin.models.mxbooks import Books
from applications.core.settings_manager import settings
from applications.core.logger.client import SysLogger
from applications.core.utils.hasher import make_password
from applications.core.decorators import required_permissions

from ..models import AdminMenu

from .common import CommonHandler


class MainHandler(CommonHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        """后台首页
        """
        path = self.request.path
        path_set = ['admin', 'admin/index']
        if self.request.path.strip('/') in path_set:
            path = '/admin/main/'

        c_menu = AdminMenu.info(path=path)
        if not c_menu:
            msg = '节点不存在或者已禁用！'
            return self.error(code=404, msg=msg);

        _bread_crumbs = AdminMenu.brand_crumbs(c_menu['id'])
        _admin_menu_parents = _bread_crumbs[0] if len(_bread_crumbs) else {'parent_id': '1'}
        _admin_menu = AdminMenu.main_menu()

        params = {
            '_admin_menu': _admin_menu,
            '_admin_menu_parents': _admin_menu_parents,
            '_bread_crumbs': _bread_crumbs,
        }
        self.render('dashboard/main.html', **params)


class WelcomeHandler(CommonHandler):
    @tornado.web.authenticated
    @required_permissions('admin:welcome')
    def get(self, *args, **kwargs):
        """后台首页
        """
        # menu = AdminMenu.main_menu()
        # print('menu ', menu)
        # self.show('abc')

        params = {

        }

        self.render('dashboard/welcome.html', **params)


class BooksListHandler(CommonHandler):
    @tornado.web.authenticated
    @required_permissions('admin:welcome:list')
    def get(self, *args, **kwargs):
        """后台首页
        """
        # menu = AdminMenu.main_menu()
        # print('menu ', menu)
        # self.show('abc')
        limit = self.get_argument('limit', 10)
        page = self.get_argument('page', 1)
        pagelist_obj = Books.Q.filter(Books.lbh != '').paginate(page=page, per_page=limit)
        if pagelist_obj is None:
            return self.error('暂无数据')

        total = pagelist_obj.total
        page = pagelist_obj.page
        items = pagelist_obj.items

        data = []
        for item in items:
            item2 = item.as_dict()

            data.append(item2)

        params = {
            'count': total,
            'uri': self.request.uri,
            'path': self.request.path,
            'data': data,
        }
        return self.success(**params)

    @tornado.web.authenticated
    @required_permissions('admin:welcome:list:delete')
    def delete(self, *args, **kwargs):
        """删除文章
        """
        # return self.show('<script type="text/javascript">alert(1)</script>')
        aid = self.get_argument('aid', None)

        book = Books.Q.filter(Books.aid == aid).first()
        if book is None:
            return self.error('不存在的数据')

        Books.Q.filter(Books.aid == aid).delete()
        Books.session.commit()
        return self.success()


class BooksListAddHandler(CommonHandler):
    """觅星添加功能"""

    @tornado.web.authenticated
    @required_permissions('admin:welcome:list:add')
    def get(self, *args, **kwargs):
        # key = self.get_argument('key', None)
        book = Books(aid=11)

        data_info = book.as_dict()
        params = {
            'book': book,
            'data_info': data_info,
        }
        self.render('dashboard/add.html', **params)

    @tornado.web.authenticated
    @required_permissions('admin:welcome:list:add')
    def post(self, *args, **kwargs):
        params = self.params()

        params['lbh'] = params.get('lbh', 0)
        params['name'] = params.get('name', 0)
        params['data'] = params.get('data', 0)
        params['xz'] = params.get('xz', 0)
        params['cj'] = params.get('cj', 0)
        params['cw'] = params.get('cw', 0)
        params['sx'] = params.get('sx', 0)
        params['jn'] = params.get('jn', 0)
        bollid = params.get('bollid', 0)
        if not bollid:
            bollid = 0
        else:
            bollid = int(bollid)
        params['bollid'] = bollid
        params['userip'] = self.request.remote_ip

        if not params.get('lbh', None) and \
                params.get('name', None) and \
                params.get('data', None) and \
                params.get('xz', None) and \
                params.get('cj', None) and \
                params.get('cw', None) and \
                params.get('sx', None):
            return self.error('数据不能为空')

        count = Books.Q.filter(Books.lbh == params['lbh']).count()
        if count > 0:
            return self.error('证书编号已被占用')

        params.pop('_xsrf', None)
        params.pop('rsa_encrypt', None)

        book = Books(**params)
        Books.session.add(book)
        Books.session.commit()
        return self.success(data=params)


class BooksListEditHandler(CommonHandler):
    """觅星编辑功能"""

    @tornado.web.authenticated
    @required_permissions('admin:welcome:list:edit')
    def get(self, *args, **kwargs):
        aid = self.get_argument('aid', None)

        book = Books.Q.filter(Books.aid == aid).first()

        if book is None:
            return self.error('不存在的数据')
        data_info = book.as_dict()
        params = {
            'data_info': data_info,
        }

        self.render('dashboard/edit.html', **params)

    @tornado.web.authenticated
    @required_permissions('admin:welcome:list:edit')
    def post(self, *args, **kwargs):
        aid = self.get_argument('aid', None)
        params = self.params()

        params['lbh'] = params.get('lbh', 0)
        params['name'] = params.get('name', 0)
        params['data'] = params.get('data', 0)
        params['xz'] = params.get('xz', 0)
        params['cj'] = params.get('cj', 0)
        params['cw'] = params.get('cw', 0)
        params['sx'] = params.get('sx', 0)
        params['jn'] = params.get('jn', 0)
        bollid = params.get('bollid', 0)
        if not bollid:
            bollid = 0
        else:
            bollid = int(bollid)
        params['bollid'] = bollid
        params['userip'] = self.request.remote_ip

        if not params.get('lbh', None) and \
                params.get('name', None) and \
                params.get('data', None) and \
                params.get('xz', None) and \
                params.get('cj', None) and \
                params.get('cw', None) and \
                params.get('sx', None):
            return self.error('数据不能为空')

        params.pop('_xsrf', None)
        params.pop('file', None)
        Books.Q.filter(Books.aid == aid).update(params)
        Books.session.commit()

        # update article cache info
        book = Books.Q.filter(Books.aid == aid).first()

        return self.success(data=params)
