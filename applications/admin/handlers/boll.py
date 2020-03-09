#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""URL处理器

[description]
"""
import tornado
import os
import json
from applications.admin.models.mxbooks import Books, Bolls
from applications.configs.settings import STATIC_PATH
from applications.core.settings_manager import settings

from applications.core.decorators import required_permissions

from .common import CommonHandler


class BollHandler(CommonHandler):
    @tornado.web.authenticated
    @required_permissions('admin:boll')
    def get(self, *args, **kwargs):
        """后台星球图片首页
        """
        params = {

        }

        self.render('boll/boll.html', **params)

    def post(self, *args, **kwargs):
        ret = {'result': 'OK'}
        # 文件暂存路径

        upload_path = os.path.join(STATIC_PATH, 'home/images/books_result_bolls/')
        # 提取表单中‘name’为‘file’的文件元数据
        print(self.request.files.keys())
        file_metas = self.request.files.get('file', None)

        if not file_metas:
            ret['result'] = 'Invalid Args'
            self.write(json.dumps(ret))
            return

        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path, filename)
            with open(filepath, 'wb') as up:
                up.write(meta['body'])
            # 保存到星球数据库
            picpath = 'home/images/books_result_bolls/' + filename
            params = {
                'bollurl': picpath,
                'bollname': filename,
            }
            boll = Bolls(**params)
            Bolls.session.add(boll)
        Bolls.session.commit()
        self.write(json.dumps(ret))



class BollListHandler(CommonHandler):
    @tornado.web.authenticated
    @required_permissions('admin:boll:list')
    def get(self, *args, **kwargs):
        """星球图片
        """
        limit = self.get_argument('limit', 10)
        page = self.get_argument('page', 1)
        pagelist_obj = Bolls.Q.filter().paginate(page=page, per_page=limit)
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
    @required_permissions('admin:boll:list:delete')
    def delete(self, *args, **kwargs):
        """删除
        """
        id = self.get_argument('id', None)

        boll = Bolls.Q.filter(Bolls.id == id).first()
        if boll is None:
            return self.error('不存在的数据')

        Bolls.Q.filter(Bolls.id == id).delete()
        Bolls.session.commit()
        return self.success()






