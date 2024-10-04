import streamlit as st
from transaction import create_transaction, get_account_balance
from database import session, Account
from utils import validate_account_type

# Página principal
st.title('Contabilidad Personal')

# Crear una nueva cuenta contable
st.header('Crear Cuenta Contable')
account_name = st.text_input('Nombre de la cuenta')
account_type = st.selectbox('Tipo de cuenta', ['Activo', 'Pasivo', 'Patrimonio', 'Ingresos', 'Gastos'])

if st.button('Crear Cuenta'):
    is_valid, msg = validate_account_type(account_type)
    if is_valid:
        new_account = Account(account_name=account_name, account_type=account_type)
        session.add(new_account)
        session.commit()
        st.success(f'Cuenta {account_name} creada con éxito')
    else:
        st.error(msg)

# Registrar una nueva transacción
st.header('Registrar Transacción')
debit_account_id = st.number_input('ID Cuenta Débito', min_value=1)
credit_account_id = st.number_input('ID Cuenta Crédito', min_value=1)
amount = st.number_input('Monto de la transacción', min_value=0.0)
description = st.text_area('Descripción de la transacción')

if st.button('Registrar Transacción'):
    success, message = create_transaction(debit_account_id, credit_account_id, amount, description)
    if success:
        st.success(message)
    else:
        st.error(message)

# Ver el balance de una cuenta
st.header('Consultar Balance de Cuenta')
account_id = st.number_input('ID de la Cuenta', min_value=1)
if st.button('Consultar Balance'):
    balance = get_account_balance(account_id)
    if balance is not None:
        st.write(f'El balance de la cuenta {account_id} es {balance}')
    else:
        st.error('Cuenta no encontrada')
