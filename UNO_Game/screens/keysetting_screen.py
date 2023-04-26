import pygame
import pygame_gui
import json

# json 파일 로드
with open('display_config.json', 'r') as f:
    config_data = json.load(f)

    # json 파일로부터 받은 해상도 값 반영
screen_width = config_data['resolution']['width']
screen_height = config_data['resolution']['height']

data = {"resolution": {"width": screen_width, "height": screen_height}}

with open('keys.json', 'r') as f:
    keyboard_data = json.load(f)

key_up = keyboard_data["keyboard"]["up"]
key_down = keyboard_data["keyboard"]["down"]
key_left = keyboard_data["keyboard"]["left"]
key_right = keyboard_data["keyboard"]["right"]
keyboard_data = {"keyboard": {"up": key_up,
                              "down": key_down, "left": key_left, "right": key_right}}

pygame.init()
font = pygame.font.SysFont(None, 100)
text = font.render("KEY SETTING", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width//2, screen_height//2 * 0.4))


class KeyChanger:
    def __init__(self, screen, font, keys=None):
        self.screen = screen
        self.font = font
        if keys is None:
            self.keys = {
                pygame.K_UP: keyboard_data["keyboard"]["up"],
                pygame.K_DOWN: keyboard_data["keyboard"]["down"],
                pygame.K_LEFT: keyboard_data["keyboard"]["left"],
                pygame.K_RIGHT: keyboard_data["keyboard"]["right"]
            }
        else:
            self.keys = keys
        self.manager = pygame_gui.UIManager(screen.get_size())

        self.up_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (screen_width // 2 * 0.75, screen_height // 2 * 0.7), (200, 50)),
            text='UP Key',
            manager=self.manager
        )

        self.down_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (screen_width // 2 * 0.75, screen_height // 2 * 0.7 * 1.4), (200, 50)),
            text='DOWN Key',
            manager=self.manager
        )

        self.left_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (screen_width // 2 * 0.75, screen_height // 2 * 0.7 * 1.8), (200, 50)),
            text='LEFT Key',
            manager=self.manager
        )

        self.right_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (screen_width // 2 * 0.75, screen_height // 2 * 0.7 * 2.2), (200, 50)),
            text='RIGHT Key',
            manager=self.manager
        )

        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.up_button:
                            self.change_key(pygame.K_UP)
                            self.up_button.set_text(
                                'UP Key: ' + pygame.key.name(self.keys[pygame.K_UP]))
                        elif event.ui_element == self.down_button:
                            self.change_key(pygame.K_DOWN)
                            self.down_button.set_text(
                                'DOWN Key: ' + pygame.key.name(self.keys[pygame.K_DOWN]))
                        elif event.ui_element == self.left_button:
                            self.change_key(pygame.K_LEFT)
                            self.left_button.set_text(
                                'LEFT Key: ' + pygame.key.name(self.keys[pygame.K_LEFT]))
                        elif event.ui_element == self.right_button:
                            self.change_key(pygame.K_RIGHT)
                            self.right_button.set_text(
                                'RIGHT Key: ' + pygame.key.name(self.keys[pygame.K_RIGHT]))

                self.manager.process_events(event)

            self.screen.fill((0, 0, 0))
            self.screen.blit(text, text_rect)

            self.manager.update(time_delta)

            self.manager.draw_ui(self.screen)

            pygame.display.flip()

    def change_key(self, key):
        new_key = None
        while new_key is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    new_key = event.key

        self.keys[key] = new_key


screen = pygame.display.set_mode((screen_width, screen_height))
keys = {pygame.K_UP: pygame.K_UP, pygame.K_DOWN: pygame.K_DOWN,
        pygame.K_LEFT: pygame.K_LEFT, pygame.K_RIGHT: pygame.K_RIGHT}
key_changer = KeyChanger(screen, font, keys)
key_changer.run()


new_up_key = keys[pygame.K_UP]
new_down_key = keys[pygame.K_DOWN]
new_left_key = keys[pygame.K_LEFT]
new_right_key = keys[pygame.K_RIGHT]

keyboard_data["keyboard"]["up"] = new_up_key
keyboard_data["keyboard"]["down"] = new_down_key
keyboard_data["keyboard"]["left"] = new_left_key
keyboard_data["keyboard"]["right"] = new_right_key

with open('keys.json', 'w') as f:
    json.dump(keyboard_data, f)

pygame.quit()
