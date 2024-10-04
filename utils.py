# Validación del tipo de cuenta (Activo, Pasivo, etc.)
def validate_account_type(account_type):
    valid_types = ['Activo', 'Pasivo', 'Patrimonio', 'Ingresos', 'Gastos']
    if account_type not in valid_types:
        return False, f"Tipo de cuenta no válido. Debe ser uno de: {', '.join(valid_types)}"
    return True, "Tipo de cuenta válido"
