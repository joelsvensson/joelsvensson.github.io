#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

"""Module providing all config from pelicanconf.py"""
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-position

# override settings
SITEURL = "https://mgio.se"
FEED_ALL_ATOM = "feeds/all.atom.xml"
RELATIVE_URLS = False
