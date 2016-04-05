#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

AUTHOR = u'kaluaim'
SITENAME = u'Sardine'
SITEURL = 'http://kaluaim.github.com/sardine'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
STATIC_PATHS = ['uploads',
                'extra/robots.txt',
                'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
DEFAULT_CATEGORY = 'misc'
THEME = '../theme'
DEFAULT_DATE_FORMAT = '%d / %m / %Y'
DEFAULT_PAGINATION = 80

PLUGINS = [
    'pelican_youtube',
]

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
SOCIAL = (('twitter', '#', 'fa fa-twitter'),
          ('facebook', '#', 'fa fa-facebook'),
          ('linkedin', '#', 'fa fa-linkedin'),)



#   _____               _ _
#  / ____|             | (_)
# | (___   __ _ _ __ __| |_ _ __   ___
#  \___ \ / _` | '__/ _` | | '_ \ / _ \
#  ____) | (_| | | | (_| | | | | |  __/
# |_____/ \__,_|_|  \__,_|_|_| |_|\___| Configurations

# If any of the filed is empty it will not be rendared.
# if 'rtl' if will import rtl.css to the site.
SRDN_SITE_DIRECTION = 'ltr'
SRDN_SITE_LOGO = 'sardine.png'
SRDN_TAGLINE = 'just a nother minimal Pelican theme'
SRDN_SIDE_TITLE_PAGES = 'Pages'
SRDN_SIDE_TITLE_MENUITEM = 'Items'
SRDN_SIDE_TITLE_LINKS = 'Links'
SRDN_SIDE_TITLE_SOCIAL = 'Social'
SRDN_SIDE_MSG = 'This is a msg area, you can use it whatever you want.'

# RSS Feed. for example use feedburnr
SRDN_RSS_TITLE = 'Subscribe in a reader'
SRDN_RSS_URL = '#'

# Email Feed
SRDN_EMAIL_TITLE = 'Subscribe via email'
SRDN_EMAIL_URL = '#'

SRDN_CATEGORY_TEXT = 'Category:'
SRDN_TAG_TEXT = 'Tag:'
SRDN_DISQUS_SITENAME = 'sardine'

# HTML footer lines, after each line <br/> will be added.
SRDN_FOOTER_LINES = (('<span>Copyright kaluaim © 2016</span>'),
                     ('<span>Powred by <a href="http://blog.getpelican.com/">Pelican</a>, using <a href="https://github.com/kaluaim/sardine">Sardine</a></span>'),)
