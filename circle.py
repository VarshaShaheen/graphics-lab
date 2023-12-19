from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x_ref = 0
y_ref = 0


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 10.0, 0, 10.0)


def circle():
    glColor(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for i in range(0, 360, 1):
        theta = math.radians(i)
        x = 1 * math.cos(theta)
        y = 1 * math.sin(theta)
        glVertex2f((x + 5 + x_ref)%11, (y + 5 + y_ref)%11)
    glEnd()
    glFlush()


def update(_):
    global x_ref, y_ref
    x_ref += 0.01
    y_ref += 0.01
    glutPostRedisplay()
    glClear(GL_COLOR_BUFFER_BIT)
    glutTimerFunc(30, update, 0)


def display():
    circle()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Circle")

    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    clearscreen()
    glutMainLoop()


if __name__ == '__main__':
    main()
