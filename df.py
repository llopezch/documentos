import pandas as pd

df=pd.read_excel("/home/user/lucho123/.vscode/documentos/Plantilla.xlsx")
df["Año"]=df["Fecha_envio"].dt.year.astype(str)
df["Mes"]=df["Fecha_envio"].dt.month

