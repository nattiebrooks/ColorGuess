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

x1 = 140
x2 = 320
x3 = 500

rect1 = pygame.Rect(x1, RECT_ROW_ONE_Y, RECT_WIDTH, RECT_HEIGHT)
rect2 = pygame.Rect(x2, RECT_ROW_ONE_Y, RECT_WIDTH, RECT_HEIGHT)
rect3 = pygame.Rect(x3, RECT_ROW_ONE_Y, RECT_WIDTH, RECT_HEIGHT)

rect4 = pygame.Rect(x1, RECT_ROW_TWO_Y, RECT_WIDTH, RECT_HEIGHT)
rect5 = pygame.Rect(x2, RECT_ROW_TWO_Y, RECT_WIDTH, RECT_HEIGHT)
rect6 = pygame.Rect(x3, RECT_ROW_TWO_Y, RECT_WIDTH, RECT_HEIGHT)


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
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

COLOR_TO_GUESS = ""
COLOR_TO_GUESS_X = 800
COLOR_TO_GUESS_Y = 300
COLOR_TO_GUESS_FIELD = FONT.render(COLOR_TO_GUESS, True, WHITE)
FPS = 60

BORDER = pygame.Rect((SCREEN_WIDTH / 2) -5, 0, 10, SCREEN_HEIGHT)

color_to_guess = random.randrange(0,6)

squares = [rect1, rect2, rect3, rect4, rect5, rect6]


def draw_window(color1, color2, color3, color4, color5, color6, color_to_guess, colors):
    
    
    COLOR_TO_GUESS_FIELD = FONT.render(str(colors[color_to_guess]), True, WHITE)
    
    SCREEN.fill(BACKGROUND_COLOR)
    SCREEN.blit(TILE_FIELD, (TILE_X, TILE_Y))
    render_multi_line(GAME_INSTRUCTIONS, INSTRUCTIONS_X, INSTRCUTIONS_Y, 18 ,WHITE)
    SCREEN.blit(COLOR_TO_GUESS_FIELD, (COLOR_TO_GUESS_X,COLOR_TO_GUESS_Y))
    
    pygame.draw.rect(SCREEN, color1, rect1)
    pygame.draw.rect(SCREEN, color2, rect2)
    pygame.draw.rect(SCREEN, color3, rect3)
    
    pygame.draw.rect(SCREEN, color4, rect4)
    pygame.draw.rect(SCREEN, color5, rect5)
    pygame.draw.rect(SCREEN, color6, rect6)
    

    pygame.display.update()

    
def create_all_colors():
    color1 = (generate_random_color(), generate_random_color(), generate_random_color())
    color2 = (generate_random_color(), generate_random_color(), generate_random_color())
    color3 = (generate_random_color(), generate_random_color(), generate_random_color())
    
    color4 = (generate_random_color(), generate_random_color(), generate_random_color())
    color5 = (generate_random_color(), generate_random_color(), generate_random_color())
    color6 = (generate_random_color(), generate_random_color(), generate_random_color())
    
    
def generate_random_color():
     random_value = random.randrange(0,256)
     return random_value

def mouse_clicks_square(colors):
    x,y = pygame.mouse.get_pos()
    pixel_col = pygame.Surface.get_at(SCREEN, (x, y))
    print(pixel_col)
    for square in squares:
        if pygame.Rect.collidepoint(square, (x,y)):
            print('square clicked')
            if(pixel_col == colors[color_to_guess]):
                print(square)
                SCREEN.fill(colors[color_to_guess])
                pygame.display.update()
                draw_winner_text(str(colors[color_to_guess]))
                break
            else:
                square.size = (0,0)
  

def render_multi_line(text, x, y, fsize,color):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            SCREEN.blit(FONT.render(l, 0, color), (x, y + fsize*i))
                  
def draw_winner_text(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    SCREEN.blit(draw_text, (SCREEN_WIDTH/2 - draw_text.get_width() /
                         2, SCREEN_HEIGHT/2 - draw_text.get_height()/2))  
    pygame.display.update()
    pygame.time.delay(5000)
         
def main():
    
    color1 = (generate_random_color(), generate_random_color(), generate_random_color())
    color2 = (generate_random_color(), generate_random_color(), generate_random_color())
    color3 = (generate_random_color(), generate_random_color(), generate_random_color())
    
    color4 = (generate_random_color(), generate_random_color(), generate_random_color())
    color5 = (generate_random_color(), generate_random_color(), generate_random_color())
    color6 = (generate_random_color(), generate_random_color(), generate_random_color())
    
    colors = [color1, color2, color3, color4, color5, color6]
    
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    

            draw_window(color1, color2, color3, color4, color5, color6, color_to_guess,colors)
            handled = False
            if pygame.mouse.get_pressed()[0] and not handled:
                mouse_clicks_square(colors)
                handled = pygame.mouse.get_pressed()[0]
                
    pygame.quit()
    sys.exit()
                    



if __name__ == "__main__":
    main()