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
env.hosts = ['35.196.13.145', '184.72.66.167']


def do_deploy(archive_path):
    """ distributes a packed archive to web servers """
    if not path.exists(archive_path):
        return False
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
