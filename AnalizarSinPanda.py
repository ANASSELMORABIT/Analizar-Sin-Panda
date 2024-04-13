# Es tracta d'aconseguir implementar en Python pur, sense usar la llibreria pandas, la consulta 10 de l'AC13:

# df.query("Curs == '2022/2023'").query("`Codi estudis`=='FP'").groupby("Temàtica")["Matrícules. Total"].sum()

# Entregar exercici en un fitxer .py
import os
def readCSV(rutaCSV):
    with open(rutaCSV,'r',encoding="utf-8") as archivo:
        dataset=[]
        lines =  archivo.readlines()
        for line in lines:
            fila = line.split(',')
            dataset.append(fila)
        return dataset
# print(len(readCSV('./recursos/Alumnes_matriculats_per_ensenyament_i_unitats_dels_centres_docents_20240322.csv')[0]))
# print(readCSV('./recursos/Alumnes_matriculats_per_ensenyament_i_unitats_dels_centres_docents_20240322.csv')[1])
def limpiarColumnas(dataset):
    titulos=dataset[0]
    numColumnas=len(titulos)
    titulosLimpios=[titulos[i] for i in (0,1,2,23,numColumnas-5,numColumnas-4,numColumnas-3)]
    datasetLimpio=[]
    datasetLimpio.append(titulosLimpios)
    for i in range(1,len(dataset)):
        datasetLimpio.append([dataset[i][j] for j in (0,1,2,23,numColumnas-5,numColumnas-4,numColumnas-3)])
    return datasetLimpio
def head(datasetLimpio,numFilas):
    titulosImprimer=datasetLimpio[0]
    print(131*'-')
    print('| {:^9} | {:4} | {:11} | {:60} | {:20} | {:20} | {:20} |'.format(*titulosImprimer))
    print(131*'-')
    for fila in datasetLimpio[1:numFilas+1]:
        print('| {:^9} | {:4} | {:11} | {:60} | {:20} | {:20} | {:20} |'.format(*fila))
        (print())
    print(131*'-')
def tail(datasetLimpio,numFilas):
    # Esta función simula el método DataFrame.tail() de pandas, printando las nºimas
    # filas del dataset
    titulosImprimer=datasetLimpio[0]
    print(131*'-')
    print('| {:^9} | {:4} | {:11} | {:60} | {:20} | {:20} | {:20} |'.format(*titulosImprimer))
    print(131*'-')
    for fila in datasetLimpio[len(datasetLimpio)-numFilas:len(datasetLimpio)]:
        print('| {:^9} | {:4} | {:11} | {:60} | {:20} | {:20} | {:20} |'.format(*fila))
        (print())
    print(131*'-')

def shape(dataset): #Este Funcion es similar a la función shape de pandas
    print(f"[{len(dataset)-1} rows x  {len(dataset[0])} columnas]")
def query(dataset,nombreColumna,valorColumna):
    # Esta función debe devolver solo las filas del dataset recibido como parámetro para las
    # que se cumpla que tienen su columna "nombreColumna" igual a "valorColumna". Simulará
    # una query de pandas de sintaxis básica (i.e .query("`nombreColumna`== valorColumna'"))
    numColumna = dataset[0].index(nombreColumna)
    queryResult = []
    queryResult.append(dataset[0])
    for fila in dataset:
        if fila[numColumna] == valorColumna:
            queryResult.append(fila)
    return queryResult
def Unique(dataset,nombreColumna): #Esta función es similar a la función unique de pandas
    numColumna = dataset[0].index(nombreColumna)
    Unicos=[]
    for i in range(1,len(dataset)):
        if dataset[i][numColumna] not in Unicos:
            Unicos.append(dataset[i][numColumna])
    return Unicos


def SumarColumna(dataset,nombreColumna): #Esta función es similar a la función sum de pandas
    numColumna = dataset[0].index(nombreColumna)
    Suma=0
    for i in range(1,len(dataset)):
        if dataset[i][numColumna] != None and dataset[i][numColumna] != '':
            Suma+=int(dataset[i][numColumna])
    return Suma

def SeleccionarColumna(dataset,nombreColumna): #Esta función es similar a la función mostre de pandas
    numColumna = dataset[0].index(nombreColumna)
    Columna=[]
    for i in range(1,len(dataset)):
        Columna.append(dataset[i][numColumna])
    return Columna
def MostrarColumna(dataset,nombreColumna): #Esta función es similar a la función mostre de pandas
    Columna=SeleccionarColumna(dataset,nombreColumna)
    print("|",nombreColumna,"|")
    print(131*'-')
    for i in range(0,len(Columna)):
        print("|",Columna[i],"|")
        (print())
    print(131*'-')
def PromedioColumna(dataset,nombreColumna): #Esta función es similar a la función mean de pandas
    numColumna = dataset[0].index(nombreColumna)
    Suma=0
    Cuenta=0
    for i in range(1,len(dataset)):
        Suma+=float(dataset[i][numColumna])
        Cuenta+=1
    Promedio=Suma/Cuenta
    return Promedio
def MosstrarFila(dataset,numFila): #Esta función es similar a la función mostre de pandas
    Titulo=dataset[0]
    print(131*'-')
    print('| {:^9} | {:4} | {:11} | {:60} | {:20} | {:20} | {:20} |'.format(*Titulo))
    print(131*'-')
    print('| {:^9} | {:4} | {:11} | {:60} | {:20} | {:20} | {:20} |'.format(*dataset[numFila]))
    print(131*'-')
    return None
def groupBy(dataset,nombreColumna): #Esta función es similar a la función de groupe by de panda
    # ColumnasGroupeadas=SeleccionarColumna(dataset,nombreColumna)
    Unicos=Unique(dataset,nombreColumna)
    DataAgroupadas=[]
    numeroColumna=dataset[0].index(nombreColumna)
    for grupo in Unicos[1:]:
        if grupo !="Temàtica":
            DatasGrupos={
                "Grupo":grupo,
                "Filas":list()
            }
            DatasGrupos['Filas'].append(dataset[0])
            for j in range(1,len(dataset)):
                if dataset[j][numeroColumna]==grupo:
                    DatasGrupos["Filas"].append(dataset[j])
            DataAgroupadas.append(DatasGrupos)
    return tuple(DataAgroupadas) # Este funcion devuelve una Tupla de diccionarios con los datos agrupados  por la columna indicada
def MostrarResulta():
    dataSet=readCSV("./recursos/Alumnes_matriculats_per_ensenyament_i_unitats_dels_centres_docents_20240322.csv")
    datasetLimpios=limpiarColumnas(dataSet)
    print("head(datasetLimpios,10)")
    head(datasetLimpios,10)
    print("tail(datasetLimpios,10)")
    tail(datasetLimpios,10)
    print("shape(datasetLimpios)")
    shape(datasetLimpios)
    DatosqueryCurs=query(dataSet,"Curs","2022/2023")
    Datosquery=query(DatosqueryCurs,"Codi estudis","FP")
    print("head(Datosquery,10)")
    head(Datosquery,10)
    print("tail(Datosquery,10)")
    tail(Datosquery,10)
    groupos=groupBy(Datosquery,"Temàtica")
    data=[]
    for grupo in groupos:
        try:
            Columna=SeleccionarColumna(grupo["Filas"],"Matrícules. Total")
            TotalColumna=sum((map(int,Columna[1:])))
            data.append([grupo["Grupo"],TotalColumna])
            print("El grupo: ",grupo["Grupo"]," tiene un total de: ",TotalColumna)
        except  Exception as e:
            print("El grupo: ",grupo["Grupo"]," tiene datos inválidos.")
    return data
            




MostrarResulta()




    




    
