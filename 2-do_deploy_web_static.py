#!/usr/bin/python3
"""
A fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        fn = archive_path.split("/")[-1]
        noxt = fn.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, noxt))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fn, path, noxt))
        run('rm /tmp/{}'.format(fn))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, noxt))
        run('rm -rf {}{}/web_static'.format(path, noxt))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noxt))
        return True
    except:
        return False
