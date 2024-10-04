import os

# Credenciales y configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "user=postgres.squjfhvfoiuthahxyxyd password=[i02au4|9ff87Lzz#?JA.] host=aws-0-us-west-1.pooler.supabase.com port=6543 dbname=postgres")

# Configuraciones adicionales (si es necesario)
DEBUG_MODE = os.getenv("DEBUG_MODE", True)