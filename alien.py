import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外星人的类"""
	
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#加载外星人图片并设置其rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#每个外星人最初都在屏幕左上角位置
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#存储外星人准确位置
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)
