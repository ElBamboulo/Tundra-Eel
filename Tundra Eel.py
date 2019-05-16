import pygame
import random
from os import path
from math import atan2, degrees, pi

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 1280
HEIGHT = 720
FPS = 60

# fenetre de jeu
width = 430
height = 200
x = 425
y = 325

# définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
##pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TUNDRA EEL")
clock = pygame.time.Clock()

def playfield(surf, playfield_x, playfield_y, playfield_width, playfield_height):
    outline_rect = pygame.Rect(playfield_x, playfield_y, playfield_width, playfield_height)
    pygame.draw.rect(surf, WHITE, outline_rect, 5)

def draw_barredevie(surf, x, y):
        BAR_LENGTH = 250
        BAR_HEIGHT = 25
        fill = (player_life / 100) *    BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, YELLOW, fill_rect)
        pygame. draw.rect(surf, WHITE, outline_rect, 2)


def draw_barredevie_boss(surf, x, y):
        BAR_LENGTH = 250
        BAR_HEIGHT = 25
        fill = (boss.life / 1000) *    BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, RED, fill_rect)
        pygame. draw.rect(surf, WHITE, outline_rect, 2)


def draw_text(surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)



def attaque_blaster():
        if player.time > 500:
            b = Blaster()
            all_sprites.add(b)
            blasters.add(b)

def attaque_bullet():
    if player.time > 500:
        bullet = Bullet()
        all_sprites.add(bullet)
        bosons.add(bullet)
        bullet_vertical = Bullet_vertical()
        all_sprites.add(bullet_vertical)
        bosons.add(bullet_vertical)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (16, 16))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + width/2
        self.rect.centery = y + height/2
        self.time = pygame.time.get_ticks()


    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -3
        if keystate[pygame.K_d]:
            self.speedx = 3
        if keystate[pygame.K_w]:
            self.speedy = -3
        if keystate[pygame.K_s]:
            self.speedy =  3
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > x + width -3:
            self.rect.right = x + width-3
        if self.rect.left < x+3:
            self.rect.left = x+3
        if self.rect.bottom > y + height-3:
            self.rect.bottom = y + height-3
        if self.rect.top < y+4:
            self.rect.top = y+4


class Boss(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.largeur = 100
        self.hauteur = 200
        self.image = boss_images[0]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = 175
        self.life = 1000
        self.time = pygame.time.get_ticks()
        self.list_pos = 1

    def update(self):
            now = pygame.time.get_ticks()
            if now - self.time >= 75:
                self.image = boss_images[self.list_pos]
                self.list_pos = 2
            if now - self.time >= 150:
                self.image = boss_images[self.list_pos]
                self.list_pos = 3
            if now - self.time >= 225:
                self.image = boss_images[self.list_pos]
                self.list_pos = 0
            if now - self.time >= 300:
                self.image = boss_images[self.list_pos]
                self.list_pos = 1
                self.time = now



class Blaster(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(blaster_img, (160, 160))
        self.rect = self.image.get_rect()
        self.radius= 20
        self.rect.centerx = random.randint(player.rect.centerx - 400, player.rect.centerx + 400)
        self.rect.centery = random.randint(player.rect.centery - 250, player.rect.centery + 250)
        self.angle = degrees(atan2(player.rect.centerx - self.rect.centerx,player.rect.centery  - self.rect.centery))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.time > 600:
            self.image = pygame.transform.scale(blaster_tir_img, (160, 160))
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.shoot()
        if now - self.time > 1200:
            self.kill()


    def shoot(self):
        laser = Laser(self.rect.centerx, self.rect.centery, self.angle)
        all_sprites.add(laser)
        lasers.add(laser)




class Laser(pygame.sprite.Sprite):
    def __init__(self, laser_x, laser_y, angle) :
        pygame.sprite.Sprite.__init__(self)
        self.largeur = 60
        self.longueur = 1500
        self.image = pygame.transform.scale(laser_img, (self.largeur, self.longueur))
        self.image = pygame.transform.rotate(self.image, angle)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, RED, self.rect, 2)
        self.rect.centerx = laser_x
        self.rect.centery = laser_y

    def update(self):
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.largeur = 60
        self.hauteur = 20
        positions = [x, x+width+self.largeur]
        self.image = pygame.transform.scale(laser_img, (self.largeur, self.hauteur))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, RED, self.rect, 2)
        self.rect.centerx = positions[random.randint(0, 1)]
        self.pos_initiale = self.rect.centerx
        self.rect.centery = random.randint(y+10, y + height -10)
        self.speedx = 4
        self.time = pygame.time.get_ticks()

    def update(self):
        if self.pos_initiale == x:
            self.rect.x += self.speedx
        if self.pos_initiale == x+width+self.largeur:
            self.rect.x += -self.speedx


class Bullet_vertical(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.largeur = 20
        self.hauteur = 35
        positions = [y, y+height+self.hauteur]
        self.image = pygame.transform.scale(laser_img, (self.largeur, self.hauteur))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, RED, self.rect, 2)
        self.rect.centerx = random.randint(x + 10, x+width-10)
        self.rect.centery = positions[random.randint(0, 1)]
        self.pos_initiale = self.rect.centery
        self.speedy = 4
        self.time = pygame.time.get_ticks()

    def update(self):
        if self.pos_initiale == y:
            self.rect.y += self.speedy
        if self.pos_initiale == y+height+self.hauteur:
            self.rect.y += -self.speedy


class Fight_button(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.largeur = 150
        self.hauteur = 75
        self.image = pygame.transform.scale(fight_button_img, (self.largeur, self.hauteur))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + self.largeur/1.7
        self.rect.centery = y + height + self.hauteur + 10

class Heal_button(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.largeur = 150
        self.hauteur = 75
        self.image = pygame.transform.scale(heal_button_img, (self.largeur, self.hauteur))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + width - self.largeur/1.7
        self.rect.centery = y + height + self.hauteur +10



# Charge tous les graphiques du jeu

player_img = pygame.image.load(path.join(img_dir, "heart.png")).convert_alpha()
player_img2 =  pygame.transform.scale(player_img, (160, 160))
blaster_img = pygame.image.load(path.join(img_dir, "blaster1.png")).convert_alpha()
blaster_tir_img = pygame.image.load(path.join(img_dir, "blaster2.png")).convert_alpha()
laser_img = pygame.image.load(path.join(img_dir, "laser.png")).convert_alpha()
fight_button_img = pygame.image.load(path.join(img_dir, "fight.png")).convert_alpha()
heal_button_img = pygame.image.load(path.join(img_dir, "heal.png")).convert_alpha()
fight_button_img2 = pygame.image.load(path.join(img_dir, "fight2.png")).convert_alpha()
heal_button_img2 = pygame.image.load(path.join(img_dir, "heal2.png")).convert_alpha()
title_img = pygame.image.load(path.join(img_dir, "tundraeel.png")).convert_alpha()
boss_images = []
boss_list = ['boss1.png', 'boss24.png', 'boss3.png',
               'boss24.png']
for img in boss_list:
    boss_images.append(pygame.image.load(path.join(img_dir, img)).convert_alpha())

player = Player()
boss = Boss()
fight_button = Fight_button()
heal_button = Heal_button()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(boss)
buttons = pygame.sprite.Group()
buttons.add(fight_button)
buttons.add(heal_button)
all_sprites.add(fight_button)
all_sprites.add(heal_button)
boss2 = pygame.sprite.Group()
boss2.add(boss)
bosons = pygame.sprite.Group()
lasers = pygame.sprite.Group()
blasters = pygame.sprite.Group()



#BOUCLE DE JEU

delai = FPS
tour_player = False
menu = True
jeu = False
running = True
fight = True
heal = False
boutton_jeu = True
bouton_quitter = False
i = 0
last_hit = 0
player_life = 100

#Fonctions attaques

choix_attaque = random.randint(0, 2)



while running:
    # garder la boucle en marche à la bonne vitesse
    clock.tick(FPS)
    # Entrée de processus (événements)
    for event in pygame.event.get():
        # vérifier la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False
    if menu:
        key = pygame.key.get_pressed()
        screen.fill(BLACK)
        screen.blit(title_img,(250,80) )
        draw_text(screen, "Press SPACE to start the game", 30, WIDTH / 2, y+height)
        screen.blit(player_img2, (WIDTH/2 - 90, 250))
        if key[pygame.K_SPACE]:
            player.__init__()
            menu = False
            jeu = True
        pygame.display.flip()



    if jeu:
        if choix_attaque == 0:
            # Mettre à jour
            all_sprites.update()

            # Dessiner / rendu
            screen.fill(BLACK)
            playfield(screen, x, y, width, height)
            i = i + 1.2
            if i >= delai:
                attaque_blaster()
                i = 0

            hits = pygame.sprite.spritecollide(player, lasers, False, pygame.sprite.collide_rect)
            for hit in hits:
                print("radis")

            now = pygame.time.get_ticks()
            all_sprites.draw(screen)
            draw_barredevie(screen, x, y + height+15)
            draw_barredevie_boss(screen, width + x-80, 200)
            draw_text(screen, str(player_life), 30, WIDTH / 2 + 64, y + height+13)
            draw_text(screen, str(boss.life), 30, width + x+50, 230)
            if now - player.time >= 10000:
                player.__init__()
                jeu = False
                tour_player = True
                i = 0
                choix_attaque = random.randint(0, 2)
            # après avoir tout dessiné, retourner l'affichage
            pygame.display.flip()


        if choix_attaque == 1 or choix_attaque == 2:
                # Mettre à jour
                all_sprites.update()

                # Dessiner / rendu
                screen.fill(BLACK)
                playfield(screen, x, y, width, height)
                now = pygame.time.get_ticks()
                i = i + 2
                if i >= delai:
                    attaque_bullet()
                    i = 0

                hits = pygame.sprite.spritecollide(player, bosons, False, pygame.sprite.collide_rect)
                for hit in hits:
                    if now - last_hit > 500:
                        player_life = player_life - 10
                        last_hit = pygame.time.get_ticks()

                if player_life <= 0:
                    jeu = False
                    player_life = 100
                    boss.life = 1000
                    menu = True


                all_sprites.draw(screen)
                draw_barredevie(screen, x, y + height+15)
                draw_barredevie_boss(screen, width + x-80, 200)
                draw_text(screen, str(player_life), 30, WIDTH / 2 + 64, y + height+13)
                draw_text(screen, str(boss.life), 30, width + x+50, 230)
                if now - player.time >= 10000:
                    player.__init__()
                    jeu = False
                    tour_player = True
                    i = 0
                    last_hit = 0
                    choix_attaque = random.randint(0, 2)
                # après avoir tout dessiné, retourner l'affichage
                pygame.display.flip()

    if tour_player:
        key = pygame.key.get_pressed()
        screen.fill(BLACK)
        playfield(screen, x-50, y, width+100, height)
        boss2.update()
        boss2.draw(screen)
        buttons.draw(screen)
        draw_barredevie(screen, x, y + height+15)
        draw_barredevie_boss(screen, width + x-80, 200)
        draw_text(screen, str(player_life), 30, WIDTH / 2 + 64, y + height+13)
        draw_text(screen, str(boss.life), 30, width + x+50, 230)
        if fight:
            fight_button.image = pygame.transform.scale(fight_button_img2, (fight_button.largeur, fight_button.hauteur))
            heal_button.image = pygame.transform.scale(heal_button_img, (heal_button.largeur, heal_button.hauteur))
            if key[pygame.K_RETURN]:
                boss.life = boss.life- random.randint(80, 120)
                print(boss.life)
                player.__init__()
                tour_player = False
                jeu = True
                fight_button.image = pygame.transform.scale(fight_button_img, (fight_button.largeur, fight_button.hauteur))
                if boss.life <= 0:
                    tour_player = False
                    jeu = False
                    player_life = 100
                    boss.life = 1000
                    menu = True
            if key[pygame.K_RIGHT]:
                fight = False
                fight_button.image = pygame.transform.scale(fight_button_img, (fight_button.largeur, fight_button.hauteur))
                heal = True


        if heal:
            heal_button.image = pygame.transform.scale(heal_button_img2, (heal_button.largeur, heal_button.hauteur))
            fight_button.image = pygame.transform.scale(fight_button_img, (fight_button.largeur, fight_button.hauteur))
            if key[pygame.K_RETURN]:
                player_life = player_life + random.randint(30, 50)
                if player_life >= 100:
                    player_life = 100
                print(player_life)
                print(boss.life)
                player.__init__()
                fight = True
                tour_player = False
                jeu = True
                heal = False
                heal_button.image = pygame.transform.scale(heal_button_img, (heal_button.largeur, heal_button.hauteur))
            if key[pygame.K_LEFT]:
                heal = False
                heal_button.image = pygame.transform.scale(heal_button_img, (heal_button.largeur, heal_button.hauteur))
                fight = True


        pygame.display.flip()




pygame.quit()
exit()