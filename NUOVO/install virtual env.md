# virtualenv for RedHat6
https://www.digitalocean.com/community/tutorials/how-to-run-django-with-mod_wsgi-and-apache-with-a-virtualenv-python-environment-on-a-debian-vps

# compiling python 2.7
http://cysec.org/blog/2011/06/10/compiling-mod_wsgi-for-a-custom-python-build/index.html

# compiling mod_wsgi
if ldd libpython2.7.so.1.0 => not found
libpython2.7.so.1.0 => not found
ln -s /usr/local/python2.7.3/lib/libpython2.7.so.1.0 /lib64/

## Problems with python2.7 (bzip)
CompressionError: bz2 module is not available

## installation bzip
sudo cp /usr/lib64/python2.6/lib-dynload/bz2.so /usr/local/lib/python2.7/

## install virtual env 
mkdir app
cd app
virtualenv -p /usr/local/bin/python2.7 env

## install uwsgi with pip
.env/bin/pip install uwsgi



## install packagages
env/bin/pip install geobricksrestengine
env/bin/pip install geobricksgeocoding

## install with nginx




Installing python 2.7 mod_wsgi in apache
sudo yum install httpd-devel
https://www.fir3net.com/Programming/Python/how-do-i-compile-modwgsi-for-python-27.html



