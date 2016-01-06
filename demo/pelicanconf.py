#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kaluaim'
SITENAME = u'Sardine'
SITEURL = 'http://kaluaim.github.com/sardine'

PATH = 'content'
PLUGINS = ['pelican.plugins.embed_tweet']
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
THEME = '../theme'
DEFAULT_DATE_FORMAT = '%d / %m / %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', '#'),
          ('facebook', '#'),)

DEFAULT_PAGINATION = 100

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Sardine configurations
SRDN_SITE_DIRECTION = 'ltr'
SRDN_TAGLINE = 'just a nother minimal Pelican theme'
SRDN_SIDE_TITLE_PAGES = 'Pages'
SRDN_SIDE_TITLE_MENUITEM = 'Items'
SRDN_SIDE_TITLE_LINKS = 'Links'
SRDN_SIDE_TITLE_SOCIAL = 'Social'
SRDN_SIDE_MSG = 'This is a msg area, you can use it whatever you want.'
SRDN_FOOTER_CR_YEAR = '2016'
