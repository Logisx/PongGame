import pygame
from pong.game import Game

FPS = 120
width, height = 700, 500

def game_loop(window):
    clock = pygame.time.Clock()
    game = Game(window)
    run = True
    game.start()

    while run:
        clock.tick(FPS)
        start_new_game = game.move()
        if start_new_game:
            return True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            game.wall.left_y -= 4
        elif keys[pygame.K_s]:
            game.wall.left_y += 4
        
        if keys[pygame.K_UP]:
            game.wall.right_y -= 4
        elif keys[pygame.K_DOWN]:
            game.wall.right_y += 4
        
        pygame.display.update()

    pygame.quit()
    return None

def main():
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pong')
    pygame.font.init()

    while game_loop(window):
        game_loop(window)
    

main()