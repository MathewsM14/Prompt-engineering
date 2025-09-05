import pandas as pd
import glob
import os

# Ruta relativa a la carpeta con los excels
carpeta = os.path.join("synthetic_data")

# Buscar todos los archivos .xlsx en la carpeta
archivos = glob.glob(os.path.join(carpeta, "*.xlsx"))

# Leer y guardar todos los dataframes
dataframes = [pd.read_excel(archivo) for archivo in archivos]

# Unirlos en un solo DataFrame
df_final = pd.concat(dataframes, ignore_index=True)

# Guardar el archivo combinado en la misma carpeta
salida = os.path.join(carpeta, "resultado_final.xlsx")
df_final.to_excel(salida, index=False)

print(f"Archivo combinado guardado en: {salida}")



