#Libreria para desarrollo de videojuegos y libreria random que genera numeros pseudoaleatorios
#importo el algoritmo_2048 que es donde se encuentra casi toda la estructura del juego 
#funciones_2048 importo funciones_2048 que es donde estan todas las funciones
import pygame
import random
import algoritmo_2048 as regla 
import funciones_2048 as fun

            
    
def main():
    #Setup de la libreria
    pygame.init() 
    
    #display de 480 por 480
    mysurface = pygame.display.set_mode((480,480))
    
    #Imagenes
    control = pygame.image.load("control_juego.png")
    dos = pygame.image.load("dos.png")
    cero = pygame.image.load("cero.png")
    cuatro = pygame.image.load("cuatro.png")
    ocho = pygame.image.load("ocho.png")
    win = pygame.image.load("you_win.png")
    over = pygame.image.load("game_over.png")
     
    #Edicion de texto
    my_font = pygame.font.SysFont("Courier",20)
    
    #Ajustar el tamano de las imagenes
    control = pygame.transform.scale(control,(50,50))
    dos = pygame.transform.scale(dos,(50,50))
    cero = pygame.transform.scale(cero,(50,50))
    cuatro = pygame.transform.scale(cuatro,(50,50))
    ocho = pygame.transform.scale(ocho,(50,50))
    win = pygame.transform.scale(win,(150,150))
    over = pygame.transform.scale(over,(150,150))
    
    #creo la lista de los cuadritos de la cuadricula
    my_position = [0]*16
    
    #llamo random 
    rng = random.Random()
    
    

    #Conversion from Color Name to RGB:
    #Cambio de color el fondo de la ventana
    #https://www.rapidtables.com/web/color/RGB_Color.html
    #https://www.pygame.org/docs/ref/draw.html        
    mysurface.fill((204,255,255))  #Escala RGB Rojo[0-255], Verde[0-255], Blue[0-255]        

    #Poner la imagen del control en una coordenada en especifico
    mysurface.blit(control,(400,120))
    mysurface.blit(dos,(140,30))
    mysurface.blit(cero,(190,30))
    mysurface.blit(cuatro,(240,30))
    mysurface.blit(ocho,(290,30))    
    
    #Creo las primeras posiciones aleatorias para poner los primeros dos numeros inicales
    my_position = fun.different_pos(rng, my_font, mysurface, my_position)
    my_position = fun.different_pos(rng, my_font, mysurface, my_position)
            
    #Definir un ciclo/bucle de repeticion
    while True:
        evento = pygame.event.poll()
        if evento.type == pygame.QUIT:
            break #Se sale del bucle cuando el usuario cierra la ventana

        if evento.type == pygame.MOUSEBUTTONDOWN:  # llamo MOUSEBUTTONDOWN que activa las opciones para usar el mouse
            if pygame.mouse.get_pressed()[0]:   
                pos = pygame.mouse.get_pos()
                if pos[0]>= 399 and pos[0] <=452 and pos[1] >= 115 and pos[1] <= 171: #Oprime imagen del control
                    fun.ventana2()                                                      #llama otra ventana

        #Creo un cuadrado del tamano de la cuadricula grande         
        pygame.draw.polygon(mysurface,(204,204,255),[(120,120),(120,360),(360,360),(360,120)])        
        
        #line(surface, color, start_pos, end_pos, width=1) -> Rect
        #creo la cuadricula
        a=120
        for i in range (5):
            pygame.draw.line(mysurface,(0,0,0),(a,120),(a,360),3)
            pygame.draw.line(mysurface,(0,0,0),(120,a),(360,a),3)
            a+=60
        
        
        # Imprimos los numeros en la cuadricula
        fun.put_numbers(my_font, mysurface, my_position)
        
        
            
        # detecto el uso de las fechas de arriba, abajo, derecha e izquierda
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                my_position = regla.partir_lista(my_position,False,False)
                print("Izquierda")
                my_position = fun.different_pos(rng, my_font, mysurface, my_position)
            elif evento.key == pygame.K_RIGHT:
                my_position = regla.partir_lista(my_position,False,True)
                my_position = fun.different_pos(rng, my_font, mysurface, my_position)
                print("Derecha")
            elif evento.key == pygame.K_UP:
                my_position = regla.partir_lista(my_position,True,False)
                my_position = fun.different_pos(rng, my_font, mysurface, my_position)
                print("Arriba")
            elif evento.key == pygame.K_DOWN:
                my_position = regla.partir_lista(my_position,True,True)
                my_position = fun.different_pos(rng, my_font, mysurface, my_position)
                print("Abajo")        
        
       
        if 2048 in my_position:
            mysurface.blit(win,(165,165))
        if len(my_position) == 0:
            mysurface.blit(over,(165,165))
           
        
        pygame.display.flip() #dibuja todo en cada bucle
    
    #Cerrar el pygame
    pygame.quit()
        
main()

