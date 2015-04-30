#!/usr/bin/env bash

# rasterio
sudo add-apt-repository ppa:ubuntugis/ppa

# update quiet
# apt-get update -qq
sudo apt-get update
sudo apt-get -y install python-numpy libgdal1h gdal-bin libgdal-dev

# rasterio?
sudo apt-get install g++

# numpy (needs fortran to compile)
sudo apt-get -y install libblas3gf libc6 libgcc1 libgfortran3 liblapack3gf libstdc++6 build-essential gfortran python-all-dev libatlas-base-dev

# numpy dependency
sudo apt-get -y install python-dev

# scipy dependency
#sudo apt-get -y install libblas-dev liblapack-dev
# yum install blas lapack (there is not DEVEL on redhat6 so it's imporssible to install with pip install scipy!)
yum install scipy

# general
sudo apt-get -y install python-pip
sudo apt-get -y install python-virtualenv 
#sudo pip install virtualenv

# install scipy using apt-get?
#sudo apt-get install python-scipy 