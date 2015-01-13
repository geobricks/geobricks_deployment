import subprocess
import os
from shutil import rmtree

virtualenv_path = "env"


def install_virtualenv_and_package(package_file, install_path="", virtualenv=True):
    # read file
    print package_file

     # TODO: remove it
    install_path += virtualenv_path
    if not check_virtualenv(install_path):
        install_virtualenv(install_path)

    # read dependencies
    with open(package_file) as f:
        libraries = f.readlines()
        for library in libraries:
            install_pip(library)


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
    output = subprocess.check_call(["virtualenv", install_path + "env"])
    print output


def install_pip(name, install_path="", virtualenv=True, upgrade=False):
    print name
    cmd = os.path.join(install_path, "env", "bin") if virtualenv else install_path
    cmd = os.path.join(cmd, "pip")
    print cmd
    cmd = [cmd, "install", name]
    if upgrade:
        cmd.append("--upgrade")
    print cmd
    output = subprocess.check_call(cmd)
    print output

