import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
  
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column (String(250), nullable=False)
    email = Column(String(90), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    favoritos = relationship('Favoritos',backref='personajes', lazy=True)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    gender =  Column(String(250), nullable=False)
    hair_color =  Column(String(250), nullable=False)
    Favoritos= relationship("favoritos", backref="personajes", lazy=True)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    orbital_period =  Column(String(250), nullable=False)
    population =  Column(String(250), nullable=False)
    Favoritos = relationship("favoritos", backref="planetas", lazy=True)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cargo_capacity =  Column(String(250), nullable=False)
    length =  Column(String(250), nullable=False)
    model =  Column(String(250), nullable=False)
    favoritos= relationship("favoritos", backref="vehiculos", lazy=True)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id =Column(Integer, ForeignKey('usuario.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    Vehiculos_id = Column(Integer, ForeignKey("vehiculos.id"))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
