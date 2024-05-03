import numpy as np
import statistics
import math
import matplotlib.pyplot as plt


EXPERIMENTOS = 30
CORRIDAS = 100

Z = 2.57

listaPrepararTerreno = []
listaConstruirBases = []
listaCañeriaCloacas = []
listaLevantarParedes = []
listaConstruirTecho = []
listaInsElectrica = []
listaInsGas = []
listaColocarAberturas = []
listaColocarPisos = []
listaPintarCasa = []
frecuencias = [0 for _ in range(10)]

def obtener_extremos(muestra,z, cantidad, cant_desvios=1): 
    media = statistics.mean(muestra)
    desvio_estandar = (statistics.stdev(muestra))*cant_desvios
    extremo_inferior = (media - z*(desvio_estandar/math.sqrt(cantidad)))  
    extremo_superior = (media + z*(desvio_estandar/math.sqrt(cantidad))) 

    print ("La muestra poblacional tiene el extremo inferior: " + str(extremo_inferior) + " y el extremo superior: " + 
           str(extremo_superior))
    



def obtenerTiempos(): 
    preparar_terreno = np.random.uniform(2,4)
    listaPrepararTerreno.append(preparar_terreno)
    construir_bases = np.random.uniform(3,5)
    listaConstruirBases.append(construir_bases)
    cañeria_cloacas = np.random.uniform(1,2)
    listaCañeriaCloacas.append(cañeria_cloacas)
    levantar_paredes = np.random.uniform(4,8)
    listaLevantarParedes.append(levantar_paredes)
    aberturas = np.random.uniform(1,3)
    listaColocarAberturas.append(aberturas)
    construir_techo = np.random.uniform(3,6)
    
    camino1 = cañeria_cloacas + levantar_paredes + construir_techo
    camino2 = cañeria_cloacas + aberturas + construir_techo

    listaConstruirTecho.append(construir_techo)
    instalacion_electrica = np.random.uniform(2,5)
    listaInsElectrica.append(instalacion_electrica)
    instalacion_gas = np.random.uniform(2,4)
    listaInsGas.append(instalacion_gas)
    pisos = np.random.uniform(2,4)

    camino3 = construir_techo + instalacion_electrica + pisos
    camino4 = construir_techo + instalacion_gas + pisos

    listaColocarPisos.append(pisos)
    pintar_casa = np.random.uniform(2,3)
    listaPintarCasa.append(pintar_casa)

    tareas = [preparar_terreno, construir_bases, cañeria_cloacas, levantar_paredes, 
              aberturas, construir_techo, instalacion_electrica, instalacion_gas, pisos, pintar_casa]
    indice = tareas.index(max(tareas))
    frecuencias[indice] += 1
    suma = (preparar_terreno + construir_bases + max(camino1,camino2)  + max(camino3, camino4) + pintar_casa)
    return suma
   

def obtener_tarea_mas_critica():
    porcentaje_preparar_terreno = (frecuencias[0]/(EXPERIMENTOS * CORRIDAS)) * 100
    porcentaje_bases = (frecuencias[1] / (EXPERIMENTOS * CORRIDAS)) * 100
    porcentaje_cañeria = ( frecuencias[2]/ (EXPERIMENTOS * CORRIDAS)) * 100
    porcentaje_paredes= (frecuencias[3]/(EXPERIMENTOS * CORRIDAS)) * 100 
    porcentaje_techo= (frecuencias[4]/(EXPERIMENTOS * CORRIDAS)) * 100 
    porcentaje_insElectrica= (frecuencias[5]/(EXPERIMENTOS * CORRIDAS)) * 100 
    porcentaje_insGas=(frecuencias[6]/(EXPERIMENTOS * CORRIDAS)) * 100 
    porcentaje_aberturas= (frecuencias[7]/(EXPERIMENTOS * CORRIDAS)) * 100 
    porcentaje_pisos= (frecuencias[8]/(EXPERIMENTOS * CORRIDAS)) * 100 
    porcentaje_pintar_casa= (frecuencias[9]/(EXPERIMENTOS * CORRIDAS)) * 100

    print (f"Frecuencia preparar terreno: {frecuencias[0]}")
    print (f"Frecuencia bases: {frecuencias[1]}")
    print (f"Frecuencia cañeria: {frecuencias[2]}")
    print (f"Frecuencia levantar paredes: {frecuencias[3]}")
    print (f"Frecuencia techo: {frecuencias[4]}")
    print (f"Frecuencia instalacion electrica: {frecuencias[5]}")
    print (f"Frecuencia instalacion gas: {frecuencias[6]}")
    print (f"Frecuencia abertura: {frecuencias[7]}")
    print (f"Frecuencia pisos: {frecuencias[8]}")
    print (f"Frecuencia pintar casa: {frecuencias[9]}")

    print (f"Porcentaje al preparar terreno: {porcentaje_preparar_terreno:.2f} %")
    print (f"Porcentaje al construir bases: {porcentaje_bases:.2f} %")
    print (f"Porcentaje en cañeria: {porcentaje_cañeria:.2f} %")
    print (f"Porcentaje en paredes: {porcentaje_paredes:.2f} %")
    print (f"Porcentaje en techo: {porcentaje_techo:.2f} %")
    print (f"Porcentaje en instalacion electrica: {porcentaje_insElectrica:.2f} %")
    print (f"Porcentaje en instalacion de gas: {porcentaje_insGas:.2f} %")
    print (f"Porcentaje en aberturas: {porcentaje_aberturas:.2f} %")
    print (f"Porcentaje en pisos: {porcentaje_pisos:.2f} %")
    print (f"Porcentaje al pintar la casa: {porcentaje_pintar_casa:.2f} %")

    porcentajes = {
        "Preparar el terreno": porcentaje_preparar_terreno,
        "Construir las bases": porcentaje_bases, 
        "Preparar la cañeria de cloacas": porcentaje_cañeria, 
        "Levantar las paredes": porcentaje_paredes, 
        "Construir el techo": porcentaje_techo, 
        "Instalacion Electrica": porcentaje_insElectrica,
        "Instalacion de gas": porcentaje_insGas, 
        "Colocar aberturas": porcentaje_aberturas,
        "Colocar los pisos": porcentaje_pisos,
        "Pintar la casa": porcentaje_pintar_casa,
    }

    tarea_critica = max(porcentajes, key= porcentajes.get)
    porcentaje_critico = porcentajes[tarea_critica]

    return tarea_critica, porcentaje_critico



def realizarHistograma(corridas, experimentos):
    plt.subplot(221) #Grafico en la posicion inferior derecha
    plt.hist(corridas, alpha=0.7,color="green", edgecolor="black")
    plt.xlabel("Tiempo de finalizacion (dias)")   
    plt.ylabel("Frecuencia")
    plt.title("Distribucion de los tiempos de las 3000 corridas")

    plt.subplot(222)
    plt.hist(experimentos, alpha=0.7,color="yellow", edgecolor="black")
    plt.xlabel("Tiempo de finalizacion (dias)")
    plt.ylabel("Frecuencia")
    plt.title("Distribucion de los tiempos promedios de los 30 experimentos")
    plt.show()


def realizarExperimentos():
    
    lista_experimento = []
    for experimento in range(EXPERIMENTOS): 
        lista_corrida = []
        for corrida in range(CORRIDAS): 
            tiempo_total = obtenerTiempos()
            lista_corrida.append(tiempo_total)
        lista_experimento.append(np.mean(lista_corrida))
    tiempo_prom_finalizacion = round(np.mean(lista_experimento))
    print("El tiempo promedio de finalizacion del proyecto es de: " + str(tiempo_prom_finalizacion) + " dias ")
    obtener_extremos(lista_experimento,Z,len(lista_experimento))

    tarea_critica, porcentaje_critico = obtener_tarea_mas_critica()
    print (f"La tarea mas critica es {tarea_critica} con un porcentaje de {porcentaje_critico:.2f} % del tiempo total")
    realizarHistograma(lista_corrida, lista_experimento)


realizarExperimentos()