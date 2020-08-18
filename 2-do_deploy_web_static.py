#!/usr/bin/python3
"""
this script generates an archive file
"""
from fabric.api import local
from fabric.api import run
from fabric.api import put
from fabric.api import env
from datetime import datetime
from os import path


env.hosts = ['184.72.66.167', '35.196.13.145']


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


def do_deploy(archive_path):
    """ distributes a packed archive to web servers """
    if path.exists(archive_path) is False:
        return False
    print(env.port)
    alt_path = archive_path[9:]
    arch_folder = "/data/web_static/releases/" + alt_path[:-4]
    new_file = "/tmp/" + alt_path
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(arch_folder))
        run("sudo tar -xzf {} -C {}".format(new_file, arch_folder))
        run("sudo rm -rf {}".format(new_file))
        run("sudo mv {}/web_static/*{}".format(arch_folder, arch_folder))
        run("sudo rm -rf {}/web_static".format(arch_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} /data/web_static/current".format(arch_folder))
        return True
    except:
        return False
