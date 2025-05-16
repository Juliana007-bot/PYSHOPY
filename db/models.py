from .database import Base
from sqlalchemy import Column,Integer,String,Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

class Medico(Base):
    __tablename__ = "medico"
    id = Column(Integer , 
                primary_key=True)
    nombre = Column(String(60))
    apellido = Column(String(60))
    especialidad = Column(String(60))

        #Relacion uno a muchos con paciente
    Paciente =relationship("Paciente" , 
                            back_populates="Medico")


class Paciente(Base):
    __tablename__ = "paciente"
    id = Column(Integer,
                primary_key=True)
    nombre=Column(String(60))
    apellido=Column(String(60))
    Tipo_de_documento=Column(String(60))
    numero_de_documento=Column(Integer)
    telefono = Column(Integer)

    #Clave foranea
    medico_id =Column(Integer, 
                      ForeignKey('medico.id'))






