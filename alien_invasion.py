import sys

import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Setting()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	
	#创建一个用于存储子弹的编组
	bullets = Group()
	
	#创建一个外星人编组
	aliens = Group()
	
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#开始游戏主循环
	while True:
		
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
		
run_game()
