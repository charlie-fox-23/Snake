import pygame
import sys
import random

pygame.init()

#screen
screen_width,screen_height = 640,480
screen = pygame.display.set_mode((screen_width,screen_height))
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

clock = pygame.time.Clock()
fps = 10


#snake postition
snake_pos = [[100,50]]

snake_body = [[100,50],[90,50],[80,50]]

#snake postition player 2
snake2_pos = [[300,50]]
snake2_body = [[300,50],[310,50],[320,50]]
#snake direction player 2
direction2 = "left"
change_to2 = direction2

score2 = 0

#Initial Direction of snake
direction = "right"
change_to = direction

food_pos = [
  random.randrange(1,(screen_width//10))*10,
  random.randrange(1,(screen_height//10))*10]
food_spawn = True

def show_score2 (choice,color,font,size) :
  score_font2 = pygame.font.SysFont(font,size)
  score_surface2 = score_font2.render("Score2 : " + str(score2),True,color )
  score_rect2 = score_surface2.get_rect()
  if choice == 1 :
    score_rect2.midtop = (screen_width//2,15)
  else:
    score_rect2.midtop = (screen_width/25,screen_height/1.25)
  screen.blit(score_surface2,score_rect2)

score = 0
def show_score (choice,color,font,size) :
   score_font = pygame.font.SysFont(font,size)
   score_surface = score_font.render("Score : " + str(score),True,color )
   score_rect = score_surface.get_rect()
   if choice == 1 :
    score_rect.midtop = (screen_width/10,15)
   else:
     score_rect.midtop = (screen_width/2,screen_height/1.25)
   screen.blit(score_surface,score_rect)

def game_over2() :
  my_font2 = pygame.font.SysFont("times new roman",50)
  go_surface2 = my_font2.render("Player2 Score is: " + str(score2),True,red)
  go_rect2 = go_surface2.get_rect()
  go_rect2.midtop = (screen_width / 2, screen_height / 4)
  screen.fill(black)
  screen.blit(go_surface2, go_rect2)
  show_score2(0, red, 'times new roman', 20)
  pygame.display.flip()
  pygame.time.wait(3000)
  pygame.quit()
  sys.exit



def game_over() :
  my_font = pygame.font.SysFont("times new roman",50)
  go_surface = my_font.render("Your Score is: " + str(score),True,green)
  go_rect = go_surface.get_rect()
  go_rect.midtop = (screen_width / 2, screen_height / 4)
  screen.fill(black)
  screen.blit(go_surface, go_rect)
  show_score(0, green, 'times new roman', 20)
  pygame.display.flip()
  pygame.time.wait(3000)
  pygame.quit()
  sys.exit()



while True :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      pygame.quit() 
      sys.exit()
    elif event.type == pygame.KEYDOWN :
      if event.key == pygame.K_UP and direction != "down" :
        change_to = "up"
      if event.key == pygame.K_DOWN and direction != "up" :
        change_to = "down"
      if event.key == pygame.K_LEFT and direction != "right" :
        change_to = "left"
      if event.key == pygame.K_RIGHT and direction != "left" :
        change_to = "right"
      
      

      
#     keys for player 2
      if event.key == pygame.K_w and direction2 != "down" :
        change_to2 = "up"
      if event.key == pygame.K_s and direction2 != "up" :
        change_to2 = "down"
      if event.key == pygame.K_a and direction2 != "right" :
        change_to2 = "left"
      if event.key == pygame.K_d and direction2 != "left" :
        change_to2 = "right"

  #player 2
  if change_to2 == "up" and direction2 != "down" :
    direction2 = "up"
  if change_to2 == "down" and direction2 != "up" :
    direction2 = "down"
  if change_to2 == "left" and direction2 != "right" :
    direction2 = "left"
  if change_to2 == "right" and direction2 != "left" :
    direction2 = "right"

  #player 1
  if change_to == "up" and direction != "down" :
    direction = "up"
  if change_to == "down" and direction != "up" :
    direction = "down"
  if change_to == "left" and direction != "right" :
    direction = "left"
  if change_to == "right" and direction != "left" :
    direction = "right"

  if direction == "up" :
    snake_pos [0][1]-=10
  if direction == "down" :
    snake_pos [0][1]+=10
  if direction == 'left' :
    snake_pos [0][0]-=10
  if direction == 'right' :
    snake_pos [0][0]+=10

#movement for snake2 
  if direction2 == 'up' :
    snake2_pos [0][1]-=10
  elif direction2 == 'down' :
    snake2_pos [0][1]+=10
  elif direction2 == 'left' :
    snake2_pos [0][0]-=10
  elif direction2 == 'right' :
    snake2_pos [0][0]+=10

  snake2_body.insert(0,list(snake2_pos[0]))
  if snake2_pos[0]==food_pos:
    score2 +=1 
    food_spawn = False
  else:
    snake2_body.pop()
    
    
  
  #snake body grow
  snake_body.insert(0,list(snake_pos[0])) 
  if snake_pos[0] == food_pos :
    score +=1
    food_spawn = False
  else :
    snake_body.pop()
  
  if not food_spawn :
    # food_pos = [random.randrange(1,(screen_width//10*10)),
    #             random.randrange(1,(screen_height//10*10))]
    food_pos = [random.randrange(1, (screen_width // 10)) * 10,
      random.randrange(1, (screen_height // 10)) * 10]

  food_spawn = True

 


  #Game over functionality
  if snake_pos [0][0]<0 or snake_pos[0][0]>screen_width-10 :
    game_over()


  if snake_pos [0][1]<0 or snake_pos[0][1]>screen_height-10 :
    game_over()

  for block in snake_body [1:]:
    if snake_pos [0]==block :
      game_over()


  if snake2_pos[0][0]<0 or snake2_pos[0][0]>screen_width-10 or snake2_pos[0][1]<0 or snake2_pos[0][1]>screen_height-10 :
    game_over2()
  
  for block in snake2_body [1:] :
    if snake2_pos[0] == block :
      game_over2()
       
    screen.fill(black)

  border_thickness = 10
  pygame.draw.rect(screen,white,pygame.Rect(0,0,screen_width,screen_height),border_thickness)

  for pos in snake_body :
    pygame.draw.rect(screen,green,pygame.Rect(pos[0],pos[1],10,10))

  pygame.draw.rect(screen,blue,pygame.Rect(food_pos[0],food_pos[1],10,10))

  for pos in snake2_body :
    pygame.draw.rect(screen,red,pygame.Rect(pos[0],pos[1],10,10))
  
  show_score2(1,red,"consolas",20)
  show_score(1,green,"consolas",20)
  
  pygame.display.flip()
  clock.tick(fps)