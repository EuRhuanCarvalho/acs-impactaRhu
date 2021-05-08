# 1 importar os módulos
import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# 2 Criar conexão com o BD SQLITE
engine = sqlalchemy.create_engine("sqlite:///serverexercico1.db")
connection = engine.connect()

# 3 Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()  # criando a sessão

# 4 Criar tabela no banco de dados:
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)
                    """)

# 5 Mapeando a tabela


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


'''
# INSERT dados na tabela
funcionario1 = Funcionario('Rhuan', 33, 10000)
session.add(funcionario1)
session.commit()


# inserindo multiplos dados
funcionario2 = Funcionario('Caroline', 30, 10000)
funcionario3 = Funcionario('Rafael', 22, 3000)
funcionario4 = Funcionario('Thais', 30, 10000)
funcionario5 = Funcionario('Samuel', 29, 6000)
lista = [funcionario2, funcionario3, funcionario4, funcionario5]
session.add_all(lista)
session.commit()
'''
# perguntando dados ao usuário (Mano! meu sonho!!!)
'''
lista = []
for dados in range(3):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    salario = float(input('Salario: '))
    funcionario = Funcionario(nome, idade, salario)
    lista.append(funcionario)

# inserindo na lista de objetos no banco
session.add_all(lista)
session.commit()
'''

# consultando dados na tabela
print('-'*30)
retorno = session.query(Funcionario).order_by(Funcionario.nome).all()
for funcionario in retorno:
    print(funcionario.id, funcionario.nome,
          funcionario.idade, funcionario.salario)

# consultando funcionários com salario acima de 6000
print('-'*30)
salario_acima = session.query(Funcionario).filter(Funcionario.salario >
                                                  6000).order_by(Funcionario.nome).all()
for salario in salario_acima:
    print(salario.id, salario.nome, salario.idade, salario.salario)

connection.close()
