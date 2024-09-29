import pygame
pygame.init()

width, height = 800, 600
block_size = 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game") 
clock = pygame.time.Clock()

class Snake():
    def __init__(self):
        self.x, self.y = block_size, block_size
        self.xdir, self.ydir = 1, 0
        self.head = pygame.Rect(self.x, self.y, block_size, block_size)
        self.body = [pygame.Rect(self.x- block_size, self.y, block_size, block_size)]
        self.dead = True
    def update(self):
        self.body.append(self.head)
        for x in range(len(self.body)-1):
            self.body[x].x, self.body[x].y = self.body[x+1].x, self.body[x+1].y
        self.head.x += self.xdir * block_size 
        self.head.y += self.ydir * block_size 
        self.body.remove(self.head)
            
def draw_grid():
    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen ,"#3c3c3b", rect, 1)

snake = Snake()
draw_grid()

run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    snake.update()
    screen.fill("black")
    draw_grid()
    pygame.draw.rect(screen, "green", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
    pygame.display.update()
pygame.quit()