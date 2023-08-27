import math
import numpy as np


def move_axis(pos):
    """МАТРИЦА ПЕРЕМЕЩЕНИЯ"""
    tx, ty, tz = pos
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])


def move_around_x(a):
    """МАТРИЦА ВРАЩЕНИЯ ПО X"""
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(a), math.sin(a), 0],
        [0, -math.sin(a), math.cos(a), 0],
        [0, 0, 0, 1]
    ])


def move_around_y(a):
    """МАТРИЦА ВРАЩЕНИЯ ПО Y"""
    return np.array([
        [math.cos(a), 0, -math.sin(a), 0],
        [0, 1, 0, 0],
        [math.sin(a), 0, math.cos(a), 0],
        [0, 0, 0, 1]
    ])


def move_around_z(a):
    """МАТРИЦА ВРАЩЕНИЯ ПО Z"""
    return np.array([
        [math.cos(a), math.sin(a), 0, 0],
        [-math.sin(a), math.cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def scale(n):
    """МАТРИЦА МАШТАБИРОВАНИЯ"""
    return np.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]
    ])