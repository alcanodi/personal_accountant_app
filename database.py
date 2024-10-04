import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import declarative_base, sessionmaker

# Cargar las configuraciones
from config import DATABASE_URL

# Configuración de la base de datos
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Modelo base para las tablas
Base = declarative_base()

# Definición de la tabla 'accounts' para las cuentas contables
class Account(Base):
    __tablename__ = 'accounts'
    account_id = Column(Integer, primary_key=True)
    account_name = Column(String(255), nullable=False)
    account_type = Column(String(50), nullable=False)  # Activo, Pasivo, Patrimonio, Ingresos, Gastos
    balance = Column(DECIMAL(10, 2), default=0)

# Definición de la tabla 'transactions' para las transacciones
class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True)
    transaction_date = Column(Date, nullable=False)
    description = Column(String, nullable=True)
    debit_account_id = Column(Integer, ForeignKey('accounts.account_id'))
    credit_account_id = Column(Integer, ForeignKey('accounts.account_id'))
    amount = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, default="NOW()")

# Crear las tablas si no existen
Base.metadata.create_all(engine)
