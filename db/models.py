from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey 

#create la clase de modelo(Entidad)

class Categoria(Base):
    __tablename__ = "categorias"
    id =  Column(Integer,
               primary_key=True,
               )

    nombre = Column (String(50))


class productos (Base):
    __tablename__ = "productos"
    Nombre = Column (String(40))
    Modelo = Column (String(60))
    Precio = Column (Integer)
    id = Column (Integer, 
                    primary_key=True)
    categorias_id = Column(Integer, ForeignKey ("categorias.id"))

 