import pygame
import random  # random module to place
pygame.init()

# code for setting up the screen
WIDTH = 500
HEIGHT = 500
pressed = None
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Santa Game')
fontName = pygame.font.match_font('arial')
font = pygame.font.Font(fontName, 30)

# code for loading Santa image and set up Santa in the game
santa = pygame.image.load('santa.png')
SANTA_WIDTH, SANTA_HEIGHT = santa.get_size()
santa = pygame.transform.scale(santa, (SANTA_WIDTH // 2, SANTA_HEIGHT // 2))
santa_y = HEIGHT / 2
SANTA_SPEED = 1

# code for loading the present image and set up Santa in the game
present_image = pygame.image.load('present.png')
PRESENT_WIDTH, PRESENT_HEIGHT = present_image.get_size()
present = pygame.transform.scale(present_image, (PRESENT_WIDTH, PRESENT_HEIGHT))
PRESENT_SPEED = 0.1
present_x = WIDTH - PRESENT_WIDTH//2
present_y = random.randint(0, HEIGHT)

picked = False
score = 0

while True:
    screen.fill((0, 0, 0))
    
    # add santa to the middle of edge of the screen with x=0, and y half way
    screen.blit(santa, (0, santa_y))
                
    santa_rect = santa.get_rect()
    santa_rect.x = 0
    santa_rect.y = santa_y

    # Your TASK 1: only one line of code
    # use the above code for Santa as examples.
    # add your code here to add the present to the screen
    


    # Your TASK 2:only one line of code
    # your previous knowledge
    # on moving an object across the screen along x
    # add your code here to change the present's x value based on the PRESENT_SPEED

    # Your TASK 3:only three lines of code
    # use the above Santa code as examples to add the three varaibles:
    # the present_rect,   present_rect.x  and present_rect.y


    

    # Together TASK 4: eight lines of code
    # detect when Santa has collided with a present (picked up a present)
    # Three things need to happen when Santa has picked up a present:
    # 1: increase the score by 1;
    # 2: increase the speed of the present to make the game harder
    # 3: make the present come from the right edge again at a higher speed



    # The following are the normal event loop.
    # The event we are interested in is key down and up, then identify which key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pressed = event.key
        elif event.type == pygame.KEYUP:
            pressed = None
            
    # Your TASK 4: six lines of code
    # check if the pressed variable is an UP key or DOWN key
    # if it's UP: move Santa up else down but within the screen boundaries


    # A new skill for you to learn: add text to the screen
    score_text = font.render('Score: ' + str(score), False, (255, 255, 255))
    screen.blit(score_text, (WIDTH / 2, 0))

    pygame.display.flip()
