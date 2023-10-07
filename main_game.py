import pygame
import random
import time
import sys

#Music initialiser
pygame.mixer.init()
pygame.init()

# Creating Display
screen_width = 900
screen_length = 600
screen_size = (screen_width,screen_length)
game_display = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Background images
img1 = pygame.image.load("home_page.png")
img1 = pygame.transform.scale(img1, (screen_width, screen_length)).convert_alpha()

img2 = pygame.image.load("about.png")
img2 = pygame.transform.scale(img2, (screen_width, screen_length)).convert_alpha()

img_level = pygame.image.load("level.png")
img_level = pygame.transform.scale(img_level, (screen_width, screen_length)).convert_alpha()

img_easy = pygame.image.load("easy.png")
img_easy = pygame.transform.scale(img_easy, (screen_width, screen_length)).convert_alpha()

img_medium = pygame.image.load("medium.png")
img_medium = pygame.transform.scale(img_medium, (screen_width, screen_length)).convert_alpha()


img_hard = pygame.image.load("hard.png")
img_hard = pygame.transform.scale(img_hard, (screen_width, screen_length)).convert_alpha()

img_game_over = pygame.image.load("game_over.png")
img_game_over = pygame.transform.scale(img_game_over, (screen_width, screen_length)).convert_alpha()

pygame.display.update()


#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
grey = (200, 200, 200)
blue = (0, 0, 255)
creme = (255, 253, 208)

#Text Printer
def screen_text(str, color, x, y, size): 
    Font = pygame.font.SysFont('gabriola', size)
    text = Font.render(str, True, color)
    game_display.blit(text, [x, y])

# To create a long snake we need to draw
# the snake rect again and again and also 
# delete the position outside of its lenght
def long_snake(window, color, list1, size):
    for x, y in list1:
       pygame.draw.rect(window, color, [x, y, size, size])

def home_page():
    exit_welcome = False
    while not exit_welcome:
        game_display.fill(white)
        game_display.blit(img1, (0, 0))
        screen_text("GDSC App Development Submission", blue, 0, 0,  40)
        about_rect = pygame.draw.rect(game_display, red, [760, 475, 100, 30])
        screen_text("About", blue, 780, 480, 25)
        while True: 
            for event in pygame.event.get(): 
        
            # if user types QUIT then the screen will close 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit() 
        
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if about_rect.collidepoint(event.pos): 
                        about()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or pygame.K_KP_ENTER:
                        level_screen()

            pygame.display.update()
            clock.tick(60)



def about():
    game_display.fill(white)
    game_display.blit(img2, (0, 0))
    screen_text("GDSC App Development Submission", (100,100,100), 200, 550,  40)
    screen_text('WELCOME TO SNAKE GAME', white, 250, 100, 40)
    headline = "Here we will learn about how to play this game. Let's get you started:"
    screen_text(headline, black, 100, 200, 20)
    lines = ["1. The purpose in this game is to eat the food and create the highest score.",
             "2. Use arrow keys to change the direction of snake while moving.",
             "3. The more food you eat, the more will be snake speed and length.",
             "4. If you bust yourself against the walls or your own body the game will be over.",
             "5. Keep in mind ,while moving in one direction don't press the arrrow key of",
             "     opposite direction, the game will be over."]
    x = 50
    for line in lines:
        screen_text(line, white, 100, 200+x, 30)
        x+=30
    back_rect = pygame.draw.rect(game_display, grey, [0, 0, 80, 30])
    screen_text("BACK", blue, 20, 8, 20)
    while True: 
        for event in pygame.event.get(): 
    
        # if user types QUIT then the screen will close 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
    
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if back_rect.collidepoint(event.pos): 
                    home_page()

        pygame.display.update()

def level_screen():
    game_display.fill(white)
    game_display.blit(img_level, (0,0))
    screen_text("GDSC App Development Submission", blue, 200, 550,  40)

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos): 
                    game_loop(0.3, img_easy, "1")

                elif medium_rect.collidepoint(event.pos): 
                    game_loop(0.6, img_medium, "2")

                elif hard_rect.collidepoint(event.pos): 
                    game_loop(1, img_hard, "3")

        screen_text("SELECT YOUR LEVEL", creme, 150, 130, 50)

        easy_rect = pygame.draw.rect(game_display, black, [150, 200, 150, 80]) 
        screen_text("EASY", blue, 185, 225, 40)

        medium_rect = pygame.draw.rect(game_display, black, [350, 200, 150, 80])
        screen_text("MEDIUM", blue, 365, 225, 40)
    
        hard_rect = pygame.draw.rect(game_display, black, [550, 200, 150, 80])
        screen_text("HARD", blue, 580, 225, 40)

        pygame.display.update()


    

#Gmae loop
def game_loop(velocity_init, img , level):
    if level == "1":
        color = (0, 255, 255)
        color_snake = white
        color_food = blue
        file = "high_score1.txt"

    elif level == "2":
        color = grey
        color_snake = (255, 255, 0)
        color_food = blue
        file = "high_score2.txt"

    elif level == "3":
        color = creme
        color_snake = creme
        color_food = red
        file = "high_score3.txt"


    # Game Specific variable
    game_over =False
    game_end =False
    snake_x = 425
    snake_y = 275
    snake_size = 10
    score = 0
    fps = 60 
    v_x = 0
    v_y = 0
    food_x = random.randint(0, screen_width-20)
    food_y = random.randint(0, screen_length-20)
    
    velocity_changer = 1
    snake_length = 1
    snake_pos_list = []
    
    while not game_end:
        if game_over:
            try:
                with open(file, "r") as f:
                    content1 = f.read()
                    if int(content1) < score: 
                        with open(file, "w") as g:
                            g.write(str(score))

            except:
                with open(file, "a") as f:
                    f.write("0")

            game_display.fill(white)
            game_display.blit(img_game_over, (0,0))
            screen_text("PRESS ENTER TO PLAY AGAIN!!!", creme, 90, 380, 70)
            screen_text("GDSC App Development Submission", creme, 200, 550, 40)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or pygame.K_RETURN:
                        level_screen()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        v_x = velocity_changer
                        v_y = 0

                    elif event.key == pygame.K_LEFT:
                        v_x = -velocity_changer
                        v_y = 0

                    elif event.key == pygame.K_UP:
                        v_y = -velocity_changer
                        v_x = 0

                    elif event.key == pygame.K_DOWN:
                        v_y = velocity_changer
                        v_x = 0

            snake_x += v_x 
            snake_y += v_y

            if abs(snake_x-food_x)<12 and abs(snake_y-food_y)<12:
                pygame.mixer.music.load('food.mp3')
                pygame.mixer.music.play()
                score += 10
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_length)
                snake_length += 10
                velocity_changer += velocity_init          
                
            snake_head_list = []

            snake_head_list.append(snake_x)
            snake_head_list.append(snake_y)

            snake_pos_list.append(snake_head_list)

            if len(snake_pos_list)>snake_length:
                del snake_pos_list[0]

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_length:
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
                game_over = True

            if snake_head_list in snake_pos_list[:-1]:
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
                game_over = True
                

            game_display.fill(white)
            game_display.blit(img, (0,0))

            screen_text("GDSC App Development Submission", color, 200, 550,  40)
            try:
                with open(file, "r") as f:
                    content = f.read()
                    if int(content) > score:
                        screen_text(f"High Score:{content}", color, 720, 0,  40)

                    else:
                        screen_text(f"High Score:{score}", color, 720, 0,  40)

            except:
                screen_text("High Score:0", color, 720, 0,  40)

            screen_text(f"Score:{score}", color, 0, 0, 40)

            long_snake(game_display, color_snake, snake_pos_list, snake_size)

            pygame.draw.circle(game_display, color_food, [food_x, food_y], 10, 0)

        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

home_page()
# name_input()
# game_loop()