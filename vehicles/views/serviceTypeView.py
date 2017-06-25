#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for
# from vehicleapp import app, db
# from app.models import Post
# from __init__ import app, db
from vehicles.app import app
from vehicles.extensions import DB, exc
from vehicles.models.models import ServiceType
# from __init__ import exc
# import app, db
import sys
# sys.path.append("vehicleapp/models")
# from models.serviceType import ServiceType
# from vehicleapp.models import

import json
import inspect


@app.route('/addservicetype', methods=['POST', 'GET'])
def addservicetype():

    # http://127.0.0.1:53000/addservicetype
    print("inside addservicetype")
    data = request.get_json() or request.form
    print("response : " + json.dumps(data))
    print("response serviceName: " + data['serviceName'])
    servicetype = ServiceType(data['serviceName'],
                              data['sDisplayName'],
                              data['serviceDescri'])
    DB.session.add(servicetype)
    DB.session.commit()
    flash('New entry was successfully posted')
    response2 = (
        {
            "status": True,
            "description": "New entry was successfully posted"
        }
    )

    return app.response_class(json.dumps(response2), content_type='application/json')


@app.route('/listservicetypes', methods=['POST', 'GET'])
def listservicetypes():
    # http://127.0.0.1:53000/listservicetypes
    print("inside listservicetypes")
    # print("stack:"+str(inspect.stack()))
    service_type_list = []
    print("request method:" + request.method)

    if (request.method == 'POST'):
        data = request.get_json()

        if (data['vehicleTypeId']):
            vehicletype = DB.session.query(ServiceType).filter_by(
                vehicle_type_id=data['vehicleTypeId'])
            print("filtering by vehicleTypeId:" + str(data['vehicleTypeId']))
        else:
            servicetype = DB.session.query(ServiceType)
            print("no filtering - POST method")
    else:
        servicetype = DB.session.query(ServiceType)
        print("no filtering - GET method")

    for lservicetype in servicetype:
        service_type_list.append({
            "id": lservicetype.id,
            "name": lservicetype.name,
            "display_name": lservicetype.display_name,
            "description": lservicetype.description
        })

    return app.response_class(json.dumps(service_type_list), content_type='application/json')

 # view for editing service types


@app.route('/editservicetypes', methods=['POST', 'GET'])
def editservicetypes():
    # http://127.0.0.1:53000/editservicetypes
    print("inside 2 editservicetypes")
    data = request.get_json()
    print("editservicetypes input : " + json.dumps(data))
    print("editservicetypes input serviceTypeId: " + str(data['serviceName']))
    recexists = 0
    db_last_apicall_date = ""

    l_serviceType = DB.session.query(ServiceType).filter_by(id=data['id'])

    response2 = ""

    if (data['id']):
        try:
            record = l_serviceType.one()
            recexists = 1
        except Exception:
            print("No service type record in DB")
            pass
        finally:
            print("servicetypes data exists in DB")

    if (recexists == 1):
        print("existing servicetypes data")
        print("id:" + str(record.id))
        print("service name:" + str(record.name))
        print("sdisplay_text:" + str(record.display_name))

    if (recexists == 1) and (l_serviceType.count() > 0):
        print("trying to update new values")
        record.name = data['serviceName']
        record.display_name = data['sDisplayName']
        record.description = data['sDescription']

    if (recexists == 0):

        servicetypes = ServiceType(
            data['serviceName'],
            data['sDisplayName'],
            data['sDescription']
        )
        DB.session.add(servicetypes)

    exception_info = 0

    try:
        DB.session.commit()
    except exc.IntegrityError as err:
        print("exception")
        DB.session.rollback()
        if "Duplicate entry" in str(err):
            print("Duplicate exception")
            exception_info = 1
            response = {
                "status": False,
                "description": "IntegrityError error, ServiceType already exists"
            }
            return app.response_class(json.dumps(response), content_type='application/json')
        else:
            print("Other exception")
            response = {
                "status": False,
                "description": "unknown error adding/updating ServiceType info"
            }
            return app.response_class(json.dumps(response), content_type='application/json')

    finally:

        print("finally")
    if (exception_info > 0):
        response2 = (
            {
                "status": False,
                "description": "Exception occured while processing record"
            }
        )
    if (exception_info == 0):
        response2 = (
            {
                "status": True,
                "description": "New entry was successfully posted"
            }
        )

    return app.response_class(json.dumps(response2), content_type='application/json')


@app.route('/deleteservicetype', methods=['POST', 'GET'])
def deleteservicetype():
    # http://127.0.0.1:53000/deleteservicetype
    print("inside 2 deleteservicetype")
    data = request.get_json()
    print("deleteservicetype input : " + json.dumps(data))
    print("deleteservicetype input id: " + str(data['id']))
    try:
        ServiceType.query.filter_by(id=data['id']).delete()
        DB.session.commit()
    except Exception:
        print("No ServiceType record in DB")
        pass
        print("Other exception")
        response = {
            "status": False,
            "description": "unknown error deleting ServiceType info"
        }
        return app.response_class(json.dumps(response), content_type='application/json')

    finally:
        print("Deleted the ServiceType data from DB")

    response = (
        {
            "status": True,
            "description": "Deleted the ServiceType data from DB"
        }
    )

    return app.response_class(json.dumps(response), content_type='application/json')
