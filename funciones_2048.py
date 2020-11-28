import os
import algoritmo_2048 as regla

def position(coor, my_font, mysurface, num):
    if num != 0:        
        numero = my_font.render(str(num),True,(0,0,0))
    else:
        numero = my_font.render("   ",True,(0,0,0))
        
    x = 145 + 60*(coor%4)
    y = 140 + 60*(coor//4)
    mysurface.blit(numero,(x,y))


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

def put_numbers(my_font, my_surface, my_position):
    for i in range(len(my_position)):
        position(i, my_font, my_surface, my_position[i])
        

def ventana2():
    os.system("python3 instruccciones_2048.py")
    
            
