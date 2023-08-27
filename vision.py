import cv2
import OpenGL
import numpy as np
import pygame as pg
from cam import Camera
from projection import Projection
from object_create import Object
import math

class SoftRender:
    def __init__(self):
        pg.init()  # инициализатор pegame
        self.RES = self.WIDTH, self.HEIGHT = 1200, 700  # расширение окна
        self.H_WIDTH, H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2  # половинки окна
        self.FPS = 60  # макс количество фпс
        self.screen = pg.display.set_mode(self.RES)  # установка окна
        self.clock = pg.time.Clock()  # управление временем и установления стабильного фпс в сек
        self.create_objects()  # инициализатор метода создания объектов

    def create_objects(self):
        """СОЗДАНИЕ ОБЪЕКТОВ НА ЭКРАНЕ"""
        self.camera = Camera(self, [0.5, 1, 1])
        self.proj = Projection(self)
        self.object = Object(self)
        self.object.move([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 6)

    def draw(self):
        """ГРАФИКА"""
        self.screen.fill(pg.Color('black'))
        self.object.draw()

    def run(self):
        """СТАРТ"""
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]  # если обнаружен какой то тип-закрытия, вызывается exit()
            pg.display.set_caption(str(self.clock.get_fps()))  # fps в заголовок окна
            pg.display.flip()  # обновление содержимого окна, обновляет изменения
            self.clock.tick(self.FPS)  # ограничивает выполнение программы так, чтобы она не выполнялась быстрее


if __name__ == '__main__':
    app = SoftRender()
    app.run()





