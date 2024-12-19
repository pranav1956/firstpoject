import pygame 
import random 

#constants

background_color = (255,255,0)
ballradius = 15
width,height = 800,600
fps = 60
paddle_height = 30
paddle_width = 125
paddle_x = width//2 - paddle_width//2
paddle_y = height - paddle_height - 50
paddle_color = (255,0,0)
ball_radius = 15
ball_color = (0,255,0)
paddle_speed = 9
score = 0
ball_speed = 7
ball_y = 0
ball_x = 100
pause = False

#starting pygame 

pygame.init()
running = True
clock = pygame.time.Clock()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Catch the ball")    

#font
pygame.font.init()
font = pygame.font.Font(None,36)
font2 = pygame.font.Font(None,75)


#game loop 

while running:
    
    clock.tick(fps)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
           

    window.fill((background_color))
    
    #drawing the paddle - 
    pygame.draw.rect(window,paddle_color,(paddle_x,paddle_y,paddle_width,paddle_height))


    #moving the paddle (user)
    if not pause:
        if key[pygame.K_LEFT] :
            paddle_x-=paddle_speed
        if key[pygame.K_RIGHT] :
            paddle_x+=paddle_speed
        if paddle_x+paddle_width<0:
            paddle_x = width
        if paddle_x > width:
            paddle_x=-1*paddle_width
    
    
    #ball
    
    pygame.draw.circle(window,ball_color,(ball_x,ball_y),ball_radius)
    if not pause:
     ball_y+=ball_speed
    if ball_y > height:
        ball_y = 0
        ball_x = random.randint(ball_radius,width-ball_radius)
        score-=1
    if (paddle_x<=ball_x<=paddle_x+paddle_width) and (ball_y + ball_radius > paddle_y):
        score+=1
        ball_y = 0
        ball_x = random.randint(ball_radius,width-ball_radius)
    if pause:
        t = "PAUSED"
        x = font2.render(t,True,(64, 224, 208))
        window.blit(x, (width//2-100,height//2-30))
    
 


    score_text = font.render(str(score), True, (0, 0, 0))  # Black color for text
    window.blit(score_text, (10, 10))  # Position (10, 10) from the top-left corner
    pygame.display.update()


