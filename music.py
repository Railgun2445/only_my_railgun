import time
import pygame

def music_player(sn):
	file = sn + '.mp3'
	pygame.mixer.init()
	track = pygame.mixer.music.load(file)

	#播放音乐10秒后停止
	pygame.mixer.music.play()
	time.sleep(2)
	pygame.mixer.music.stop()