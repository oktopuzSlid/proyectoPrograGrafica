from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import CUBOT
import Cuadrotex

def draw(value):
    if value ==1 :
        CUBOT.drawtall(0,0,0,1,2,0.2,0,0,0,'./TEXTURAS/puertamadera.png')
        glPushMatrix()
        glScalef(2, 4, 1)
        Cuadrotex.drawtall(-0.5,-0.5,0.225,0,0,0,'./TEXTURAS/puerta.png')
        glPopMatrix()
    if value == 2:
        CUBOT.drawtall(0, 0, 0, 1, 2, 0.2, 0, 0, 0, './TEXTURAS/puertamadera.png')
        glPushMatrix()
        glScalef(2, 4, 1)
        Cuadrotex.drawtall(-0.5, -0.5, 0.225, 0, 0, 0, './TEXTURAS/puerta2.png')
        glPopMatrix()
