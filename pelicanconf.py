#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""Module providing config vars."""

from datetime import datetime

# DEV settings, overrides in publishconf
SITEURL = "http://localhost:8000"
RELATIVE_URLS = True


AUTHOR = "Joel"
SITENAME = "mgio.se"
SITETITLE = "mgio AB"
SITESUBTITLE = "Joel Svensson, 0703 20 13 13"
# https://developers.google.com/search/docs/appearance/snippet#meta-descriptions
# SITEDESCRIPTION = "TEST-SITEDESCRIPTION"

SITELOGO = f"{SITEURL}/images/joel.jpg"
FAVICON = f"{SITEURL}/favicon.svg"

PATH = "content"
ARTICLE_PATHS = ["blogposts"]
ARTICLE_URL = "blogposts/{date:%Y}/{slug}/"
ARTICLE_SAVE_AS = "blogposts/{date:%Y}/{slug}/index.html"

TIMEZONE = "Europe/Rome"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
THEME = "themes/Flex"
THEME_COLOR = "light"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

CUSTOM_CSS = "css/override.css"
STATIC_PATHS = [
    "CNAME",
    "css",
    "images",
    "favicon.svg",
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = ""
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_DOMAIN = SITEURL

DISPLAY_PAGES_ON_MENU = False
# Blogroll
LINKS = (
    ("Om Joel", "/pages/joel.html"),
    ("Om mgio", "/pages/mgio.html"),
)

# Social widget
SOCIAL = (
    ("envelope", "mailto:joel@mgio.se"),
    ("mobile", "tel:0703 20 13 13"),
    ("linkedin", "https://www.linkedin.com/in/joel-svensson-5ba45615"),
    ("github", "https://github.com/joelsvensson/joelsvensson.github.io"),
    ("rss", "/feeds/all.atom.xml"),
)

MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 5

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}
COPYRIGHT_YEAR = datetime.now().year

DELETE_OUTPUT_DIRECTORY = True
