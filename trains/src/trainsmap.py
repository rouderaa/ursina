import observer
import pygame
import math

class TrainsMap(observer.Observer):
    def __init__(self):
        pygame.init()

        self.width, self.height = 400, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2D Position Viewer")
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self, state):
        x, y, angle = state
        print(f"TrainsMap: x={x:.2f}, y={y:.2f}, angle={angle:.2f}")
        self.draw(x, y, angle)

    def set_model(self, model):
        model.attach(self)  # Attach to the model

    def draw(self, x, y, angle):
        self.screen.fill((255, 255, 255))  # White background

        # Convert model coordinates to screen coordinates
        screen_x = int(self.width / 2 + x * 100)
        screen_y = int(self.height / 2 - y * 100)

        # Draw a red dot at the position
        pygame.draw.circle(self.screen, (255, 0, 0), (screen_x, screen_y), 5)

        # Draw coordinate axes
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height / 2), (self.width, self.height / 2))
        pygame.draw.line(self.screen, (0, 0, 0), (self.width / 2, 0), (self.width / 2, self.height))

        pygame.display.flip()
        self.clock.tick(60)  # Limit to 60 fps
