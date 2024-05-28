import pygame

pygame.init() 
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Side-scrolling game')
clock = pygame.time.Clock()

X = 0
Y = 1
deltaX = 2
deltaY = 3

platforms = [(500, 400), (700, 300), (850,300), (950,400),(1100,300), (1200,400)]
player = [100, 450, 0, 0] #xpos, ypos, xvel, yvel
isOnGround = False
offset = 0

def draw_clouds():
    for x in range(100, 800,300):
        for i in range(3):#draw three curlces 
            pygame.draw.circle(screen, (255,255,255), (x + offset, 100), 40)
            pygame.draw.circle(screen, (255,255,255), (x-50 + offset, 125), 40)
            pygame.draw.circle(screen, (255,255,255), (x+50 + offset, 125), 40)
        pygame.draw.rect(screen, (255,255,255), (x-50 + offset, 100, 100, 65))
def draw_tree():
    for x in range(200, 700,200):
        for i in range(3):
            pygame.draw.rect(screen, (140,76,0), (x-25 + offset, 300, 60, 650))#tree trunk
            pygame.draw.circle(screen, (0,205,0), (x + offset, 300), 40)#leaves
            pygame.draw.circle(screen, (0,205,0), (x-50 + offset, 325), 40)
            pygame.draw.circle(screen, (0,205,0), (x-30 + offset, 365), 40)
            pygame.draw.circle(screen, (0,205,0), (x+50 + offset, 325), 40)
        pygame.draw.circle(screen, (0,205,0), (x+40 + offset, 365), 40)
        
def draw_trees():
    for x in range(400, 1400,600):
        for i in range(3):
            pygame.draw.rect(screen, (190,76,0), (x-45 + offset, 600, 1200, 1250))#tree trunk
            pygame.draw.circle(screen, (0,255,0), (x + offset, 600), 80)#leaves
            pygame.draw.circle(screen, (0,255,0), (x-100 + offset, 625), 80)
            pygame.draw.circle(screen, (0,255,0), (x-60 + offset, 665), 80)
            pygame.draw.circle(screen, (0,205,0), (x+100 + offset, 625), 80)
        pygame.draw.circle(screen, (0,205,0), (x+40 + offset, 365), 80)
def move_player():
    global isOnGround #needed to moditfy a global variable  from within a funtion 
    global offset
    for i in range(len(platforms)):
        if player[X]+50>platforms[i][X]+offset and player[0]<platforms[i][X]+100+offset and player[Y]+50>platforms[i][Y] and player[Y]+50< platforms[i][Y]+50:
            isOnGround = True
            player[Y]=platforms[i][Y]-50
            player[deltaY] = 0 
   
    if keys[pygame.K_LEFT]:
       if offset > 260 and player[X]>0:#check if you reached the left egde of the map
           player[deltaX] = -5#lets player get back to the center of the game screen 
           
       elif player[X]>400 and offset < -1500:#check tpo see were on the far right egde of the game 
            player[deltaX] = -5# let player get back to the center of the game screen
       elif player[X]>0:
            offset += 5
            player[deltaX] = 0
       else:
            player[deltaX] = 0#if player is recentened move the offset not the player 
    elif keys[pygame.K_RIGHT]:
        if offset < -1500 and player[X]<750: #makes it so u can reach th eright side of the map 
            player[deltaX] = 5
        
        elif offset >260 and player[0]<400:#checks that we arent on the left but the right
            player[deltaX] = 5
        
        elif player[X]<750:#moves player to the middle if the player is recentered 
            offset -= 5
            player[deltaX] = 0
        else:
            player[deltaX] =0#stop going off egde
    else:
        player[deltaX] = 0
        
    if isOnGround == True and keys[pygame.K_UP]: #jump
        player[deltaY] = -15
        isOnGround = False
        
        
    
    
    player[X]+=player[deltaX]
    player[Y]+=player[deltaY]
    
    if player[Y] >= 450:
        player[Y] = 450
        isOnGround = True
        
    if isOnGround == False: #gravity
        player[3] += 1
       
def draw_platforms():
    for i in range(len(platforms)):
        pygame.draw.rect(screen, (150, 10, 10), (platforms[i][0] + offset, platforms[i][1], 100, 30))










running = True
while running:# main game loopppp
    #input section
    clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    #phyiscs section
    
    move_player()
    
    #render sect6ion
    screen.fill((135,206,235))#sky blue backround
    draw_clouds()#funtion call
    draw_tree()
    draw_trees()
    pygame.draw.rect(screen, (0,205,0), (0, 500, 800, 150))
    pygame.draw.rect(screen, (255,0,255), (player[0], player[1], 50, 50))# player 
    draw_platforms()
    pygame.display.flip()#puts everything on the screen
    
pygame.quit()
    