def calculartime(lista):
    minitimp = 100
    for ciclista in lista:
        
        print(minitimp)
        if ciclista['tiempo']< minitimp:
            
            minitimp= ciclista['tiempo']
            print(minitimp)
    print(f'el tiempo menos es{minitimp}')


def ciliclista():

    numero = int(input("digite la cantidad de cliclistas "))
    list = []

    for i in range(numero):
        Ciclista={}
        Ciclista['nombre']=input("digete el nombre de la ciclista")
        Ciclista['edad']=input("digete la edad del ciclista ")
        Ciclista['pais']=input("digete el pais del cilista  ")
        Ciclista['equipo']=input("digite el equipo del ciclista")
        Ciclista['tiempo']= int (input("digite el tiempo del ciclista"))
        list.append(Ciclista)
       
    calculartime(list)
                                        
ciliclista()