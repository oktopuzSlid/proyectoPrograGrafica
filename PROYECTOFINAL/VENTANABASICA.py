
from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *
import sys
import CUBOT as cubo
import BASE
import Sala
import Puerta

#Import some other useful modules
import sys, os, traceback
#Center the window on the screen, if we're on Windows, which supports it.
if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"
#Import sin, cos, radians, degrees, etc.
from math import *
#Initialize PyGame.  You could also call "pygame.init()", but in my experience this can be faster
#(since you aren't initializing *everything*) and more portable (since some modules may require
#extra dependencies).
pygame.display.init()
db=1
#namet=["tex.jpg","sushitex.png",'pared.jpg']

#Screen configuration
screen_size = [800,600]
screen = pygame.display.set_mode((screen_size[0],screen_size[1]))
multisample = 0
#Set the window's icon, as applicable, to be just a transparent square.
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
#Set the title of the window.
pygame.display.set_caption("APARTAMENTO 5-12")
#Set the window to be multisampled.  This does depth testing at a higher resolution, leading to
#smooth, antialiased edges.  Most computers support at least multisample=4, and most support more
#(e.g. mine does 16).
if multisample:
    pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS,1)
    pygame.display.gl_set_attribute(GL_MULTISAMPLESAMPLES,multisample)
#Create the window of the requested size.  The pygame.OPENGL flag tells it to allow OpenGL to write
#directly to the window context.  The pygame.DOUBLEBUF flag tells it to make the window
#doublebuffered.  This causes the screen to only show a completed image.  This function actually
#returns a "surface" object, but it isn't useful for OpenGL programs.
pygame.display.set_mode(screen_size,OPENGL|DOUBLEBUF)

#TEXTURAS

#FIN DE TEXTURAS

glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)
#This enables depth testing (so that closer objects are always drawn in front of farther objects).
#If depth testing is not enabled, then objects are drawn "over" each other in the order you draw
#them.  For most 3D rendering, you'll want depth testing enabled.
glEnable(GL_DEPTH_TEST)

camera_rot = [30.0,20.0]      #The spherical coordinates' angles (degrees).
camera_radius = 3.0           #The sphere's radius
camera_center = [0.0,0.0,0.0] #The sphere's center



def get_input():
    global camera_rot, camera_radius
    keys_pressed = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos()
    #Check how much the mouse moved since you last called this function.
    mouse_rel = pygame.mouse.get_rel()
    #List all the events that happened.
    for event in pygame.event.get():
        #Clicked the little "X"; close the window (return False breaks the main loop).
        if   event.type == QUIT: return False
        #If the user pressed a key:
        elif event.type == KEYDOWN:
            #If the user pressed the escape key, close the window.
            if   event.key == K_ESCAPE or event.key == pygame.K_RETURN: return False
        #If the user "clicked" the scroll wheel forward or backward:
        elif event.type == MOUSEBUTTONDOWN:
            #Zoom in
            if   event.button == 4: camera_radius *= 0.9
            #Or out.
            elif event.button == 5: camera_radius /= 0.9


    #If the user is left-clicking, then move the camera about in the spherical coordinates.
    if mouse_buttons[0]:
        camera_rot[0] += mouse_rel[0]
        camera_rot[1] += mouse_rel[1]
    return True


def draw():
    global db

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glViewport(0,0,screen_size[0],screen_size[1])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(screen_size[0])/float(screen_size[1]), 0.1,100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


    camera_pos = [
        camera_center[0] + camera_radius*cos(radians(camera_rot[0]))*cos(radians(camera_rot[1])),
        camera_center[1] + camera_radius                            *sin(radians(camera_rot[1])),
        camera_center[2] + camera_radius*sin(radians(camera_rot[0]))*cos(radians(camera_rot[1]))
    ]

    gluLookAt(
        camera_pos[0],camera_pos[1],camera_pos[2],
        camera_center[0],camera_center[1],camera_center[2],
        0,1,0
    )

    # cambiar de figura
    keypress = pygame.key.get_pressed()

    if keypress[pygame.K_1]:
        db = 1

    if keypress[pygame.K_2]:
        db = 2

    if keypress[pygame.K_3]:
        db = 3


    if keypress[pygame.K_4]:
        db = 4


    if keypress[pygame.K_5]:
        db = 5

    if keypress[pygame.K_6]:
        db = 6

    if keypress[pygame.K_7]:
        db = 7


    if keypress[pygame.K_8]:
        db = 8


    if keypress[pygame.K_9]:
        db = 9


   #Dibujar Figuras

    if(db==1):

        BASE.draw(1,1,1,0,0,0,'./TEXTURAS/tex.jpg')
        BASE.drawparedes(1,1,1,0,0,0,'./TEXTURAS/pared.jpg')

    if (db == 2):

        Sala.drawmesapeq()
        #Sala.drawarmesatele()

    if (db == 3):
        Sala.drawSillones(2)
        #Sala.drawarmario()

    if (db == 4):
        Puerta.draw(2)
    #
    # if (db == 5):
    #
    #
    # if (db == 6):
    #
    #
    # if (db == 7):
    #
    #
    # if (db == 8):
    #
    #
    # if (db == 9):


    pygame.display.flip()


def main():

    clock = pygame.time.Clock()
    while True:
        if not get_input(): break

        draw()

        clock.tick(60) #Regulate the framerate to be as close as possible to 60Hz.
    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        pygame.quit()
        input()

