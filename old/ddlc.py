import pygame

def main():
	pygame.init()
	logo = pygame.image.load("PreAlpha.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Operation Dingo")
	screen = pygame.display.set_mode((1778,876))
	pygame.mixer.music.load("despacito.mid")
	pygame.mixer.music.play()
	title = pygame.image.load("Title.png")
	place = pygame.image.load("PLACEHOLDER.png")
	screen.blit(title, (0,-3))
	running = True

	while running:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					screen.blit(place, (5, 0))
				if event.key == pygame.K_d:
					pygame.mixer.music.load("despacito.mid")
					pygame.mixer.music.play()
				if event.key == pygame.K_n:
					pygame.mixer.music.load("mm2wood.mid")
					pygame.mixer.music.play()

if __name__=="__main__":
	main()