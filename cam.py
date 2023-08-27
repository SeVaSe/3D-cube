import pygame as pg
from matrich_file import *


class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = np.array([*position, 1.0])  # начальная похиция камеры
        self.forw = np.array([0,0,1,1])  # z
        self.up = np.array([0, 1, 0, 1])  # y
        self.right = np.array([1,0,0,1])  # x
        self.h_vid = math.pi / 3  # горизонталь камеры
        self.v_vid = self.h_vid * (render.HEIGHT / render.WIDTH)  # вертикаль камеры
        self.near_plosk = 0.1
        self.far_plosk = 100
        self.moving_speed = 0.1
        self.rotation_speed = 0.015

    def control(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.position -= self.right * self.moving_speed
        if key[pg.K_d]:
            self.position += self.right * self.moving_speed
        if key[pg.K_w]:
            self.position += self.forw * self.moving_speed
        if key[pg.K_s]:
            self.position -= self.forw * self.moving_speed
        if key[pg.K_q]:
            self.position += self.up * self.moving_speed
        if key[pg.K_e]:
            self.position -= self.up * self.moving_speed

        if key[pg.K_LEFT]:
            self.camera_yaw(-self.rotation_speed)
        if key[pg.K_RIGHT]:
            self.camera_yaw(self.rotation_speed)
        if key[pg.K_UP]:
            self.camera_pit(-self.rotation_speed)
        if key[pg.K_DOWN]:
            self.camera_pit(self.rotation_speed)

    def camera_yaw(self, angle):
        rotate = move_around_y(angle)
        self.forw = self.forw @ rotate
        self.up = self.up @ rotate
        self.right = self.right @ rotate

    def camera_pit(self, angle):
        rotate = move_around_x(angle)
        self.forw = self.forw @ rotate
        self.up = self.up @ rotate
        self.right = self.right @ rotate

    def move_matrix(self):
        """МАТРИЦА ПЕРЕМЕЩЕНИЯ"""
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotate_matrix(self):
        """МАТРИЦА ВРАЩЕНИЯ"""
        rx, ry, rz, rw = self.right
        fx, fy, fz, rw = self.forw
        ux, uy, uz, uw = self.up

        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_matrix(self):
        return self.move_matrix() @ self.rotate_matrix()  # перемещение камеры в пространство, как я понял