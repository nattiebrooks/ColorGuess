import pygame, sys, os
import random

#Pygame setup
pygame.font.init()
pygame.mixer.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Color Guessing Game!")

# Defaults for the game
BACKGROUND_COLOR = (5,163,251)
RECT_COLOR = (14,16,18)
RECT_WIDTH = 100
RECT_HEIGHT = 100
RECT_SPACE = 50

NUMBER_OF_SQUARES = 6
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

GAME_TITLE = 'Color Guessing Game'
FONT = pygame.font.SysFont(None, 32)
TILE_FIELD = FONT.render(GAME_TITLE, True, WHITE)
TILE_X = 450
TILE_Y = 50
# BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.png'))
FPS = 60

BORDER = pygame.Rect((SCREEN_WIDTH / 2) -5, 0, 10, SCREEN_HEIGHT)



def draw_window(color, color2, color3, color4, color5, color6):
    SCREEN.fill(BACKGROUND_COLOR)
    SCREEN.blit(TILE_FIELD, (TILE_X, TILE_Y))
    pygame.draw.rect(SCREEN, color, pygame.Rect(140, 100, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(SCREEN, color2, pygame.Rect(300, 100, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(SCREEN, color3, pygame.Rect(460, 100, RECT_WIDTH, RECT_HEIGHT))
    
    
    pygame.draw.rect(SCREEN, color4, pygame.Rect(140, 300, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(SCREEN, color5, pygame.Rect(300, 300, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(SCREEN, color6, pygame.Rect(460, 300, RECT_WIDTH, RECT_HEIGHT))
    
    pygame.display.update()

    
def create_all_colors():
    color = (generate_random_color(), generate_random_color(), generate_random_color())
    color2 = (generate_random_color(), generate_random_color(), generate_random_color())
    color3 = (generate_random_color(), generate_random_color(), generate_random_color())
    
    color4 = (generate_random_color(), generate_random_color(), generate_random_color())
    color5 = (generate_random_color(), generate_random_color(), generate_random_color())
    color6 = (generate_random_color(), generate_random_color(), generate_random_color())
    
    return color,color2, color3,color4, color5,color6

def generate_random_color():
     random_value = random.randrange(0,256)
     return random_value
    
def main():
    
    color = (generate_random_color(), generate_random_color(), generate_random_color())
    color2 = (generate_random_color(), generate_random_color(), generate_random_color())
    color3 = (generate_random_color(), generate_random_color(), generate_random_color())
    
    color4 = (generate_random_color(), generate_random_color(), generate_random_color())
    color5 = (generate_random_color(), generate_random_color(), generate_random_color())
    color6 = (generate_random_color(), generate_random_color(), generate_random_color())
    
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False     
            draw_window(color, color2, color3, color4, color5, color6)
                
    pygame.quit()
    sys.exit()
                    



if __name__ == "__main__":
    main()