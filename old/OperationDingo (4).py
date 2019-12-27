import pygame

def main():
	pygame.init()
	logo = pygame.image.load("PreAlpha.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Operation Dingo")
	screen = pygame.display.set_mode((1778,876))
	pygame.mixer.music.load("stars.mid")
	pygame.mixer.music.play()
	title = pygame.image.load("Title.png")
	place = pygame.image.load("PLACEHOLDER.png")
	level1 = pygame.image.load("Level1.png")
	lachlan = pygame.image.load("idle.png")
	screen.blit(title, (0,-3))
	running = True

	while running:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					screen.blit(level1, (0, 0))
					pygame.mixer.music.stop()
					screen.blit(lachlan, (0, 600))
				if event.key == pygame.K_RIGHT:
					print("Thanos Car")


if __name__=="__main__":
	main()