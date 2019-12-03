import os
import re
import shutil
import tempfile
from distutils.dir_util import copy_tree

cwd = os.getcwd()
NEWSETL_PATH = f"{cwd}/newsltd_etl"
cwd = os.getcwd()
REQ_PATH = f"{cwd}/requirements.txt"
REQ_DEV_PATH = f"{cwd}/requirements_dev.txt"


def get_tmp_dir():
    tmpdir = tempfile.gettempdir()
    # Path to be created
    path = f"{tmpdir}/birgitta"
    shutil.rmtree(path, ignore_errors=True)
    os.mkdir(path)
    return path


def clone_birgitta(path):
    print(f"clone birgitta to {path}")
    os.system(f"git clone --depth 1 git@github.com:telia-oss/birgitta.git {path}")  # noqa E501


def remove_newsltd():
    print(f"delete path {NEWSETL_PATH}")
    shutil.rmtree(NEWSETL_PATH)


def overwrite_newsltd(srcdir):
    src = f"{srcdir}/newsltd_etl"
    print(f"copy {src} to {NEWSETL_PATH}")
    copy_tree(f"{srcdir}/newsltd_etl", NEWSETL_PATH)


def print_git_status():
    os.system(f"git status")


def replace_birgitta_version(path, version):
    print("version:", repr(version))
    with open(path, 'r+') as f:
        content = f.read()
        restr = r"\1\2NEW_VERSION\3"
        content_new = re.sub('(.*)(birgitta==)[0-9.]+(.*)',
                             restr,
                             content)
        content_new = content_new.replace('NEW_VERSION', version)
        f.seek(0)
        f.write(content_new.strip())
        f.truncate()


def get_birgitta_version(tdir):
    version_re = re.compile('^version = \'([0-9.]+)\'$')
    for line in open(f"{tdir}/setup.py"):
        m = version_re.match(line)
        if m:
            v = m.group(1)
            print('Found birgitta version: ', v)
            return v


def set_birgitta_version(version):
    replace_birgitta_version(REQ_PATH, version)
    replace_birgitta_version(REQ_DEV_PATH, version)


tdir = get_tmp_dir()
clone_birgitta(tdir)
remove_newsltd()
overwrite_newsltd(tdir)
set_birgitta_version(get_birgitta_version(tdir))
print_git_status()
