import pygame

class Wall():
    
    def __init__(self, win):
        self.win = win
        self.wall_height = 90
        self.wall_width = 15
        self.left_y = 225
        self.right_y = 225

    def draw(self):
        if self.left_y > 405:
            self.left_y = 405
        elif self.left_y < 5:
            self.left_y = 5
        
        if self.right_y > 405:
            self.right_y = 405
        elif self.right_y < 5:
            self.right_y = 5
        
        pygame.draw.rect(self.win, (255, 255, 255), (10, self.left_y, self.wall_width, self.wall_height))
        pygame.draw.rect(self.win, (255, 255, 255), (700 - self.wall_width - 10, self.right_y, self.wall_width, self.wall_height))