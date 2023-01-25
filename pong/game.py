import pygame
import sys
from .ball import Ball
from .wall import Wall

class Game():

    def __init__(self, win):
        self.win = win
        self.start_new_game = False
        self.score_left = 0
        self.score_right = 0
    
    def start(self):
        self.ball = Ball(self.win)
        self.wall = Wall(self.win)
        self.ball.start()

    def move(self):
        self.draw_field()
        self.wall.draw()
        self.check_wall_reflection()
        self.check_borders_reflection()
        self.ball.move()
        goal = self.check_winner()
        if goal:
            self.check_end()
            if self.start_new_game == True:
                return True
            self.ball.speed = (5 + (self.score_left + self.score_right) // 2) // 2
            self.ball.reload()
        return None

    def check_borders_reflection(self):
        if self.ball.y + self.ball.direction_y >= 495: 
            self.ball.y = 495
            self.ball.direction_y = -self.ball.direction_y
            self.increase_speed()
        elif self.ball.y + self.ball.direction_y <= 5:
            self.ball.y = 5
            self.ball.direction_y = -self.ball.direction_y
            self.increase_speed()

    def check_wall_reflection(self):
        if self.ball.x <= 350:
            wall_surface = (self.wall.left_y, self.wall.left_y + self.wall.wall_height)
            if ((self.ball.x + self.ball.direction_x) - (10 + self.wall.wall_width)) <= 5 \
                and (wall_surface[0] <= (self.ball.y + self.ball.direction_y) <= wall_surface[1]):
                    self.ball.direction_x = -self.ball.direction_x
                    self.increase_speed()
        else:
            wall_surface = (self.wall.right_y, self.wall.right_y + self.wall.wall_height)
            if ((700 - 10 - self.wall.wall_width) - (self.ball.x + self.ball.direction_x)) <= 5 \
                and (wall_surface[0] <= (self.ball.y + self.ball.direction_y) <= wall_surface[1]):
                    self.ball.direction_x = -self.ball.direction_x
                    self.increase_speed()

    def increase_speed(self):
        if self.ball.speed < 10:
            koef = 0.5
            self.ball.direction_x = self.ball.direction_x * (self.ball.speed + koef) / self.ball.speed
            self.ball.direction_y = self.ball.direction_y * (self.ball.speed + koef) / self.ball.speed
            self.ball.speed += koef


    def check_winner(self):
        if self.ball.x <= 5:
            self.ball.left_made_goal = False
            self.score_right += 1
            return True
        elif self.ball.x >= 695:
            self.ball.left_made_goal = True
            self.score_left += 1
            return True
        return False
        
    def check_end(self):
        if self.score_left == 10:
            self.end_game('Left win!')
            return None
        elif self.score_right == 10:
            self.end_game('Right win!')
            return None
        return None

    def end_game(self, winner):
        self.win.fill((0, 0, 0))
        my_font1 = pygame.font.SysFont('impact', 60)
        text1_width, text1_height = my_font1.size(winner)
        text1_surface = my_font1.render(winner, False, (255, 255, 255))
        self.win.blit(text1_surface, (350 - text1_width // 2, 240 - text1_height))
        
        my_font2 = pygame.font.SysFont('impact', 30)
        text2_width, text2_height = my_font2.size('Press N to start again, Q to exit')
        text2_surface = my_font2.render('Press N to start again, Q to exit', False, (255, 255, 255))
        self.win.blit(text2_surface, (350 - text2_width // 2, 270))

        pygame.display.update()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_n]:
                run = False
                self.start_new_game = True
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit(0)
         
        return None

    def draw_field(self):
        self.win.fill((0, 0, 0))
        for i in range(7):
            pygame.draw.rect(self.win, (255, 255, 255), (347, 20 + i*70, 6, 40))
        my_font = pygame.font.SysFont('impact', 60)
        text_width, text_height = my_font.size(str(self.score_left))
        text_surface_left = my_font.render(str(self.score_left), False, (255, 255, 255))
        text_surface_right = my_font.render(str(self.score_right), False, (255, 255, 255))
        self.win.blit(text_surface_left, (350 // 2 - text_width // 2, 20))
        self.win.blit(text_surface_right, (350 + 175 - text_width // 2, 20))