#!/usr/bin/python 3
"""
this module deletes stuff
"""

from fabric.api import *


env.hosts = ['35.196.13.145', '184.72.66.167']
env.user = 'ubuntu'


def do_clean(number=0):
    """ delete out of date archives """
    if number == 0 or number == 1:
        local(' ')
    else:
