#《外星人入侵》函数模块
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_event(event,ai_settings,screen,ship,bullets):
	"""响应按下按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right =True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_event(event,ship):
	"""响应松开按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
		
def check_events(ai_settings,screen,ship,bullets):
	"""响应鼠标键盘事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)
		

def update_bullets(bullets):
	"""更新子弹位置，并删除已消失的子弹"""
	bullets.update()
	
	#删除消失子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
						
def fire_bullet(ai_settings,screen,ship,bullets):
	"""如果没达到子弹限制，发射一颗子弹"""
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		
def get_number_aliens_x(ai_settings,alien_width):
	"""计算每行可容纳外星人"""
	available_space_x = ai_settings.screen_width-2*alien_width
	number_aliens_x = int(available_space_x/(2*alien_width))
	return number_aliens_x
	
def get_number_rows(ai_settings,ship_height,alien_height):
	"""计算可容纳外星人行数"""
	available_sapce_y = (ai_settings.screen_height - ship_height - 
		3*alien_height)
	return int(available_sapce_y/(2*alien_height))

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""创建一个外星人并加入当前行"""
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + alien_number*alien_width*2
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + row_number*alien.rect.height*2
	aliens.add(alien)
	
def create_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人群"""
	#获得单个外星人的宽度
	#确定一行可以容纳的外星人数量
	#外星人间距为外星人宽度
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	
	#创建一群外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#创建一个外星人并加入当前行
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
		
def update_screen(ai_setting,screen,ship,aliens,bullets):
	"""更新屏幕图像，并切换到新屏幕"""
	#每次循环重绘制屏幕
	screen.fill(ai_setting.bg_color)
	ship.blitme()
	aliens.draw(screen)
	
	#在飞船和外星人后绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	"""	
	bullets.draw(screen)  bullets 编组不可以直接使用draw()方法。应为在bullet
	类中没有image属性
	"""
	#让最近绘制的屏幕可见
	pygame.display.flip()
