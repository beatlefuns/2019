class Setting():
	"""存储《外星人入侵》游戏的所有设置的类"""
	
	def __init__(self):
		"""初始化游戏设置"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		#调整飞船移动速度
		self.ship_speed_factor = 1.5
		
		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 3
