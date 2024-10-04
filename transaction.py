from database import session, Account, Transaction
from sqlalchemy.exc import SQLAlchemyError

# Función para crear una transacción
def create_transaction(date_id,debit_account_id, credit_account_id, amount, description=None):
    try:
        # Crear la nueva transacción
        transaction = Transaction(
            transaction_date = date_id,
            debit_account_id=debit_account_id,
            credit_account_id=credit_account_id,
            amount=amount,
            description=description
        )
        session.add(transaction)

        # Actualizar saldos de las cuentas involucradas
        '''debit_account = session.query(Account).get(debit_account_id)
        credit_account = session.query(Account).get(credit_account_id)

        if debit_account and credit_account:
            debit_account.balance -= amount
            credit_account.balance += amount
        else:
            raise Exception("Una de las cuentas no existe.")'''

        session.commit()
        return True, "Transacción registrada con éxito"
    
    except SQLAlchemyError as e:
        session.rollback()
        return False, f"Error en la transacción: {e}"

# Función para obtener el balance de una cuenta
def get_account_balance(account_id):
    try:
        account = session.query(Account).get(account_id)
        if account:
            return account.balance
        else:
            return None
    except SQLAlchemyError as e:
        return f"Error al obtener el balance: {e}"
