"""
    Esta función recibe como argumento una lista de objetos de clase models.CentroPoblado
    y retorna una lista con tuplas de tres elementos (distancia,verticeOrigen,verticeDestino)
    las cuales representan las aristas de un grafo.
"""
import random
from calculateRange import calculateRange

def generateGraph(centrosPoblados):
    grafo = []
    
    for cep in centrosPoblados:
        copia = centrosPoblados[:] # genera una copia de todos los centros poblados
        copia.remove(cep) #removemos el cep seleccionado para no generar un camino al mismo punto
        destinosPorCep = random.randint(3,5) # seleccionamos entre 3 y 5 destinos por cada centro poblado
        for _ in range(destinosPorCep):
            destino = random.choice(copia) #seleccionamos un destino al azar
            copia.remove(destino) #removemos el destino para que no se repita
            #Generamos una nueva arista
            distancia = calculateRange(cep,destino)
            arista = (distancia,cep.codigo,destino.codigo)
            grafo.append(arista)
    return grafo

if __name__ == "__main__":
    from application.services.read import leerDataSet
    centrosPoblados = leerDataSet("dataset.csv",1,50)
    grafo = generateGraph(centrosPoblados)
    print(grafo)
