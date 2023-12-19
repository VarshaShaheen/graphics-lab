from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

x_ref = 0
y_ref = 0
theta1 = 90
theta2 = 90


def clearscreen():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(0, 10.0, 0, 10.0)


def update(_):
    global theta1, theta2
    if theta1 <= 180 and theta2 >= 0:
        theta1 += 1
        theta2 -= 1
    glutPostRedisplay()
    glClear(GL_COLOR_BUFFER_BIT)
    glutTimerFunc(30, update, 0)


def body():
    glColor(1.0, 0.5, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(4.5, 4.5)
    glVertex2f(5, 6)
    glVertex2f(5.5, 4.5)
    glEnd()
    glFlush()

    glColor(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(5.0, 5.8)
    glVertex2f(5.5, 5.6)
    glVertex2f(5.0, 5.4)
    glEnd()
    glFlush()


def peacock():
    global theta1, theta2
    glColor(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    angle = math.radians(90)
    x = 3 * math.cos(angle)
    y = 3 * math.sin(angle)
    glVertex2f(5, 5)
    glVertex2f((x + 5), (y + 5))
    glEnd()
    glColor(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(0, 360, 1):
        theta = math.radians(i)
        x1 = 0.3 * math.cos(theta)
        y1 = 0.3 * math.sin(theta)
        glVertex2f((x + x1 + 5), (y + y1 + 5))
    glEnd()
    glFlush()

    glColor(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    angle = math.radians(theta1)
    x = 3 * math.cos(angle)
    y = 3 * math.sin(angle)
    glVertex2f(5, 5)
    glVertex2f((x + 5), (y + 5))
    glEnd()
    glColor(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(0, 360, 1):
        theta = math.radians(i)
        x1 = 0.3 * math.cos(theta)
        y1 = 0.3 * math.sin(theta)
        glVertex2f((x + x1 + 5), (y + y1 + 5))
    glEnd()
    glFlush()

    if theta1 >= 120:
        glColor(0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        angle = math.radians(theta1 - 30)
        x = 3 * math.cos(angle)
        y = 3 * math.sin(angle)
        glVertex2f(5, 5)
        glVertex2f((x + 5), (y + 5))
        glEnd()
        glColor(0.0, 1.0, 0.0)
        glBegin(GL_POLYGON)
        for i in range(0, 360, 1):
            theta = math.radians(i)
            x1 = 0.3 * math.cos(theta)
            y1 = 0.3 * math.sin(theta)
            glVertex2f((x + x1 + 5), (y + y1 + 5))
        glEnd()
        glFlush()

    if theta1 >= 150:
        glColor(0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        angle = math.radians(theta1 - 60)
        x = 3 * math.cos(angle)
        y = 3 * math.sin(angle)
        glVertex2f(5, 5)
        glVertex2f((x + 5), (y + 5))
        glEnd()
        glColor(0.0, 1.0, 0.0)
        glBegin(GL_POLYGON)
        for i in range(0, 360, 1):
            theta = math.radians(i)
            x1 = 0.3 * math.cos(theta)
            y1 = 0.3 * math.sin(theta)
            glVertex2f((x + x1 + 5), (y + y1 + 5))
        glEnd()
        glFlush()

    if theta1 >= 180:
        glColor(0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        angle = math.radians(theta1 - 90)
        x = 3 * math.cos(angle)
        y = 3 * math.sin(angle)
        glVertex2f(5, 5)
        glVertex2f((x + 5), (y + 5))
        glEnd()
        glColor(0.0, 1.0, 0.0)
        glBegin(GL_POLYGON)
        for i in range(0, 360, 1):
            theta = math.radians(i)
            x1 = 0.3 * math.cos(theta)
            y1 = 0.3 * math.sin(theta)
            glVertex2f((x + x1 + 5), (y + y1 + 5))
        glEnd()
        glFlush()

    glBegin(GL_LINES)
    glColor(0.0, 0.0, 1.0)
    angle = math.radians(theta2)
    x = 3 * math.cos(angle)
    y = 3 * math.sin(angle)
    glVertex2f(5, 5)
    glVertex2f((x + 5), (y + 5))
    glEnd()
    glColor(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(0, 360, 1):
        theta = math.radians(i)
        x1 = 0.3 * math.cos(theta)
        y1 = 0.3 * math.sin(theta)
        glVertex2f((x + x1 + 5), (y + y1 + 5))
    glEnd()
    glFlush()

    if theta2 <= 60:
        glColor(0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        angle = math.radians(theta2 + 30)
        x = 3 * math.cos(angle)
        y = 3 * math.sin(angle)
        glVertex2f(5, 5)
        glVertex2f((x + 5), (y + 5))
        glEnd()
        glColor(0.0, 1.0, 0.0)
        glBegin(GL_POLYGON)
        for i in range(0, 360, 1):
            theta = math.radians(i)
            x1 = 0.3 * math.cos(theta)
            y1 = 0.3 * math.sin(theta)
            glVertex2f((x + x1 + 5), (y + y1 + 5))
        glEnd()
        glFlush()

    if theta2 <= 30:
        glColor(0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        angle = math.radians(theta2 + 60)
        x = 3 * math.cos(angle)
        y = 3 * math.sin(angle)
        glVertex2f(5, 5)
        glVertex2f((x + 5), (y + 5))
        glEnd()
        glColor(0.0, 1.0, 0.0)
        glBegin(GL_POLYGON)
        for i in range(0, 360, 1):
            theta = math.radians(i)
            x1 = 0.3 * math.cos(theta)
            y1 = 0.3 * math.sin(theta)
            glVertex2f((x + x1 + 5), (y + y1 + 5))
        glEnd()
        glFlush()
    body()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Peacock")

    glutDisplayFunc(peacock)
    glutTimerFunc(0, update, 0)
    clearscreen()
    glutMainLoop()


if __name__ == "__main__":
    main()
