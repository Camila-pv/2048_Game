
import pygame

def main():
    #Setup de la libreria
    pygame.init() 
    
    #display de 480 por 480
    mysurface = pygame.display.set_mode((300,300))
    
    #Edicion de texto
    my_font = pygame.font.SysFont("Courier",16)
    
    mysurface.fill((204,255,255))  #Escala RGB Rojo[0-255], Verde[0-255], Blue[0-255]       
    

    
    #Definir un ciclo/bucle de repeticion
    while True:
        evento = pygame.event.poll()
        if evento.type == pygame.QUIT:
            break #Se sale del bucle cuando el usuario cierra la ventana

        pygame.display.flip() #dibuja todo en cada bucle
    
    #Cerrar el pygame
    pygame.quit()
        
main()




