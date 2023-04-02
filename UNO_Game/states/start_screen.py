import pygame
from scene.start_screen import StartScreen
from state import State


class StartState(State):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if StartScreen.start_button_rect.collidepoint(event.pos):
                    # 게임 시작 버튼을 누르면 다음 상태로 이동
                    self.scene_manager.change_scene('main')
                elif StartScreen.setting_button_rect.collidepoint(event.pos):
                    # 설정 버튼을 누르면 설정 상태로 이동
                    self.scene_manager.change_scene('setting')
                elif StartScreen.exit_button_rect.collidepoint(event.pos):
                    # 종료 버튼을 누르면 게임 종료
                    self.quit = True

    def update(self):
        pass

    def render(self):
        pass
