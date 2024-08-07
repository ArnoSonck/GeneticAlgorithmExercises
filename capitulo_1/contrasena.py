import random
import datetime

# Genes
geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!¡.,"
objetivo = "¡Hola Mundo!"

# Generando conjetura
def generar_padre(longitud):
    genes = []
    while len(genes) < longitud:
        tamanoMuestral = min(longitud-len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, tamanoMuestral))
    return ''.join(genes)

# Calculando Aptitud
def obtener_aptitud(conjetura):
    return sum(1 for esperado, real in zip(objetivo,conjetura) if esperado == real)

# Mutación
def mudar(padre):
    indice = random.randrange(0,len(padre))
    genesDelNino = list(padre)
    nuevoGen, alterno = random.sample(geneSet, 2)
    genesDelNino[indice] = alterno if nuevoGen == genesDelNino[indice] else nuevoGen
    return ''.join(genesDelNino)

# Visualización
def mostrar(conjetura):
    diferencia = (datetime.datetime.now()-horaInicio).total_seconds()
    aptitud = obtener_aptitud(conjetura)
    print("{}\t{}\t{}".format(conjetura, aptitud, diferencia))

# Programa principal
random.seed()
horaInicio = datetime.datetime.now()
mejorPadre = generar_padre(len(objetivo))
mejorAptitud = obtener_aptitud(mejorPadre)
mostrar(mejorPadre)

while True:
    nino = mudar(mejorPadre)
    ninoAptitud = obtener_aptitud(nino)
    if mejorAptitud >= ninoAptitud:
        continue
    mostrar(nino)
    if ninoAptitud >= len(mejorPadre) >= len(mejorPadre):
        break
    mejorAptitud = ninoAptitud
    mejorPadre = nino

