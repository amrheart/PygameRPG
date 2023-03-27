import pygame
import math
import time

# cardinal direction constants
E = 0
N = 1
NE = 2
NW = 3
S = 4
SE = 5
SW = 6
W = 7

# events
PEACE = 0
BATTLE = 1

# action constants
WALKING = 0
ATTACKING = 1
TALKING = 2
DYING = 3
BEING_HIT = 4
STOPPED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("orce_sprite_sheet.png")
        self.image.set_colorkey((105, 74, 46))
        self.sprite_surf = pygame.Surface((96,96))
        
        #self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0,0,96,96)
        self.rectcenterx = self.rect.width/2
        self.rectcentery = self.rect.height/2
        
        self.crop_rect = pygame.Rect(0,0,96,96)
        
        
        # my stuff
        self.cur_x = 0
        self.cur_y = 0
        self.x_change = 0
        self.y_change = 0
        self.movetox = self.cur_x
        self.movetoy = self.cur_y
        self.move_angle = 0
        
        # animation stuff
        self.direction = S
        self.action = STOPPED
        self.frame_width = 96
        self.row_height = 0
        self.steps = 8
        self.step = 0
        self.anim_timer = pygame.time.Clock()
        self.elapsed_time = 0
        self.dir_offset = self.frame_width * self.steps
        
    def update(self):
        self.click_move()
        self.animate()

    # increment the sprites movement
    def click_move(self):
        # Player is at the location
        if self.movetox-10 < self.rect.x < self.movetox+10 and self.movetoy-10 < self.rect.y < self.movetoy+10:
                pass
        else:
            print("move sprite")
            # move the sprite a little towards the goal
            self.cur_x = self.cur_x + self.x_change *2
            self.cur_y = self.cur_y + self.y_change *2
            self.set_pos((self.cur_x, self.cur_y))
            print(self.cur_x)
            print(self.cur_y)
        
    # sets new movement parameters. Used by click move function
    def path_find(self, pos):
        self.movetox = pos[0]
        self.movetoy = pos[1]
        x_difference = pos[0] - self.cur_x
        y_difference = pos[1] - self.cur_y
        
        # update states based on x and y difference
        if x_difference > 0:
            if y_difference > 0:
                self.direction = SE
            else:
                self.direction = NE
        else:
            if y_difference > 0:
                self.direction = SW
            else:
                self.direction = NW
        
        hypotenuse = x_difference**2 + y_difference**2
        hypotenuse = math.sqrt(hypotenuse)
        self.x_change = x_difference / hypotenuse
        self.y_change = y_difference / hypotenuse
        print(self.x_change)
        print(self.y_change)
        
    # utility function to set coordinate directly
    def set_pos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    # call every tick to progress the animation cycle
    def animate(self):
        self.elapsed_time = self.elapsed_time + self.anim_timer.tick()
        
        # reset the step counter if we exceed the max step
        if self.step == self.steps:
            self.step = 0
        
        # increment the step
        if self.elapsed_time/1000 > .25:
            self.crop_rect.x = self.direction * self.dir_offset + self.step * self.frame_width
            self.step = self.step + 1
            self.elapsed_time = 0

        
class Scene:
    def __init__(self):
        self.background = [[]*10]
        self.image = pygame.image.load("rough ripple earth medium to ground tileset.bmp")
        
        self.rect = pygame.Rect(0,0,128,96)
        self.crop_rect = pygame.Rect(640,384,128,96)


pygame.init()

#create the player
p1 = Player()


# create a new group for sprites
g1 = pygame.sprite.GroupSingle()
g1.add(p1)

canvas = pygame.display.set_mode((1280, 960))
clock = pygame.time.Clock()
running = True

# create the scene
s1 =  Scene()

pygame.display.set_caption("New Canvas")
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse clicked")
            mouse_pos = pygame.mouse.get_pos()
            g1.sprite.path_find(mouse_pos)
    canvas.fill("purple")
    p1.update()
    canvas.blit(s1.image, s1.rect, area=s1.crop_rect)
    canvas.blit(p1.image, p1.rect, area=p1.crop_rect)
    pygame.display.flip()
    
    dt = clock.tick(60)/1000
    
pygame.quit()