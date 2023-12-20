from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import time
import math
import sys

xref = 0
yref = 0
temp = 0


def body():
    global xref, yref
    glColor(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(0, 360, 1):
        theta = math.radians(i)
        x = 1.5 * math.cos(theta)
        y = 1 * math.sin(theta)
        glVertex2f((x + xref), (y + yref))
    glEnd()


def beak():
    global xref, yref
    glColor(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(xref + 1, yref + 0.5)
    glVertex2f(xref + 2, yref)
    glVertex2f(xref + 1, yref - 0.5)
    glEnd()


def wings():
    global xref, yref
    if temp % 2 == 0:
        glColor(1.0, 0.0, 0.0)
        glBegin(GL_POLYGON)
        glVertex2f(xref - 0.5, yref)
        glVertex2f(xref, yref + 2)
        glVertex2f(xref + 0.5, yref)
        glEnd()
    else:
        glColor(1.0, 0.0, 0.0)
        glBegin(GL_POLYGON)
        glVertex2f(xref + 0.5, yref)
        glVertex2f(xref, (yref - 2))
        glVertex2f(xref - 0.5, yref)
        glEnd()


def tail():
    global xref, yref
    glColor(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(xref - 1, yref + 0.3)
    glVertex2f(xref - 2, yref)
    glVertex2f(xref - 1, yref - 0.3)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    beak()
    tail()
    body()
    wings()
    glutSwapBuffers()


def clearscreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-10, 10, -10, 10.0)


def keyboard(key, x, y):
    global xref, yref, temp
    key = key.decode()
    if key == "w":
        yref = yref + 1
        temp = temp +1
        display()
    elif key == "s":
        yref = yref - 1
        temp = temp + 1
        display()
    elif key == "a":
        xref = xref - 1
        temp = temp + 1
        display()
    elif key == "d":
        xref = xref + 1
        temp = temp + 1
        display()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Bird")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    clearscreen()
    glutMainLoop()


if __name__ == '__main__':
    main()
