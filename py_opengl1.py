from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.glut import *
def display
  glclear(GL_COLOR_BUFFUER_BIT)
	glutSolidSphere(0.5,20,20)
	glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowPosition(100,100)
glutInitWindowSize(400,400)
glutDisplayFunc(display)
glutMainLoop()
