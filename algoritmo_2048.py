#Creo la función algoritmo que es la estructura del juego para poder funcionar
#La función recibe la lista my_position y los números w,x,y,z que pueden ser 0,1,2,3 o 3,2,1,0 segun corresponda el caso
#Creo 4 listas que se van a segun la fila o columna correspondiente, es decir en cada lista va a tener 4 numeros 
#Vetical bool que dice si el moviviento de los números es vertical u horizontal 
#Adelante es un bool que dice si moviviento de los números es adelante o atras
def partir_lista(my_position,vertical,adelante):
    lista1=[]
    lista2=[]
    lista3=[]
    lista4=[]
    
    if vertical:
        for i in range(0,4):                # En este for repartimos los elementos de la lista en 4 a las 4 listas , conformados en filas y columnas
            lista1.append(my_position[i*4])
            lista2.append(my_position[(i*4)+1])
            lista3.append(my_position[(i*4)+2])
            lista4.append(my_position[(i*4)+3])
    else:
        for i in range(0,4):                # En este for repartimos los elementos de la lista en 4 a las 4 listas , conformados en filas y columnas
            lista1.append(my_position[i])
            lista2.append(my_position[i+4])
            lista3.append(my_position[i+8])
            lista4.append(my_position[i+12])
    
    if adelante:
        w=0; x=1; y=2; z=3
    else:
        w=3; x=2; y=1; z=0
        
    lista1 = algoritmo(lista1,w,x,y,z)
    lista2 = algoritmo(lista2,w,x,y,z)
    lista3 = algoritmo(lista3,w,x,y,z)
    lista4 = algoritmo(lista4,w,x,y,z)
    
    lista_total=[]
    if vertical:
        for i in range(0,4):
            lista_total.append(lista1[i])
            lista_total.append(lista2[i])
            lista_total.append(lista3[i])
            lista_total.append(lista4[i])
    else:
        lista_total = lista1 + lista2 + lista3 +lista4
    
    return lista_total
            

    
def algoritmo(lista,w,x,y,z):
    v=[]                            #v=[] es una listan donde se va a guardar la poscion en donde se encuentra un numero diderente de 0 elavuando la listas inciales 
    
    if z==3:                                # Se guarda las posiciones diferentes de 0 que encuentre en la lista correspondiente y depende del caso 
        for i in range(0,4):
            if lista[i]!=0:
                v.append(i) 
    else:
        for i in range(3,-1,-1):
            if lista[i]!=0:
                v.append(i) 
        
    ### 1
    if len(v)==1:
        b=v[0]
        a= lista[b] 
        lista[b]=0
        lista[z]=a 
        
    #### 2
    if len(v)==2:
        if lista[v[0]] == lista[v[1]]: 
            suma = lista[v[0]] + lista[v[1]] 
            lista[v[0]] = 0 
            lista[v[1]] = 0
            lista[z] = suma
        else:
            lista[z]=lista[v[1]] 
            lista[y]=lista[v[0]]
            lista[x] = 0
            lista[w] = 0 
            

    #### 3 
    if len(v)==3:
        if lista[v[0]] != lista[v[1]] == lista[v[2]]:
            s = lista[v[1]] + lista[v[2]]
            lista[z] = s
            lista[y] = lista[v[0]] 
            lista[x] = 0
            lista[w] = 0 
        elif lista[v[0]] == lista[v[1]] != lista[v[2]]:
            lista[z] = lista[v[2]]
            su = lista[v[0]] + lista[v[1]]
            lista[y]= su 
            lista[x] = 0
            lista[w] = 0 
        elif lista[v[0]] == lista[v[1]] == lista[v[2]]:
            conteo = lista[v[1]] + lista[v[2]]
            lista[z] = conteo
            lista[y] = lista[v[0]]
            lista[x] = 0
            lista[w] = 0 
        ##### el el else esta el caso en que los tres numeros son diferentes y el caso en que el primero y el ultmo sean iguales
        else:
            lista[z]=lista[v[2]] 
            lista[y]=lista[v[1]]
            lista[x]=lista[v[0]]
            lista[w] = 0 
            
    #### 4
    if len(v) ==4:
        if lista[v[0]] != lista[v[1]] != lista[v[2]] == lista[v[3]]: 
            conte= lista[v[2]] + lista[v[3]] 
            lista[z] = conte
            lista[y] = lista[v[1]] 
            lista[x] =lista[v[0]]
            lista[w] = 0 
        elif lista[v[0]] != lista[v[1]] == lista[v[2]] != lista[v[3]]:
            cont = lista[v[1]] + lista[v[2]]
            lista[y] = cont
            lista[x] = lista[v[0]] 
            lista[w] = 0
        elif lista[v[0]] == lista[v[1]] != lista[v[2]] != lista[v[3]]:
            con = lista[v[0]] + lista[v[1]]
            lista[x] = con 
            lista[w] = 0
        elif lista[v[0]] == lista[v[1]] != lista[v[2]] == lista[v[3]]:
            co = lista[v[2]] + lista[v[3]]
            lista[z] = co
            c = lista[v[0]] + lista[v[1]]
            lista[y] = c
            lista[x] = 0
            lista[w] = 0 
        elif lista[v[0]] == lista[v[1]] == lista[v[2]] == lista[v[3]]: 
            co = lista[v[2]] + lista[v[3]]
            lista[z] = co
            c = lista[v[0]] + lista[v[1]]
            lista[y] = c
            lista[x] = 0
            lista[w] = 0 
            
    
            
    return lista


