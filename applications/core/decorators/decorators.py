#!/usr/bin/env python
# -*- coding: utf-8  -*-

from tornado.util import import_object


def required_permissions(*dargs, **dkargs):
    """权限控制装饰器
    """
    User = import_object('applications.admin.models.User')
    SUPER_ADMIN = import_object('applications.configs.settings.SUPER_ADMIN')
    def wrapper(method):
        # @functools.wraps(method)
        def _wrapper(*args, **kargs):
            code = dargs[0]
            self = args[0]
            user_id = self.current_user.get('id')
            # print(self.current_user, user_id)
            if int(user_id) in SUPER_ADMIN:
                return method(*args, **kargs)

            obj = User.Q.filter(User.id==user_id).first()
            if obj and obj.permission and code not in obj.permission:
                if obj.role_permission and code not in obj.role_permission:
                    return self.error('未授权', 401)
            return method(*args, **kargs)
        return _wrapper
    return wrapper
