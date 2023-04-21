import pygame

# 이미지 로드 및 애니메이션을 위한 Card 클래스
class CardLoad:
    def __init__(self, card_value):
        self.card_value = card_value    # 카드의 정보 (튜플 값, ("Red", 5) 형식)
        print(self.card_value)  # 디버깅용 (로드 이미지랑 비교)
        self.image = pygame.image.load(f"assets/images/cards/{self.card_value[0]}_{self.card_value[1]}.png")  # 카드 이미지 로드
        self.current_card_pos = (230, 120)  # currentCard(오픈 카드)일 때 이미지 위치
    

    # currentCard일 때 이미지 로드
    def current_card_draw(self, surface):
        surface.blit(self.image, self.current_card_pos)
