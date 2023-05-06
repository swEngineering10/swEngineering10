import sys
import pygame

pygame.init()
fps = 5
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []

button_image = pygame.image.load(r"assets\images\cards\UNO_Button.png")
button_scale = pygame.transform.scale(button_image, (100, 100))
pygame.image.save(button_scale, r"assets\images\cards\UNO_Button.png")
button_image = pygame.image.load(r"assets\images\cards\UNO_Button.png")

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.on_click()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def on_click(self):
        print("버튼이 눌렸습니다!")

button = Button(100, 100, button_image)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    button.handle_event(event)

    # 화면 그리기
    screen.fill((255, 255, 255))
    button.draw(screen)
    pygame.display.flip()
    fpsClock.tick(fps)



    '''
    def __init__(self, x, y, width, height, image, onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        
        
        
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        objects.append(self)
        
        
    def process(self):
        mousePos = pygame.mouse.get_pos()
        #.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            #self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                #self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
            
        screen.blit(self.buttonSurface, self.buttonRect)
        
        
        
def myFunction():
    print('Button Pressed')

Button(30, 30, 400, 100, button_image, myFunction)
#Button(30, 140, 400, 100, 'Button Two (multiPress)', myFunction, True)



while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)
'''