#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""URL处理器

[description]
"""
import tornado

from applications.core.cache import sys_config
from applications.core.settings_manager import settings
from applications.core.logger.client import SysLogger

from .common import CommonHandler

from ..utils import tpl_params
from ..models.content import Contact
from ..models.content import Article


class IndexHandler(CommonHandler):
    def get(self, *args, **kwargs):
        """首页
        """
        params = {

        }

        self.render_html('index.html', **params)


class ShopHandler(CommonHandler):
    def get(self, *args, **kwargs):
        """商店
        """
        params = {

        }

        self.render_html('shop.html', **params)


class AboutHandler(CommonHandler):
    def get(self, *args, **kwargs):
        """关于
        """
        params = {

        }

        self.render_html('about.html', **params)