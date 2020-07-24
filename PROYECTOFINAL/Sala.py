from OpenGL.GL import *
import pygame
import CUBOT
import Cuadrotex

def inittex(name):
    img = pygame.image.load(name)
    textureData = pygame.image.tostring(img, "RGB", 1)
    width = img.get_width()
    height = img.get_height()
    return [textureData,width,height]

def drawmesa():

    CUBOT.drawtall(0,0,0,1,0.05,1,0,0,0,'./TEXTURAS/mesa1.jpg')
    CUBOT.drawtall(0, -0.2, 0, 1, 0.05, 1, 0, 0, 0, './TEXTURAS/mesa1.jpg')
    glPushMatrix()
    #PATAS DE LA MESA
    CUBOT.drawtall(-0.8, -0.2, 0.8, 0.08, 0.2, 0.08, 0, 0, 0, './TEXTURAS/mesa1.jpg')
    CUBOT.drawtall(0.8, -0.2, 0.8, 0.08, 0.2, 0.08, 0, 0, 0, './TEXTURAS/mesa1.jpg')
    CUBOT.drawtall(-0.8, -0.2, -0.8, 0.08, 0.2, 0.08, 0, 0, 0, './TEXTURAS/mesa1.jpg')
    CUBOT.drawtall(0.8, -0.2, -0.8, 0.08, 0.2, 0.08, 0, 0, 0, './TEXTURAS/mesa1.jpg')
    glPopMatrix()

def drawSillones(value):
    if value == 1:
        CUBOT.drawtall(0,-0.2,0, 2, 0.2, 1, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(1, 0.2, 0, 1, 0.2, 1, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(-1, 0.2, 0, 1, 0.2, 1, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(-2, 0.2, 0.1, 0.2, 0.7, 1, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(2, 0.2, 0.1, 0.2, 0.7, 1, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(0, 0.3, -1, 2.2, 0.8, 0.2, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(-0.9, 0.9, -0.6, 0.9, 0.5, 0.2, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(0.9, 0.9, -0.6, 0.9, 0.5, 0.2, 0, 0, 0, './TEXTURAS/sillones.png')

    if value == 2:
        CUBOT.drawtall(0, -0.2, 0, 1, 0.2, 1, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(0, 0.2, 0, 1, 0.2, 1, 0, 0, 0, './TEXTURAS/sillones.png')

        CUBOT.drawtall(-1, 0.2, 0.1, 0.2, 0.7, 1, 0, 0, 0, './TEXTURAS/sillones.png')
        CUBOT.drawtall(1, 0.2, 0.1, 0.2, 0.7, 1, 0, 0, 0, './TEXTURAS/sillones.png')

        CUBOT.drawtall(0, 0.29, -1.1, 1.1, 0.8, 0.2, 0, 0, 0, './TEXTURAS/sillones.png')

        CUBOT.drawtall(0, 0.9, -0.6, 0.7, 0.5, 0.2, 0, 0, 0, './TEXTURAS/sillones.png')

def drawmesapeq():

    CUBOT.drawtall(0,0.5,0,0.5,0.05,0.5,0,0,0,'./TEXTURAS/mesa2.png')
    CUBOT.drawtall(0, 0.3, 0, 0.5, 0.03, 0.5, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(0, -0.35, 0, 0.5, 0.05, 0.5, 0, 0, 0, './TEXTURAS/mesa2.png')
    glPushMatrix()
    #PATAS DE LA MESA
    CUBOT.drawtall(-0.35, 0, 0.35, 0.08, 0.5, 0.08, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(0.35, 0, 0.35, 0.08, 0.5, 0.08, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(-0.35, 0, -0.35, 0.08, 0.5, 0.08, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(0.35, 0, -0.35, 0.08, 0.5, 0.08, 0, 0, 0, './TEXTURAS/mesa2.png')
    glPopMatrix()

def drawarmario():
    CUBOT.drawtall(0, 0, 0, 1, 0.5, 0.5, 0, 0, 0, './TEXTURAS/mesa2.png')
    glPushMatrix()
    glScalef(2, 1, 1)
    Cuadrotex.drawtall(-0.5, -0.5, 0.515, 0, 0, 0, './TEXTURAS/puertalibreria.png')
    glPopMatrix()
    CUBOT.drawtall(0, 2.5, 0, 1, 0.02, 0.5, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(0, 1.90, 0, 1, 0.02, 0.5, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(0, 1.25, 0, 1, 0.02, 0.5, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(0, 1, -0.5, 1, 1.5, 0.02, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(-1, 1, 0, 0.02, 1.5, 0.5, 0, 0, 0, './TEXTURAS/mesa2.png')
    CUBOT.drawtall(1, 1, 0, 0.02, 1.5, 0.5, 0, 0, 0, './TEXTURAS/mesa2.png')

def drawarmesatele():
#MESA
    CUBOT.drawtall(0, -0.4, 0, 1, 0.02, 0.5, 0, 0, 0, './TEXTURAS/mesatele.png')


    CUBOT.drawtall(0, 0.5, 0, 1, 0.02, 0.75, 0, 0, 0, './TEXTURAS/mesatele.png')
    CUBOT.drawtall(0, 0.1, 0, 1, 0.01, 0.5, 0, 0, 0, './TEXTURAS/mesatele.png')

    CUBOT.drawtall(0, 0, -0.5, 1, 0.5, 0.02, 0, 0, 0, './TEXTURAS/mesatele.png')

    CUBOT.drawtall(-1, 0, 0, 0.02, 0.5, 0.5, 0, 0, 0, './TEXTURAS/mesatele.png')
    CUBOT.drawtall(1, 0, 0, 0.02, 0.5, 0.5, 0, 0, 0, './TEXTURAS/mesatele.png')



