#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import os

from tornado.escape import json_decode

from applications.core.settings_manager import settings
from applications.core.cache import cache

from applications.core.logger.client import SysLogger
from applications.core.utils import Func
from applications.core.models import BaseModel

from sqlalchemy.types import Integer
from sqlalchemy.types import Numeric
from sqlalchemy.types import VARCHAR
from sqlalchemy.types import VARCHAR
from sqlalchemy.types import Text
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.types import DATETIME
from sqlalchemy import Column, CHAR, TEXT, SmallInteger
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint


class Books(BaseModel):
    """
        Books model
        """
    __tablename__ = 'mx_addonarticle'

    aid = Column(Integer, primary_key=True)
    #typeid = Column(SmallInteger, nullable=True)
    #body = Column(TEXT,  default='')
    #redirecturl = Column(VARCHAR(255), nullable=True, default='')
    #templet = Column(VARCHAR(30), nullable=True, default='')

    userip = Column(CHAR(15), nullable=True, default='')

    lbh = Column(VARCHAR(250), nullable=True, default='')
    name = Column(VARCHAR(250), nullable=True, default='')
    data = Column(VARCHAR(250), nullable=True, default='')
    xz = Column(VARCHAR(250), nullable=True, default='')
    cj = Column(VARCHAR(250), nullable=True, default='')
    cw = Column(VARCHAR(250), nullable=True, default='')
    sx = Column(VARCHAR(250), nullable=True, default='')
    jn = Column(VARCHAR(250), nullable=True, default='')

    utc_created_at = Column(TIMESTAMP, default=Func.utc_now)

    @property
    def created_at(self):
        return Func.dt_to_timezone(self.utc_created_at)

    @property
    def updated_at(self):
        return Func.dt_to_timezone(self.utc_updated_at)


class Bolls(BaseModel):
    """
        Boll model
        """
    __tablename__ = 'mx_boll'

    id = Column(Integer, primary_key=True)

    bollurl = Column(VARCHAR(250), nullable=True, default='')
    bollname = Column(VARCHAR(250), nullable=True, default='')

    utc_created_at = Column(TIMESTAMP, default=Func.utc_now)

    @property
    def created_at(self):
        return Func.dt_to_timezone(self.utc_created_at)

    @property
    def updated_at(self):
        return Func.dt_to_timezone(self.utc_updated_at)