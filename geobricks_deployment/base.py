import subprocess
import os
import glob
from shutil import rmtree, copy

library_path = __file__
virtualenv_path = "env"
resources_path = "resources"

print library_path


def install_virtualenv_and_package(package_file, install_path="", virtualenv=True):
    print package_file
    print install_path

    # install_path it's not used yet
    install_path += virtualenv_path
    if not check_virtualenv(install_path):
        install_virtualenv(install_path)

    # read dependencies
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), package_file)) as f:
        libraries = f.read().splitlines()
        for library in libraries:
            install_pip(library)

    # copy resources files to current directory
    copy_resources_to_env()


def upgrade_packages(package_file, install_path="", virtualenv=True):
    # read dependencies
    with open(package_file) as f:
        libraries = f.readlines()
        for library in libraries:
            install_pip(library, install_path, virtualenv, True)


def check_virtualenv(path):
    if os.path.isdir(path):
        return True
    else:
        return False


def install_virtualenv(install_path=""):
    # TODO: set python as parameter, this doesn't work for all the version (but it's ok for RH6)
    cmd = ["virtualenv", "-p", "/usr/local/bin/python2.7", virtualenv_path]
    print cmd
    output = subprocess.check_call(cmd)
    print output


def install_pip(name, install_path="", virtualenv=True, upgrade=False):
    cmd = os.path.join(install_path, virtualenv_path, "bin") if virtualenv else install_path
    cmd = os.path.join(cmd, "pip")
    name = name.split(" ")
    cmd = [cmd, "install"]
    for n in name:
        cmd.append(n)
    if upgrade:
        if len(name) == 1:
            cmd.append("--upgrade")
            print cmd
            output = subprocess.check_call(cmd)
            print output
    else:
        print cmd
        output = subprocess.check_call(cmd)
        print output


def copy_resources_to_env():
    src_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), resources_path, "*")
    files = glob.glob(src_path)
    for f in files:
        copy(f, ".")
