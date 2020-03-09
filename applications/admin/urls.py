#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .handlers import dashboard
from .handlers import passport
from .handlers import member
from .handlers import user
from .handlers import role
from .handlers import menu
from .handlers import config
from .handlers import content
from .handlers import boll

# 其他 URL 通过 acl 获取
urls = [
    # passport
    (r"/admin/login/?(.html)?", passport.LoginHandler),
    (r"/admin/logout/?(.html)?", passport.LogoutHandler),
    (r"/admin/captcha/?(.png)?", passport.CaptchaHandler),

    # dashboard
    (r"/admin/?(.html)?", dashboard.MainHandler),
    (r"/admin/index/?(.html)?", dashboard.MainHandler),
    (r"/admin/main/?(.html)?", dashboard.MainHandler),
    (r"/admin/welcome/?(.html)?", dashboard.WelcomeHandler),
    (r"/admin/welcome/list?(.html)?", dashboard.BooksListHandler),


    # mixing
    (r"/admin/welcome/list/delete?(.html)?", dashboard.BooksListHandler),
    (r"/admin/welcome/list/add?(.html)?", dashboard.BooksListAddHandler),
    (r"/admin/welcome/list/edit?(.html)?", dashboard.BooksListEditHandler),

    (r"/admin/boll/?(.html)?", boll.BollHandler),
    (r"/admin/boll/list?(.html)?", boll.BollListHandler),
    (r"/admin/boll/list/delete?(.html)?", boll.BollListHandler),
    (r"/admin/boll/upload?(.html)?", boll.BollHandler),

    # config
    (r"/admin/config/index?(.html)?", config.ConfigHandler),
    (r"/admin/config/list/?(.html)?", config.ConfigListHandler),
    (r"/admin/config/delete?(.html)?", config.ConfigHandler),
    (r"/admin/config/add?(.html)?", config.ConfigAddHandler),
    (r"/admin/config/edit?(.html)?", config.ConfigEditHandler),

    # menu
    (r"/admin/menu/index?(.html)?", menu.MenuHandler),
    (r"/admin/menu/delete?(.html)?", menu.MenuHandler),
    (r"/admin/menu/add?(.html)?", menu.MenuAddHandler),
    (r"/admin/menu/edit?(.html)?", menu.MenuEditHandler),
    (r"/admin/menu/sort?(.html)?", menu.MenuSortHandler),
    (r"/admin/menu/status?(.html)?", menu.MenuStatusHandler),
    (r"/admin/menu/icon?(.html)?", menu.MenuIconHandler),

    # user
    (r"/admin/user/index/?(.html)?", user.UserHandler),
    (r"/admin/user/delete/?(.html)?", user.UserHandler),
    (r"/admin/user/list/?(.html)?", user.UserListHandler),
    (r"/admin/user/add/?(.html)?", user.UserAddHandler),
    (r"/admin/user/edit/?(.html)?", user.UserEditHandler),
    (r"/admin/user/unlocked/?(.html)?", user.UserUnlockedHandler),
    (r"/admin/user/info/?(.html)?", user.UserInfoHandler),

    # user_role
    (r"/admin/role/index/?(.html)?", role.RoleHandler),
    (r"/admin/role/delete/?(.html)?", role.RoleHandler),
    (r"/admin/role/list/?(.html)?", role.RoleListHandler),
    (r"/admin/role/add/?(.html)?", role.RoleAddHandler),
    (r"/admin/role/edit/?(.html)?", role.RoleEditHandler),


    # member
    (r"/admin/member/index/?(.html)?", member.MemberHandler),
    (r"/admin/member/delete/?(.html)?", member.MemberHandler),
    (r"/admin/member/list/?(.html)?", member.MemberListHandler),
    (r"/admin/member/add/?(.html)?", member.MemberAddHandler),
    (r"/admin/member/edit/?(.html)?", member.MemberEditHandler),
    (r"/admin/member/authorize/?(.html)?", member.MemberAuthorizeHandler),
    (r"/admin/member/authorize/list/?(.html)?", member.MemberAuthorizeListHandler),

    # article
    (r"/admin/article/index/?(.html)?", content.ArticleHandler),
    (r"/admin/article/delete/?(.html)?", content.ArticleHandler),
    (r"/admin/article/list/?(.html)?", content.ArticleListHandler),
    (r"/admin/article/add/?(.html)?", content.ArticleAddHandler),
    (r"/admin/article/edit/?(.html)?", content.ArticleEditHandler),

    # company
    (r"/admin/content/upload/?(.html)?", content.UploadHandler),
    (r"/admin/company/team/?(.html)?", content.CompanyTeamHandler),
    (r"/admin/team/list/?(.html)?", content.TeamListHandler),
    (r"/admin/team/delete/?(.html)?", content.TeamListHandler),
    (r"/admin/team/edit/?(.html)?", content.TeamEditHandler),
    (r"/admin/team/add/?(.html)?", content.TeamAddHandler),
]
