import numpy as np

# Problema 1: Documentacion
def area_circulo(radio: float) -> float:
    """
    Calcula el area de un circulo dado su radio.
    Parametros:
    radio (float): Radio del circulo.
    Retorna:
    float: Area del circulo.
    """
    area = np.pi * radio**2
    return area

# Problema 2: Matriz de rotacion
def rot_x(x, y, z, angle, axis='x'):
    """
    Rota un punto (x, y, z) alrededor del eje x por un ángulo dado en grados.
    Parametros:
    x (float): Coordenada x del punto.
    y (float): Coordenada y del punto.
    z (float): Coordenada z del punto.
    angle (float): Ángulo de rotación en grados.
    axis (str): Eje de rotación; debe ser 'x' para esta función.
    Retorna:
    np.array: Nuevo punto rotado como un array numpy.
    """
    punto = np.array([x, y, z])
    theta = np.radians(angle)
    Rx = np.array([
        [1, 0,           0          ],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return Rx @ punto

def rot_y(x, y, z, angle, axis='y'):
    """
    Rota un punto (x, y, z) alrededor del eje y por un ángulo dado en grados.
    Parametros:
    x (float): Coordenada x del punto.
    y (float): Coordenada y del punto.
    z (float): Coordenada z del punto.
    angle (float): Ángulo de rotación en grados.
    axis (str): Eje de rotación; debe ser 'y' para esta función.
    Retorna:
    np.array: Nuevo punto rotado como un array numpy.
    """
    punto = np.array([x, y, z])
    theta = np.radians(angle)
    Ry = np.array([
        [ np.cos(theta), 0, -np.sin(theta)],
        [ 0,           1, 0          ],
        [np.sin(theta), 0, np.cos(theta)]
    ])
    return Ry @ punto

def rot_z(x, y, z, angle, axis='z'):
    """
    Rota un punto (x, y, z) alrededor del eje z por un ángulo dado en grados.
    Parametros:
    x (float): Coordenada x del punto.
    y (float): Coordenada y del punto.
    z (float): Coordenada z del punto.
    angle (float): Ángulo de rotación en grados.
    axis (str): Eje de rotación; debe ser 'z' para esta función.
    Retorna:
    np.array: Nuevo punto rotado como un array numpy.
    """
    punto = np.array([x, y, z])
    theta = np.radians(angle)
    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,           0,          1]
    ])
    return Rz @ punto

def rotar(x, y, z, angle, axis):
    """
    Rota un punto (x, y, z) alrededor de un eje especificado ('x', 'y', o 'z') por un ángulo dado en grados.
    Parametros:
    x (float): Coordenada x del punto.
    y (float): Coordenada y del punto.
    z (float): Coordenada z del punto.
    angle (float): Ángulo de rotación en grados.
    axis (str): Eje de rotación; puede tomar valor 'x', 'y' o 'z'.
    Retorna:
    np.array: Nuevo punto rotado como un array numpy.
    """
    if axis == 'x':
        return rot_x(x, y, z, angle)
    elif axis == 'y':
        return rot_y(x, y, z, angle)
    elif axis == 'z':
        return rot_z(x, y, z, angle)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'.")
    
    
# Problema 3: Wrapper
def rotate_point_wrapper(x, y, z, angle, axis):
    """
    Wrapper para rotar un punto en 3D.
    Parametros:
    x, y, z: Coordenadas del punto.
    angle: Ángulo de rotación en grados.
    axis: Eje de rotación ('x', 'y', 'z').
    f: insertar valor de variable a expresiones dentro de cadenas de texto
    Retorna:
    np.array: Punto rotado.
    """
    punto_rotado = rotar(x, y, z, angle, axis)
    print(f"Punto original: ({x}, {y}, {z})")
    print(f"Punto rotado ({angle}° alrededor de '{axis}'): {punto_rotado}")
    return punto_rotado


rotate_point_wrapper(3, 3, 3, 100, 'x')
rotate_point_wrapper(3, 3, 3, 100, 'y')
rotate_point_wrapper(3, 3, 3, 100, 'z')