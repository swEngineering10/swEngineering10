import pygame

from utility import BackGround


# 전역변수 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


class ImageButton():
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.x
        self.image_rect.y = self.y


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.on_click()

    
    def on_click(self):
        print("클릭!!")


    def draw(self, surface):
        surface.blit(self.image, self.image_rect)


# 색깔 선택 팝업창을 위한 색깔 이미지 버튼
class ColorImageButton():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.image.load(f"assets/images/color_chooser/{self.color}.png")
        self.image_width = self.image.get_rect().width
        self.image_height = self.image.get_rect().height
        self.hovered_image = pygame.image.load(f"assets/images/color_chooser/{self.color}_active.png")
        self.hovered_image_width = self.hovered_image.get_rect().width
        self.hovered_image_height = self.hovered_image.get_rect().height
        self.new_x = self.x - (self.hovered_image_width - self.image_width) // 2
        self.new_y = self.y - (self.hovered_image_height - self.image_height) // 2
        self.image_rect = pygame.Rect(self.x, self.y, self.image_width, self.image_height)
        self.blit_image = self.image

    def handle_event(self, event, game_init, surface):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.image_rect.collidepoint(mouse_pos):
                self.on_click(game_init)
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.image_rect.collidepoint(mouse_pos):
                self.on_hover(surface)
            else:
                self.on_hover_exit(surface)

    # 색깔 선택 시 selectedColor에 색깔 부여
    def on_click(self, game_init):
        if self.color == "Blue" :
            game_init.selectedColor = 1
        elif self.color == "Red" :
            game_init.selectedColor = 2
        elif self.color == "Green" :
            game_init.selectedColor = 3
        elif self.color == "Yellow" :
            game_init.selectedColor = 4

    def on_hover(self, surface):
        self.image_rect = pygame.Rect(self.new_x, self.new_y, self.hovered_image_width, self.hovered_image_height)
        self.blit_image = self.hovered_image
        self.draw(surface)

    def on_hover_exit(self, surface):
        self.blit_image = self.image
        self.image_rect = pygame.Rect(self.x, self.y, self.image_width, self.image_height)
        self.draw(surface)

    def draw(self, surface):
        surface.blit(self.blit_image, self.image_rect)


# 챌린지 팝업창에 들어갈 버튼
class ChallengeTextButton():
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.rect_width = width
        self.rect_height = height
        self.button_rect = pygame.Rect(self.x, self.y, self.rect_width, self.rect_height)
        self.hovered = False

        # 텍스트
        self.text = text
        self.font_path = "assets/fonts/NanumSquare_acB.ttf"
        self.font = pygame.font.Font(self.font_path, 20)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.rect_width // 2, self.y + self.rect_height // 2))

    def handle_event(self, event, game_init, surface):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(mouse_pos):
                self.on_click(game_init)
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(mouse_pos):
                self.hovered = True
            else:
                self.hovered = False

    # 챌린지 여부
    def on_click(self, game_init):
        if self.text == "챌린지" :
            game_init.IsChallenge = 0
        elif self.text == "포기" :
            game_init.IsChallenge = 1


    def on_hover(self, surface):
        surface.fill(GRAY, (self.x, self.y, self.rect_width, self.rect_height))

    def on_hover_exit(self, surface):
        surface.fill(WHITE, (self.x, self.y, self.rect_width, self.rect_height))

    def draw(self, surface):
        if self.hovered :
            self.on_hover(surface)
        else :
            self.on_hover_exit(surface)
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.rect_width, self.rect_height), 2)
        surface.blit(self.text_surface, self.text_rect)




# 챌린지 여부를 선택하는 팝업창
class IsChanllengePopup():
    def __init__(self):
        self.background = BackGround()  # BackGround 객체 생성
        self.width = self.background.x_pos * 0.6
        self.height = self.background.y_pos * 0.4
        self.x = (self.background.x_pos - self.width) // 2
        self.y = self.background.y_pos * 0.5 

        # 텍스트 관련 속성
        self.text = "도전하시겠습니까?"
        self.font_path = "assets/fonts/NanumSquare_acB.ttf"
        self.font = pygame.font.Font(self.font_path, 24)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height * 0.3))

        # 버튼 x, y, width, height 설정하기
        self.button_width = self.width * 0.3
        self.button_height = self.height * 0.3
        self.spacing = (self.width - 2 * self.button_width) // 3
        self.button_x = self.x + self.spacing
        self.button_y = self.y + self.height * 0.55

        # 버튼 인스턴스 생성
        self.challenge_button = ChallengeTextButton(self.button_x, self.button_y, self.button_width, self.button_height, "챌린지")
        self.giveup_button = ChallengeTextButton(self.button_x + self.spacing + self.button_width, self.button_y, self.button_width, self.button_height, "포기")

    def popup_draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)
        surface.blit(self.text_surface, self.text_rect)
        self.challenge_button.draw(surface)
        self.giveup_button.draw(surface)


# 색깔을 선택하는 팝업창
class SelectColorPopup():
    def __init__(self):
        self.background = BackGround()  # BackGround 객체 생성
        self.width = self.background.x_pos * 0.6
        self.height = self.background.y_pos * 0.4
        self.x = (self.background.x_pos - self.width) // 2
        self.y = self.background.y_pos * 0.5 

        # 텍스트 관련 속성
        self.text = "바꿀 색깔을 선택하세요!"
        self.font_path = "assets/fonts/NanumSquare_acB.ttf"
        self.font = pygame.font.Font(self.font_path, 24)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height * 0.3))

        # 버튼 너비와 높이 가져오기
        self.button_image = "assets/images/color_chooser/red.png"
        button_image = pygame.image.load(self.button_image)
        self.button_width = button_image.get_width()
        self.button_height = button_image.get_height()
        self.spacing = (self.width - (4 * self.button_width)) // 5 + self.button_width      # 버튼 간격 계산
        
        # 버튼 x, y 계산
        button_x = self.x + self.spacing - self.button_width
        button_y = self.y + self.height * 0.6

        # 버튼 인스턴스 생성
        self.blue_button = ColorImageButton(button_x, button_y, "Blue")
        self.red_button = ColorImageButton(button_x + self.spacing, button_y, "Red")
        self.green_button = ColorImageButton(button_x + 2 * self.spacing, button_y, "Green")
        self.yellow_button = ColorImageButton(button_x + 3 * self.spacing, button_y, "Yellow")


    def popup_draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)
        surface.blit(self.text_surface, self.text_rect)
        self.red_button.draw(surface)
        self.blue_button.draw(surface)
        self.green_button.draw(surface)
        self.yellow_button.draw(surface)



# 정보를 알려주는 팝업창들

class InfoPopup():
    def __init__(self, text):
        self.background = BackGround()  # BackGround 객체 생성
        self.width = self.background.x_pos * 0.8
        self.height = self.background.y_pos * 0.15
        self.x = (self.background.x_pos - self.width) // 2
        self.y = self.background.y_pos * 0.1 

        # 텍스트 관련 속성
        self.text = text
        self.font_path = "assets/fonts/NanumSquare_acB.ttf"
        self.font = pygame.font.Font(self.font_path, 20)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

    def popup_draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)
        surface.blit(self.text_surface, self.text_rect)