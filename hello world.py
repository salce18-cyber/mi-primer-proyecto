# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:54:56 2026

@author: AA-u243
"""

import os
from dotenv import load_dotenv

# 1. Obtener la ruta exacta de la carpeta donde está guardado este script
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_al_env = os.path.join(directorio_actual, '.env')

# 2. Cargar el archivo .env usando su ruta absoluta
load_dotenv(dotenv_path=ruta_al_env)

# 3. Leer las variables de entorno de forma segura
servidor = os.getenv('DB_HOST')
usuario = os.getenv('DB_USER')
token = os.getenv('API_KEY')

# 4. Probar que funcionó simulando la conexión
print("--- SIMULACIÓN DE CONEXIÓN ---")
if servidor and usuario and token:
    print(f"✅ Éxito: Conectando a la base de datos en '{servidor}'")
    print(f"👤 Usuario autenticado: '{usuario}'")
    print(f"🔑 Clave API validada correctamente: [{token[:3]}...{token[-3:]}]") # Oculta parte del token por seguridad
else:
    print("❌ Error: No se pudieron leer las variables. Revisa que tu archivo '.env' esté al lado de este script.")
print("------------------------------")