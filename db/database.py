from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#coneccion string
# represemta la base de datos a conectarse
#depende de la base de datos que use y el lenguaje de programacion

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3315/py-shopy'



#crear el objeto de conexion
conn = create_engine(SQLALCHEMY_DATABASE_URL)

#la clase base para los modelos
Base =declarative_base()