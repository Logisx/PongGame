import pygame
import math
from random import randint


class Ball():

    def __init__(self, win):
        self.win = win
        self.x = 350
        self.y = 250
        self.direction_x = 0
        self.direction_y = 0
        self.speed = 2.5
        self.left_made_goal = None

    def start(self):
        self.reload()

    def move(self):
        self.x += self.direction_x
        self.y += self.direction_y
        self.draw()

    def reload(self):
        self.x = 350
        self.y = 250
        self.draw()
        self.choose_direction()

    def draw(self):
        pygame.draw.circle(self.win, (255, 255, 255), (self.x, self.y), 10)

    def choose_direction(self):
        if self.left_made_goal == None:
            self.left_made_goal = randint(0,1)
        negative_degree = randint(0, 1)
        if negative_degree:
            degree = randint(-45, -10)
        else:
            degree = randint(10, 45)
        radians = math.radians(degree)
        self.direction_x = (-1)*self.speed * math.cos(radians)
        self.direction_y = self.speed * math.sin(radians)
            
        if self.left_made_goal:
            self.direction_x = -self.direction_x
        