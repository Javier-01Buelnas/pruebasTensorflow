#ejemplo con la libreria pandas
import pandas as pd

dataframe = pd.read_csv('calif.csv')
print (dataframe, '\n')

descripcion = dataframe.describe()
print (descripcion, '\n')

nombreColumna = dataframe['NOMBRE']
print (nombreColumna, '\n')

nombreEspecifico = dataframe['NOMBRE'][0]
print ('El nombre que eligio es: ', nombreEspecifico, '\n')

nomyAppColumnas = dataframe[['NOMBRE','MATERIA']]
print (nomyAppColumnas, '\n')

maxCalificacion = dataframe['CALIFICACION'] >=70
print (maxCalificacion, '\n')

filtro = dataframe['CALIFICACION'] >= 70
dataframe2 = dataframe[filtro]
print (dataframe2, '\n')


#transformar los datos del archivo .csv a un array
conversionArray = dataframe2.values
print (conversionArray, '\n')

elegirNombreArray = conversionArray[0,0]
print (elegirNombreArray)
