import pygame as pg


from matrich_file import *
import numpy as np


class Object:
    def __init__(self, render):
        self.render = render
        self.vershina = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                  (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)], dtype=np.float64)
        self.grani = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (1, 5, 6, 2), (0, 4, 7, 3), (2, 6, 3, 7)]

    def draw(self):
        self.screen_proj()

    def screen_proj(self):
        # Apply camera matrix and projection matrix
        vershina = self.vershina @ self.render.camera.camera_matrix()
        vershina = vershina @ self.render.proj.projection_matrix

        # Perspective divide
        vershina /= vershina[:, -1].reshape(-1, 1)

        # Apply screen transformation matrix
        vershina = vershina @ self.render.proj.to_screen_matrix
        vershina = vershina[:, :2]

        w, h = self.render.RES

        for gr in self.grani:
            polygon = [vershina[index] for index in gr]
            if not (np.any(polygon == w // 2) | (polygon == h // 2)):
                pg.draw.polygon(self.render.screen, pg.Color('blue'), polygon, 3)

        for vr in vershina:
            if not (np.any(vr == w // 2) or np.any(vr == h // 2)):
                pg.draw.circle(self.render.screen, pg.Color('red'), vr.astype(int), 6)

    def move(self, pos):
        self.vershina = self.vershina @ move_axis(pos)

    def scale_o(self, scale_to):
        self.vershina = self.vershina @ scale(scale_to)

    def rotate_x(self, angle):
        self.vershina = self.vershina @ move_around_x(angle)

    def rotate_y(self, angle):
        self.vershina = self.vershina @ move_around_y(angle)

    def rotate_z(self, angle):
        self.vershina = self.vershina @ move_around_z(angle)