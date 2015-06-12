#!/bin/bash

# sudo apt-get install pip

# sudo pip install virtualenvwrapper

# sudo pip install virtualenv

# install virtual env

# virtualenv -p /usr/local/bin/python2.7 env/

# creating virtualenv
virtualenv env/

# install packages
env/bin/pip install -r https://raw.githubusercontent.com/mapbox/rasterio/master/requirements.txt
env/bin/pip install rasterio
env/bin/pip install fiona
env/bin/pip install GeobricksCommon

env/bin/pip install GeobricksGeocoding

#env/bin/pip install GeobricksProcessing
env/bin/pip install GeobricksProj4ToEPSG
env/bin/pip install GeobricksGISRaster
env/bin/pip install GeobricksGISVector

env/bin/pip install GeobricksDBMS
env/bin/pip install GeobricksSpatialQuery
env/bin/pip install GeobricksDistribution
env/bin/pip install GeobricksGeostatistics

# scipy is needed for pysal (added as dependency so in theory should be already loaded)
env/bin/pip install scipy  
env/bin/pip install GeobricksMapClassify
env/bin/pip install GeobricksRasterCorrelation

env/bin/pip install GeobricksRESTEngine

# Install GDAL (due to the problem with GDAL is install pygdal)
# sudo apt-get install  libgdal-dev #and all the other packages
#export CPLUS_INCLUDE_PATH=/usr/include/gdal
#export C_INCLUDE_PATH=/usr/include/gdal
#env/bin/pip install GDAL
env/bin/pip install pygdal
# env/bin/pip install pygdal=1.9.2 (for redhat6)

# install uwsgi
env/bin/pip install uwsgi
