import seaborn as sns #!pip install seaborn en la consola

#Seaborn trae algunos datasets de prueba, exploremos uno:
from seaborn import load_dataset
tips = load_dataset("tips")
tips.head()

tips.describe()

#Veamos los tipos de datos
tips.dtypes

#Funcion info()
tips.info()

#Tipos de objeto
type(tips)

#Dimensiones
print(tips.shape)

#Obtener la totalidad de registros por columnas
tips.count()

#Listar los nombres de las columnas
print(tips.columns)
