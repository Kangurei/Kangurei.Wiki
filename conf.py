# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Kangurei/Kangurei.Wiki@gh-pages"
}

# 站点设置
site_name = "Kangurei's Wiki"
site_logo = "${static_prefix}logo.png"
site_build_date = "2022-03-24T22:00+08:00"
author = "Kangurei"
email = "kangurei@fantasai.ink"
author_homepage = "https://www.fantasai.ink"
description = " "
key_words = ['Maverick', 'Kangurei', 'Kepler', 'WIKI']
language = 'zh-CN'
external_links = [
    {
        "name": "Kangurei's Blog",
        "url": "https://www.fantasia.ink",
        "brief": " "
    },
    {
        "name": "Kangurei's Pan",
        "url": "https://pan.fantasia.ink/",
        "brief": " "
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/Kangureiii",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/Kangurei",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5528704865/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
