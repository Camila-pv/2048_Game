
import pygame

def main():
    #Setup de la libreria
    pygame.init() 
    
    #display de 450 por 239
    mysurface = pygame.display.set_mode((450,239))
    
    #Imagen de instrucciones
    i = pygame.image.load("i.png")
    #Ajustar el tamano de la imagene
    i = pygame.transform.scale(i,(500,359))
    
    mysurface.fill((204,255,255))  #Escala RGB Rojo[0-255], Verde[0-255], Blue[0-255]        

    
    #Definir un ciclo/bucle de repeticion
    while True:
        evento = pygame.event.poll()
        if evento.type == pygame.QUIT:
            break #Se sale del bucle cuando el usuario cierra la ventana
        #Poner de las instrucciones en una coordenada en especifico   
        mysurface.blit(i,(-30,-100))
        pygame.display.flip() #dibuja todo en cada bucle
    
    #Cerrar el pygame
    pygame.quit()
        
main()




