# =========================================
# ETL - INGESTA UTF-8 CORRECTA
# =========================================

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://MELISA\\SQLEXPRESS/BI_Ciberseguridad?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# 🔥 IMPORTANTE: usar UTF-8
df = pd.read_csv(
    "data/incidentes_ciberseguridad_150k.csv",
    encoding="utf-8"
)

# fallback si falla (archivos latinos)
# df = pd.read_csv("data/incidentes_ciberseguridad_150k.csv", encoding="latin1")

df = df.fillna("")

df.to_sql(
    "stg_incidentes_raw",
    engine,
    if_exists="replace",
    index=False
)

print("✔ Datos cargados correctamente en UTF-8")