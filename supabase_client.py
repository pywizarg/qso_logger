from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

# Cargar URL y clave de Supabase desde el archivo .env
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Crear cliente de Supabase
supabase = create_client(url, key)

# Función para obtener las bandas (esto es solo un ejemplo)
def get_bands():
    return supabase.table("bands").select("*").execute()

# Función para obtener modos
def get_modes():
    return supabase.table("modes").select("*").execute()

# Función para obtener países
def get_countries():
    return supabase.table("countries").select("*").execute()
