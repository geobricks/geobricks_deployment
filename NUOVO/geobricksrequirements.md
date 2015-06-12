# geobricksdistribution:
## requiremenets
### install psycopg2 (in theory that one can be installed in the whole system and not just in the virtual enviroment)

if not installed
```
sudo yum install python-devel postgresql-devel -y

-y force installation
```

### rasterio (https://github.com/mapbox/rasterio) (in theory that one can be installed in the whole system and not just in the virtual enviroment)
after the installation of the packages:
```
$ sudo add-apt-repository ppa:ubuntugis/ppa
$ sudo apt-get update -qq
$ sudo apt-get install python-numpy libgdal1h gdal-bin libgdal-dev
```

install rasterio

```
env/bin/pip install -r https://raw.githubusercontent.com/mapbox/rasterio/master/requirements.txt
env/bin/pip install rasterio
```

### install geobricksdistribution
this will install geobricksdbms and geobricksgisraster as dependency

```
env/bin/pip install geobricksdistribution
```

### gdal (pygdal)
install on redhat6. If the gdal version install is 1.9.2 and not the latest one, install it as
https://pypi.python.org/pypi/pygdal/1.10.1.0

```
env/bin/pip install pygdal==1.9.2
```

then you can use it as ```from osgeo import gdal```
