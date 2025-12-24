import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = \
        "postgresql://sysadmin:password@localhost/sysdesign_v1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False