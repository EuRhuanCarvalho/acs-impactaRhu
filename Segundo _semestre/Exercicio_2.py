import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine("sqlite:///serverexercicio2.db")
connection = engine.connect()

Base = declarative_base(engine)
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
                        ID INTEGER PRIMARY KEY,
                        NOME varchar(255) NOT NULL)
                    """)

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255) NOT NULL,
                        PAGINAS INT NOT NULL,
                        AUTOR_ID INT NOT NULL)

                    """)


class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor('Rhuan Carvalho')
autor2 = Autor('Caroline Oliveira')

lista = [autor1, autor2]
session.add_all(lista)
session.commit()

resultado = session.query(Autor)
for a in resultado:
    print(a.id, a.nome)


livro1 = Livro('Titulo do livro 1', 200, autor1.id)
livro2 = Livro('Titulo do livro 2', 1000, autor2.id)

session.add(livro1)
session.add(livro2)
session.commit()

resultado = session.query(Livro).order_by(Livro.titulo)
for r in resultado:
    print(r.id, r.titulo, r.paginas, r.autor_id)

# Fazendo um JOIN na consulta:

resultado = session.query(Autor, Livro).filter(Livro.autor_id == Autor.id)
for r in resultado:
    print(r.autor.nome, r.livro.titulo)
