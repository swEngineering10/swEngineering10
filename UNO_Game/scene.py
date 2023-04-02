# #베이스 클래스. 즉 다른 클래스들이 상속받는 클래스
import globals
import pygame
import utils


class Scene:
    def __init__(self):
        pass
    def onEnter(self):
        pass
    def onExit(self):
        pass
    #input처리
    def input(self, sm):
        pass
    def update(self, sm):
        pass
    #draw itself
    def draw(self, sm, screen):
        pass

#Scenes
class MainMenuScene(Scene):
    def onEnter(self):
        #print('Entering main menu')
        pass
    def onExit(self):
        #print('Exiting main menu')
        pass
    #input처리
    def input(self, sm):
        # print('main menu input')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:   
            sm.push(FadeTransitionScene(self, SettingScene()))
        if keys[pygame.K_s]:
            sm.push(FadeTransitionScene(self, GameScene()))
        if keys[pygame.K_q]:
            sm.pop()
    def update(self, sm):
        # print('main menu update')
        pass
    #draw itself
    def draw(self, sm, screen):
        # background
        screen.fill(globals.DARK_GREY)
        utils.drawText(screen, 'Main Menu. Reture=Setings, S=Game Start, q=quit', 50, 50)

class SettingScene(Scene):
    def onEnter(self):
        pass
    def onExit(self):
        pass
    #input처리
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:   
            # 화면 전환이 아니라 설정 변경인듯?
            pass
        if keys[pygame.K_q]:
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
    def update(self, sm):
        # print('setting update')
        pass
    #draw itself
    def draw(self, sm, screen): #여기를 수정하면 될듯?
        # background
        screen.fill(globals.DARK_GREY)
        utils.drawText(screen, 'Setting. Return=Setings, q=quit')

class GameScene(Scene):
    def onEnter(self):
        pass
    def onExit(self):
        pass
    def input(self, sm):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:   
            sm.pop()
            sm.push(FadeTransitionScene(self, MainMenuScene()))
    def update(self, sm):
        pass
    def draw(self, sm, screen):
        #background
        screen.fill(globals.DARK_GREY)

#페이드인 페이드아웃 같이 전환할 때 자연스럽게 하는 화면
class TransitionScene(Scene):
    def __init__(self, fromScene, toScene):
        self.currentPercentage = 0
        self.fromScene = fromScene
        self.toScene = toScene
    def update(self, sm):
        self.currentPercentage += 2
        if self.currentPercentage >= 100:
            sm.pop()
            if self.toScene is not None:
                sm.push(self.toScene)

class FadeTransitionScene(TransitionScene):
    def draw(self, sm, screen):
        if self.currentPercentage < 50:
            self.fromScene.draw(sm, screen)
        else:
            if self.toScene is None:
                sm.scenes[-2].draw(sm, screen)
            self.toScene.draw(sm, screen)
        # fade overlay
        overlay = pygame.Surface((700, 500))
        # 0 = 투명 255 = 불투명
        # 0% = 0, 50% = 255, 100% = 0
        alpha = int(abs((255 - ((255/50)*self.currentPercentage))))
        overlay.set_alpha(255 - alpha)
        overlay.fill(globals.BLACK)
        screen.blit(overlay, (0, 0))


class SceneManager:
    def __init__(self):
        self.scenes = []
    def isEmpty(self):
        return len(self.scenes) == 0
    def enterScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onEnter()
    def exitScene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].onExit()
    #input처리
    def input(self): # 인덱스 -1이 가장 마지막. 0은 가장 처음. 1은 두 번째
        if len(self.scenes) > 0:
            self.scenes[-1].input(self)
    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update(self)
    #draw itself
    def draw(self, screen):
        if len(self.scenes) > 0:
            self.scenes[-1].draw(self, screen)
        # present screen
        pygame.display.flip()
    def push(self, scene):
        self.exitScene()
        self.scenes.append(scene)
        self.enterScene()
    def pop(self):
        self.exitScene()
        self.scenes.pop()
        self.enterScene()
    def set(self, scenes):
        # pop all scenes
        while len(self.scenes) > 0:
            self.pop()
        # add new scenes
        for s in scenes:
            self.push(s)
