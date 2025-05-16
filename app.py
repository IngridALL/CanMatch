import os
from dotenv import load_dotenv

env = os.getenv("APP_ENV", "dev")

if env == "dev":
    load_dotenv(".env.dev")
elif env == "staging":
    load_dotenv(".env.staging")
else:
    load_dotenv(".env.prod")

print(f"Hola mundo desde el entorno de {env}")




