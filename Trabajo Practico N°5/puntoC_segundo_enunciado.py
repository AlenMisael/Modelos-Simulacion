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

def obtener_extremos(muestra,z, cantidad, cant_desvios=1): 
    media = statistics.mean(muestra)
    desvio_estandar = (statistics.stdev(muestra))*cant_desvios
    extremo_inferior = (media - z*(desvio_estandar/math.sqrt(cantidad)))  
    extremo_superior = (media + z*(desvio_estandar/math.sqrt(cantidad))) 

    print ("La muestra poblacional tiene el extremo inferior: " + str(extremo_inferior) + " y el extremo superior: " + 
           str(extremo_superior))
    

def calculoAccesoSuperior(): 
    retirar_alfombras = np.random.uniform(1,5)
    aplicar_detergente = np.random.uniform(1,3)
    enjuagar_alfombras = np.random.uniform(1,3)
    return retirar_alfombras + aplicar_detergente + enjuagar_alfombras    

def calculoAccesoMedio(): 
    mojar_vehiculo = np.random.uniform(1,6)
    aplicar_detergente = np.random.uniform(6,12)
    enjuagar_vehiculo = np.random.uniform(5,10)
    return mojar_vehiculo + aplicar_detergente + enjuagar_vehiculo

def calculoAccesoInferior():
    aspirar_interiores = np.random.uniform(10,15)
    return aspirar_interiores




def obtenerPromedioTiempos(): 
    acceso_superior = calculoAccesoSuperior()
    listaAccesoSuperior.append(acceso_superior)
    acceso_medio = calculoAccesoMedio()
    listaAccesoMedio.append(acceso_medio)
    acceso_inferior = calculoAccesoInferior()
    listaAccesoInferior.append(acceso_inferior)
    accesos = [acceso_superior, acceso_medio, acceso_inferior]
    indice = accesos.index(max(accesos))
    frecuencias[indice] += 1
    return max(acceso_superior, acceso_medio, acceso_inferior)
   

def obtener_acceso_mas_critico():
    porcentajeA = (frecuencias[0]/(EXPERIMENTOS * CORRIDAS)) * 100
    porcentajeB = ( frecuencias[1]/ (EXPERIMENTOS * CORRIDAS)) * 100
    porcentajeC = (frecuencias[2] / (EXPERIMENTOS * CORRIDAS)) * 100
    print (f"Frecuencia acceso superior: {frecuencias[0]}")
    print (f"Frecuencia acceso medio: {frecuencias[1]}")
    print (f"Frecuencia acceso inferior: {frecuencias[2]}")

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
    plt.hist(corridas,alpha=0.7,color="green", edgecolor="black")
    plt.xlabel("Tiempo de finalizacion (minutos)")   
    plt.ylabel("Frecuencia")
    plt.title("Distribucion de los tiempos de las 3000 corridas")

    plt.subplot(222)
    plt.hist(experimentos, alpha=0.7,color="yellow", edgecolor="black")
    plt.xlabel("Tiempo de finalizacion (minutos)")
    plt.ylabel("Frecuencia")
    plt.title("Distribucion de los tiempos promedios de los 30 experimentos")
    plt.show()


def realizarExperimentos():
    
    lista_experimento = []
    for experimento in range(EXPERIMENTOS): 
        lista_corrida = []
        for corrida in range(CORRIDAS): 
            tiempo_total = obtenerPromedioTiempos()
            lista_corrida.append(tiempo_total)
        lista_experimento.append(np.mean(lista_corrida))
  

    tiempo_prom_finalizacion = (np.mean(lista_experimento))
    tiempo_prom_accesoSuperior = round(np.mean(listaAccesoSuperior))
    tiempo_prom_medio = round(np.mean(listaAccesoMedio))
    tiempo_prom_accesoInferior= round(np.mean(listaAccesoInferior))
    print (f"Tiempo promedio del acceso superior: {tiempo_prom_accesoSuperior} minutos")
    print (f"Tiempo promedio del acceso medio: {tiempo_prom_medio} minutos")
    print (f"Tiempo promedio del acceso inferior: {tiempo_prom_accesoInferior} minutos")
   
    acceso_critico, porcentaje_critico = obtener_acceso_mas_critico()
    print("El tiempo promedio de finalizacion del proyecto es de: " + str(tiempo_prom_finalizacion) + " minutos ")
    obtener_extremos(lista_experimento,Z,len(lista_experimento))

    print (f"El acceso mas critico es el {acceso_critico} con un porcentaje de {porcentaje_critico:.2f} % del tiempo total")
    realizarHistograma(lista_corrida, lista_experimento)


realizarExperimentos()