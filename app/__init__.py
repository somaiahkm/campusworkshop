"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7s35269vf5qbb5apg-a.oregon-postgres.render.com",
        database="mypostgredb_smfu",
        user="somaiah",
        password="VwY4x3g9JOXywVOvlnjIzIcV1sGsumVz")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
