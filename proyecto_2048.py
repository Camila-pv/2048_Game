
#Libreria para desarrollo de videojuegos y libreria random que genera números pseudoaleatorios
import pygame
import random

def main():
    #Setup de la libreria
    pygame.init() 
    
    #display de 480 por 480
    mysurface = pygame.display.set_mode((480,480))
    
    #Imagen de control
    control = pygame.image.load("control_juego.png")
    trofeo = pygame.image.load("trofeo.png")
    dos = pygame.image.load("dos.png")
    cero = pygame.image.load("cero.png")
    cuatro = pygame.image.load("cuatro.png")
    ocho = pygame.image.load("ocho.png")
    
    #Edicion de texto
    my_font = pygame.font.SysFont("Courier",16)
    
    #Ajustar el tamaño de la imagen del control
    control = pygame.transform.scale(control,(50,50))
    trofeo = pygame.transform.scale(trofeo,(50,50))
    dos = pygame.transform.scale(dos,(50,50))
    cero = pygame.transform.scale(cero,(50,50))
    cuatro = pygame.transform.scale(cuatro,(50,50))
    ocho = pygame.transform.scale(ocho,(50,50))
    
    
    
    #Definir un ciclo/bucle de repeticion
    while True:
        evento = pygame.event.poll()
        if evento.type == pygame.QUIT:
            break #Se sale del bucle cuando el usuario cierra la ventana
        
        mysurface.fill((204,255,255))  #Escala RGB Rojo[0-255], Verde[0-255], Blue[0-255]
        
        
        
        #Conversion from Color Name to RGB:
        #https://www.rapidtables.com/web/color/RGB_Color.html
        #https://www.pygame.org/docs/ref/draw.html
        
        #Creo un cuadrado del tamaño de la cuadricula grande 
        b=120
        for i in range(5):
            #pygame.draw.polygon(mysurface,(255,204,229),[(b,120),(b,180),(180,180),(180,120)])
            pygame.draw.polygon(mysurface,(204,204,255),[(120,120),(120,360),(360,360),(360,120)])
            b+=60
            
            
        #line(surface, color, start_pos, end_pos, width=1) -> Rect
        #creo la cuadricula
        a=120
        for i in range (5):
            pygame.draw.line(mysurface,(0,0,0),(a,120),(a,360),3)
            pygame.draw.line(mysurface,(0,0,0),(120,a),(360,a),3)
            a+=60
        
        #poner la imagen del control en una coordenada en especifico
        mysurface.blit(control,(400,120))
        mysurface.blit(trofeo,(400,180))
        mysurface.blit(dos,(140,30))
        mysurface.blit(cero,(190,30))
        mysurface.blit(cuatro,(240,30))
        mysurface.blit(ocho,(290,30))
        
        rng = random.Random()
        p1 = rng.randrange(1,17)
        p2 = rng.randrange(1,17)
        
        numero = my_font.render("2",True,(0,0,0))
        mysurface.blit(numero,(145,320))

        if evento.type == pygame.KEYDOWN:
            key = evento.dict["key"]
            
                
        
        
        
        
        

        
        
        
        pygame.display.flip() #dibuja todo en cada bucle
    
    #Cerrar el pygame
    pygame.quit()
        
main()






##################################################
##################################################
#Instrucciones -¿como jugar?
##################################################
##################################################
#El objetivo del juego es combinar números juntos (potencias de 2) con el fin 
#de alcanzar el máximo de baldosas '2048 'y ganar el juego!

#El área de juego 2048 es una cuadrícula de 4x4 con 16 ranuras cuadradas. 
#Al principio del juego, tiene dos plazas (también llamados «tejas») con un 'número '2 interior.

#Cuando usted hace 2 baldosas con el mismo número en el interior se unen,
#se funden en uno nuevo  con un número que es la adición de la 2 anterior : 2 +2 = 4,
# 4 +4 = 8, 1024 ... 1024 = 2048 !

#Para mover las fichas en la parrilla, sólo tienes que elegir una 
#dirección  (arriba, derecha, abajo o izquierda) .
# Todas las fichas se mueven en la dirección elegida, hasta que se funden
# con una baldosa que tiene el mismo número o son bloqueados por una baldosa con un número diferente.

#En un equipo, sólo tiene que  utilizar las flechas del teclado 4 .
# En un dispositivo móvil con interfaz táctil (como un dispositivo iOS o Android) , 
#deslizar con el dedo en la dirección deseada.


###################################################
###################################################
# numero de las flechas
###################################################
###################################################
# arriba - 1073741906
# abajo - 1073741905
# izquierda - 1073741904
# derecha - 1073741903