#게임 파일
import pygame
import scene

# Initialize Pygame
pygame.init()

# 상수
SCREEN_SIZE = (830,830)
DARK_GREY = (50,50,50)
MUSTARD = (209,206,25)

# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('UNO Game')
clock = pygame.time.Clock()


#sceneManager는 scene stack이라고 생각하면 됨
sceneManager = scene.SceneManager()
mainMenu = scene.MainMenuScene()
sceneManager.push(mainMenu) # 스택에 메인메뉴 화면을 넣은 것임

running = True
while running:
# game loop
    
    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if sceneManager.isEmpty():
        running = False
    sceneManager.input()
    sceneManager.update()
    sceneManager.draw(screen)

    # -----
    # INPUT
    # -----

    

    # if game_state == 'playing':
        #new_plaer ~~
     
    # ------
    # UPDATE
    # ------

    #if game_state == 'playing':
        #update animation
        
    # if world_isWon():
        # game_state = 'won'
    # if world_isLost():
     #   game_state = 'lost'
    
    # ------
    # DRAW
    # ------

    #background
    #screen.fill(DARK_GREY)

    # if game_state == 'win':
        # draw win screen   
    # if game_state == 'lose':
        # draw lose screen
    
    # present screen
    pygame.display.flip()

    clock.tick(60)

#quit
pygame.quit()

