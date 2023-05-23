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


# 설정 버튼
class SettingButton():
    def __init__(self) :
        self.x = 5
        self.y = 5
        self.image = pygame.image.load("assets/images/etc_game_image/setting.png")
        self.image_width = self.image.get_rect().width
        self.image_height = self.image.get_rect().height
        self.hovered_image = pygame.image.load("assets/images/etc_game_image/setting_active.png")
        self.hovered_image_width = self.hovered_image.get_rect().width
        self.hovered_image_height = self.hovered_image.get_rect().height        
        self.image_rect = pygame.Rect(self.x, self.y, self.image_width, self.image_height)
        self.new_x = self.x - (self.hovered_image_width - self.image_width) // 2
        self.new_y = self.y - (self.hovered_image_height - self.image_height) // 2
        self.blit_image = self.image

    def handle_event(self, event, game_init, surface):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.image_rect.collidepoint(mouse_pos):
                self.on_click(game_init)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.on_click(game_init)

        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.image_rect.collidepoint(mouse_pos):
                self.on_hover(surface)
            else:
                self.on_hover_exit(surface)

    # 설정 버튼 눌렀을 때 이벤트
    def on_click(self, game_init):
        if game_init.isPaused == False :
            game_init.isPaused = True       # 게임 중단
        else :
            game_init.isPaused = False

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


# 팝업창에 들어갈 텍스트 버튼
class PopupTextButton():
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

    # 버튼 클릭 이벤트
    def on_click(self, game_init):
        # 챌린지 팝업 버튼
        if self.text == "챌린지" :
            game_init.IsChallenge = 1
        elif self.text == "포기" :
            game_init.IsChallenge = 0

        # 스왑 팝업 버튼
        elif self.text == "스왑" :
            game_init.IsSwap = True
        elif self.text == "스왑하지 않기" :
            game_init.IsSwap = False

        # 설정 팝업 버튼
        elif self.text == "설정" :
            pass
        elif self.text == "처음 화면으로" :
            pass
        elif self.text == "계속하기" :
            game_init.isPaused = False
        elif self.text == "종료하기" :
            pygame.quit()
            quit()


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


# 스왑 선택 팝업창에 들어갈 텍스트 버튼
class SwapPopupButton():
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

    # 버튼 클릭 이벤트
    def on_click(self, game_init):
        game_init.swapNumber = int(self.text)

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


# 설정 팝업창
class SettingPopup():
    def __init__(self):
        self.background = BackGround()  # BackGround 객체 생성
        self.background_width = self.background.x_pos
        self.background_height = self.background.screen_height

        self.width = self.background_width * 0.7
        self.height = self.background_height * 0.7
        self.x = (self.background_width - self.width) // 2
        self.y = (self.background_height - self.height) // 2

        # 버튼 x, y, width, height 설정하기
        self.button_width = self.width * 0.5
        self.button_height = self.height * 0.15
        self.spacing = (self.height - 4 * self.button_height) // 5 + self.button_height
        self.button_x = self.x + (self.width - self.button_width) // 2
        self.button_y = self.y + self.spacing - self.button_height

        self.setting_button = PopupTextButton(self.button_x, self.button_y, self.button_width, self.button_height, "설정")
        self.start_button = PopupTextButton(self.button_x, self.button_y + self.spacing, self.button_width, self.button_height, "처음 화면으로")
        self.continue_button = PopupTextButton(self.button_x, self.button_y + 2*self.spacing, self.button_width, self.button_height, "계속하기")
        self.exit_button = PopupTextButton(self.button_x, self.button_y + 3*self.spacing, self.button_width, self.button_height, "종료하기")


    def popup_draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)
        self.setting_button.draw(surface)
        self.start_button.draw(surface)
        self.continue_button.draw(surface)
        self.exit_button.draw(surface)


# 스왑 상대를 선택하는 팝업창
class SelectSwapPopup():
    def __init__(self, game_init):
        self.background = BackGround()  # BackGround 객체 생성
        self.game_init = game_init
        self.width = self.background.x_pos * 0.7
        self.height = self.background.y_pos * 0.4
        self.x = (self.background.x_pos - self.width) // 2
        self.y = self.background.y_pos * 0.5 

        # 텍스트 관련 속성
        self.text = "스왑 상대를 선택해주세요!"
        self.font_path = "assets/fonts/NanumSquare_acB.ttf"
        self.font = pygame.font.Font(self.font_path, 24)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height * 0.3))

        # 버튼 x, y, width, height 설정하기
        self.number = self.game_init.numPlayers - 1
        self.button_width = self.width * 0.15
        self.button_height = self.height * 0.3
        self.spacing = (self.width - self.number * self.button_width) // (self.number + 1)
        self.button_x = self.x + self.spacing
        self.button_y = self.y + self.height * 0.55

        self.swap_button_list = []  # 버튼 객체를 저장할 리스트

        # 버튼 인스턴스 생성
        for i in range(1, self.number + 1):
            # 버튼의 좌표 계산
            button_x = self.button_x + (i - 1) * (self.button_width + self.spacing)

            button_text = str(i)        # 버튼의 텍스트

            # 버튼 객체 생성 및 리스트에 추가
            button = SwapPopupButton(button_x, self.button_y, self.button_width, self.button_height, button_text)
            self.swap_button_list.append(button)

    def popup_draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)
        surface.blit(self.text_surface, self.text_rect)
        
        # 버튼 리스트
        for i in range(self.number):
            self.swap_button_list[i].draw(surface)



# 스왑 여부를 선택하는 팝업창
class IsSwapPopup():
    def __init__(self):
        self.background = BackGround()  # BackGround 객체 생성
        self.width = self.background.x_pos * 0.8
        self.height = self.background.y_pos * 0.4
        self.x = (self.background.x_pos - self.width) // 2
        self.y = self.background.y_pos * 0.5 

        # 텍스트 관련 속성
        self.text = "다른 플레이어의 덱과 스왑하시겠습니까?"
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
        self.swap_button = PopupTextButton(self.button_x, self.button_y, self.button_width, self.button_height, "스왑")
        self.not_swap_button = PopupTextButton(self.button_x + self.spacing + self.button_width, self.button_y, self.button_width, self.button_height, "스왑하지 않기")

    def popup_draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 2)
        surface.blit(self.text_surface, self.text_rect)
        self.swap_button.draw(surface)
        self.not_swap_button.draw(surface)



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
        self.challenge_button = PopupTextButton(self.button_x, self.button_y, self.button_width, self.button_height, "챌린지")
        self.giveup_button = PopupTextButton(self.button_x + self.spacing + self.button_width, self.button_y, self.button_width, self.button_height, "포기")

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



# 우노 버튼
class UNOButton():
    def __init__(self):
        self.background = BackGround()
        self.image = pygame.image.load("assets/images/cards/UNO_Button.png")
        self.image_rect = self.image.get_rect()
        self.image_width = self.image_rect.width
        self.image_height = self.image_rect.height
        self.background_width = self.background.x_pos
        self.background_height = self.background.y_pos
        self.x = self.background.x_pos - self.image_width - 10
        self.y = self.background.y_pos - self.image_height
        self.image_rect.x = self.x
        self.image_rect.y = self.y

        self.hovered_image = pygame.image.load("assets/images/cards/UNO_Button_active.png")
        self.hovered_image_width = self.hovered_image.get_rect().width
        self.hovered_image_height = self.hovered_image.get_rect().height        
        self.new_x = self.x - (self.hovered_image_width - self.image_width) // 2
        self.new_y = self.y - (self.hovered_image_height - self.image_height) // 2
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

    def on_hover(self, surface):
        self.image_rect = pygame.Rect(self.new_x, self.new_y, self.hovered_image_width, self.hovered_image_height)
        self.blit_image = self.hovered_image
        self.draw(surface)

    def on_hover_exit(self, surface):
        self.blit_image = self.image
        self.image_rect = pygame.Rect(self.x, self.y, self.image_width, self.image_height)
        self.draw(surface)
    
    def on_click(self, game_init):
        game_init.isUNO = True

    def draw(self, surface):
        surface.blit(self.blit_image, self.image_rect)


# 플레이어 이름 로드 텍스트 박스
class PlayerName():
    def __init__(self, text):

        # 텍스트
        self.text = text
        self.font_path = "assets/fonts/NanumSquare_acB.ttf"
        self.font = pygame.font.Font(self.font_path, 20)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_length = self.text_surface.get_width()

        self.box_width = self.text_length + 40
        self.box_height = 40

        self.background = BackGround()
        self.background_height = self.background.y_pos - 40

        self.rect_x = 10
        self.rect_y = self.background_height - 10
        self.name_box = pygame.Rect(self.rect_x, self.rect_y, self.box_width, self.box_height)


    def draw(self, surface, game_init):
        self.turn_calc(game_init)

        pygame.draw.rect(surface, WHITE, (self.rect_x, self.rect_y, self.box_width, self.box_height))
        pygame.draw.rect(surface, BLACK, (self.rect_x, self.rect_y, self.box_width, self.box_height), 2)
        surface.blit(self.text_surface, (self.rect_x + 20, self.rect_y + 8))
        surface.blit(self.turn_text_surface, (self.turn_text_x + 20, self.rect_y + 8))

    def turn_calc(self, game_init) :
        if game_init.playerTurn == 0 :
            self.turn_text = f"{self.text}의 차례입니다."
            self.turn_text_surface = self.font.render(self.turn_text, True, (0, 0, 0))
            self.turn_text_x = self.box_width + self.rect_x
        else :
            self.turn_text = f"컴퓨터 {game_init.playerTurn}의 차례입니다."
            self.turn_text_surface = self.font.render(self.turn_text, True, (0, 0, 0))
            self.turn_text_x = self.box_width + self.rect_x