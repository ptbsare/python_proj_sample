from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glutWireTeapot(0.5)
	glFlush()
def idle():
	glRotate(0.000,1.0,1.0,1.0)	
	display()
glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowPosition(100,100)
glutInitWindowSize(400,400)
glutCreateWindow("py_opengl")
glutDisplayFunc(display)
glutIdleFunc(idle)
glutMainLoop()
