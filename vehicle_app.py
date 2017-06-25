#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from flask import Flask, render_template
from flask import render_template
import logging
from logging.handlers import RotatingFileHandler
import os
import pymysql.cursors
from flask import jsonify

import json
import binascii
import zlib
import time
import datetime
from urllib.request import urlopen
# from flask import current_app as app
# import config
import boto

import sys
# sys.path.append("vehicles/")
# from vehicles.__init__ import app, config
from vehicles.app import app

from vehicles.views import googlecloudapiimages
from vehicles.views import serviceTypeView
from vehicles.views import vehicleTypeView
from vehicles.views import zipcodeView
from vehicles.views import locationView
from vehicles.views import vehicleConditionView
from vehicles.views import availableServicesView
from vehicles.views import specialServicesView

import shutil
import tempfile
# import oauth2_plugin
# import oauth2_client
# import gcs_oauth2_boto_plugin

# get local config data
# cfgserverport = app.config.get('PythonServerData',
#   'VEHICLE_SERVICE_PORT')
cfgserverport = app.config['VEHICLE_SERVICE_PORT']
print("cfgserverport:"+str(cfgserverport))
# Use server environment config data if available.
tmpserverport = int(os.environ.get('ENV_VEHICLE_SERVICE_PORT',
   cfgserverport))

# tmpserverport = int(os.environ.get('ENV_VEHICLE_SERVICE_PORT'))
print("tmpserverport : "+str(tmpserverport))

print(" root  "+__name__)

@app.route('/')
def index():
    #  app.log                                                                                                                            ger.warning('testing warning log')

    # app.logger.error('testing error log')
    # http://127.0.0.1:53000/
    app.logger.info('testing info log')

    return render_template('index.html')



if __name__ == '__main__':
            # initialize the log handler
    # logHandler = RotatingFileHandler(
    #    'vehicle_app_routes_call.log', maxBytes=1000, backupCount=1)

    # set the log handler level
    # logHandler.setLevel(logging.INFO)

    # set the app logger level
    # app.logger.setLevel(logging.INFO)

    # app.logger.addHandler(logHandler)

    app.run(debug=True, port=tmpserverport)
