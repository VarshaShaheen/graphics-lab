from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import time
import math
import sys

x_inc = 0
y_inc = 0


def update(_):
    global x_inc, y_inc

    x_inc = x_inc + 1
    y_inc = y_inc + 1

    glutPostRedisplay()
    glutTimerFunc(40, update, 0)


def drawCircle(x1, y1, r):
    glColor(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        x = r * math.cos(math.radians(i))
        y = r * math.sin(math.radians(i))
        glVertex2f(x + x1, y + y1)
    glEnd()

def drawCircle2(x1, y1, r):
    glColor(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        x = r * math.cos(math.radians(i))
        y = r * math.sin(math.radians(i))
        glVertex2f(x + x1, y + y1)
    glEnd()


def car():
    global x_inc, y_inc
    glColor(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(80, 60)
    glVertex2f(80, 80)
    glVertex2f(90, 80)
    glVertex2f(90, 60)
    glEnd()

    glColor(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(80, 60)
    glVertex2f(80, 80)
    glVertex2f(90, 80)
    glVertex2f(90, 60)
    glEnd()

    glColor(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(84, 80)
    glVertex2f(84, 20)
    glVertex2f(86, 20)
    glVertex2f(86, 80)
    glEnd()

    if  x_inc <= 60:
        drawCircle(85, 70, 5)
    else:
        drawCircle2(85, 70, 5)

    if x_inc == 60:
        time.sleep(5)

    glColor(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(0 + x_inc, 20)
    glVertex2f(15 + x_inc, 20)
    glVertex2f(15 + x_inc, 30)
    glVertex2f(0 + x_inc, 30)
    glEnd()

    glColor(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        x = 1 * math.cos(math.radians(i))
        y = 1 * math.sin(math.radians(i))
        glVertex2f(x + 2 + x_inc, y + 20)
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(360):
        x = 1 * math.cos(math.radians(i))
        y = 1 * math.sin(math.radians(i))
        glVertex2f(x + 13 + x_inc, y + 20)
    glEnd()


def clearscreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0, 100, 0, 100.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    car()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(1000, 1000)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Car")

    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    clearscreen()
    glutMainLoop()


if __name__ == '__main__':
    main()
