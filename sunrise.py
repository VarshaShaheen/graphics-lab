from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

x_ref = 0
y_ref = 0


def mountains():
    glColor(1.0, 0.2, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(3, 5)
    glVertex2f(6, 0)
    glEnd()
    glFlush()
    glBegin(GL_TRIANGLES)
    glVertex2f(5, 0)
    glVertex2f(7.5, 5)
    glVertex2f(10, 0)
    glEnd()
    glFlush()


def circle():
    glColor(1.0, 1.0, 0.0)
    if y_ref > 4:
        glColor(1.0, 0.5, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 360, 1):
        theta = math.radians(i)
        x = 1.5 * math.cos(theta)
        y = 1.5 * math.sin(theta)
        glVertex2f((x + 5), (y + y_ref))
    glEnd()
    glFlush()


def update(_):
    global x_ref, y_ref
    if y_ref < 7:
        y_ref += 0.1

    glutPostRedisplay()
    glClear(GL_COLOR_BUFFER_BIT)
    glutTimerFunc(200, update, 0)


def clearscreen():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, 10.0, 0, 10.0)


def display():
    circle()
    mountains()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Sunrise")

    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    clearscreen()
    glutMainLoop()


if __name__ == "__main__":
    main()
