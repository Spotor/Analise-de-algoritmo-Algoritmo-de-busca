import time

datasetA = open('resposta-dataset-a.csv', 'w')
datasetB = open('resposta-dataset-b.csv', 'w')
datasetC = open('resposta-dataset-c.csv', 'w')

def baseA():
    arqA = open('dataset-1-a.csv', 'r+')
    encontrarA = int(input("Inseira o número que deseja encontrar: "))
    linhaA = arqA.read()
    listaA = linhaA.split('\n')
    i = 0
    for a in listaA:
        if encontrarA == int(a):
            datasetA.write('True\n')
            datasetA.write(str(i) + '\n')
            return True
        i+= 1
    datasetA.write('False\n')
    datasetA.write('-1\n')
    arqA.close()

def baseB():
    arqB = open('dataset-1-b.csv', 'r+')
    encontrarB = int(input("Inseira o número que deseja encontrar: "))
    linhaB = arqB.read()
    listaB = linhaB.split('\n')
    b = 0
    for x in listaB:
        if encontrarB == int(x):
            datasetB.write('True\n')
            datasetB.write(str(b) + '\n')
            return True
        b+= 1
    datasetB.write('False\n')
    datasetB.write('-1\n')
    arqB.close()

def baseC():
    arqC = open('dataset-1-c.csv', 'r+')
    encontrarC = int(input("Inseira o número que deseja encontrar: "))
    linhaC = arqC.read()
    listaC = linhaC.split('\n')
    c = 0
    for z in listaC:
        if encontrarC == int(z):
            datasetC.write('True\n')
            datasetC.write(str(c) + '\n')
            return True
        c+= 1
    datasetC.write('False\n')
    datasetC.write('-1\n')
    arqC.close()

inicioA = time.time()
baseA()
fimA = time.time()
datasetA.write(str((fimA - inicioA)*1000))

inicioB = time.time()
baseB()
fimB = time.time()
datasetB.write(str((fimB - inicioB)*1000))

inicioC = time.time()
baseC()
fimC = time.time()
datasetC.write(str((fimC - inicioC)*1000))

datasetA.close()
datasetB.close()
datasetC.close()






