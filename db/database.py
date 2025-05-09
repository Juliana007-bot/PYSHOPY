from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URl = 'mariadb://root@admin/localhost:3315/py-shopy'
engine = create_engine()