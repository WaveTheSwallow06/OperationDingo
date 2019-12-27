import pygame

def main():
	pygame.init()
	logo = pygame.image.load("PreAlpha.png")
	nice = "mm2wood.mid"
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Operation Dingo")
	screen = pygame.display.set_mode((1778,876))
	pygame.mixer.music.load("mm2wood.mid")
	pygame.mixer.music.play()
	x = 1778
	y = 876
	display_surface = pygame.display.set_mode((x, y ))
	image = pygame.image.load("Title.png")
	running = True

	while running:
		for event in pygame.event.get():
			image(x,y)
			if event.type == pygame.QUIT:
					running = False

if __name__=="__main__":
	main()