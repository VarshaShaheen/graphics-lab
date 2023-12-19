from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

sys.setrecursionlimit(1000000)


def clearscreen():
    gluOrtho2D(0, 500, 0, 500)


def getpixel(x, y):
    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    print(color)
    return color[0][0]


def setPixel(x, y, color):
    print("Entered setPixel")
    glPointSize(8)
    glColor(*color)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def floodFill(x, y, old_color, new_color):
    current_color = getpixel(x, y)
    if all(current_color == old_color):
        setPixel(x, y, new_color)
        floodFill(x - 8, y, old_color, new_color)
        floodFill(x + 8, y, old_color, new_color)
        floodFill(x, y - 8, old_color, new_color)
        floodFill(x, y + 8, old_color, new_color)


def rectangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(100, 100)
    glVertex2f(300, 100)
    glVertex2f(300, 300)
    glVertex2f(100, 300)
    glEnd()
    glFlush()


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print("mouse detected")
        y = 500 - y
        old_color = getpixel(x, y)
        floodFill(x, y, old_color, [0.0, 1.0, 0.0])


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Rectangle")

    glutDisplayFunc(rectangle)
    glutMouseFunc(mouse)
    clearscreen()
    glutMainLoop()


if __name__ == "__main__":
    main()
