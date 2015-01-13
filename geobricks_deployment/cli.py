#!/usr/bin/env python
# from geobricks_deployment import base
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from geobricks_deployment import base
from argh import arg, dispatch_commands
from argh.decorators import named


@named('buildenv')
# @arg('package', help='Keyword to search the library')
def build_lib(package="default"):
    """ build library """
    print package
    # TODO: fast workarounf to "pip install missing txt file..."
    file_requirement_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), package + "_pip_requirements.py")
    base.install_virtualenv_and_package(file_requirement_path)
    # base.install_virtualenv_and_package(package + "_pip_requirements.txt")


@named('upgrade')
# @arg('package', help='Keyword to search the library')
def upgrade_lib(package="default"):
    """ build library """
    print package
    # TODO: fast workarounf to "pip install missing txt file..."
    file_requirement_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), package + "_pip_requirements.py")
    base.upgrade_packages(file_requirement_path)
    # base.upgrade_packages(package + "_pip_requirements.txt")


def main():
    dispatch_commands([build_lib, upgrade_lib])

if __name__ == '__main__':
    main()
