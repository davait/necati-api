#! /usr/bin/env python3

from bson import ObjectId

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

from config import *

from app_tools import JSONEncoder

import logging
import os

# Current environment
config = globals()[os.environ['FLASK_ENV']]

# Backend app defs
application = Flask(config.APPLICATION_NAME)
application.config.from_object(config)
application.json_encoder = JSONEncoder

application.config['MONGO_URI'] = ''.join([
    'mongodb://', config.MONGODB_USERNAME,
    ':', config.MONGODB_PASSWORD,
    '@', config.MONGODB_HOSTNAME,
    ':', config.MONGODB_PORT,
    '/', config.MONGODB_DATABASE
])

mongo = PyMongo(application)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@application.route('/new_task', methods=['POST'], endpoint='new_task')
def new_task():
    data = request.get_json(force=True)

    if not data or 'cmd' not in data:
        return jsonify(
                exception = True,
                message = 'Required parameter missing'
            ), 200

    input_items = {
        'cmd': data['cmd']
    }

    result = mongo.db.tasks.insert_one(input_items)

    return jsonify(
        message = 'Task saved successfully',
        exception = False,
        id = result.inserted_id,
    ), 201


@application.route('/get_output/:<id>', methods=['GET'], endpoint='get_output')
@application.route('/get_output', methods=['GET'], endpoint='get_output')
def get_output(id = None):
    if not id:
        # Return all contents from database
        tasks = mongo.db.tasks.find()
    else:
        mongo_id_length = len(id)
        if mongo_id_length != 12 and mongo_id_length != 24:
            # Id must be a 12-byte input or a 24-character hex string
            return jsonify(
                    exception = True,
                    message = 'Parameter format is not valid'
                ), 200
        tasks = mongo.db.tasks.find({'_id': ObjectId(id)})

    item = {}
    data = []

    for task in tasks:
        item = {
            'id': str(task['_id']),
            'cmd': task['cmd']
        }
        data.append(item)

    return jsonify(
        exception = False,
        output = data
    )


@application.route('/')
def index():
    return jsonify(
        status = True,
        message = 'Welcome to Necati REST API'
    )


# Run Flask API
if __name__ == '__main__':
    application.run(host = config.API_HOST,
        port = config.API_PORT,
        debug = config.API_DEBUG
    )
