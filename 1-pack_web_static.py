#!/usr/bin/python3
"""
Fabric script that Generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''
    Generates a tgz archive from the
    contents of the web_static folder
    '''
    try:
        local('mkdir -p versions')
        dt_format = '%Y%m%d%H%M%S'
        ar_path = 'versions/web_static_{}.tgz'.format(
            datetime.now().strftime(dt_format))
        local('tar -cvzf {} web_static'.format(ar_path))
        print('web_static packed: {} -> {}'.format(ar_path,
              os.path.getsize(ar_path)))
    except:
        return None
