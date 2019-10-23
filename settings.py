class Settings():
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(230,230,230)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =(60,60,60)
        self.bullets_allowed = 5
        #子弹速度设置
        self.bullet_speed_factor = 1

        #飞船速度设置
        self.ship_speed_factor = 1.5

