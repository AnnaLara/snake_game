import pygame
import random
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Nokia Snake Game")
win.fill((0, 0, 0))
vel = 20


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    def draw_square(self):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, 20, 20))

class Snake:
    def __init__(self, pos_list):
        self.pos_list = pos_list

    def draw_snake(self):
        for pos in self.pos_list:
            s = Square(pos[0], pos[1])
            s.draw_square()

    def move_body_pos(self, direction, eat):
        new_head = self.new_head_pos(direction)
        self.pos_list.insert(0, new_head)
        if not eat:
            self.pos_list.remove(self.pos_list[-1])

    def new_head_pos(self, direction):
        x = self.pos_list[0][0]
        y = self.pos_list[0][1]
        if direction == 'l':
            if x - vel < 0:
                x = 480
            else:
                x -= vel
        if direction == 'r':
            if x + vel > 480:
                x = 0
            else:
                x += vel
        if direction == 'u':
            if y - vel < 0:
                y = 480
            else:
                y -= vel
        if direction == 'd':
            if y + vel > 480:
                y = 0
            else:
                y += vel
        return [x, y]

    def if_crash(self):
        for i in range(1, len(self.pos_list)):
            if self.pos_list[0] == self.pos_list[i]:
                return True

    def if_finds_food(self, food):
        if self.pos_list[0] == [food.x, food.y]:
            return True


class Food:
    def __init__(self):
        pass

    def generate_food_coord(self, snake_pos_list):
        self.x = random.randint(0, 24)*20
        self.y = random.randint(0, 24)*20

        for pos in snake_pos_list:
            if [self.x, self.y] == pos:
                self.generate_food_coord(snake_pos_list)

    def draw_food_square(self):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, 20, 20))

snake = Snake([[60, 20], [40, 20], [20, 20], [0, 20]])
snake.draw_snake()
pygame.display.update()

run = True
food = Food()
food.generate_food_coord(snake.pos_list)
print(food.x, food.y)

direction = 'r'
eat = False

while run:
    pygame.time.delay(150)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and direction != 'r':
        direction = 'l'

    if keys[pygame.K_RIGHT] and direction != 'l':
        direction = 'r'

    if keys[pygame.K_UP] and direction != 'd':
        direction = 'u'

    if keys[pygame.K_DOWN] and direction != 'u':
        direction = 'd'


    win.fill((0, 0, 0))
    snake.move_body_pos(direction, eat)
    eat = False
    snake.draw_snake()


    food.draw_food_square()


    pygame.display.update()

    if snake.if_crash():
        print('Crash!')
        run = False

    if snake.if_finds_food(food):
        print('Food!')
        food.generate_food_coord(snake.pos_list)
        print(food.x, food.y)
        eat = True



pygame.quit()
