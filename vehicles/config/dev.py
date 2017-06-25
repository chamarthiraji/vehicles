#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os

TESTING = False
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = True

# DATABASE SETTINGS

import os
# below will be used to get environment variable data
# used if exists
# replace '' or -1 with the actual values if needed
#  or it will use values from from OS environment variables
# If, OS environment variable exists, 
#    then OS environment variable will be used

mysql_db_username = os.environ.get('ENV_MYSQL_USER', 
	'')
mysql_db_password = os.environ.get('ENV_MYSQL_PASSWORD', 
	'')
mysql_db_name = os.environ.get('ENV_MYSQL_DB', 
	'')
mysql_db_hostname = os.environ.get('ENV_MYSQL_HOST', 
	'')
mysql_db_port = os.environ.get('ENV_MYSQL_PORT', 
	-1)
mysql_uri = os.environ.get('ENV_MYSQL_URI')

# PORT = 3306
# HOST = "0.0.0.0"
SQLALCHEMY_ECHO = False
# SECRET_KEY = "SOME SECRET"

if mysql_uri:
	SQLALCHEMY_DATABASE_URI = "pymysql+"+mysql_uri
	print("using environment's db uri")
else:
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}".format(DB_USER=mysql_db_username,
                                                                                        DB_PASS=mysql_db_password,
                                                                                        DB_ADDR=mysql_db_hostname,
                                                                                        DB_PORT=mysql_db_port,
                                                                                        DB_NAME=mysql_db_name)
	print("using constructed db uri")

# SQLALCHEMY_DATABASE_URI='mysql+pymysql://vehicles:{db_password}@localhost/vehiclesdb'.format(db_password=os.environ.get('VEHICLES_DB_PASSWORD'))

# PythonServerData
VEHICLE_SERVICE_PORT=53000

# Google cloud config data
GC_BUCKET_NAME=''
GC_PROJECT_ID=''
GC_CLIENT_ID=''
GC_CLIENT_SECRET=''
GC_URI=''
GC_PROJECT_NUM=''
GC_DOWLOADED_LOCAL_DIR='vehicles/static/gc_downloaded_images'
GC_TEMP_DOWLOADED_LOCAL_DIR='static/gc_downloaded_images'