import pygame
import random

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('JUMP!')
icon = pygame.image.load('man.png')
pygame.display.set_icon(icon)
pygame.mixer.music.load('fon_music.mp3')
pygame.mixer.music.play()

stone_img = [pygame.image.load('stone1.png'), pygame.image.load('stone2.png'), pygame.image.load('stone3.png')]
stone_options = [30, 454, 42, 449, 40, 462]

frog_img = [pygame.image.load('frog.png')]
image_counter = 0

class Stone:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_stn(self, radius, y, width, image):
        self.x = radius
        self.y =y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))


user_width = 60
user_height = 100
user_x = display_width // 3
user_y = display_height - user_height - 100

stone_width = 20
stone_height = 70
stone_x = display_width - 50
stone_y = display_height - stone_height - 100


clock = pygame.time.Clock()
make_jump = None
jump_counter = 30


def main():
    global make_jump
    game = True
    stn_arr = []
    create_stone(stn_arr)
    land = pygame.image.load('mountains.jpg')
    game_ov = pygame.image.load('game_over.png')
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()


        display.blit(land, (0, 0))
        draw_array(stn_arr)

        draw_frog()
        if check_colision(stn_arr):
            display.blit(game_ov, (250, 150))
            game = False

        pygame.display.update()
        clock.tick(70)
    return game_over()

def jump():
    global user_y, jump_counter, make_jump
    if jump_counter >= -30:
        user_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = None

def create_stone(array):
    choice = random.randrange(0, 3)
    img = stone_img[choice]
    width = stone_options[choice*2]
    height = stone_options[choice*2 + 1]
    array.append(Stone(display_width + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = stone_img[choice]
    width = stone_options[choice*2]
    height = stone_options[choice*2 + 1]
    array.append(Stone(display_width + 300, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = stone_img[choice]
    width = stone_options[choice*2]
    height = stone_options[choice*2 + 1]
    array.append(Stone(display_width + 600, height, width, img, 4))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius-maximum < 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0,5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)

    return radius

def draw_array(array):
    for stn in array:
        check = stn.move()
        if not check:
            radius = find_radius(array)

            choice = random.randrange(0, 3)
            img = stone_img[choice]
            width = stone_options[choice * 2]
            height = stone_options[choice * 2 + 1]
            stn.return_stn(radius, height, width, img)

def draw_frog():
    display.blit(frog_img[image_counter], (user_x, user_y + 55))

def check_colision(barriers):
    for barrier in barriers:
        if user_y + user_height >= barrier.y:
            if barrier.x <= user_x <= barrier.x+ barrier.width:
                return True
            elif barrier.x <= user_x + user_width <= barrier.x+ barrier.width:
                return True

    return False

def game_over():
    stop = True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

main()
