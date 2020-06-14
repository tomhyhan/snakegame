import pygame
import random
import math

class snake_body:
    move_vel_x = 0
    move_vel_y = 0
    snake_list = []
    snake_lng = 1
    snake_speed = 19

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.snake_body = [self.x,self.y]

    def draw(self,window):
        self.move()
        if len(self.snake_list) > self.snake_lng:
            self.snake_list.pop(0)
        for item in self.snake_list:
            pygame.draw.rect(window,(255,0,0),[item[0],item[1],20,20])

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            snake_body.move_vel_x = self.snake_speed
            snake_body.move_vel_y = 0
        elif keys[pygame.K_LEFT]:
            snake_body.move_vel_x = -self.snake_speed
            snake_body.move_vel_y = 0
        elif keys[pygame.K_UP]:
            snake_body.move_vel_x = 0
            snake_body.move_vel_y = -self.snake_speed
        elif keys[pygame.K_DOWN]:
            snake_body.move_vel_x = 0
            snake_body.move_vel_y = self.snake_speed

        self.x += snake_body.move_vel_x
        self.y += snake_body.move_vel_y

        body = [self.x,self.y]
        self.snake_list.append(body)
    # def body(self):
    #     self.snake_list.append(self.snake_body)
    #     return self.snake_list


class snake_food:

    def __init__(self, foodx, foody):
        self.foodx = foodx
        self.foody = foody

    def draw(self,surface):
        pygame.draw.rect(surface,(0,255,9),[self.foodx,self.foody,20,20])


def get_draw(window,snake,food):
    window.fill((0, 0, 0))
    snake.draw(window)
    food.draw(window)
    pygame.display.update()


def main():
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption("snake game using class")
    snake = snake_body(300, 300)
    food = snake_food(100,100)
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        snake.snake_speed = 20
        get_draw(window, snake,food)

        if math.sqrt((snake.x - food.foodx) **2 + (snake.y - food.foody)**2)< 20:
            food.foodx = random.randint(0,590)
            food.foody = random.randint(0,590)
            snake.snake_lng += 1

    pygame.quit()

main()