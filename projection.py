import numpy as np
import math


class Projection:
    """ПРОЕКЦИЯ"""
    def __init__(self, render):
        NEAR = render.camera.near_plosk  # представляет значение ближней плоскости проекции (ближней границы "видимости")
        FAR = render.camera.far_plosk  # представляет значение дальней плоскости проекции (дальней границы "видимости")
        RIGHT = math.tan(render.camera.h_vid / 2)  # горизонтальный угол обзора камеры
        LEFT = -RIGHT
        TOP = math.tan(render.camera.v_vid / 2)  # вертикальный угол обзора камеры
        BOTTOM = -TOP

        # НАЧИНАЕТ ЛЮТЫЙ П*****
        ## эта часть тупа для облегчения написания формулы матрицы проекции
        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        ##

        # матрица проекции
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        HW, HH = render.WIDTH // 2, render.HEIGHT // 2
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])

