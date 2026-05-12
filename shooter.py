import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Space Shooter')
        self.clock = pygame.time.Clock()
        self.running = True

        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(400, 500)
        self.all_sprites.add(self.player)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0)) # Black background
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()

# Create an instance of the Game

if __name__=="__main__":
    game = Game()
    game.run()