import pygame
from .sceneBase import SceneBase
from .gameScene import GameScene

from .assets import luckywheel_title, bet_tilte, quit_title

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(luckywheel_title['img'], luckywheel_title['xy'])
        screen.blit(bet_tilte['img'], bet_tilte['xy'])
        screen.blit(quit_title['img'], quit_title['xy'])