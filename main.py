import pygame, sys, os

#Pygame setup
pygame.font.init()
pygame.mixer.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("My Basic Shooter")

# Defaults for the game
BACKGROUND_COLOR = (5,163,251)
RECT_COLOR = (14,16,18)

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.png'))
FPS = 60

BORDER = pygame.Rect((SCREEN_WIDTH / 2) -5, 0, 10, SCREEN_HEIGHT)



def draw_window():
    SCREEN.fill(BACKGROUND_COLOR)
    # SCREEN.blit(BACKGROUND_IMAGE, (0,0))
    pygame.draw.rect(SCREEN, RECT_COLOR, BORDER)

        
    pygame.display.update()

    
    
def main():

    
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
                
    pygame.quit()
    sys.exit()
                    



if __name__ == "__main__":
    main()