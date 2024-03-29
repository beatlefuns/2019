import pygame

class Ship():
	"""模拟飞船操作"""
	
	def __init__(self,ai_setting,screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ai_setting = ai_setting
		#加载飞船并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘新飞船放置在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		"""根据移动标志调整飞船位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_setting.ship_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ai_setting.ship_speed_factor
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_setting.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.bottom -= self.ai_setting.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.ai_setting.ship_speed_factor
		
		self.rect.centerx = self.center
		self.rect.bottom =self.bottom
