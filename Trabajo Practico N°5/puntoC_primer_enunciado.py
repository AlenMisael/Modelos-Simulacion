import numpy as np
import statistics
import math
import matplotlib.pyplot as plt


EXPERIMENTOS = 30
CORRIDAS = 100

Z = 2.57

listaAccesoSuperior = []
listaAccesoMedio = []
listaAccesoInferior = []
frecuencias = [0,0,0]

acceso_superior = {
    'romper_huevos': (2,4), 
    'revolver_huevos': (3,6), 
    'cocinar_huevos': (2,5)
}
acceso_medio = {
    'cortar_panes':(3,6), 
    'preparar_tostadas': (2,5)
}
acceso_inferior = {
    'preparar_bebidas_calientes': (4,8),
    'preparar_bebidas_frias': (3,7)
}

def obtener_extremos(muestra,z, cantidad, cant_desvios=1): 
    media = statistics.mean(muestra)
    desvio_estandar = (statistics.stdev(muestra))*cant_desvios
    extremo_inferior = (media - z*(desvio_estandar/math.sqrt(cantidad)))  
    extremo_superior = (media + z*(desvio_estandar/math.sqrt(cantidad))) 

    print ("La muestra poblacional tiene el extremo inferior: " + str(extremo_inferior) + " y el extremo superior: " + 
           str(extremo_superior))
    

def calculoAccesoSuperior(rango_superior): 
    tarea1 = np.random.uniform(rango_superior['romper_huevos'][0],rango_superior['romper_huevos'][1])
    tarea2 = np.random.uniform(rango_superior['revolver_huevos'][0], rango_superior['revolver_huevos'][1])
    tarea3 = np.random.uniform(rango_superior['cocinar_huevos'][0], rango_superior['cocinar_huevos'][1])
    return tarea1 + tarea2 + tarea3    

def calculoAccesoMedio(rango_medio): 
    tarea1 = np.random.uniform(rango_medio['cortar_panes'][0], rango_medio['cortar_panes'][1])
    tarea2 = np.random.uniform(rango_medio['preparar_tostadas'][0], rango_medio['preparar_tostadas'][1])
    return tarea1 + tarea2

def calculoAccesoInferior(rango_inferior):
    tarea1 = np.random.uniform(rango_inferior['preparar_bebidas_calientes'][0], rango_inferior['preparar_bebidas_calientes'][1])
    tarea2 = np.random.uniform(rango_inferior['preparar_bebidas_frias'][0], rango_inferior['preparar_bebidas_frias'][1])
    return tarea1 + tarea2




def obtenerPromedioTiempos(rango_superior, rango_medio, rango_inferior): 
    acceso_superior = calculoAccesoSuperior(rango_superior)
    listaAccesoSuperior.append(acceso_superior)
    acceso_medio = calculoAccesoMedio(rango_medio)
    listaAccesoMedio.append(acceso_medio)
    acceso_inferior = calculoAccesoInferior(rango_inferior)
    listaAccesoInferior.append(acceso_inferior)
    accesos = [ acceso_inferior, acceso_medio, acceso_superior]
    indice = accesos.index(max(accesos))
    frecuencias[indice] += 1 
    return max(acceso_superior, acceso_medio, acceso_inferior)
   

def obtener_acceso_mas_critico():
    print(f"Frecuencia acceso superior: {frecuencias[0]}")
    print(f"Frecuencia acceso medio: {frecuencias[1]}")
    print(f"Frecuencia acceso inferior: {frecuencias[2]}")

    porcentajeA = (frecuencias[0]/(EXPERIMENTOS * CORRIDAS)) * 100
    porcentajeB = (frecuencias[1]/ (EXPERIMENTOS * CORRIDAS)) * 100
    porcentajeC = (frecuencias[2] / (EXPERIMENTOS * CORRIDAS)) * 100
    print (f"Porcentaje A: {porcentajeA:.2f} %")
    print (f"Porcentaje B: {porcentajeB:.2f} %")
    print (f"Porcentaje C: {porcentajeC:.2f} %")
    if (porcentajeA > porcentajeB) and (porcentajeA > porcentajeC): 
        acceso_critico = "Acceso Superior"
        porcentaje_critico = porcentajeA
    else: 
        if (porcentajeB > porcentajeA) and (porcentajeB > porcentajeC): 
            acceso_critico = "Acceso Medio"
            porcentaje_critico = porcentajeB
        else: 
            acceso_critico = "Acceso Inferior"
            porcentaje_critico = porcentajeC
    return acceso_critico, porcentaje_critico


def realizarHistograma(corridas, experimentos):
    plt.subplot(221) #Grafico en la posicion inferior derecha
    plt.hist(corridas, alpha=0.7,color="green", edgecolor="black")
    plt.xlabel("Tiempos de finalizacion (minutos)")   
    plt.ylabel("Frecuencia")
    plt.title("Distribucion de los tiempos de las 3000 corridas")

    plt.subplot(222)
    plt.hist(experimentos, alpha=0.7,color="yellow", edgecolor="black")
    plt.xlabel("Tiempos de finalizacion (minutos)")
    plt.ylabel("Frecuencia")
    plt.title("Distribucion de los tiempos promedios de los 30 experimentos")
    plt.show()


def realizarExperimentos(rango_superior, rango_medio, rango_inferior):
    lista_experimento = []
    for experimento in range(EXPERIMENTOS): 
        lista_corrida = []
        for corrida in range(CORRIDAS): 
            tiempo_total = obtenerPromedioTiempos(rango_superior, rango_medio, rango_inferior)
            lista_corrida.append(tiempo_total)
        lista_experimento.append(np.mean(lista_corrida))

    tiempo_prom_finalizacion = round(np.mean(lista_experimento))
   
   
    acceso_critico, porcentaje_critico = obtener_acceso_mas_critico()
    print("El tiempo promedio de finalizacion del proyecto es de: " + str(tiempo_prom_finalizacion) + " minutos ")
    obtener_extremos(lista_experimento,Z,len(lista_experimento))

    print (f"El acceso mas critico es el {acceso_critico} con un porcentaje de {porcentaje_critico:.2f} % del tiempo total")
    realizarHistograma(lista_corrida, lista_experimento)


realizarExperimentos(acceso_superior, acceso_medio, acceso_inferior)