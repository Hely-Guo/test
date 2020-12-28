import os
from datetime import timedelta

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-DIFFICULT-SECRET-KEY'

    # SQLALCHEMY_DATABASE_URI = 'mysql://scott:tiger@localhost/mydatabase'
    # SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=60)