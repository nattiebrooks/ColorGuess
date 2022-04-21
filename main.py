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
RECT_WIDTH = 150
RECT_HEIGHT = 150
RECT_SPACE = 50

RECT_ROW_ONE_Y = 150
RECT_ROW_TWO_Y = 350


rect1 = pygame.Rect(140, RECT_ROW_ONE_Y, RECT_WIDTH, RECT_HEIGHT)
rect2 = pygame.Rect(320, RECT_ROW_ONE_Y, RECT_WIDTH, RECT_HEIGHT)
rect3 = pygame.Rect(500, RECT_ROW_ONE_Y, RECT_WIDTH, RECT_HEIGHT)


rect4 = pygame.Rect(140, RECT_ROW_TWO_Y, RECT_WIDTH, RECT_HEIGHT)
rect5 = pygame.Rect(320, RECT_ROW_TWO_Y, RECT_WIDTH, RECT_HEIGHT)
rect6 = pygame.Rect(500, RECT_ROW_TWO_Y, RECT_WIDTH, RECT_HEIGHT)

NUMBER_OF_SQUARES = 6
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

GAME_TITLE = 'Color Guessing Game'
FONT = pygame.font.SysFont(None, 32)
TILE_FIELD = FONT.render(GAME_TITLE, True, WHITE)
TILE_X = 450
TILE_Y = 50

GAME_INSTRUCTIONS = '''Instructions:\nGuess which square is the color of\nthe rgb code listed below. Guessing\ncorrectly will color the background\nthe same color as the square.'''
INSTRUCTIONS_X = 800
INSTRCUTIONS_Y = 150
INSTRUCTIONS_FIELD = FONT.render(GAME_INSTRUCTIONS, True,WHITE)
# BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.png'))

COLOR_TO_GUESS = ""
COLOR_TO_GUESS_X = 800
COLOR_TO_GUESS_Y = 300
COLOR_TO_GUESS_FIELD = FONT.render(COLOR_TO_GUESS, True, WHITE)
FPS = 60

BORDER = pygame.Rect((SCREEN_WIDTH / 2) -5, 0, 10, SCREEN_HEIGHT)



def draw_window(color, color2, color3, color4, color5, color6):
    COLOR_TO_GUESS_FIELD = FONT.render(str(color6), True, WHITE)
    
    SCREEN.fill(BACKGROUND_COLOR)
    SCREEN.blit(TILE_FIELD, (TILE_X, TILE_Y))
    # SCREEN.blit(INSTRUCTIONS_FIELD, (INSTRUCTIONS_X,INSTRCUTIONS_Y))
    render_multi_line(GAME_INSTRUCTIONS, INSTRUCTIONS_X, INSTRCUTIONS_Y, 18 ,WHITE)
    SCREEN.blit(COLOR_TO_GUESS_FIELD, (COLOR_TO_GUESS_X,COLOR_TO_GUESS_Y))
    
    pygame.draw.rect(SCREEN, color, rect1)
    pygame.draw.rect(SCREEN, color2, rect2)
    pygame.draw.rect(SCREEN, color3, rect3)
    
    pygame.draw.rect(SCREEN, color4, rect4)
    pygame.draw.rect(SCREEN, color5, rect5)
    pygame.draw.rect(SCREEN, color6, rect6)
    
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

def mouse_clicks_square():
    x,y = pygame.mouse.get_pos()
    # print ('absolute:', x,y)
    # if x > rect1.width/2 and y > rect1.height/2:
    squares = [rect1, rect2, rect3, rect4, rect5, rect6]
    for square in squares:
        if pygame.Rect.collidepoint(square, (x,y)):
            print('square clicked')
            print(square)
  

def render_multi_line(text, x, y, fsize,color):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            SCREEN.blit(FONT.render(l, 0, color), (x, y + fsize*i))
                  
        
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
            # x,y = pygame.mouse.get_pos()
            # print the 'absolute' mouse position (relative to the screen)
            # print ('absoulte:', x,y)
            draw_window(color, color2, color3, color4, color5, color)
            handled = False
            if pygame.mouse.get_pressed()[0] and not handled:
                # print('click!')
                # if pygame.Rect.collidepoint(pygame.mouse.get_pos()):
                    # print('rect clicked')
                mouse_clicks_square()
                handled = pygame.mouse.get_pressed()[0]
                
    pygame.quit()
    sys.exit()
                    



if __name__ == "__main__":
    main()