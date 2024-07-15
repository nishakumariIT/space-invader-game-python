import pygame,sys,random,math

#INITIALIZE 
pygame.init()
# FUNCTIONS
# FOR BULLET FIRE TO KILL ENEMY 
#DISTANCE FIND COORDINATES MATH FORMULA APPLY AND then math library import
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance =math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance < 37:
       return True
    else:
       return False
over_font = pygame.font.Font(None,54)
def game_over():  
    render = over_font.render(f"GAME OVER AND score is {score}",True,(255,255,255))
    window.blit(render,(90,300))
# SCORE FUNCTION
def show_score():
    render = font.render(f"SCORE IS 0",{score},True,(255,255,255))
    window.blit(render,(50,50))

#SHOWING TEXT ON WINDOW 
font = pygame.font.Font(None,34)

#varibale create
score = 0


#CREATING WINDOW
window =pygame.display.set_mode((800,600))
#IMAGES IN PYGAME
#1) LOAD IMAGE
playerImg =pygame.image.load("D:\\space invader game\\assets\\player.png")
playerX =336
playerY =500
playerMovement =0
#2) showing image window
#window.blit(playerImg,(playerX,playerY))

#ENEMY IMAGE
enemyImg =[]
enemyX =[]
enemyY =[]
enemyMovement =[]
num_of_enemies =6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("D:\\space invader game\\assets\\enemy.png"))
    enemyX.append(random.randint(10,490))
    enemyY.append(random.randint(0,150))
    enemyMovement.append(5)

print(enemyImg)

#BULLET
bulletImg = pygame.image.load("D:\\space invader game\\assets\\bullet.png")
bulletX = playerX
bulletY = 500
bullet_fire = False

#BACKGROUND IMAGE
bgImg = pygame.image.load("D:\\space invader game\\assets\\background.png")
#GAME LOOP--> WHILE LOOP // IF WE GIVEN IT TRUE IT WILL CONTINUE RUN
while True:
    #DRAWING BACKGROUND IMAGE 
    window.blit(bgImg,(0,0))
    show_score()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
              bullet_fire = True
              #PLAYER  MOVEMENT
            if event.key ==pygame.K_RIGHT:
                playerMovement =5
            if event.key ==pygame.K_LEFT:
                playerMovement =-5
            if event.type == pygame.KEYUP:
                playerMovement =0
    playerX +=playerMovement
    if playerX <= 0:
        playerX =0
    elif playerX >= 736:
        playerX = 736
    window.blit(playerImg,(playerX,playerY))
    for i in range(num_of_enemies):
        if enemyY[i] >= 436:
            for j in range( num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break
        if isCollision(enemyX[i], enemyY[i], playerX, playerY):
            game_over()
        if enemyX[i] <= 0:
            enemyMovement[i] = 5
            #whenever enemy touch the left and right boundry they move to down
            enemyY[i] += 50
        if enemyX[i] >= 736:
            enemyMovement[i] = -5
            enemyY[i] += 50
            enemyX[i] += enemyMovement[i]
            
        else:
            enemyX[i] += enemyMovement[i]
          # To check bullet
            # collision variable create
            collided = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collided:
              score += 1
              enemyX[i] =random.randint(10,490)
            #whenever enemy touch the left and right boundry they move to down
        window.blit(enemyImg[i], (enemyX[i], enemyY[i]))  
    
   # if enemyX <= 0:
   #    enemyMovement = 5
   # if enemyX >= 736:
   #     enemyMovement = -5cls
   
   # enemyX += enemyMovement
   # window.blit(enemyImg,(enemyX,enemyY))
    if bullet_fire:
        bulletY -= 15
    if bulletY <= 0:
        bulletX = playerX
        bullet_fire = False
        window.blit(bulletImg,(bulletX,bulletY))
    if not bullet_fire:
        bulletY = 500
        bulletX = playerX
    pygame.display.update()