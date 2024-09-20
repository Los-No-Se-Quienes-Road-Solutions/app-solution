"""
    Solution 1 
    Mauricio Abraham Rivo Rojas Sánchez - U202211572
"""
import heapq as hq

import application.extensions.unionfind as unionfind

def kruskal(G,id):
    aristas = []
    resultado = []
    for arista in G:
        costo,nodo,vecino = arista
        hq.heappush(aristas,(costo,nodo,vecino))

    while len(aristas):
        costo,u,v = hq.heappop(aristas)
        pu = unionfind.find(id,u)
        pv = unionfind.find(id,v)
        if pu != pv:
            resultado.append((costo,u,v))
            unionfind.union(id,pu,pv)
    return resultado

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from application.services.read import leerDataSet,leerArchivo
    from application.services.generateGraph import generateGraph
    centrosPoblados = leerDataSet("dataset.csv",1)

    tipoMuestra = {
        'RESTANTES':0,
        'DEPARTAMENTALES':1,
        'PROVINCIALES':2,
        'DISTRITALES':3
    }

    muestra = [] #lista centros poblados
    id = {}
    for cep in centrosPoblados:
        if cep.capital == tipoMuestra['DEPARTAMENTALES']: #es capital departamental
            id[cep.codigo] = cep.codigo
            muestra.append(cep)
    G = generateGraph(muestra)
    arbolExpMin = kruskal(G,id)
    print(arbolExpMin)
    #Config mapa
    plt.figure(figsize=(15,5))
    plt.title("Mapa")
    plt.xlabel("Coord X")
    plt.ylabel("Coord Y")
    #Pintando mapa
    x = []
    y = []
    for cep in centrosPoblados:
        x.append(cep.coordX)
        y.append(cep.coordY)
    plt.plot(x,y,'ro')
    def searchLocation(codigo):
        for cep in centrosPoblados:
            if cep.codigo == codigo:
                return cep


    def drawEdges(aristas,color):
        for arista in aristas:
            _,origen,destino = arista
            o = searchLocation(origen)
            d = searchLocation(destino)
            x = [o.coordX,d.coordX]
            y = [o.coordY,d.coordY]
            plt.plot(x, y, color=color, marker="8", markeredgecolor="black")
    
    #Pintar grafo
    drawEdges(G,"blue")
    #Pintar arbol de expansion minima
    drawEdges(arbolExpMin,"white")
    plt.show()