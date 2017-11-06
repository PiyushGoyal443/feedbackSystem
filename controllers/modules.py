"""
module to import all necessary modules
"""

# tornado modules
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.escape import json_encode, json_decode
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.web import RequestHandler, Application, removeslash

# other modules
import json
from os.path import join, dirname, isfile
import os
from motor import MotorClient
import jwt
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta

secret = os.environ['SECRET']

db = MotorClient("mongodb://ujjwal:ujjwal@ds249355.mlab.com:49355/iwp_feedback")["IWP"]
