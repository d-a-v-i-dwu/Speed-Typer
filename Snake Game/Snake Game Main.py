import pygame
from pygame.locals import *
from pygame.rect import Rect
import time
import random

class Snake:
    def __init__(self, parent_screen, length=2):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("Snake Game/block.jpg").convert() #loads an image
        self.x = [40] * length
        self.y = [40] * length
        self.direction = "down"
        
    def draw(self):
        self.parent_screen.fill((105, 165, 67))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i])) #blit draws an image, (what you're drawing, (where))

    def increase_length(self):
        self.length += 1
        self.x.append(0)
        self.y.append(0)

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i], self.y[i] = self.x[i-1], self.y[i-1]

        if self.direction == "up":
            self.y[0] -= 40
        elif self.direction == "down":
            self.y[0] += 40
        elif self.direction == "left":
            self.x[0] -= 40
        else:
            self.x[0] += 40
        self.draw()

        head_rect = self.block.get_rect()
        head_rect[0], head_rect[1] = self.x[0], self.y[0]
        self.head_rect = pygame.Rect(head_rect)

class Apple:
    def __init__(self, parent_screen):
        self.apple = pygame.image.load("Snake Game/apple.jpg").convert()
        self.parent_screen = parent_screen

        self.x = random.randrange(0, 760, 40)
        self.y = random.randrange(0, 560, 40)
        apple_rect = self.apple.get_rect()
        apple_rect[0], apple_rect[1] = self.x, self.y
        self.apple_rect = pygame.Rect(apple_rect)

    def draw(self):
        self.parent_screen.blit(self.apple,(self.x, self.y))

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((800, 600)) #set mode is initializing a game window
        self.window_rect = pygame.Rect(0, 0, 800, 600)
        self.surface.fill((105, 165, 67)) #fill colours the background, rgb nums
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.running = True
        self.pause = False

    def play(self):
        self.snake.walk()
        self.self_collide()
        self.border_collide()
        self.apple_collide()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def apple_collide(self):
        sound = pygame.mixer.Sound("Snake Game/1_snake_game_resources_ding.mp3")
        if self.snake.head_rect.colliderect(self.apple.apple_rect):
            self.snake.increase_length()
            new_apple = Apple(self.surface)
            self.apple = new_apple
            pygame.mixer.Sound.play(sound)
    
    def border_collide(self):
        if not self.window_rect.contains(self.snake.head_rect):
            self.pause = True

    def self_collide(self):
        for i in range(1, self.snake.length):
            if self.snake.x[0] == self.snake.x[i] and self.snake.y[0] == self.snake.y[i]:
                self.pause = True

    def display_score(self):
        font = pygame.font.SysFont("calibri", 25)
        score = font.render(f"Score: {(self.snake.length-2) * 100}", True, (255, 255, 255))
        self.surface.blit(score, (20, 20))

    def show_game_over(self):
        self.surface.fill((105, 165, 67))
        font = pygame.font.SysFont('calibri', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (125, 200))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (125, 250))
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                    if event.key == K_RETURN:
                        self.pause = False

                    if event.key == K_UP and self.snake.direction != "down":
                        self.snake.direction = "up"
                    if event.key == K_DOWN and self.snake.direction != "up":
                        self.snake.direction = "down"
                    if event.key == K_LEFT and self.snake.direction != "right":
                        self.snake.direction = "left"
                    if event.key == K_RIGHT and self.snake.direction != "left":
                        self.snake.direction = "right"

                elif event.type == QUIT:
                    self.running = False
            
            if not self.pause:
                self.play()
            else:
                self.show_game_over()
                self.reset()

            time.sleep(0.15)

if __name__ == "__main__":
    game = Game()
    game.run()