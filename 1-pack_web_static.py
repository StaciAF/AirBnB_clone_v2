#!/usr/bin/python3
"""
this script generates an archive file
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ create a tar archive of web_static """
    dated = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(dated.year,
                                                            dated.month,
                                                            dated.day,
                                                            dated.hour,
                                                            dated.minute,
                                                            dated.second)
    local("mkdir -p versions")
    create_arch = local("tar -cvzf " + archive + " web_static")
    if create_arch.succeeded:
        return archive
    else:
        return None
