import pygame

def main():
	pygame.init()
	logo = pygame.image.load("PreAlpha.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Operation Dingo")
	screen = pygame.display.set_mode((1778,876))
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__=="__main__":
	main()