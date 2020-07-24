from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

def inittex(name):
    img = pygame.image.load(name)
    textureData = pygame.image.tostring(img, "RGB", 1)
    width = img.get_width()
    height = img.get_height()
    return [textureData,width,height]

def drawtall(x,y,z,rx,ry,rz,name):
    width=inittex(name)[1]
    height = inittex(name)[2]
    textureData=inittex(name)[0]
    bgImgGL = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, bgImgGL)  # (a que se une la textura, nombre de la textura)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 3, width, height, GL_RGB, GL_UNSIGNED_BYTE, textureData)
    glEnable(GL_TEXTURE_2D)

    glPushMatrix()
    glTranslatef(x,y,z)
    glRotatef(rx,1,0,0)
    glRotatef(ry, 0, 1, 0)
    glRotatef(rz, 0, 0, 1)


    glBegin(GL_QUADS)


    glTexCoord2f(0, 1)
    glVertex3f(0, 1, 0)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 0)
    glTexCoord2f(1, 0)
    glVertex3f(1, 0, 0)
    glTexCoord2f(0, 0)
    glVertex3f(0, 0, 0)

    glEnd()

    glPopMatrix()