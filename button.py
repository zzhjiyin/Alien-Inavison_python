import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):

        self.ai_settings = ai_settings
       #初始化按键属性
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按键的尺寸和位置
        self.width, self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,50)

        #创建按钮rect对象并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #按钮标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """msg渲染为图像，并使其居中在按钮上"""
        self.msg_imge = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_imge_rect = self.msg_imge.get_rect()
        self.msg_imge_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个颜色填充按钮，再绘制文本"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_imge,self.msg_imge_rect)
