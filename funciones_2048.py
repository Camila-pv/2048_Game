import os
import algoritmo_2048 as regla


# L a funcion posicion es la que pone el numero correspodientes en cierta coordenada asignada
def position(coor, my_font, mysurface, num):
    x1=145
    fac = 7
    if num != 0:        
        numero = my_font.render(str(num),True,(0,0,0))
        if num < 10:
            x1 = 145
        elif num < 100:
            x1 = 145-fac
        elif num < 1000:
            x1 = 145 - fac*2
        else:
            x1 = 145 - fac*3
    else:
        numero = my_font.render("   ",True,(0,0,0))
        
    x = x1 + 60*(coor%4)
    y = 140 + 60*(coor//4)
    mysurface.blit(numero,(x,y))

# Comprueba si se puede hacer otro movimiento y el que decide si se puede poner otro 2 en la cuadricula
def different_pos(ran, my_font, my_surface, my_position):
    if 0 in my_position:
        while(True):
            p = ran.randrange(0,16)
            if(my_position[p] == 0):
                my_position[p] = 2
                position(p, my_font, my_surface, my_position[p])
                return my_position
    else:
        if my_position == regla.partir_lista(my_position,True,True):
            if my_position == regla.partir_lista(my_position,True,False):
                if my_position == regla.partir_lista(my_position,False,True):
                    if my_position == regla.partir_lista(my_position,False,False):
                        return []
        return my_position 

# Llama la funcion position para obtener las coordenadas y poder poner el numero en la cuadricula 
def put_numbers(my_font, my_surface, my_position):
    for i in range(len(my_position)):
        position(i, my_font, my_surface, my_position[i])
        
# Llamo el archivo instruccciones_2048.py para crear otra ventana, donde se encuentra las instrucciones del juego
def ventana2():
    os.system("python3 instruccciones_2048.py")
    
            
