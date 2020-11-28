
import pygame

def main():
    #Setup de la libreria
    pygame.init() 
    
    #display de 480 por 480
    mysurface = pygame.display.set_mode((394,429))
     
    
    #Imagenes
    instrucciones = pygame.image.load("instrucciones_2048.png")
    
     #Ajustar el tamano de las imagenes
    instrucciones = pygame.transform.scale(instrucciones,(394,429))
    
    mysurface.fill((204,255,255))  #Escala RGB Rojo[0-255], Verde[0-255], Blue[0-255]        
    
    #Poner la imagen del control en una coordenada en especifico
    #mysurface.blit(instrucciones,(400,120))
    
    
    
    #Definir un ciclo/bucle de repeticion
    while True:
        evento = pygame.event.poll()
        if evento.type == pygame.QUIT:
            break #Se sale del bucle cuando el usuario cierra la ventana
            
        mysurface.blit(instrucciones,(0,0))

        pygame.display.flip() #dibuja todo en cada bucle
    
    #Cerrar el pygame
    pygame.quit()
        
main()




