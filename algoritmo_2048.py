# L funcion partir_lista clasifica que tipo de lista se le ingresa para luego modificarla
def partir_lista(my_position,vertical,adelante):
    # Se crean 4 listas las cuales representan las columnas y las filas
    lista1=[]
    lista2=[]
    lista3=[]
    lista4=[]
    
    # Clasifica que tipo de lista es , con respecto al sentido que se tiene y se agrega alas listas por separado conformadas cada una por 4 elementos
    if vertical:
        for i in range(0,4):               
            lista1.append(my_position[i*4])
            lista2.append(my_position[(i*4)+1])
            lista3.append(my_position[(i*4)+2])
            lista4.append(my_position[(i*4)+3])
    else:
        for i in range(0,4):               
            lista1.append(my_position[i])
            lista2.append(my_position[i+4])
            lista3.append(my_position[i+8])
            lista4.append(my_position[i+12])
    
    # Clasifica si la funcion ingresada va hacia adelante o hacia atras y asigna valores correspondientes de w,x,y y z
    if adelante:
        w=0; x=1; y=2; z=3
    else:
        w=3; x=2; y=1; z=0
        
    # Con los valores asignados anteriormente se usan para llamar la funcion algoritmo
    lista1 = algoritmo(lista1,w,x,y,z)
    lista2 = algoritmo(lista2,w,x,y,z)
    lista3 = algoritmo(lista3,w,x,y,z)
    lista4 = algoritmo(lista4,w,x,y,z)
    
    # Creo una lista total que guarde los elementos que tenian lista1, lista2, lista3 y lista 4
    lista_total=[]
    
    # Clasifica si es vertical o no para poderlo guardar segun corresponda el caso
    if vertical:
        for i in range(0,4):
            lista_total.append(lista1[i])
            lista_total.append(lista2[i])
            lista_total.append(lista3[i])
            lista_total.append(lista4[i])
    else:
        lista_total = lista1 + lista2 + lista3 +lista4
    
    return lista_total 
            

# La funcion algoritmo es la funcion principal del juego ya que aqui es donde se hace el manojo inicial y final de los turnos en el juego     
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
        
    ### Caso 1 , en donde la longitud de v sea 1
    if len(v)==1:
        b=v[0]
        a= lista[b] 
        lista[b]=0
        lista[z]=a 
        
    #### Caso 2 , en donde la longitud de v sea 2
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
            

    #### Caso 3 , en donde la longitud de v sea 3
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
            
    #### Caso 4´ , en donde la longitud de v sea 4
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
        elif lista[v[0]] == lista[v[1]] == lista[v[2]] != lista[v[3]]: 
            suma = lista[v[1]] + lista[v[2]]
            lista[y] = suma
            lista[x] = lista[v[0]]
            lista[w] = 0
        elif lista[v[0]] != lista[v[1]] == lista[v[2]] == lista[v[3]]: 
            suma = lista[v[2]] + lista[v[3]]
            lista[z] = suma
            lista[y] = lista[v[1]]
            lista[x] = lista[v[0]]
            lista[w] = 0
    
            
    return lista


