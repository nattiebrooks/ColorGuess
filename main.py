import pygame, sys, os

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

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

GAME_TITLE = 'Color Guessing Game'


# BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.png'))
FPS = 60

BORDER = pygame.Rect((SCREEN_WIDTH / 2) -5, 0, 10, SCREEN_HEIGHT)



def draw_window():
    SCREEN.fill(BACKGROUND_COLOR)
    pygame.draw.rect(SCREEN,WHITE, pygame.Rect(130, 130, 200, 200))
        
    pygame.display.update()

    
 
    
def main():

    
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
            draw_window()
                
    pygame.quit()
    sys.exit()
                    



if __name__ == "__main__":
    main()