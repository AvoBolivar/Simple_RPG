import Market
import pygame
import sys
import Images
import random

# TODO make an enemy class that allows copies of itself all do the same thing
# drew up setup, already changed some variables
# need to either figure out health bar or completely just take away health bar from enemies
# or make them all different
# TODO finish the point system of the game
# TODO finish making the store hardest part might be knowing when you can not buy anymore
# TODO think about adding inventory, if so how to use it and tell the player what they have
# TODO if so their is no max, they would just waste their items


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.x = 100
        self.y = 50
        self.speed = 5
        self.health = 100
        self.armour = 100
        self.armour_level = 1
        self.image = pygame.image.load("knight_idle_1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

        self.idle_images = []
        self.idle_images.append(pygame.image.load("knight_idle_1.png"))
        self.idle_images.append(pygame.image.load("knight_idle_2.png"))
        self.idle_images.append(pygame.image.load("knight_idle_3.png"))
        self.idle_images.append(pygame.image.load("knight_idle_4.png"))

        self.move_right_images = []
        self.move_right_images.append(pygame.image.load("knight_move_1.png"))
        self.move_right_images.append(pygame.image.load("knight_move_2.png"))
        self.move_right_images.append(pygame.image.load("knight_move_3.png"))
        self.move_right_images.append(pygame.image.load("knight_move_4.png"))

        self.move_left_images = []
        self.move_left_images.append(pygame.image.load("knight_run_left_1.png"))
        self.move_left_images.append(pygame.image.load("knight_run_left_2.png"))
        self.move_left_images.append(pygame.image.load("knight_run_left_3.png"))
        self.move_left_images.append(pygame.image.load("knight_run_left_4.png"))

        self.move_up_images = []
        self.move_up_images.append(pygame.image.load("knight_forward_run-1.png.png"))
        self.move_up_images.append(pygame.image.load("knight_forward_run-2.png.png"))
        self.move_up_images.append(pygame.image.load("knight_forward_run-3.png.png"))
        self.move_up_images.append(pygame.image.load("knight_forward_run-4.png.png"))
        self.move_up_images.append(pygame.image.load("knight_forward_run-5.png.png"))
        self.move_up_images.append(pygame.image.load("knight_forward_run-6.png.png"))

        self.move_down_images = []
        self.move_down_images.append(pygame.image.load("knight_back_run-1.png.png"))
        self.move_down_images.append(pygame.image.load("knight_back_run-2.png.png"))
        self.move_down_images.append(pygame.image.load("knight_back_run-3.png.png"))
        self.move_down_images.append(pygame.image.load("knight_back_run-4.png.png"))
        self.move_down_images.append(pygame.image.load("knight_back_run-5.png.png"))
        self.move_down_images.append(pygame.image.load("knight_back_run-6.png.png"))

        self.player_list = self.idle_images

    def update(self):
        if player_action == 0:
            self.player_list = self.idle_images

        if player_action == 1:
            self.player_list = self.move_right_images
            self.x += self.speed
        if player_action == 2:
            self.player_list = self.move_left_images
            self.x -= self.speed
        if player_action == 3:
            self.player_list = self.move_down_images
            self.y -= self.speed
        if player_action == 4:
            self.player_list = self.move_up_images
            self.y += self.speed

        collect_coins = pygame.sprite.spritecollide(player, background_images, True)
        if collect_coins:
            Market.coins += 25

        self.index += 1
        if self.index >= len(self.player_list):
            self.index = 0

        self.image = self.player_list[self.index]
        self.rect.center = [self.x, self.y]


class PlayerHitBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("trigger_box-1.png.png")
        self.rect = self.image.get_rect()
        self.rect.center = [player.x+14, player.y + 2]

    def update(self):
        self.rect.center = [player.x+12, player.y+2]


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("chort_idle_anim_f0.png")
        self.rect = self.image.get_rect()
        self.attack_type = -1
        self.war = 0
        self.x = 300
        self.y = 200
        self.coins = 0
        self.in_range = False
        self.radius = 80
        self.speed = 2
        self.rect.center = [self.x, self.y]
        self.index = 0

        self.idle_images = []
        self.idle_images.append(pygame.image.load("chort_idle_anim_f0.png"))
        self.idle_images.append(pygame.image.load("chort_idle_anim_f1.png"))
        self.idle_images.append(pygame.image.load("chort_idle_anim_f2.png"))
        self.idle_images.append(pygame.image.load("chort_idle_anim_f3.png"))

        self.run_right = []
        self.run_right.append(pygame.image.load("chort_run_anim_f0.png"))
        self.run_right.append(pygame.image.load("chort_run_anim_f1.png"))
        self.run_right.append(pygame.image.load("chort_run_anim_f2.png"))
        self.run_right.append(pygame.image.load("chort_run_anim_f3.png"))

        self.coin_bag = []
        self.coin_bag.append(pygame.image.load("coin_bag-1.png"))
        self.coin_bag.append(pygame.image.load("coin_bag-2.png"))
        self.coin_bag.append(pygame.image.load("coin_bag-3.png"))
        self.coin_bag.append(pygame.image.load("coin_bag-4.png"))

    def update(self):
        if self.index >= len(self.idle_images):
            self.index = 0

        if enemy_health_bar.status == 0:
            self.image = self.coin_bag[self.index]
            self.index += 1

            self.looted = pygame.sprite.spritecollide(player, enemy_group, True)
            if self.looted:
                 add_enemies()
                 self.coins += 10

        if enemy_health_bar.status == 1:
            if self.x+self.radius >= player.x >= self.x-self.radius and self.y-self.radius <= player.y <= self.y+self.radius:
                if 15 < self.x - player.x < 19 and -3 < self.y - player.y < 3:
                    self.war = 1
                    # war is if in line to attack
                    # attacking equals 1 when a is pressed regardless of anything else
                    self.image = self.idle_images[self.index]
                    if player_attacking == 0:
                        self.attack_type = 0
                    if player_attacking == 1:
                        self.attack_type = 1
                else:
                    self.war = 0
                    self.attack_type = -1
                    if self.x < player.x+19:
                        self.x += self.speed
                    if self.x > player.x+19:
                        self.x -= self.speed
                    if self.y < player.y:
                        self.y += self.speed
                    if self.y > player.y:
                        self.y -= self.speed
                self.image = self.run_right[self.index]
            else:
                self.image = self.idle_images[self.index]
                self.war = 0

            self.index += 1
            self.rect.center = [self.x, self.y]
        else:
            self.attack_type = 2


class CommonEnemy(pygame.sprite.Sprite):
    def __init__(self, idle_images, run_images, speed, health, x, y, worth, radius):
        super().__init__()
        self.run_images = run_images
        self.idle_images = idle_images
        self.image = (self.idle_images[0])
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = [self.x, self.y]
        self.index_length = len(self.idle_images)
        self.radius = radius
        self.speed = speed
        self.health = health
        self.worth = worth
        self.index = 0
        self.enemy_ready_to_attack = 0
        self.alive = True

    def update(self):
        # checking to see if index surpassed list length
        if self.index >= self.index_length:
            self.index = 0

        if self.x + self.radius >= player.x >= self.x - self.radius and self.y - self.radius <= player.y <= self.y + self.radius:
            # player is in the radius of the enemy
            if not(15 < self.x - player.x < 19 and -3 < self.y - player.y < 3):
                self.enemy_ready_to_attack = 0
                # if in the radius tho not in line of attack
                if self.x < player.x + 19:
                    self.x += self.speed
                if self.x > player.x + 19:
                    self.x -= self.speed
                if self.y < player.y:
                    self.y += self.speed
                if self.y > player.y:
                    self.y -= self.speed
        else:
            # if player not in radius
            self.image = self.idle_images[self.index]

        if attack.attack_type == 2 and self.health > 0:
            # this means enemy is getting hit
            self.health -= 20

        if self.health <= 0:
            pygame.sprite.spritecollide(attack, common_group, True)
            self.alive = False
            print(imp.alive)
            self.kill()
            print(imp.alive)

        # after running it all
        self.index += 1
        self.rect.center = [self.x, self.y]


class CoinBag(pygame.sprite.Sprite):
    def __init__(self, amount):
        super().__init__()
        self.image = pygame.image.load("coin_bag-1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [player.x+ 30, player.y]
        self.index = 0
        self.worth = amount

    def update(self):
        if self.index >= len(Images.coin_bag):
            self.index = 0

        self.image = Images.coin_bag[self.index]
        self.index += 1


class EnemyHealth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.status = 1
        self.intervals = self.hp/4
        self.getHit = Market.player_level*30
        self.image = pygame.image.load("Enemy_health-1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [enemy.x, enemy.y-10]

    def update(self):
        self.rect.center = [enemy.x, enemy.y-10]
        if enemy.attack_type == 1:
            self.hp -= self.getHit

        if self.hp <= self.hp-self.intervals:
            self.image = pygame.image.load("Enemy_health-2.png")
        if self.hp <= self.hp - self.intervals*2:
            self.image = pygame.image.load("Enemy_health-3.png")
        if self.hp <= self.hp - self.intervals*3:
            self.image = pygame.image.load("Enemy_health-4.png")
        if self.hp <= 0:
            self.image = pygame.image.load("attacking-7.png")
            self.status = 0


class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("attacking-7.png")
        self.rect = self.image.get_rect()
        self.rect.center = [0, 0]
        self.transition = 0
        self.x = 0
        self.y = 0
        self.index = 0
        self.attack_type = 0

        self.empty_list = []
        self.empty_list.append(pygame.image.load("attacking-7.png"))
        self.empty_list.append(pygame.image.load("attacking-6.png"))

        self.enemy_hit = []
        self.enemy_hit.append(pygame.image.load("enemy attack-1.png"))
        self.enemy_hit.append(pygame.image.load("enemy attack-2.png"))
        self.enemy_hit.append(pygame.image.load("enemy attack-3.png"))
        self.enemy_hit.append(pygame.image.load("enemy attack-4.png"))

        self.war = []
        self.war.append(pygame.image.load("attacking-1.png"))
        self.war.append(pygame.image.load("attacking-2.png"))
        self.war.append(pygame.image.load("attacking-3.png"))
        self.war.append(pygame.image.load("attacking-4.png"))
        self.war.append(pygame.image.load("attacking-5.png"))
        self.war.append(pygame.image.load("attacking-6.png"))
        self.war.append(pygame.image.load("attacking-7.png"))
        self.war.append(pygame.image.load("attacking-8.png"))
        self.war.append(pygame.image.load("attacking-9.png"))
        self.war.append(pygame.image.load("attacking-10.png"))
        self.war.append(pygame.image.load("attacking-11.png"))
        self.war.append(pygame.image.load("attacking-12.png"))

        self.player_attacking_right = []
        self.player_attacking_right.append(pygame.image.load("player attack right-1.png"))
        self.player_attacking_right.append(pygame.image.load("player attack right-2.png"))
        self.player_attacking_right.append(pygame.image.load("player attack right-3.png"))
        self.player_attacking_right.append(pygame.image.load("player attack right-4.png"))
        self.player_attacking_right.append(pygame.image.load("player attack right-5.png"))
        self.player_attacking_right.append(pygame.image.load("player attack right-6.png"))

        self.image_list = self.enemy_hit

    def update(self):
        # self.attack_type, if 1 that means only enemy and if 2 that is both if 0 nothing happens
        if self.index >= len(self.image_list):
            self.index = 0

        if self.transition == 0:
            if attacking == 0:
                self.image = pygame.image.load("attacking-7.png")

            if attacking == 1:
                self.image_list = self.player_attacking_right
                self.attack_type = 3
                self.image = self.player_attacking_right[self.index]
            else:
                self.attack_type = 0

        enemy_ready = pygame.sprite.spritecollide(player_hitbox, common_group, False)
        if enemy_ready:
            if self.index > len(self.enemy_hit):
                self.index = 0
            self.transition = 1
            self.image_list = self.enemy_hit
            self.image = self.enemy_hit[self.index]
            if attacking == 1:
                self.image_list = self.war
                self.image = self.war[self.index]
        else:
            self.transition = 0

        self.x = player.x+10
        self.y = player.y
        self.rect.center = [self.x, self.y]

        self.index += 1


class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.initial_health = 100
        self.incraments = self.hp/5
        self.image = pygame.image.load("sqr_health_5.png")
        self.rect = self.image.get_rect()
        self.rect.center = [60, 10]

    def update(self):
        Market.player_health = self.hp

        if attack.transition == 1 and armour_bar.hp <= 0:
            self.hp -= 2

        if self.hp <= self.initial_health-self.incraments:
            self.image = pygame.image.load("sqr_health_4.png")
        if self.hp <= self.initial_health-self.incraments*2:
            self.image = pygame.image.load("sqr_health_3.png")
        if self.hp <= self.initial_health-self.incraments*3:
            self.image = pygame.image.load("sqr_health_2.png")
        if self.hp <= self.initial_health-self.incraments*4:
            self.image = pygame.image.load("sqr_health_1.png")
        if self.hp <= self.initial_health-self.incraments*5:
            self.image = pygame.image.load("attacking-7.png")

        if self.hp <= 0:
            game_over()


class Armour(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sqr_armour_5.png")
        self.rect = self.image.get_rect()
        self.rect.center = [60, 30]
        self.initial_health = 100
        self.hp = 100
        self.incraments = self.hp/5

    def update(self):
        Market.player_armour = self.hp

        if attack.transition == 1:
            self.hp -= 2

        if self.hp <= self.initial_health-self.incraments:
            self.image = pygame.image.load("sqr_armour_4.png")
        if self.hp <= self.initial_health-self.incraments*2:
            self.image = pygame.image.load("sqr_armour_3.png")
        if self.hp <= self.initial_health-self.incraments*3:
            self.image = pygame.image.load("sqr_armour_2.png")
        if self.hp <= self.initial_health-self.incraments*4:
            self.image = pygame.image.load("sqr_armour_1.png")
        if self.hp <= self.initial_health-self.incraments*5:
            self.image = pygame.image.load("attacking-7.png")


class ShopButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("shop_button.png")
        self.rect = self.image.get_rect()
        self.rect.center = [50, 370]

    def clicked(self):
        if shop_showing == 1:
            button_clicked = pygame.sprite.spritecollide(cursor, shop_group, False)
            if button_clicked:
                self.image = pygame.image.load("shop_button_press.png")
                Market.shop_window()
                Market.coins = Market.amnt_of_money[len(Market.amnt_of_money)-1]

    def unclick(self):
        self.image = pygame.image.load("shop_button.png")


class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("table_2.png")
        self.rect = self.image.get_rect()
        self.rect.center = [520, 50]


class Clerk(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("elf_f_idle_anim_f0.png")
        self.rect = self.image.get_rect()
        self.rect.center = [520, 31]
        self.index = 0
        self.idle_list = []
        self.idle_list.append(pygame.image.load("elf_f_idle_anim_f0.png"))
        self.idle_list.append(pygame.image.load("elf_f_idle_anim_f1.png"))
        self.idle_list.append(pygame.image.load("elf_f_idle_anim_f2.png"))
        self.idle_list.append(pygame.image.load("elf_f_idle_anim_f3.png"))

    def update(self):
        if self.index >= len(self.idle_list):
            self.index = 0

        self.image = self.idle_list[self.index]

        self.index += 1


class ShoppingArea(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("shop.png")
        self.rect = self.image.get_rect()
        self.rect.center = [530, 70]


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("crosshair_1.png")
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)


class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("text box.png")
        self.rect = self.image.get_rect()
        self.rect.center = [520, 370]


class StatHolder(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("stats_holder.png")
        self.rect = self.image.get_rect()
        self.rect.center = [520, 300]


class StatTitle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("stat title-1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [520, 235]


class CoinSymbol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin_anim_f0.png")
        self.rect = self.image.get_rect()
        self.rect.center = [490, 360]
        self.index = 0

    def update(self):
        if self.index >= len(Images.coin_icon):
            self.index = 0

        self.image = Images.coin_icon[self.index]
        self.index += 1


class ArmorSymbol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("body_armor-1.png.png")
        self.rect = self.image.get_rect()
        self.rect.center = [500, 260]


class HeartSymbol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("heart-1.png.png")
        self.rect = self.image.get_rect()
        self.rect.center = [500, 290]


class Numbers(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Numbers-10.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.collected = 0
        self.digits = 0
        self.a_nums = 0
        self.h_nums = 0

        self.imgs = []
        self.imgs.append(pygame.image.load("Numbers-10.png"))
        self.imgs.append(pygame.image.load("Numbers-1.png"))
        self.imgs.append(pygame.image.load("Numbers-2.png"))
        self.imgs.append(pygame.image.load("Numbers-3.png"))
        self.imgs.append(pygame.image.load("Numbers-4.png"))
        self.imgs.append(pygame.image.load("Numbers-5.png"))
        self.imgs.append(pygame.image.load("Numbers-6.png"))
        self.imgs.append(pygame.image.load("Numbers-7.png"))
        self.imgs.append(pygame.image.load("Numbers-8.png"))
        self.imgs.append(pygame.image.load("Numbers-9.png"))

    def update(self):
        # setup is ones, tens, hundreds, thousands
        if self.collected < Market.coins:
            self.digits = [int(x) for x in str(Market.coins)]
            for k in range(len(self.digits)):
                places[-k-1].image = self.imgs[self.digits[-k-1]]

        self.collected = coins

    def done_shopping(self):
        self.a_nums = [int(x) for x in str(Market.amnt_of_amor)]
        for k in range(len(self.a_nums)):
            amor_gui[-k-1].image = self.imgs[self.a_nums[-k-1]]


def game_over():
    sys.exit()


def add_enemies():
    location = [random.randint(100, 240), random.randint(100, 240)]
    imp = CommonEnemy(Images.imp_idle, Images.imp_run, 2.2 + .5 * i, 100, location[0], location[1], 10, 100)
    common_group.add(imp)


def killed():
    imp_dead = pygame.sprite.spritecollide(attack, common_group, True)
    if imp_dead:
        spawn_coin_bag(20)



pygame.init()

width = 600
height = 400

screen = pygame.display.set_mode((width, height))

Clock = pygame.time.Clock()

# variable that says whether the shop button is showing or not
shop_showing = 0
attack_type = 0
player_attacking = 0
attacking = 0
coins = 0
enemy_ready_to_attack = 0

# Sprite groups
background_images = pygame.sprite.Group()

# player
player_stuff = pygame.sprite.Group()
player = Player()
player_action = 0

# player hitbox
player_hitbox = PlayerHitBox()
player_stuff.add(player_hitbox)

# enemy
enemy = Enemy()
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

# common enemy
common_group = pygame.sprite.Group()
for i in range(5):
    location = [random.randint(100, 300), random.randint(120, 300)]
    imp = CommonEnemy(Images.imp_idle, Images.imp_run, 2.2+.5*i, 100, location[0], location[1], 10, 100)
    common_group.add(imp)


# common enemy coin bag spawn
def spawn_coin_bag(amount):
    print("made coin bag")
    coin = CoinBag(amount)
    background_images.add(coin)


# enemy health bar
enemy_health_bar = EnemyHealth()
enemy_group.add(enemy_health_bar)
# attacking image
attack = Attack()

# health bar
health_bar = Health()

# armour bar
armour_bar = Armour()

# mouse
cursor = Cursor()

# text box
textbox = TextBox()
statholder = StatHolder()
stat_title = StatTitle()
armor_symbol = ArmorSymbol()
armor_ones = Numbers(530, 260)
armor_tens = Numbers(544, 260)
heart_symbol = HeartSymbol()
heart_ones = Numbers(530, 290)
heart_tens = Numbers(544, 290)
coin_icon = CoinSymbol()

# numbers
number_group = pygame.sprite.Group()
ones = Numbers(505, 363)
tens = Numbers(519, 363)
hundreds = Numbers(533, 363)
thousands = Numbers(547, 363)
places = [ones, tens, hundreds, thousands]
amor_gui = [armor_ones, armor_tens]
health_gui = [heart_ones, heart_tens]
number_group.add(ones, tens, hundreds, thousands)
number_group.add(armor_ones, armor_tens)
number_group.add(heart_ones, heart_tens)

# shop button
shop_button = ShopButton()
shop_group = pygame.sprite.Group()
shop_group.add(shop_button)

# shop clerk
clerk = Clerk()

# Shop
shop = Shop()
shopping_area = ShoppingArea()
all_sprites = pygame.sprite.Group()

all_sprites.add(shopping_area, clerk, shop)
all_sprites.add(attack)
all_sprites.add(player)
all_sprites.add(cursor)
all_sprites.add(health_bar, armour_bar)
all_sprites.add(textbox)
all_sprites.add(statholder, armor_symbol, heart_symbol, stat_title)
all_sprites.add(coin_icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_action = 1
            if event.key == pygame.K_LEFT:
                player_action = 2
            if event.key == pygame.K_UP:
                player_action = 3
            if event.key == pygame.K_DOWN:
                player_action = 4

            if event.key == pygame.K_a:
                attacking = 1
                killed()

        if event.type == pygame.KEYUP:
            attacking = 0
            player_action = 0
            attack_type = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            shop_button.clicked()
        if event.type == pygame.MOUSEBUTTONUP:
            shop_button.unclick()

    pygame.display.flip()
    screen.fill((0, 0, 0))
    if player.x >= 480 and player.y <= 80:
        shop_group.draw(screen)
        shop_showing = 1
    else:
        shop_showing = 0
    armour_bar.update()
    health_bar.update()
    attack.update()
    player.update()
    clerk.update()
    number_group.update()
    enemy.update()
    common_group.update()
    background_images.update()
    enemy_health_bar.update()
    player_stuff.update()
    coin_icon.update()
    cursor.update()
    background_images.draw(screen)
    player_stuff.draw(screen)
    enemy_group.draw(screen)
    common_group.draw(screen)
    all_sprites.draw(screen)
    number_group.draw(screen)
    Clock.tick(12)
