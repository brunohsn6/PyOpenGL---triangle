from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import shaders
import numpy as np

VERTEX_SHADER = """
#version 330

in vec4 position;

void main(){

gl_Position = position;

}
"""

FRAGMENT_SHADER = """
#version 330

void main(){

gl_FragColor=vec4(1.0f, 0.0f, 0.0f, 1.0f);

}
"""

shaderProgram: None = None


def initialize():
    global VERTEX_SHADER
    global FRAGMENT_SHADER
    global shaderProgram

    vertexShader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fragmentShader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)

    shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)
    triangles = [-0.5, -0.5, 0.0,
                 0.5, -0.5, 0.0,
                 0.0, 0.5, 0.0]
    triangles = np.array(triangles, dtype=np.float32)

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, triangles.nbytes, triangles, GL_STATIC_DRAW)

    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(position)


def render():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glUseProgram(shaderProgram)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glUseProgram(0)
    glutSwapBuffers()



def main():
    glutInit()

    glutInitWindowSize(680, 500)
    glutInitWindowPosition(200, 200)
    glutCreateWindow("task opengl Square-   Triangle")
    initialize()
    glutDisplayFunc(render)

    glutMainLoop()


if __name__ == "__main__":
    main()
