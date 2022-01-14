import pygame
from pygame import *
import math
import random
import os

os.environ["SDL_VIDEO_WINDOW_POS"] = "100,50"

# Colors
"""
BLITZ
Created by: Sahaij Gadhri, Ibrahim Khatib, Shan Ehsan
~ 3500 lines of code
~ using classes, functions, fileIo, and sprite collision
"""



# Initializes pygame & colours
pygame.init()
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255 ,255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
BEIGE = (228, 199, 166)
GREY = (128,128,128)
BROWN = (71,48,18)

PI = 3.141592653

# Screen size is 1366x768
displayWidth = 1366
displayHeight = 768
size = (displayWidth,displayHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Player movement")


display.set_caption("Blitz")#program name when ran
display.set_icon(image.load("Images/hooters.jpg"))#program icon when ran


# ____ Globals _____

# Fonts for blitting text 
''' Fonts '''
smallFont = pygame.font.SysFont('Arial',15,True,False)
ammoFont = pygame.font.SysFont('Calibri',25,True,False)
mediumFont = pygame.font.SysFont('Calibri',30,True,False)
point20Font = pygame.font.SysFont('Calibri',20,True,False)
largeFont = pygame.font.SysFont('Arial',40,True,False)
thiccFont = pygame.font.SysFont('Calibri',100,True,False)
# Player Variables

''' Images '''
# Player images
spritePic1 = pygame.image.load("Images/sprite1.0.png")
spritePic2 = pygame.image.load("Images/sprite3.0.png")
spritePic3 = pygame.image.load("Images/sprite4.0.png")
spritePic4 = pygame.image.load("Images/sprite5.0.png")
spritePic5 = pygame.image.load("Images/sprite6.0.png")
spritePic6 = pygame.image.load("Images/sprite7.0.png")
crossHair = pygame.image.load("Images/crosshair.png")

# Bacground images
grassBack = pygame.image.load("Images/grass back.png")

# SFX files
pygame.mixer.init()
pygame.mixer.music.load("Sounds/startScreen.wav")
pygame.mixer.music.play(15)

# Wall images
wallPic1 = pygame.image.load("Images/wall1.png")
wallPic2 = pygame.image.load("Images/wall2.png")
wallPic3 = pygame.image.load("Images/wall3.png")
wallPicList = [wallPic1,wallPic2,wallPic3]
cratePic = pygame.image.load("Images/crate.png")
cratePic2 = pygame.image.load("Images/crate2.png")

# Gun pictures
shotgunPic = pygame.image.load("Images/shotgun.png")
railgunPic = pygame.image.load("Images/railgun.png")
pistolPic = pygame.image.load("Images/pistol.png")
suppressedPistolPic = pygame.image.load("Images/suppressedPistol.png")
umpPic = pygame.image.load("Images/UMP-45.png")
carbinePic = pygame.image.load("Images/carbine.png")
awpPic = pygame.image.load("Images/sniper.png")
ak47Pic = pygame.image.load("Images/ak47.png")
revolverPic = pygame.image.load("Images/revolver.png")
raygunPic = pygame.image.load("Images/raygun2.0.png")
mp40Pic = pygame.image.load("Images/mp40.png")
m1927Pic = pygame.image.load("Images/m1927.png")
s12Pic = pygame.image.load("Images/S12v1.png")
cz75Pic = pygame.image.load("Images/cz75.png")
rampart17Pic = pygame.image.load("Images/rampart17.png")
rpgPic = pygame.image.load("Images/RPG.png")
grenadeLauncherPic = pygame.image.load("Images/grenadeLauncher.png")

#Enemy pictures

ghostPic = pygame.image.load("Images/phantom.png")
shooterRightPic = pygame.image.load("Images/newShooterRight.png")
shooterLeftPic = pygame.image.load("Images/newShooterLeft.png")
shooterUpPic = pygame.image.load("Images/newShooterUp.png")
shooterDownPic = pygame.image.load("Images/newShooterDown.png")
sniperEnemyPic = pygame.image.load("Images/sniper1.0.png")

#Minimap pictures
minimap = pygame.image.load("Images/minimapv2.0.png")
unknown = pygame.image.load("Images/unknown1.0.png")

# Boss pictres
beefyPic = pygame.image.load("Images/Beefy.png")
pumpPic = pygame.image.load("Images/lil Pump.png")
bottomPic = pygame.image.load("Images/bottomText.png")

# Start picture
startPage = pygame.image.load("Images/startPage.png")
instructionsPage = pygame.image.load("Images/Instructions.png")
optionsScreen = pygame.image.load("Images/optionsScreen.png")
check = pygame.image.load("Images/check.png")
deathAlert = pygame.image.load("Images/deathScreen.png")
savePic = pygame.image.load("Images/save.png")
selectScreen = pygame.image.load("Images/selectScreen.png")
pauseScreen = pygame.image.load("Images/pauseScreen1.png")
victoryScreen = pygame.image.load("Images/victoryScreen.png")

''' Variables '''

# Gun variables
gunName = ""
reload = False
reloadDelay = 0
hoverTimer = 25.2
accept = False
startShot = False
isArmed = False
reloading = False
hover = False
start = True


# Player Variables
base = True
orange = False
chrome = False
firefox1 = False
firefox2 = False
internetExplorer = False
EA = False

# Level variables
stageList = [ 4,
              3,
              2,
              1,5,6,7,
              8,
              9,
              10]

oneTimeDraw = True # This makes sure that the level is only drawn once
lastStage = 1 # This records the last stage the player was on to decide where the player spawns
currentObj = ""


# Start screen
display = "start" # One of many different displays, this one is for the start screen



''' Sprite List '''
allSpriteList = pygame.sprite.Group() # all of the sprites in one list
walls = pygame.sprite.Group() # all of the walls, used for collision and drawing

# Player lists
playerList = pygame.sprite.Group() # the player will be in a list for collision
bullets = pygame.sprite.Group()
shrapnel = pygame.sprite.Group()
gunList = pygame.sprite.Group()

#Enemy lists
enemyList = pygame.sprite.Group()
ghostList = pygame.sprite.Group()
shooterList = pygame.sprite.Group()
sniperEnemyList = pygame.sprite.Group()
shooterBullets = pygame.sprite.Group()
sniperBullets = pygame.sprite.Group()

# Boss lists
beefyList = pygame.sprite.Group()
beefyBalls = pygame.sprite.Group()
pumpList = pygame.sprite.Group()
pumpMines = pygame.sprite.Group()
bottomList = pygame.sprite.Group()
bossKilledList = [""] # List of the bosses that you have killed in this playthrough


#Objective lists
zoneList = pygame.sprite.Group()

#Saving Variables - File IO
loadFile = open("Save.txt","r") # reads from the save file
loadInfo = []
loadInfo = loadFile.read().split()



''' Classes '''
#Player class - all of the player info is stored and called here, also used to update the player every frame
class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height,posX,posY): # passes in the width,height,and postion of where you want the player to be
        super().__init__() # initializes the sprite class
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect() # Gets the rect of the player
        # Booleans
        self.wallHit = False # used for wall collision
        # Movement
        self.vx = 0 # player "vx" is used for horizontal movement
        self.vy = 0 # player "vy" is used for vertical movement
        self.rect.y = posY
        self.rect.x = posX
        # Health
        self.health = 300
        self.fullHealth = 300
        # Arm Rotation - This allows for the right arm to move using the outside of the player rect
        self.center = (self.rect.x,self.rect.y)
        self.center2 = (self.rect.x,self.rect.y)
        self.radius = 25
        self.armCenter = (self.center[0]+self.radius,self.center[1])
        self.switch = False # this is for the player to switch between their arms and their gun
        self.xp = 0 # this is the experience the player has gained
        self.level = int(loadInfo[1])
        self.stopTimer = 0 # this is for the last level, this makes sure the player does not move for 500 frames
        self.godMode = False# This makes the player invincible
        self.dead = False # This decides when the player is dead
        self.screenTimer = 0

    def changeVelocity(self,x,y):
        #uses the input from the keybaord to increased displacement
        self.vx += x
        self.vy += y

    def move(self,walls):
        """ This makes sure the player can't go through walls by making it so that
        the player's rect changes so that is is equal to the opposite side of the wall it
        hits.
        """
        self.rect.x += self.vx
        wallHitList = pygame.sprite.spritecollide(self,walls,False)
        for wall in wallHitList:
            if self.vx > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right
        
        self.rect.y += self.vy
        wallHitList = pygame.sprite.spritecollide(self,walls,False)
        for wall in wallHitList:
            if self.vy > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom
                
    def rightArm(self,mx,my):
        # Uses the rect of the player and trig to identify where to put the right arm
        # of the player. It finds the distance from the mx,my position to the middle of the rect, and
        # uses that value to place a circle at the edges in a way that allows for the circle to move in
        # in a circle around the player.
        self.center2 = (self.rect.x + 20 ,self.rect.y + 20)
        self.vector = (mx - self.center2[0],my + self.center2[1])
        self.dist = math.sqrt((self.vector[0] ** 2 + self.vector[1] ** 2))
        if self.dist > 0:
            self.scalar = (self.radius / self.dist)
            self.armCenter = (int(round(self.center2[0] + self.vector[0] * self.scalar)),int(round(self.center2[1] + self.vector[1] * self.scalar)))
        pygame.draw.circle(screen,BLACK,self.armCenter,10)

    def takeDmg(self):
        """
        This uses the sprite groups to identify which sprite the player collided with and makes
        a difference in player health accordingly.
        """
        if self.godMode == False:
            for bullet in shooterBullets:
                playerHitList = pygame.sprite.spritecollide(bullet,playerList,False)
                for player in playerHitList:
                    player.health -= bullet.dmg
                    sound = pygame.mixer.Sound("Sounds/damage.wav")
                    channel = sound.play()
                    shooterBullets.remove(bullet)
            for bullet in sniperBullets:
                playerHitList = pygame.sprite.spritecollide(bullet,playerList,False)
                for player in playerHitList:
                    player.health -= bullet.dmg
                    sound = pygame.mixer.Sound("Sounds/damage.wav")
                    channel = sound.play()
                    sniperBullets.remove(bullet)
            for ghost in ghostList:
                playerHitList = pygame.sprite.spritecollide(ghost,playerList,False)
                for player in playerHitList:
                    player.health -= ghost.dmg
                    sound = pygame.mixer.Sound("Sounds/damage.wav")
                    channel = sound.play()
                    ghostList.remove(ghost)
                    ghost.ghostBar = False
            for thing in shrapnel:
                playerHitList = pygame.sprite.spritecollide(thing,playerList,False)
                for player in playerHitList:
                    player.health -= thing.dmg
                    sound = pygame.mixer.Sound("Sounds/damage.wav")
                    channel = sound.play()
                    shrapnel.remove(thing)
            for ball in beefyBalls:
                playerHitList = pygame.sprite.spritecollide(ball,playerList,False)
                for player in playerHitList:
                    player.health -= ball.dmg
                    sound = pygame.mixer.Sound("Sounds/damage.wav")
                    channel = sound.play()
                    beefyBalls.remove(ball)
            for b in bottomList:
                playerHitList = pygame.sprite.spritecollide(b,playerList,False)
                for player in playerHitList:
                    player.health -= b.dmg
                    sound = pygame.mixer.Sound("Sounds/damage.wav")
                    channel = sound.play()                
                
                
                
    def death(self):
        # if the player's health is less than 0, the player is declared dead. This will make a death noise
        # and turn the screen white
        if self.health <= 0:
            screen.fill(BLACK)
            pygame.mixer.music.stop()
            self.dead = True
            sound = pygame.mixer.Sound("Sounds/death.wav")
            channel = sound.play()
#_______________________________________________________________________________________________________________________________________________________
class LeftArm(pygame.sprite.Sprite): # The left arm has it's own group so that it can have proper collision 
    def __init__(self,player):
        super().__init__()
        # Similar to the right arm, but more complex.
        self.center = (player.rect.x,player.rect.y)
        self.center2 = (player.rect.x,player.rect.y)
        self.radius = 25 # defines the radius of the player circle
        self.armCenter = [self.center[0]+self.radius,self.center[1]]
        self.image = pygame.Surface([15,15])
        self.rect = pygame.Rect(self.armCenter[0] + 15, self.armCenter[1] + 15,10,10)
        
        
        
    def update(self,mb):
        self.center = (player.rect.x + 20,player.rect.y + 20) # defines the middle of the rect for calculations
        self.vector = (mx - self.center[0],my - self.center[1]) # Defines the "vector" tuple that finds the difference between the center and mx,my
        self.dist = math.sqrt((self.vector[0] ** 2 + self.vector[1] ** 2))# Defines the distance from the middle to the edge
        if self.dist > 0:
            self.scalar = self.radius / self.dist # Uses the radius to find the edge of the circle
            self.armCenter = [int(round(self.center[0] + self.vector[0] * self.scalar)),int(round(self.center[1] + self.vector[1] * self.scalar))] #uses self.scalar as a coefficient for arm rotation
        if not mb[0]:
            pygame.draw.circle(screen, BLACK, self.armCenter,10) # draws the circle
            
        if mb[0]:
            # Places the fist away from the player when the player is punching
            if mx <= player.rect.x and my <= player.rect.y:
                pygame.draw.circle(screen, BLACK, (self.armCenter[0] - 10,self.armCenter[1] - 10),10)
                self.armCenter[0] = self.armCenter[0] - 10
                self.armCenter[1] = self.armCenter[1] - 10
            if mx >= player.rect.x and my >= player.rect.y:
                pygame.draw.circle(screen, BLACK, (self.armCenter[0] + 10,self.armCenter[1] + 10),10)
                self.armCenter[0] = self.armCenter[0] + 10
                self.armCenter[1] = self.armCenter[1] + 10
            if my <= player.rect.y and mx >= player.rect.x:
                pygame.draw.circle(screen, BLACK, (self.armCenter[0] + 10,self.armCenter[1] - 10),10)
                self.armCenter[0] = self.armCenter[0] + 10
                self.armCenter[1] = self.armCenter[1] - 10
            if my >= player.rect.y and mx <= player.rect.x:
                pygame.draw.circle(screen, BLACK, (self.armCenter[0] - 10,self.armCenter[1] + 10),10)
                self.armCenter[0] = self.armCenter[0] - 10
                self.armCenter[1] = self.armCenter[1] + 10
                
        self.rect = pygame.Rect(self.armCenter[0] - 10, self.armCenter[1] - 10,20,20)
#__________________________________________________________________________________________________________________________________________________________
class Enemies(pygame.sprite.Sprite): # The 3 enemies stem from this class. Used to keep track of enemy information
    def __init__(self,posX,posY,name,level,image,direction): # pass in the position of the enemy,the name, the difficulty, the image, and the direction they face
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

        # creates the info of the enemy depending on the name
        if name == "rusher":
            # depending on the level of the enemy, the health and speed change
            if level == 1:
                self.vx = 1
                self.vy = 1
                self.health = 120
            if level == 2:
                self.vx = 2
                self.vy = 2
                self.health = 120
            if level == 3:
                self.vx = 3
                self.vy = 3
                self.health = 150
            self.dmg = 20
            # ghost bar is a boolean that returns true if the ghost is shot, and then shows the ghosts healthbar
            self.ghostBar = False
        if name == "shooter":
            if level == 1:
            # Sets up the health and dmg of the shooter,as well as how often a bullet is shot
                self.health = 200
                self.bulletTime = 0
                self.dmg = 50
            self.shooterBar = False
        if name == "sniperEnemy":
            # Sets up the health and dmg of the shooter,as well as how often a bullet is shot
            self.rect.x = posX
            self.rect.y = posY
            self.bulletTime= 0
            if level == 1:
                self.health = 150
                self.dmg = 100
            self.sniperBar = False
        self.direction = direction
        self.alert = False
        self.name = name


    """
    This set of child functions updates the various enemies
    """
    def updateGhost(self,playerX,playerY):
        # programmed to follow the player, even through walls
        if self.rect.x + 100 <= playerX  or self.rect.x - 100 <= playerX and not self.alert:
            if self.rect.y - 100 <= playerY or self.rect.y + 100 <= playerY:
                self.alert = True
        if self.alert:
            if self.rect.x >= playerX:
                self.rect.x -= self.vx
            if self.rect.x <= playerX:
                self.rect.x += self.vx
            if self.rect.y >= playerY:
                self.rect.y -= self.vy
            if self.rect.y <= playerY:
                self.rect.y += self.vy
        screen.blit(self.image,[self.rect.x,self.rect.y])
        

    def updateShooter(self):
        # this enemy shoots in only one direction regardless of any external variables
        if self.direction == "right":
            self.image == shooterRightPic
        if self.direction == "left":
            self.image==shooterLeftPic
        if self.direction == "up":
            self.image==shooterUpPic
        if self.direction == "down":
            self.image==shooterDownPic
        # Created the bullet for the shooter to shoot every 30 frames
        self.bulletTime += 1
        if self.bulletTime >= 30:
            self.bulletTime = 0
            shooterBullet = Bullet(BLACK,6,6,"shooter",self.rect.x + 50,self.rect.y + 50)
            shooterBullets.add(shooterBullet)
        screen.blit(self.image,[self.rect.x,self.rect.y + 20])
    def updateSniper(self,player,image):
        # Rotates in accordance the player positions using trig to find the distance and positin
        self.image = image
        self.ang = math.atan2(-(player.rect.x-self.rect.x),-(player.rect.y-self.rect.y)) # finds the angle at which the player is at, and uses inverted tan to find the distance given 2 values
        self.rPic = pygame.transform.rotate(self.image,math.degrees(self.ang)) # new picture that is rotated in accordance to the angle
        # Places the rect in the middle of the picture for best collision
        self.picX = self.rect.x - self.rPic.get_width()//2 
        self.picY = self.rect.y - self.rPic.get_height()//2
        
        screen.blit(self.rPic,[self.picX + 25,self.picY + 30])

        self.bulletTime += 1
        # Creates a bullet for the sniper to shoot every 100 frames
        if self.bulletTime >= 100:
            self.bulletTime = 0
            sniperBullet = Bullet(BLACK,8,8,"sniperEnemy",self.rect.x,self.rect.y + 30)
            sniperBullets.add(sniperBullet)
            sniperBullet.trajectory(player.rect.x + 15,player.rect.y + 15)
            
#__________________________________________________________________________________________________________________________________________________________
class Boss(pygame.sprite.Sprite): # Boss class for boss info (like health and dmg output)
    def __init__(self,name,posX,posY): # pass in the name and position of the boss
        super().__init__()
        if name == "Beefy": # Beefy is a boss that requires you to shoot his bullets to skill him
            self.image = beefyPic
            self.rect = self.image.get_rect()
            self.rect.x = posX
            self.rect.y = posY
            self.health = 800
            self.bulletTime = 0
        if name == "pump":
            self.image = pumpPic
            self.rect = self.image.get_rect()
            self.rect.x = posX
            self.rect.y = posY
            self.health = 3000
        if name == "bottom":
            self.image = bottomPic
            self.rect = self.image.get_rect()
            self.rect.x = posX
            self.rect.y = posY
            self.health = 13000
            self.vx = 20 # this is how many pixels bottom text can cross when rushin
            self.vy = 4 # This is how fast he adjusts his y position when not charging
            self.chargeTimer = 0 # init the charge timer ~ used to charge every 240 frames
            self.chargeDirection = "left" # the direction that he is charging in
            self.dmg = 100 # how much dmg he does every frame that you are in contact 
            
    def updateBeefy(self,kills):
        # Updates beefy by making him shoot bullets in random directions with random speeds
        # You have to shoot those bullets to kill him
        screen.blit(self.image,[self.rect.x,self.rect.y])
        self.bulletTime += 1
        # Creates a bullet for beefy every 60 frames
        if self.bulletTime >= 60:
            self.bulletTime = 0
            ball = Bullet(GREEN,26,26,"Beefy",(random.randrange(self.rect.x - 200,self.rect.x + 200)),200)
            beefyBalls.add(ball)

        # erases the ball after 1000 frames if you do not hit it. This is to make sure the player is not overloaded
        for ball in beefyBalls:
            ball.eraseTimer += 1
            if ball.eraseTimer >= 1000:
                beefyBalls.remove(ball)
            if ball.health <= 0:
                player.xp += 1
                beefyBalls.remove(ball)
                self.health -= 20
        # draws the beefy balls
        for ball in beefyBalls:
            pygame.draw.circle(screen,BLACK,[ball.rect.x + 12,ball.rect.y + 12],15)
        # removes beefy if his health is 0    
        if self.health <= 0:
            for beefy in beefyList:
                player.xp += 300
                beefyList.remove(beefy)
                kills.append("Beefy")

    def updatePump(self,kills):
        # Every time lil Pump is shot, he randomly explodes a portion of the map
        # This blits the lil pump picture and removes him if the health is less than 0
        screen.blit(self.image,[self.rect.x,self.rect.y])
        if self.health <= 0:
            for pump in pumpList:
                player.xp += 300
                pumpList.remove(pump)
                kills.append("pump")

    def updateBottom(self):
        screen.blit(self.image,[self.rect.x,self.rect.y])
        if player.stopTimer >= 500:
            self.chargeTimer += 1 # if the chargeTimer is 240, bottom text will charge you
            if self.chargeTimer >= 200:
                if self.chargeTimer >= 240:
                    if self.chargeDirection == "left": # when the charge direction is left, bottom will charge right
                        if self.rect.x >= 60:
                            self.rect.x -= self.vx
                            if self.rect.x == 60: # when bottom hits a x postion of 60, his direction is changed to right
                                self.chargeTimer = 0
                                self.chargeDirection = "right"
                    if self.chargeDirection == "right":# when the charge direction is right, bottom will charge left
                        if self.rect.x <= 1120:
                            self.rect.x += self.vx
                            if self.rect.x == 1120: #when bottom hits a x postion of 1120, his direction is changed to left
                                self.chargeTimer = 0
                                self.chargeDirection = "left"
                
            else:
                # if the charge timer is less than 240, bottom's y postion will update according to the player's
                if self.rect.y < player.rect.y - 10:
                    self.rect.y += self.vy
                if self.rect.y > player.rect.y - 10 and self.rect.y >= 150:
                    self.rect.y -= self.vy
    
        if self.health <= 0:
            bottomList.remove(bottom)
            Hud.gameOver = True
        
        
#__________________________________________________________________________________________________________________________________________________________
class Guns(pygame.sprite.Sprite): # all of the guns in the game root from this class. This holds info like ammo and fire rate. It also allows for collision so the player can pick it up
    def __init__(self,color,width,height,posX,posY,name,dmg): # pass in the color, width + height of the gun, the position is will be placed before the player picks it up, name and dmg
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.x = posX
        self.y = posY
        self.width = width
        self.height = height
        self.pic = None
        self.name = name
        self.dmg = dmg
        # depending on the name of the gun, it will create information about it
        # Each gun has a different firing rate, picture and ammo count
        if name == "ak47":
            self.ammo = 30
            self.fullAmmo = 30
            self.gunPic = ak47Pic
            self.bulletTime = 30
        if name == "mp40":
            self.ammo = 32
            self.fullAmmo = 32
            self.gunPic = mp40Pic
            self.bulletTime = 24
        if name == "m1927":
            self.ammo = 50
            self.fullAmmo = 50
            self.gunPic = m1927Pic
            self.bulletTime = 5
        if name == "raygun":
            self.ammo = 20
            self.fullAmmo = 20
            self.gunPic = raygunPic
            self.bulletTime = 0
        if name == "shotgun":
            self.ammo = 5
            self.fullAmmo = 5
            self.gunPic = shotgunPic
            self.bulletTime = 0
        if name == "s12":
            self.ammo = 8
            self.fullAmmo = 8
            self.gunPic = s12Pic
            self.bulletTime = 0
        if name == "railgun":
            self.ammo = 100
            self.fullAmmo = 100
            self.gunPic = railgunPic
        if name == "pistol":
            self.ammo = 8
            self.fullAmmo = 8
            self.gunPic = pistolPic
            self.suppressed = False
        if name == "awp":
            self.ammo = 4
            self.fullAmmo = 4
            self.gunPic = awpPic
            self.bulletTime = 0
        if name == "ump":
            self.ammo = 24
            self.fullAmmo = 24
            self.gunPic = umpPic
            self.bulletTime = 10
        if name == "carbine":
            self.ammo = 18
            self.fullAmmo = 18
            self.gunPic = carbinePic
            self.bulletTime = 0
        if name == "revolver":
            self.ammo = 6
            self.fullAmmo = 6
            self.gunPic = revolverPic
            self.bulletTime = 0
        if name == "cz75":
            self.ammo = 12
            self.fullAmmo = 12
            self.bulletTime = 0
            self.gunPic = cz75Pic
        if name == "rampart-17":
            self.ammo = 16
            self.fullAmmo = 16
            self.bulletTime = 0
            self.gunPic = rampart17Pic
        if name == "rpg":
            self.ammo = 1
            self.fullAmmo = 1
            self.bulletTime = 0
            self.gunPic = rpgPic
        if name == "grenade launcher":
            self.ammo = 5
            self.fullAmmo = 5
            self.bulletTime = 0
            self.gunPic = grenadeLauncherPic

        # This class also creates bullets for the enemies
        if name == "shooter":
            # depending on the direction of the shooter, the bullet will update with set value of either up,down,left or right.
            if shooter.direction == "left":
                self.vx = -20
                self.vy = 0
            if shooter.direction == "right":
                self.vx = 20
                self.vy = 0
            if shooter.direction == "up":
                self.vx = 0
                self.vy = -20
            if shooter.direction == "down":
                self.vx = 0
                self.vy = 20
            self.dmg = 5
            
    def drawGun(self):
        self.pic = self.gunPic
        screen.blit(self.pic,[self.x,self.y])

    def update(self,mx,my,gun,mb,name):
        if name == "pistol":
            if pistol.suppressed:
                self.pic = suppressedPistolPic
                self.image = suppressedPistolPic
            else:
                self.pic = gun
                self.image = gun
        else:
            self.pic = gun
            self.image = gun
        # rotates the gun similar to the arm
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 23
        self.rect.y = player.rect.y + 20
        self.ang = math.atan2(-(mx-self.rect.x),-(my-self.rect.y)) # finds the angle by uing inverse tan to find theta
        self.rPic = pygame.transform.rotate(self.pic,math.degrees(self.ang)) # rotates the picture according to the angle
        self.picX = self.rect.x - self.rPic.get_width()//2 
        self.picY = self.rect.y - self.rPic.get_height()//2
        screen.blit(self.rPic,[self.picX,self.picY])
        if self.name == "rampart-17" and my >= 75:
            pygame.draw.line(screen,RED,[self.rect.x,self.rect.y],[mx,my],1) # draws the laser sight for the rampart



class Bullet(pygame.sprite.Sprite): # class for the bullets. Allows for collision and info to be stored
    def __init__(self,color,width,height,name,posX,posY): # pass in the color of the bullet, width + height, name of the gun its firing from, and position
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.rangeLimit = False # sets to true if the bullet has existed on the screen for too long
        self.rangeTimer = 0 # Timer that decides when the bullet should be destroyed; limiting range.
        self.name = name
        self.explode = False # used to explode the rpg and grenade launcher
        # Same variables for every gun
        if name == "ak47":
            self.speed = 15.0 #decides how fast the bullet travels
            self.dmg = 60 # the damage output of the gun
        if name == "mp40":
            self.speed = 16.0
            self.dmg = 50
        if name == "m1927":
            self.speed = 17.0
            self.dmg = 33
        if name == "raygun":
            self.speed = 18.0
            self.dmg = 300
        if name == "railgun":
            self.speed = 15.0
            self.dmg = 20
        if name == "shotgun":
            self.speed = 9.0
            self.dmg = 150
        if name == "s12":
            self.speed = 11.0
            self.dmg = 100
        if name == "pistol":
            self.speed = 20.0
            self.dmg = 25
            if pistol.suppressed:
                self.dmg = 15
                self.speed = 20.0
        if name == "ump":
            self.speed = 18.0
            self.dmg = 10
        if name == "carbine":
            self.speed = 18.0
            self.dmg = 50
        if name == "awp":
            self.speed = 16.0
            self.dmg = 300
        if name == "revolver":
            self.speed = 15.0
            self.dmg = 75
        if name == "cz75":
            self.speed = 17.0
            self.dmg = 20
        if name == "rampart-17":
            self.speed = 20.0
            self.dmg = 70
        if name == "rpg":
            self.speed = 10.0
            self.dmg = 2000
        if name == "grenade launcher":
            self.speed = 17.0
            self.dmg = 300
            
        # Enemies
        if name == "shooter":
            self.dmg = 40
            if shooter.direction == "left":
                self.vx = -20
                self.vy = 0
            if shooter.direction == "right":
                self.vx = 20
                self.vy = 0
            if shooter.direction == "up":
                self.vx = 0
                self.vy = -20
            if shooter.direction == "down":
                self.vx = 0
                self.vy = 20
            self.dmg = 50
        if name == "sniperEnemy":
            self.speed = 16.0
            self.dmg = 100

        # Bosses
        if name == "Beefy":
            self.vx = random.randrange(-6,6)    
            self.vy = random.randint(1,6)
            self.eraseTimer = 0
            self.health = 20
            self.dmg = 50
        if name == "mine": # used for lil pump. When shot he creates a random mine that explodes instantly
            self.vx = 0
            self.vy = 0
            self.dmg = 100
            
            
    def trajectory(self,mx,my):
        # Finds the angle that the bullet will shoot at
        self.dx = mx - self.rect.x # finds the difference from mx and the rect of the gun
        self.dy = my - self.rect.y #finds the difference from my and the rect of the gun
        self.dist = math.sqrt(self.dx**2 + self.dy**2) # uses the above values to find the hypotenuse
        frameSpeed = self.dist/self.speed # the speed of the bullet is the distance over the time
        self.vx = self.dx/frameSpeed # makes the velocity of the bullet in x pos = to the distance over the speed
        self.vy = self.dy/frameSpeed # makes the velocity of the bullet in y pos = to the distance over the speed
        
    def update(self):
        if self.explode:
            # changes the vx and vy to random values if an explosion is active
            self.vx = random.randrange(-10,10)
            self.vy = random.randrange(-10,10)
        # increases the x and y by the velocity
        self.rect.x += self.vx
        self.rect.y += self.vy       
        
        

    
#____________________________________________________________________________________________________________________________________________________________
class Wall(pygame.sprite.Sprite): # wall class creates wall and barriers as well as crates for players to break
    def __init__(self,color,width,height,posX,posY,health,wallType): # pass in the coor, width + height, position , health and type
        super().__init__()
        self.name = wallType
        # Different wall types that the player can interact with
        if wallType == "wall":
            self.image = wallPicList[random.randrange(0,2)]
            self.image = pygame.transform.scale(self.image,(width,height))
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = posX
            self.rect.y = posY
            self.health = health
        if wallType == "barrier":
            self.image = pygame.Surface([width,height])
            self.rect = self.image.get_rect()
            self.rect.x = posX
            self.rect.y = posY
            pygame.draw.rect(screen,color,self.rect)
            self.health = health
        if wallType == "crate":
            self.image = cratePic
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = posX
            self.rect.y = posY
            pygame.draw.rect(screen,color,self.rect)
            self.health = health
        if wallType == "crate2":
            self.image = cratePic2
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = posX
            self.rect.y = posY
            pygame.draw.rect(screen,color,self.rect)
            self.health = health

#___________________________________________________________________________________________________________________________________________________________

class Zone(pygame.sprite.Sprite): # a type of objective the player captures for xp
    def __init__(self,color,width,height,posX,posY): # pass in the width + height, and positions
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.color = color
        self.capTimer = 0
        self.width = width
        
        
    def update(self,zones,player): # updates when the player touches the zone, adds to an integer value that gives 500 xp when 1500 is reached
        zoneTouchList = pygame.sprite.spritecollide(player,zones,False)
        for zone in zoneTouchList:
            self.capTimer += 1
            if self.capTimer == 1500:
                zones.remove(zone)
                player.xp += 500
                sound = pygame.mixer.Sound("Sounds/zoneDone.wav")
                channel = sound.play()
        
        
#___________________________________________________________________________________________________________________________________________________________
class HUD(pygame.sprite.Sprite): # updates the top of the screen with info about the player, gun and objective
    def __init__(self,color):
        super().__init__()
        self.image = pygame.Surface([1400,75])
        self.rect = self.image.get_rect()
        self.color = color
        self.fpsDisplay = False
        self.gameOver = False

    def update(self,gunName,health,miniMap,currentStage,fpsDisplay,enemyList,obj):
        """
        Shows -
        health
        ammo
        objective
        map
        etc...
        
        """
        pygame.draw.rect(screen,self.color,self.rect)
        gunText = point20Font.render("Current Weapon:",True,BLACK)
        currentGunText = point20Font.render(gunName.upper(),True,BLACK)
        screen.blit(gunText,[1000,15])
        screen.blit(currentGunText,[1030,35])

        screen.blit(savePic,[1200,30])
        objText = mediumFont.render("Current Objective:",True,BLACK)
        screen.blit(objText,[55,5])

        if currentStage == 69:
            currentObjText = point20Font.render("How did you get in here?",True,RED)
            screen.blit(currentObjText,[80,35])
        
        if obj == "zone":
            currentObjText = point20Font.render("Capture the zone",True,RED)
            screen.blit(currentObjText,[80,35])
            
        if currentStage == 4:
            for beefy in beefyList:
                pygame.draw.rect(screen,RED,(554,275,beefy.health//4,20))
                pygame.draw.rect(screen,BLACK,(554,275,beefy.health//4,20),1)
                currentObjText = point20Font.render("Kill Beefy",True,RED)
                screen.blit(currentObjText,[80,35])
                
        if currentStage == 6:
            currentObjText = point20Font.render("Reach level 15 to fight final boss",True,RED)
            screen.blit(currentObjText,[70,35])
            
        if currentStage == 7:
            for bottom in bottomList:
                if bottom.health >= 0:
                    currentObjText = point20Font.render("Kill Bottom text",True,RED)
                    pygame.draw.rect(screen,RED,(bottom.rect.x - 30,bottom.rect.y - 25,bottom.health//50,20))
                    pygame.draw.rect(screen,BLACK,(bottom.rect.x - 30,bottom.rect.y - 25,bottom.health//50,20),1)
                    screen.blit(currentObjText,[80,35])

            
        if currentStage == 10:
            for pump in pumpList:
                pygame.draw.rect(screen,RED,(475,575,pump.health//8,20))
                pygame.draw.rect(screen,BLACK,(475,575,pump.health//8,20),1)
                currentObjText = point20Font.render("Kill lil Pump",True,RED)
                screen.blit(currentObjText,[80,35])
        
            
                
            

        if gunName=="":
            currentGunText = point20Font.render("FISTS",True,BLACK)
        if self.fpsDisplay:
            fpsStr = str(fpsDisplay)
            fpsStr = fpsStr[11] + fpsStr[12]
            fpsText = point20Font.render("FPS:" + fpsStr,True,BLACK)
            screen.blit(fpsText,[45,120])

        screen.blit(gunText,[1000,15])
        screen.blit(currentGunText,[1030,35])
        screen.blit(minimap,[5,0])

        playerInfoText = mediumFont.render("Player: ",True,BLACK)
        screen.blit(playerInfoText,[380,5])

        
        stageText = point20Font.render("Current Zone: " + str(currentStage), True, BLACK)
        screen.blit(stageText,[800,15])
        
        ammoAlertText = mediumFont.render("Ammo:",True,BLACK)
        screen.blit(ammoAlertText,[1250,5])
        
        ammoAlertText = mediumFont.render("Ammo:",True,BLACK)
        screen.blit(ammoAlertText,[1250,5])

        xpText = point20Font.render("Level",True,BLUE)
        screen.blit(xpText,[490,10])

        healthText = point20Font.render("Health",True,GREEN)
        screen.blit(healthText,[490,40])
        pygame.draw.rect(screen,GREEN,(590,40,player.health//3,20))

        numHealthText = smallFont.render(str(player.health//2),True,BLACK)
        screen.blit(numHealthText,[690,40])
        
        if player.xp <= 100 and player.xp > 0:
            pygame.draw.rect(screen,BLUE,(590,10,player.xp,20))

        if player.xp > 100:
            player.xp = 0
            player.level += 1

        
        currentPlayerLevelText = smallFont.render(str(player.level),True,BLACK)
        screen.blit(currentPlayerLevelText,[575,10])
        
        nextLevel = player.level + 1
        nextPlayerLevelText = smallFont.render(str(nextLevel),True,BLACK)
        screen.blit(nextPlayerLevelText,[695,10])
        
        if player.godMode:
            player.level = 15
            
        
        for enemy in enemyList:
            if enemy.name == "rusher":
                if enemy.ghostBar:
                     pygame.draw.rect(screen,RED,(enemy.rect.x + 20,enemy.rect.y - 20,enemy.health//4,10))
                     pygame.draw.rect(screen,BLACK,(enemy.rect.x + 20,enemy.rect.y - 20,enemy.health//4,10),1)
                
            if enemy.name == "shooter":
                if enemy.shooterBar:
                    if enemy.direction == "left":
                        pygame.draw.rect(screen,RED,(enemy.rect.x + 50,enemy.rect.y + 10 ,enemy.health//4,10))
                        pygame.draw.rect(screen,BLACK,(enemy.rect.x + 50,enemy.rect.y + 10,enemy.health//4,10),1)
                    if enemy.direction == "right":
                        pygame.draw.rect(screen,RED,(enemy.rect.x + 50,enemy.rect.y + 10 ,enemy.health//4,10))
                        pygame.draw.rect(screen,BLACK,(enemy.rect.x + 50,enemy.rect.y + 10,enemy.health//4,10),1)
                    if enemy.direction == "up":
                        pygame.draw.rect(screen,RED,(enemy.rect.x + 15,enemy.rect.y + 10 ,enemy.health//4,10))
                        pygame.draw.rect(screen,BLACK,(enemy.rect.x + 15,enemy.rect.y + 10,enemy.health//4,10),1)
                    if enemy.direction == "down":
                        pygame.draw.rect(screen,RED,(enemy.rect.x + 15,enemy.rect.y + 10 ,enemy.health//4,10))
                        pygame.draw.rect(screen,BLACK,(enemy.rect.x + 15,enemy.rect.y + 10,enemy.health//4,10),1)
                        
            if enemy.name == "sniperEnemy":
                if enemy.sniperBar:
                    pygame.draw.rect(screen,RED,(enemy.rect.x + 20,enemy.rect.y - 20,enemy.health//4,10))
                    pygame.draw.rect(screen,BLACK,(enemy.rect.x + 20,enemy.rect.y - 20,enemy.health//4,10),1)
        
        
        if gunName is not "":
            if gunName == "pistol":
                if pistol.ammo >= 5:
                    ammoText = ammoFont.render((str(pistol.ammo) + "/"+str(pistol.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(pistol.ammo)+ "/"+str(pistol.fullAmmo)),True,RED)
            if gunName == "ak47":
                if ak47.ammo >= 11:
                    ammoText = ammoFont.render((str(ak47.ammo) + "/"+str(ak47.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(ak47.ammo)+ "/"+str(ak47.fullAmmo)),True,RED)
            if gunName == "mp40":
                if mp40.ammo >= 13:
                    ammoText = ammoFont.render((str(mp40.ammo) + "/"+str(mp40.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(mp40.ammo)+ "/"+str(mp40.fullAmmo)),True,RED)
            if gunName == "m1927":
                if m1927.ammo >= 16:
                    ammoText = ammoFont.render((str(m1927.ammo) + "/"+str(m1927.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(m1927.ammo)+ "/"+str(m1927.fullAmmo)),True,RED)
            if gunName == "raygun":
                if raygun.ammo >= 6:
                    ammoText = ammoFont.render((str(raygun.ammo) + "/"+str(raygun.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(raygun.ammo)+ "/"+str(raygun.fullAmmo)),True,RED)
            if gunName == "shotgun":
                if shotgun.ammo >= 3:
                    ammoText = ammoFont.render((str(shotgun.ammo) + "/"+str(shotgun.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(shotgun.ammo)+ "/"+str(shotgun.fullAmmo)),True,RED)
            if gunName == "s12":
                if s12.ammo >= 5:
                    ammoText = ammoFont.render((str(s12.ammo) + "/"+str(s12.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(s12.ammo)+ "/"+str(s12.fullAmmo)),True,RED)
            if gunName == "railgun":
                if railgun.ammo >= 26:
                    ammoText = ammoFont.render((str(railgun.ammo) + "/"+str(railgun.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(railgun.ammo)+ "/"+str(railgun.fullAmmo)),True,RED)
            if gunName == "ump":
                if ump.ammo >= 8:
                    ammoText = ammoFont.render((str(ump.ammo) + "/"+str(ump.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(ump.ammo)+ "/"+str(ump.fullAmmo)),True,RED)
            if gunName == "carbine":
                if carbine.ammo >= 5:
                    ammoText = ammoFont.render((str(carbine.ammo) + "/"+str(carbine.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(carbine.ammo)+ "/"+str(carbine.fullAmmo)),True,RED)
            if gunName == "awp":
                if awp.ammo >= 2:
                    ammoText = ammoFont.render((str(awp.ammo) + "/"+str(awp.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(awp.ammo)+ "/"+str(awp.fullAmmo)),True,RED)
            if gunName == "revolver":
                if revolver.ammo >= 3:
                    ammoText = ammoFont.render((str(revolver.ammo) + "/"+str(revolver.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(revolver.ammo)+ "/"+str(revolver.fullAmmo)),True,RED)
            if gunName == "cz75":
                if cz75.ammo >= 4:
                    ammoText = ammoFont.render((str(cz75.ammo) + "/"+str(cz75.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(cz75.ammo)+ "/"+str(cz75.fullAmmo)),True,RED)
            if gunName == "rampart-17":
                if rampart17.ammo >= 4:
                    ammoText = ammoFont.render((str(rampart17.ammo) + "/"+str(rampart17.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(rampart17.ammo)+ "/"+str(rampart17.fullAmmo)),True,RED)
            if gunName == "rpg":
                if rpg.ammo >= 1:
                    ammoText = ammoFont.render((str(rpg.ammo) + "/"+str(rpg.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(rpg.ammo)+ "/"+str(rpg.fullAmmo)),True,RED)
            if gunName == "grenade launcher":
                if grenadeLauncher.ammo >= 2:
                    ammoText = ammoFont.render((str(grenadeLauncher.ammo) + "/"+str(grenadeLauncher.fullAmmo)),True,BLACK)
                else:
                    ammoText = ammoFont.render((str(grenadeLauncher.ammo)+ "/"+str(grenadeLauncher.fullAmmo)),True,RED)
                
                    
                
                    
            screen.blit(ammoText,[1250,50])
                
            
for i in range(1):
    # Defines all of the guns so that you can use any of them at the start from the save file
    global awp
    awp = Guns(BLACK,20,57,700,400,"awp",awpPic)
    
    global carbine
    carbine = Guns(BLACK,20,57,600,400,"carbine",carbinePic)

    global railgun
    railgun = Guns(BLACK,20,57,800,400,"railgun",railgunPic)

    global ak47
    ak47 = Guns(BLACK,20,57,500,400,"ak47",ak47Pic)

    global revolver
    revolver = Guns(BLACK,30,61,500,200,"revolver",revolverPic)

    global raygun
    raygun = Guns(BLACK,30,61,600,200,"raygun",raygunPic)

    global mp40
    mp40 = Guns(BLACK,20,57,700,200,"mp40",mp40Pic)

    global m1927
    m1927 = Guns(BLACK,20,57,800,200,"m1927",m1927Pic)

    global s12
    s12 = Guns(BLACK,20,57,800,600,"s12",s12Pic)

    global shotgun
    shotgun = Guns(BLACK,20,57,700,600,"shotgun",shotgunPic)

    global pistol
    pistol = Guns(BLACK,20,57,600,600,"pistol",pistolPic)
    

    global ump
    ump = Guns(BLACK,20,57,500,600,"ump",umpPic)

    global cz75
    cz75 = Guns(BLACK,30,32,200,600,"cz75",cz75Pic)

    global rampart17
    rampart17 = Guns(BLACK,30,79,200,400,"rampart-17",rampart17Pic)

    global rpg
    rpg = Guns(BLACK,30,68,200,200,"rpg",rpgPic)

    global grenadeLauncher
    grenadeLauncher = Guns(BLACK,30,68,350,200,"grenade launcher",grenadeLauncherPic)
        


''' Functions '''

#Player functions
def playerSprite(posX,posY,base,orange):
    # draws the player sprite
    if base == True:
        pygame.draw.circle(screen,BEIGE,[posX,posY],25)
        pygame.draw.circle(screen,(20,90,50),[posX,posY],10)
        pygame.draw.circle(screen,BLACK,[posX,posY],25,3)
    if orange:
        screen.blit(spritePic1,[posX - 25,posY - 25])
    if chrome:
        screen.blit(spritePic2,[posX - 25,posY - 25])
    if firefox1:
        screen.blit(spritePic3,[posX - 25,posY - 25])
    if firefox2:
        screen.blit(spritePic4,[posX - 25,posY - 25])
    if internetExplorer:
        screen.blit(spritePic5,[posX - 25,posY - 25])
    if EA:
        screen.blit(spritePic6,[posX - 25,posY - 25])
        
        
    

def breakWall(walls,leftArm,dmg):
    # if the player's fist comes into contact with the wall, you can break the wall
    wallBreakList = pygame.sprite.spritecollide(leftArm,walls,False)
    for wall in wallBreakList:
        wall.health -= dmg
        sound = pygame.mixer.Sound("Sounds/wallCollision.wav")
        channel = sound.play()
        if wall.health <= 0:
            walls.remove(wall)


# shooting functions
"""
These all work the same. It runs an iterable list through "pygame.sprite.spritecollide" with a single object, and test if there is
collision. If there is, then the specified action takes place. If the player shoots an enemy, the enemy loses health; and vice versa. All the bosses except beefy act the same way.
You need to shoot beefys bullets to kill him.
"""
def shootWall(bullets,walls,dmg):
    for bullet in bullets:
        wallShootList = pygame.sprite.spritecollide(bullet,walls,False)
        for wall in wallShootList:
            if bullet.name is not "mine":
                wall.health -= dmg
            if wall.health <= 0:
                walls.remove(wall)
            xCap = bullet.rect.x
            yCap = bullet.rect.y
            if gunName == "rpg":
                explodeBullet("rpg",40,xCap,yCap)
            bullets.remove(bullet)
            if gunName == "grenade launcher":
                explodeBullet("grenade launcher",40,xCap,yCap)
            bullets.remove(bullet)
                

    for bullet in shooterBullets:
        wallShootList = pygame.sprite.spritecollide(bullet,walls,False)
        for wall in wallShootList:
            shooterBullets.remove(bullet)
        
    for bullet in shrapnel:
        wallShootList = pygame.sprite.spritecollide(bullet,walls,False)
        for wall in wallShootList:
            if bullet.name is not "mine":
                wall.health -= bullet.dmg//100
            shrapnel.remove(bullet)
            if wall.health <= 0:
                walls.remove(wall)
        

    for bullet in sniperBullets:
        wallShootList = pygame.sprite.spritecollide(bullet,walls,False)
        for wall in wallShootList:
            if wall.name == "wall":
                walls.remove(wall)
            sniperBullets.remove(bullet)

    for ball in beefyBalls:
        wallShootList = pygame.sprite.spritecollide(ball,walls,False)
        for wall in wallShootList:
            ball.vx = -ball.vx
            ball.vy = -ball.vy
            
    
    
        

def shootGhosts(bullets,ghosts):
    for bullet in bullets:
        ghostHitList = pygame.sprite.spritecollide(bullet,ghosts,False)
        for ghost in ghostHitList:
            ghost.ghostBar = True
            ghost.health -= bullet.dmg
            xCap = bullet.rect.x
            yCap = bullet.rect.y
            ghost.alert = True
            bullets.remove(bullet)
            if bullet.name == "rpg":
                explodeBullet("rpg",60,xCap,yCap)
            if bullet.name == "grenade launcher":
                explodeBullet("grenade launcher",20,xCap,yCap)
    for bullet in shrapnel:
        ghostHitList = pygame.sprite.spritecollide(bullet,ghosts,False)
        for ghost in ghostHitList:
            ghost.ghostBar = True
            ghost.health -= bullet.dmg
            ghost.alert = True
    for ghost in ghosts:
        if ghost.health <= 0:
            player.xp += 5
            ghost.ghostBar = False
            ghosts.remove(ghost)

def shootShooters(bullets,shooters):
    for bullet in bullets:
        shooterHitList = pygame.sprite.spritecollide(bullet,shooters,False)
        for shooter in shooterHitList:
            shooter.shooterBar = True
            shooter.health -= bullet.dmg
            xCap = bullet.rect.x
            yCap = bullet.rect.y
            bullets.remove(bullet)
            if bullet.name == "rpg":
                explodeBullet("rpg",60,xCap,yCap)
            if bullet.name == "grenade launcher":
                explodeBullet("grenade launcher",20,xCap,yCap)
                
    for bullet in shrapnel:
        shooterHitList = pygame.sprite.spritecollide(bullet,shooters,False)
        for shooter in shooterHitList:
            shooter.shooterBar = True
            shooter.health -= bullet.dmg
    for shooter in shooters:
        if shooter.health <= 0:
            player.xp += 10
            shooter.shooterBar = False
            shooters.remove(shooter)

def shootSnipers(bullets,snipers):
    for bullet in bullets:
        sniperHitList = pygame.sprite.spritecollide(bullet,snipers,False)
        for sniperEnemy in sniperHitList:
            sniperEnemy.sniperBar = True
            sniperEnemy.health -= bullet.dmg
            xCap = bullet.rect.x
            yCap = bullet.rect.y
            bullets.remove(bullet)
            if bullet.name == "rpg":
                explodeBullet("rpg",60,xCap,yCap)
            if bullet.name == "grenade launcher":
                explodeBullet("grenade launcher",20,xCap,yCap)
    
    for bullet in shrapnel:
        sniperHitList = pygame.sprite.spritecollide(bullet,snipers,False)
        for sniperEnemy in sniperHitList:
            if bullet.name == "mine":
                pass
            else:
                sniperEnemy.sniperBar = True
                sniperEnemy.health -= bullet.dmg
            
    for Enemysniper in snipers:
        if Enemysniper.health <= 0:
            player.xp += 15
            Enemysniper.sniperBar = False
            snipers.remove(Enemysniper)

def shootBalls(bullets,balls):
    for bullet in bullets:
        ballHitList = pygame.sprite.spritecollide(bullet,balls,False)
        for ball in ballHitList:
            ball.health -= bullet.dmg
            xCap = bullet.rect.x
            yCap = bullet.rect.y
            bullets.remove(bullet)
            if bullet.name == "rpg":
                explodeBullet("rpg",60,xCap,yCap)
            if bullet.name == "grenade launcher":
                explodeBullet("grenade launcher",20,xCap,yCap)

    for bullet in shrapnel:
        ballHitList = pygame.sprite.spritecollide(bullet,balls,False)
        for ball in ballHitList:
            ball.health -= bullet.dmg
            
def shootBeefy(bullets,beefys):
    for beefy in beefys:
        beefyShootList = pygame.sprite.spritecollide(beefy,bullets,False)
        for bullet in beefyShootList:
            bullets.remove(bullet)

def shootPump(bullets,pumpList):
    for pump in pumpList:
        pumpShootList = pygame.sprite.spritecollide(pump,bullets,False)
        for bullet in pumpShootList:
            if bullet.name is not "mine":
                pump.health -= bullet.dmg
            mine = Bullet(BLACK,20,20,"mine",random.randrange(150,1290),random.randrange(150,600))
            pumpMines.add(mine)
            explodeBullet("mine",100,mine.rect.x,mine.rect.y)
            bullets.remove(bullet)

def shootBottom(bullets,bottomList):
    for bottom in bottomList:
        bottomShootList = pygame.sprite.spritecollide(bottom,bullets,False)
        for bullet in bottomShootList:
            bottom.health -= bullet.dmg
            bullets.remove(bullet)

    
            
    
                                               
# weapon logistics functions           
def reloadGun(gun):
    # Sets the guns ammo to its max capacity; called when r is hit
    gun.ammo = gun.fullAmmo

def destroyBullet(bullets):
    for i in bullets:
        # if a player bullet leaves the screen, its removed
        if i.rect.x >= displayWidth or i.rect.x <= 0 or i.rect.y >= displayHeight or i.rect.y <= 80:
            bullets.remove(i)
    for i in beefyBalls:
        if i.rect.x >= displayWidth or i.rect.x <= 0 or i.rect.y >= displayHeight or i.rect.y <= 80:
            beefyBalls.remove(i)
    for i in sniperBullets:
        if i.rect.x >= displayWidth or i.rect.x <= 0 or i.rect.y >= displayHeight or i.rect.y <= 80:
            sniperBullets.remove(i)
        

def updateGun(isArmed,mb):
    if isArmed:
        # decides which gun is being used by the player and updates it
        if gunName == "ak47":
            ak47.update(mx,my,ak47Pic,mb,"ak47")
        if gunName == "mp40":
            mp40.update(mx,my,mp40Pic,mb,"mp40")
        if gunName == "m1927":
            m1927.update(mx,my,m1927Pic,mb,"m1927")
        if gunName == "raygun":
            raygun.update(mx,my,raygunPic,mb,"raygun")
        if gunName == "railgun":
            railgun.update(mx,my,railgunPic,mb,"railgun")
        if gunName == "shotgun":
            shotgun.update(mx,my,shotgunPic,mb,"shotgun")
        if gunName == "s12":
            s12.update(mx,my,s12Pic,mb,"s12")
        if gunName == "pistol":
            pistol.update(mx,my,pistolPic,mb,"pistol")
        if gunName == "ump":
            ump.update(mx,my,umpPic,mb,"ump")
        if gunName == "carbine":
            carbine.update(mx,my,carbinePic,mb,"carbine")
        if gunName == "awp":
            awp.update(mx,my,awpPic,mb,"awp")
        if gunName == "revolver":
            revolver.update(mx,my,revolverPic,mb,"revolver")
        if gunName == "cz75":
            cz75.update(mx,my,cz75Pic,mb,"cz75")
        if gunName == "rampart-17":
            rampart17.update(mx,my,rampart17Pic,mb,"rampart-17")
        if gunName == "rpg":
            rpg.update(mx,my,rpgPic,mb,"rpg")
        if gunName == "grenade launcher":
            grenadeLauncher.update(mx,my,grenadeLauncherPic,mb,"grenade launcher")
            
        
            
def fullAutoWeapons(mb,gunName,isArmed,switch):
    '''
    These weapons are fully automatic. They fire one bullet every "x" amount of frames as long as left click is held down
    It also plays the weapon sound every time a bullet is fired. It takes one bullet away from the total ammo as well. 
    '''
    if gunName == "ak47":
        if ak47.ammo > 0 and isArmed and not player.switch and mb[0]:
            ak47.bulletTime += 1
            if ak47.bulletTime >= 30:
                ak47.bulletTime = 0
                bullet = Bullet(BLACK,9,9,gunName,ak47.rect.x,ak47.rect.y)
                ak47.ammo -= 1
                bullet.trajectory(mx,my)
                bullets.add(bullet)
                sound = pygame.mixer.Sound("Sounds/AK471.wav")
                channel = sound.play()
    if gunName == "mp40":
        if mp40.ammo > 0 and isArmed and not player.switch and mb[0]:
            mp40.bulletTime += 1
            if mp40.bulletTime >= 24:
                mp40.bulletTime = 0
                bullet = Bullet(BLACK,9,9,gunName,mp40.rect.x,mp40.rect.y)
                mp40.ammo -= 1
                bullet.trajectory(mx,my)
                bullets.add(bullet)
                sound = pygame.mixer.Sound("Sounds/MP40.wav")
                channel = sound.play()
    if gunName == "m1927":
        if m1927.ammo > 0 and isArmed and not player.switch and mb[0]:
            m1927.bulletTime += 1
            if m1927.bulletTime >= 5:
                m1927.bulletTime = 0
                bullet = Bullet(BLACK,9,9,gunName,m1927.rect.x,m1927.rect.y)
                m1927.ammo -= 1
                bullet.trajectory(mx,my)
                bullets.add(bullet)
                sound = pygame.mixer.Sound("Sounds/M1927.wav")
                channel = sound.play()
    if gunName == "ump":
        if ump.ammo > 0 and isArmed and not player.switch and mb[0]:
            ump.bulletTime += 1
            if ump.bulletTime >= 3:
                ump.bulletTime = 0
                bullet = Bullet(BLACK,4,4,gunName,ump.rect.x,ump.rect.y)
                ump.ammo -= 1
                bullet.trajectory(mx,my)
                bullets.add(bullet)
                sound = pygame.mixer.Sound("Sounds/UMP45.wav")
                channel = sound.play()
    if gunName == "railgun":
        if railgun.ammo > 0 and mb[0] and isArmed and not player.switch:
            bullet = Bullet(BLACK,5,5,gunName,railgun.rect.x,railgun.rect.y)
            railgun.ammo -= 1
            bullet.trajectory(mx,my)
            bullets.add(bullet)
            sound = pygame.mixer.Sound("Sounds/Railmini (mp3cut.net).wav")
            channel = sound.play()

    if gunName == "cz75":
        if cz75.ammo > 0 and isArmed and not player.switch and mb[0]:
            cz75.bulletTime += 1
            if cz75.bulletTime >= 11:
                cz75.bulletTime = 0
                bullet = Bullet(BLACK,4,4,gunName,cz75.rect.x,cz75.rect.y)
                cz75.ammo -= 1
                bullet.trajectory(mx,my)
                bullets.add(bullet)
                sound = pygame.mixer.Sound("Sounds/CZ751.wav")
                channel = sound.play()
        
'''
This function defines the ranges of certain guns,
this is done with having a specific time associated with each guns bullets and removes the bullet irrespective of collision if said timer exceeds the limit
'''
def limitRange(bullets,gunName):
    if gunName == "shotgun":
        for bullet in bullets:
            if bullet.rangeLimit:
                bullet.rangeTimer += 1
            if bullet.rangeTimer >= 30:
                bullet.rangeLimit = False
                bullet.rangeTimer = 0
                bullets.remove(bullet)
    if gunName == "s12":
        for bullet in bullets:
            if bullet.rangeLimit:
                bullet.rangeTimer += 1
            if bullet.rangeTimer >= 40:
                bullet.rangeLimit = False
                bullet.rangeTimer = 0
                bullets.remove(bullet)
    if gunName == "rpg":
        for bullet in shrapnel:
            bullet.rangeTimer += 1
            if bullet.rangeTimer >= 40:
                bullet.rangeTimer = 0
                bullet.rangeLimit = False
                shrapnel.remove(bullet)
    if gunName == "grenade launcher":
        for bullet in bullets:
            if not bullet.explode:
                if bullet.rangeLimit:
                    bullet.rangeTimer += 1
                if bullet.rangeTimer >= 40:
                    bullet.rangeLimit = False
                    xCap = bullet.rect.x
                    yCap = bullet.rect.y
                    bullet.rangeTimer = 0
                    bullets.remove(bullet)
                    explodeBullet("grenade launcher",20,xCap,yCap)
        for bullet in shrapnel:
            bullet.rangeTimer += 1
            if bullet.rangeTimer >= 40:
                bullet.rangeTimer = 0
                bullet.rangeLimit = False
                shrapnel.remove(bullet)

    for bullet in shrapnel:
        if bullet.name == "mine":
            bullet.rangeTimer += 1
            if bullet.rangeTimer >= 40:
                bullet.rangeTimer = 0
                bullet.rangeLimit = False
                shrapnel.remove(bullet)
            
                    
'''
explosion type weapon explosion animation
'''
def explodeBullet(gunName,size,xCap,yCap):
    for i in range(size):
        bullet = Bullet((255,random.randrange(87,195),random.randrange(0,51)),20,20,gunName,xCap,yCap)
        bullet.explode = True
        bullet.rangeLimit = True
        shrapnel.add(bullet)
    sound = pygame.mixer.Sound("Sounds/RPG_Reload.wav")
    channel = sound.play()
    
# Objective functions
def drawZone(zones):#drawing zones
    for zone in zones:
        pygame.draw.circle(screen,zone.color,[zone.rect.x + 50,zone.rect.y + 50],zone.width//2)
        pygame.draw.circle(screen,BLACK,[zone.rect.x + 50,zone.rect.y + 50],zone.width//2,1)
        objText = point20Font.render(str(int(zone.capTimer/1500 * 100)) + "%",True,BLACK)
        screen.blit(objText,[zone.rect.x + 40,zone.rect.y + 40])

def obj(stage,current):#the two stages where we have zones
    if stage == 1:
        current = "zone"
    if stage == 8:
        current = "zone"
    return current

# Saving function
def saveGame():
    # Saves the game by clearing "Save.txt" and adding the current stage, the players level and the gun the player has
    # Does not do this if the player has completed stage 7, instead it will save the current stage as 1
    if Hud.gameOver is not True:
        saveFile = open("Save.txt","w")
        saveFile.write(str(currentStage) + "\n")
        saveFile.write(str(player.level) + "\n")
        saveFile.write(gunName + "\n")
    if Hud.gameOver:
        saveFile = open("Save.txt","w")
        saveFile.write(str(1) + "\n")
        saveFile.write(str(player.level) + "\n")
        saveFile.write(gunName + "\n")
        
        
#Level functions
def endGame(gameOver): # This is what happens when the player kills the final boss.
    if gameOver:
        screen.fill(BLACK)
        gameAlertText = thiccFont.render("VICTORY",True,RED)
        screen.blit(gameAlertText,[550,300])
        saveGame()

        '''
        below code isnt working, fps dropping, when i try mixer thing it gives a time error, when i click on the rect it wont work
        '''
####        display = "victory"
####        pygame.mixer.music.play(0,123)
####        pygame.mixer.music.load("Sounds/victory.wav")
####        pygamemixer.music.play()
##        saveGame()
##        screen.blit(victoryScreen,[0,0])
##        pygame.mouse.set_visible(True)
##        screen.blit(victoryScreen,[0,0])
##        exitRect = pygame.Rect(507,372,355,99)
##        if exitRect.collidepoint(mx,my):
##            pygame.draw.rect(screen,BLACK,exitRect,4)
##            sound = pygame.mixer.Sound("Sounds/hover.wav")
##            channel = sound.play()
##            if mouseDown[0]:
##                screen.fill(BLACK)
##                done = True
####                saveGame()#will save and end the game

        
def drawStage(Stage): # this draws the grass background in each of the stages
    screen.blit(grassBack,(0,0))

def clearStage():# this function removes all level content once certain conditions are met, primarily used when changing levels. 
    for wall in walls:
        walls.remove(wall)
    for guns in gunList:
        gunList.remove(guns)
    for enemy in enemyList:
        enemyList.remove(enemy)
    for ghosts in ghostList:
        ghostList.remove(ghosts)
    for shooter in shooterList:
        shooterList.remove(shooter)
    for sniperEnemy in sniperEnemyList:
        sniperEnemyList.remove(sniperEnemy)
    for bullet in bullets:
        bullets.remove(bullet)
    for bullet in shooterBullets:
        shooterBullets.remove(bullet)
    for bullet in sniperBullets:
        sniperBullets.remove(bullet)
    for beefy in beefyList:
        beefyList.remove(beefy)
    for ball in beefyBalls:
        beefyBalls.remove(ball)
    for pump in pumpList:
        pumpList.remove(pump)
    for mine in pumpMines:
        pumpMines.remove(mine)
    for zone in zoneList:
        zoneList.remove(zoneList)
    for thing in shrapnel:
        shrapnel.remove(shrapnel)
'''
displays the player's location amoung the stages in the top left corner within a mini map
also determines where a player spawns, depeding on the last level he was at
'''
def changeStage(player,currentStage,lastStage):
    if display == "death":
        if currentStage is not 7:
            currentStage = lastStage
        else:
            currentStage = 7
    if currentStage == 1:
        pygame.draw.circle(screen, GREEN, (8,37),3)
        if player.rect.y <= 85:
            currentStage = 2
        if player.rect.y >= 740:
            currentStage = 8
        if player.rect.x >= 1310:
            currentStage = 5
    if currentStage == 2:
        pygame.draw.circle(screen, GREEN, (8,27),2)
        if player.rect.y <= 80:
            currentStage = 3
        if player.rect.y >= 730:
            currentStage = 1
    if currentStage == 3:
        pygame.draw.circle(screen, GREEN, (8,14),2)
        if player.rect.y >= 740:
            currentStage = 2
        if player.rect.y <= 75:
            currentStage = 4
    if currentStage == 4:
        pygame.draw.circle(screen, GREEN, (8,3),2)
        if player.rect.y >= 740:
            currentStage = 3
        if player.rect.y <= 65:
            currentStage = 69
    if currentStage == 5:
        pygame.draw.circle(screen, GREEN, (21,38),2)
        if player.rect.x >= 1330:
            currentStage = 6
        if player.rect.x <= 30:
            currentStage = 1
    if currentStage == 6:
        pygame.draw.circle(screen, GREEN, (34,38),2)
        if player.rect.x >= 1360:
            currentStage = 7
        if player.rect.x <= 20:
            currentStage = 5
    if currentStage == 7:
        pygame.draw.circle(screen, GREEN, (47,38),2)
        
    if currentStage == 8:
        if player.rect.y <= 80:
            currentStage = 1
        if player.rect.y >= 753:
            currentStage = 9
    if currentStage == 9:
        if player.rect.y <= 70:
            currentStage = 8
        if player.rect.y >= 759:
            currentStage = 10
    if currentStage == 10:
        if player.rect.y <= 70:
            currentStage = 9
        
    if currentStage == 69:
        pygame.draw.rect(screen, GREY, (0, 0, 50, 100))
        screen.blit(unknown,[0,0])
        if player.rect.y >= 740:
            currentStage = 4
    return currentStage
'''
the next set of function all follow the same purpose, they are set levels containing enemies, specific wall placement, and guns.
This allows easy munipulation and calling of levels due to each level being independant from the other. 
'''
def stage1(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 1
    # Barriers
    barrier1 = Wall(BLACK,600,30,0,75,100000000,"barrier")
    walls.add(barrier1)
    barrier1b = Wall(BLACK,800,30,700,75,1000000,"barrier")
    walls.add(barrier1b)
    barrier2 = Wall(BLACK,600,30,0,750,100000000,"barrier")
    walls.add(barrier2)
    barrier2a = Wall(BLACK,800,30,700,750,100000000,"barrier")
    walls.add(barrier2a)
    barrier3 = Wall(BLACK,30,770,0,75,100000000,"barrier")
    walls.add(barrier3)
    barrier4a = Wall(BLACK,30,350,1338,75,100000000,"barrier")
    walls.add(barrier4a)
    barrier4b = Wall(BLACK,30,770,1338,515,100000000,"barrier")
    walls.add(barrier4b)
    for i in range(10):
        wall = Wall(GREEN,20,20,400 + (10 * i),400,100,"wall")
        walls.add(wall)
    for i in range(10):
        wall = Wall(GREEN,20,20,400,400 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(10):
        wall = Wall(GREEN,20,20,500,400 + (i * 10),100,"wall")
        walls.add(wall)
    for i in range(11):
        wall = Wall(GREEN,20,20,400 + (10 * i),500,100,"wall")
        walls.add(wall)

    zone = Zone(RED,100,100,800,600)
    zoneList.add(zone)
        
    global pistol
    pistol = Guns(BLACK,20,50,600,600,"pistol",pistolPic)
    gunList.add(pistol)

    for i in range(5):
        ghost = Enemies(850 + 50 * i ,115,"rusher",1,ghostPic,None)
        ghostList.add(ghost)
        enemyList.add(ghost)
    
    shooter = Enemies(900,300,"shooter",1,shooterLeftPic,"left")
    shooterList.add(shooter)
    enemyList.add(shooter)

    shooter2 = Enemies(900,375,"shooter",1,shooterLeftPic,"left")
    shooterList.add(shooter2)
    enemyList.add(shooter2)

    global carbine
    carbine = Guns(BLACK,20,50,955,398,"carbine",carbinePic)
    gunList.add(carbine)

    shooter3 = Enemies(900,450,"shooter",1,shooterLeftPic,"left")
    shooterList.add(shooter3)
    enemyList.add(shooter3)    

   
def stage2(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 2
    barrier1 = Wall(BLACK,600,30,0,738,100000000,"barrier")
    walls.add(barrier1)
    barrier1b = Wall(BLACK,800,30,700,738,1000000,"barrier")
    walls.add(barrier1b)
    barrier3 = Wall(BLACK,30,770,0,75,100000000,"barrier")
    walls.add(barrier3)
    barrier4 = Wall(BLACK,30,770,1338,75,100000000,"barrier")
    walls.add(barrier4)
    barrier5 = Wall(BLACK,600,30,0,75,100000000,"barrier")
    walls.add(barrier5)
    barrier5b = Wall(BLACK,800,30,700,75,1000000,"barrier")
    walls.add(barrier5b)

    global shotgun
    shotgun = Guns(BLACK,20,50,600,600,"shotgun",shotgunPic)
    gunList.add(shotgun)
    for i in range(2):
        ghost = Enemies(340 + ( 42 * i) ,600,"rusher",1,ghostPic,None)
        ghostList.add(ghost)
        enemyList.add(ghost)
    for i in range(2):
        ghost = Enemies(340 + ( 42 * i) ,555,"rusher",1,ghostPic,None)
        ghostList.add(ghost)
        enemyList.add(ghost)
    for i in range(2):
        ghost = Enemies(340 + ( 42 * i) ,520,"rusher",1,ghostPic,None)
        ghostList.add(ghost)
        enemyList.add(ghost)
    for i in range(2):
        ghost = Enemies(860 + ( 42 * i) ,600,"rusher",1,ghostPic,None)
        ghostList.add(ghost)
        enemyList.add(ghost)
    for i in range(2):
        ghost = Enemies(860 + ( 42 * i) ,555,"rusher",1,ghostPic,None)
        ghostList.add(ghost)
        enemyList.add(ghost)
    for i in range(2):
        ghost = Enemies(860 + ( 42 * i) ,520,"rusher",1,ghostPic,None)
        ghostList.add(ghost)
        enemyList.add(ghost)
    
   
        
    for i in range(12):
        wall = Wall(GREEN,20,20,450 + (10 * i),615,100,"wall")
        walls.add(wall)
    for i in range(20):
        wall = Wall(GREEN,20,20,125 + (10 * i),615,100,"wall")
        walls.add(wall)
    for i in range(20):
        wall = Wall(GREEN,20,20,960 + (10 * i),615,100,"wall")
        walls.add(wall)
    for i in range(12):
        wall = Wall(GREEN,20,20,720 + (10 * i),615,100,"wall")
        walls.add(wall)
    for i in range(13):
        wall = Wall(GREEN,20,20,315 + (10 * i),490,100,"wall")
        walls.add(wall)
    for i in range(13):
        wall = Wall(GREEN,20,20,830 + (10 * i),490,100,"wall")
        walls.add(wall)
    for i in range(45):
        wall = Wall(GREEN,20,20,125 + (10 * i),425,100,"wall")
        walls.add(wall)
    for i in range(46):
        wall = Wall(GREEN,20,20,700 + (10 * i),425,100,"wall")
        walls.add(wall)
    for i in range(45):
        wall = Wall(GREEN,20,20,125 + (10 * i),325,100,"wall")
        walls.add(wall)
    for i in range(46):
        wall = Wall(GREEN,20,20,700 + (10 * i),325,100,"wall")
        walls.add(wall)
    for i in range(45):
        wall = Wall(GREEN,20,20,125 + (10 * i),325,100,"wall")
        walls.add(wall)
    for i in range(46):
        wall = Wall(GREEN,20,20,700 + (10 * i),325,100,"wall")
        walls.add(wall)
    for i in range(45):
        wall = Wall(GREEN,20,20,125 + (10 * i),235,100,"wall")
        walls.add(wall)
    for i in range(46):
        wall = Wall(GREEN,20,20,700 + (10 * i),235,100,"wall")
        walls.add(wall)
#-------------------------horizontal---------------------------------------------------
    for i in range(20):
        wall = Wall(GREEN,20,20,580,425 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(20):
        wall = Wall(GREEN,20,20,700,425 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(12):
        wall = Wall(GREEN,20,20,450,490 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(12):
        wall = Wall(GREEN,20,20,830,490 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(12):
        wall = Wall(GREEN,20,20,315,490 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(12):
        wall = Wall(GREEN,20,20,960,490 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(20):
        wall = Wall(GREEN,20,20,125,425 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(20):
        wall = Wall(GREEN,20,20,125,425 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(20):
        wall = Wall(GREEN,20,20,1170,425 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(10):
        wall = Wall(GREEN,20,20,125,235 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(10):
        wall = Wall(GREEN,20,20,1170,235 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(10):
        wall = Wall(GREEN,20,20,580,235 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(10):
        wall = Wall(GREEN,20,20,700,235 + (10 * i),100,"wall")
        walls.add(wall)
    
        
    shooter = Enemies(1225, 425, "shooter", 1, shooterDownPic, "down")
    shooterList.add(shooter)
    enemyList.add(shooter)

    global raygun
    raygun = Guns(BLACK,20,50,1260,455,"raygun",raygunPic)
    gunList.add(raygun)
    
    shooter = Enemies(40, 425, "shooter", 1, shooterDownPic, "down")
    shooterList.add(shooter)
    enemyList.add(shooter)
    
    shooter2 = Enemies(475, 125, "shooter", 1, shooterLeftPic, "left")
    shooterList.add(shooter2)
    enemyList.add(shooter2)
    shooter4 = Enemies(475, 325, "shooter", 1, shooterLeftPic, "left")
    shooterList.add(shooter4)
    enemyList.add(shooter4)
    shooter6 = Enemies(1100, 615, "shooter", 1, shooterLeftPic, "left")
    shooterList.add(shooter6)
    enemyList.add(shooter6)
    
    shooter3 = Enemies(700, 325, "shooter", 1, shooterRightPic, "right")
    shooterList.add(shooter3)
    enemyList.add(shooter3)
    shooter5 = Enemies(700, 125, "shooter", 1, shooterRightPic, "right")
    shooterList.add(shooter5)
    enemyList.add(shooter5)
    shooter5 = Enemies(100, 635, "shooter", 1, shooterRightPic, "right")
    shooterList.add(shooter5)
    enemyList.add(shooter5)
    
    sniperEnemy1 = Enemies(775, 275, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy1)
    enemyList.add(sniperEnemy1)
    
    sniperEnemy2 = Enemies(475, 275, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy2)
    enemyList.add(sniperEnemy2)
    
    sniperEnemy3 = Enemies(485, 485, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy3)
    enemyList.add(sniperEnemy3)
    
    sniperEnemy4 = Enemies(750, 485, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy4)
    enemyList.add(sniperEnemy4)

def stage3(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 3
    barrier1 = Wall(BLACK,600,30,0,738,100000000,"barrier")
    walls.add(barrier1)
    barrier1b = Wall(BLACK,800,30,700,738,1000000,"barrier")
    walls.add(barrier1b)
    
    barrier3 = Wall(BLACK,30,770,0,75,100000000,"barrier")
    walls.add(barrier3)
    barrier4 = Wall(BLACK,30,770,1338,75,100000000,"barrier")
    walls.add(barrier4)
    barrier5 = Wall(BLACK,600,30,0,75,100000000,"barrier")
    walls.add(barrier5)
    barrier5b = Wall(BLACK,800,30,700,75,1000000,"barrier")
    walls.add(barrier5b)
    for i in range(5):
        wall = Wall(GREEN,20,20,800 + (10 * i),300 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(5):
        wall = Wall(GREEN,20,20,455 + (10 * i),445 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(5):
        wall = Wall(GREEN,20,20,500 - (10 * i),300 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(5):
        wall = Wall(GREEN,20,20,845 - (10 * i), 445 + (10 * i),100,"wall")
        walls.add(wall)
    zone = Zone(RED,100,100,598,353)
    zoneList.add(zone)
    
    box = Wall(BROWN,100,100,50,650,300,"crate")
    walls.add(box)

    box1 = Wall(BROWN,100,100,610,360,300,"crate")
    walls.add(box1)

    box2 = Wall(BROWN,100,100,1250,650,300,"crate")
    walls.add(box2)
    
    global ump
    ump = Guns(BLACK,20,50,60,660,"ump",umpPic)
    gunList.add(ump)

    global rampart17
    rampart17 = Guns(BLACK,20,50,620,360,"rampart-17",rampart17Pic)
    gunList.add(rampart17)

    global revolver
    revolver = Guns(BLACK,20,50,1275,675,"revolver",revolverPic)
    gunList.add(revolver)
    
    
    sniperEnemy1 = Enemies(1200, 150, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy1)
    enemyList.add(sniperEnemy1)
    
    sniperEnemy2 = Enemies(100, 150, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy2)
    enemyList.add(sniperEnemy2)
    
    shooter2 = Enemies(1200, 350, "shooter", 1, shooterLeftPic, "left")
    shooterList.add(shooter2)
    enemyList.add(shooter2)

    shooter2 = Enemies(1000,  625, "shooter", 1, shooterLeftPic, "left")
    shooterList.add(shooter2)
    enemyList.add(shooter2)

    shooter5 = Enemies(200, 625, "shooter", 1, shooterRightPic, "right")
    shooterList.add(shooter5)
    enemyList.add(shooter5)
    shooter5 = Enemies(50, 350, "shooter", 1, shooterRightPic, "right")
    shooterList.add(shooter5)
    enemyList.add(shooter5)
    shooter = Enemies(700, 100, "shooter", 1, shooterDownPic, "down")
    shooterList.add(shooter)
    enemyList.add(shooter)
    shooter = Enemies(500, 100, "shooter", 1, shooterDownPic, "down")
    shooterList.add(shooter)
    enemyList.add(shooter)


    
def stage4(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 4
    barrier1 = Wall(BLACK,600,30,0,738,100000000,"barrier")
    walls.add(barrier1)
    barrier1b = Wall(BLACK,800,30,700,738,1000000,"barrier")
    walls.add(barrier1b)
    barrier3 = Wall(BLACK,30,770,0,75,100000000,"barrier")
    walls.add(barrier3)
    barrier4 = Wall(BLACK,30,770,1338,75,100000000,"barrier")
    walls.add(barrier4)
    barrier5 = Wall(BLACK,600,30,0,75,100000000,"barrier")
    walls.add(barrier5)
    barrier5b = Wall(BLACK,800,30,700,75,1000000,"barrier")
    walls.add(barrier5b)

    if player.godMode:
        for i in range(10):
            wall = Wall(BLACK,800,30,300 + (10 * i),75,250,"barrier")
            walls.add(wall)
    else:
        for i in range(10):
            wall = Wall(BLACK,800,30,300 + (10 * i),75,1000000000,"barrier")
            walls.add(wall)
        

    if "Beefy" not in bossKilledList:
        beefy = Boss("Beefy",554,100)
        beefyList.add(beefy)

        global m1927
        m1927 = Guns(BLACK, 590, 200, 620, 190, "m1927", m1927Pic)
        gunList.add(m1927)
    
    for i in range(10):
        wall = Wall(GREEN,20,20,200 + (10 * i),500 + (10 * i),100,"wall")
        walls.add(wall)
    for i in range(10):
        wall = Wall(GREEN,20,20,1100 - (10 * i),500 + (10 * i),100,"wall")
        walls.add(wall)

def stage5(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 5
    global s12
    s12 = Guns(BLACK, 20, 50, 640, 380, "s12", s12Pic)
    gunList.add(s12)

    barrier1 = Wall(BLACK, 1400, 30, 0, 738, 100000000, "barrier")
    walls.add(barrier1)
    barrier2a = Wall(BLACK, 30, 285, 0, 75, 100000000, "barrier")
    walls.add(barrier2a)
    barrier2b = Wall(BLACK, 30, 770, 0, 450, 100000000, "barrier")
    walls.add(barrier2b)
    barrier4a = Wall(BLACK, 30, 285, 1338, 75, 100000000, "barrier")
    walls.add(barrier4a)
    barrier4b = Wall(BLACK, 30, 770, 1338, 450, 100000000, "barrier")
    walls.add(barrier4b)
    barrier5 = Wall(BLACK, 1400, 30, 0, 75, 100000000, "barrier")
    walls.add(barrier5)

    stance1 = Wall(BLACK, 15, 125, 200, 350, 100000000, "barrier")
    walls.add(stance1)

    stance2 = Wall(BLACK, 15, 125, 400, 200, 100000000, "barrier")
    walls.add(stance2)

    stance3 = Wall(BLACK, 15, 125, 400, 500, 100000000, "barrier")
    walls.add(stance3)

    stance4 = Wall(BLACK, 15, 125, 600, 350, 100000000, "barrier")
    walls.add(stance4)

    stance5 = Wall(BLACK, 15, 125, 800, 200, 100000000, "barrier")
    walls.add(stance5)

    stance6 = Wall(BLACK, 15, 125, 800, 500, 100000000, "barrier")
    walls.add(stance6)

    for i in range(15):
        ghost = Enemies(900, 100 + (i * 42), "rusher", 1, ghostPic, None)
        ghostList.add(ghost)
        enemyList.add(ghost)

    shooter1 = Enemies(1100, 200, "shooter", 1, shooterLeftPic, "left")
    shooter2 = Enemies(1100, 500, "shooter", 1, shooterLeftPic, "left")
    shooterList.add(shooter2)
    enemyList.add(shooter2)
    shooterList.add(shooter1)
    enemyList.add(shooter1)

    sniperEnemy = Enemies(1135, 390, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy)
    enemyList.add(sniperEnemy)

    for i in range(6):
        wall = Wall(BLACK, 20, 20, 1065, 105 + (i * 20), 100, "wall")
        walls.add(wall)
    for i in range(12):
        wall = Wall(BLACK, 20, 20, 1065, 282 + (i * 20), 100, "wall")
        walls.add(wall)
    for i in range(7):
        wall = Wall(BLACK, 20, 20, 1065, 598 + (i * 20), 100, "wall")
        walls.add(wall)

    crate1 = Wall(BLACK, 90, 90, 640, 380, 120, "crate")
    walls.add(crate1)


def stage6(player):
    barrier1 = Wall(BLACK, 1400, 30, 0, 738, 100000000, "barrier")
    walls.add(barrier1)
    barrier2a = Wall(BLACK, 30, 285, 0, 75, 100000000, "barrier")
    walls.add(barrier2a)
    barrier2b = Wall(BLACK, 30, 770, 0, 450, 100000000, "barrier")
    walls.add(barrier2b)
    if player.level >= 15:# only removes barrier if player level exceeds 10, allowing for advancment to the final boss
        barrier4a = Wall(BLACK, 30, 285, 1338, 75, 100000000, "barrier")
        walls.add(barrier4a)
        barrier4b = Wall(BLACK, 30, 770, 1338, 450, 100000000, "barrier")
        walls.add(barrier4b)
    else:
        barrier4a = Wall(BLACK, 30, 285, 1338, 75, 100000000, "barrier")
        walls.add(barrier4a)
        barrier4b = Wall(BLACK, 30, 770, 1338, 450, 100000000, "barrier")
        walls.add(barrier4b)
        levelWall = Wall(RED,30,90,1302,360,1000000000,"barrier")
        walls.add(levelWall)
    stance1 = Wall(BLACK, 275, 20, 25, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 410, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 515, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 640, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 750, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 865, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 980, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 1100, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 1225, 220, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 275, 20, 25, 600, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 410, 610, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 515, 610, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 640, 610, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 750, 610, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 865, 610, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 980, 610, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 1100, 610, 100000000, "barrier")
    walls.add(stance1)
    stance1 = Wall(BLACK, 40, 10, 1225, 610, 100000000, "barrier")
    walls.add(stance1)

    global rpg
    rpg = Guns(BLACK,30,68,100,125,"rpg",rpgPic)
    gunList.add(rpg)
    crate1 = Wall(BLACK, 90, 90, 100, 110, 120, "crate2")
    walls.add(crate1)

    global grenadeLauncher
    grenadeLauncher = Guns(BLACK,30,68,100,650,"grenade launcher",grenadeLauncherPic)
    gunList.add(grenadeLauncher)
    crate1 = Wall(BLACK, 90, 90, 100, 630, 120, "crate2")
    walls.add(crate1)

   
    for i in range (5):
        shooter2 = Enemies(330 + ( i * 230), 100 , "shooter", 1, shooterDownPic, "down")
        shooterList.add(shooter2)
        enemyList.add(shooter2)
    for i in range (4):
        sniperEnemy = Enemies(450 +( i * 230), 170, "sniperEnemy", 1, sniperEnemyPic, None)
        sniperEnemyList.add(sniperEnemy)
        enemyList.add(sniperEnemy)
    for i in range (5):
        shooter2 = Enemies(330 + ( i * 230), 590 , "shooter", 1, shooterUpPic, "up")
        shooterList.add(shooter2)
        enemyList.add(shooter2)
    for i in range (4):
        sniperEnemy = Enemies(450 +( i * 230), 615, "sniperEnemy", 1, sniperEnemyPic, None)
        sniperEnemyList.add(sniperEnemy)
        enemyList.add(sniperEnemy)
    barrier5 = Wall(BLACK, 1400, 30, 0, 75, 100000000, "barrier")
    walls.add(barrier5)
    ### length of piece, height of piece, x, y
    for i in range (5):
        barrier6 = Wall(BLACK, 240, 15, 1+i**5, 75, 100000000, "barrier")
        walls.add(barrier6)

def stage7(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 7
    barrier1 = Wall(BLACK, 1400, 30, 0, 738, 100000000, "barrier")
    walls.add(barrier1)
    barrier2a = Wall(BLACK, 30, 770, 0, 75, 100000000, "barrier")
    walls.add(barrier2a)
    barrier4a = Wall(BLACK, 30, 770, 1338, 75, 100000000, "barrier")
    walls.add(barrier4a)
    barrier5 = Wall(BLACK, 1400, 30, 0, 75, 100000000, "barrier")
    walls.add(barrier5)

    bottom = Boss("bottom",1100,350)
    bottom.add(bottomList)

def stage8(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 8
    barrier1 = Wall(BLACK,600,30,0,738,100000000,"barrier")
    walls.add(barrier1)
    barrier1b = Wall(BLACK,800,30,700,738,1000000,"barrier")
    walls.add(barrier1b)
    barrier3 = Wall(BLACK,30,770,0,75,100000000,"barrier")
    walls.add(barrier3)
    barrier4 = Wall(BLACK,30,770,1338,75,100000000,"barrier")
    walls.add(barrier4)
    barrier5 = Wall(BLACK,600,30,0,75,100000000,"barrier")
    walls.add(barrier5)
    barrier5b = Wall(BLACK,800,30,700,75,1000000,"barrier")
    walls.add(barrier5b)

    for i in range(15):
        wall = Wall(BLACK,20,30,580,105 + (i*10),100,"wall")
        walls.add(wall)
    for i in range(15):
        wall = Wall(BLACK,20,30,700,105 + (i*10),100,"wall")
        walls.add(wall)
    if lastStage == 1:
        for x in range(10):
            for y in range(3):
                ghost = Enemies(387 + 50 * x,530 + 50 * y,"rusher",1,ghostPic,None)
                ghostList.add(ghost)
                enemyList.add(ghost)
    for i in range(2):
        block = Wall(BLACK,500,20,387,510 + 150 * i,10000000,"barrier")
        walls.add(block)

    zone = Zone(RED,100,100,600,550)
    zoneList.add(zone)
    

    global cz75
    cz75 = Guns(BLACK,30,32,747,133,"cz75",cz75Pic)
    if gunName is not "cz75":
        gunList.add(cz75)
    
    crate1 = Wall(BLACK, 90, 90, 747, 133, 120, "crate")
    walls.add(crate1)

    global awp
    awp = Guns(BLACK,20,57,480,130,"awp",awpPic)
    gunList.add(awp)
    crate1 = Wall(BLACK, 90, 90, 477, 133, 120, "crate")
    walls.add(crate1)

    for i in range(2):
        block = Wall(BLACK,200,20,380 + 340 * i,255,10000000,"barrier")
        walls.add(block)

    for i in range(5):
        shooter = Enemies(64 + 65 * i,600,"shooter",1,shooterUpPic,"up")
        shooterList.add(shooter)
        enemyList.add(shooter)
    for i in range(5):
        shooter = Enemies(1000 + 65 * i,600,"shooter",1,shooterUpPic,"up")
        shooterList.add(shooter)
        enemyList.add(shooter)
    
        
    
    

def stage9(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 9
    barrier1 = Wall(BLACK,600,30,0,738,100000000,"barrier")
    walls.add(barrier1)
    barrier1b = Wall(BLACK,800,30,700,738,1000000,"barrier")
    walls.add(barrier1b)
    barrier3 = Wall(BLACK,30,770,0,75,100000000,"barrier")
    walls.add(barrier3)
    barrier4 = Wall(BLACK,30,770,1338,75,100000000,"barrier")
    walls.add(barrier4)
    barrier5 = Wall(BLACK,600,30,0,75,100000000,"barrier")
    walls.add(barrier5)
    barrier5b = Wall(BLACK,800,30,700,75,1000000,"barrier")
    walls.add(barrier5b)


    for i in range(15):
        wall = Wall(BLACK,20,30,580,105 + (i*10),1000000,"barrier")
        walls.add(wall)
        
    block = Wall(BLACK,300,20,723,255,1000000,"barrier")
    walls.add(block)

    block = Wall(BLACK,150,20,580,345,1000000,"barrier")
    walls.add(block)

    block = Wall(BLACK,20,90,1023,255,100000,"barrier")
    walls.add(block)

    for i in range(5):
        wall = Wall(BLACK,20,20,1023,345 + 10 * i,100,"wall")
        walls.add(wall)

    block = Wall(BLACK,20,90,1023,400,100000,"barrier")
    walls.add(block)

    for i in range(4):
        shooter = Enemies(1020 + 75 * i,600,"shooter",1,shooterUpPic,"up")
        shooterList.add(shooter)
        enemyList.add(shooter)

    for i in range(5):
        ghost = Enemies(750 + 50 * i,345,"rusher",1,ghostPic,None)
        ghostList.add(ghost)
        enemyList.add(ghost)


    for x in range(10):
            for y in range(3):
                ghost = Enemies(75 + 50 * x,575 + 50 * y,"rusher",1,ghostPic,None)
                ghostList.add(ghost)
                enemyList.add(ghost)

    if lastStage == 8:
        sniperEnemy = Enemies(650,600,"sniperEnemy",1,sniperEnemyPic,None)
        sniperEnemyList.add(sniperEnemy)
        enemyList.add(sniperEnemy)

    

    for i in range(56):
        wall = Wall(BLACK,20,20,30 + 10 * i,255,100,"wall")
        walls.add(wall)

    for i in range(4):
        crate1 = Wall(BLACK, 90, 90, 90 + 120 * i, 170, 120, "crate")
        walls.add(crate1)


    global mp40    
    mp40 = Guns(BLACK,20,57,120,170,"mp40",mp40Pic)
    gunList.add(mp40)

    global m1927
    m1927 = Guns(BLACK,20,57,210,170,"m1927",m1927Pic)
    gunList.add(m1927)

    global ak47
    ak47 = Guns(BLACK,20,57,330,170,"ak47",ak47Pic)
    gunList.add(ak47)

    global revolver
    revolver = Guns(BLACK,20,57,450,170,"revolver",revolverPic)
    gunList.add(revolver)
 

    

def stage10(player):#setting of all the barriers, walls, eneimes, crates, objectives and guns of stage 10
    clearStage()
    barrier1 = Wall(BLACK,1400,30,0,738,100000000,"barrier")
    walls.add(barrier1)
    barrier3 = Wall(BLACK,30,770,0,75,100000000,"barrier")
    walls.add(barrier3)
    barrier4 = Wall(BLACK,30,770,1338,75,100000000,"barrier")
    walls.add(barrier4)
    barrier5 = Wall(BLACK,600,30,0,75,100000000,"barrier")
    walls.add(barrier5)
    barrier5b = Wall(BLACK,800,30,700,75,1000000,"barrier")
    walls.add(barrier5b)


    global grenadeLauncher
    grenadeLauncher = Guns(BLACK,30,68,646,690,"grenade launcher",grenadeLauncherPic)
    gunList.add(grenadeLauncher)
    
    block = Wall(BLACK,200,20,555,232,10000000000,"barrier")
    walls.add(block)

    crate1 = Wall(BLACK, 90, 90, 800, 400, 120, "crate")
    walls.add(crate1)
    global railgun
    railgun = Guns(BLACK,20,57,800,400,"railgun",railgunPic)
    gunList.add(railgun)


    if "pump" not in bossKilledList:
        pump = Boss("pump",550,600)
        pumpList.add(pump)


    sniperEnemy1 = Enemies(1250,650, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy1)
    enemyList.add(sniperEnemy1)
    
    sniperEnemy2 = Enemies(65,650, "sniperEnemy", 1, sniperEnemyPic, None)
    sniperEnemyList.add(sniperEnemy2)
    enemyList.add(sniperEnemy2)
    
    
    
    

def devRoom(player):# a special room containing all of the guns in the game. only available with god mode on
    barrier1 = Wall(BLACK,600,30,0,738,100000000,"barrier")
    walls.add(barrier1)
    barrier1b = Wall(BLACK,800,30,700,738,1000000,"barrier")
    walls.add(barrier1b)
    barrier3 = Wall(BLACK,30,770,0,75,100000000,"barrier")
    walls.add(barrier3)
    barrier4 = Wall(BLACK,30,770,1338,75,100000000,"barrier")
    walls.add(barrier4)
    barrier5 = Wall(BLACK,1400,30,0,75,100000000,"barrier")
    walls.add(barrier5)

    Enemies((random.randrange(1,500)),100,"rusher",1,ghostPic,None)

    global awp
    awp = Guns(BLACK,20,57,700,400,"awp",awpPic)
    gunList.add(awp)

    global carbine
    carbine = Guns(BLACK,20,57,600,400,"carbine",carbinePic)
    gunList.add(carbine)

    global railgun
    railgun = Guns(BLACK,20,57,800,400,"railgun",railgunPic)
    gunList.add(railgun)

    global ak47
    ak47 = Guns(BLACK,20,57,500,400,"ak47",ak47Pic)
    gunList.add(ak47)

    global revolver
    revolver = Guns(BLACK,30,61,500,200,"revolver",revolverPic)
    gunList.add(revolver)

    global raygun
    raygun = Guns(BLACK,30,61,600,200,"raygun",raygunPic)
    gunList.add(raygun)

    global mp40
    mp40 = Guns(BLACK,20,57,700,200,"mp40",mp40Pic)
    gunList.add(mp40)

    global m1927
    m1927 = Guns(BLACK,20,57,800,200,"m1927",m1927Pic)
    gunList.add(m1927)

    global s12
    s12 = Guns(BLACK,20,57,800,600,"s12",s12Pic)
    gunList.add(s12)

    global shotgun
    shotgun = Guns(BLACK,20,57,700,600,"shotgun",shotgunPic)
    gunList.add(shotgun)

    global pistol
    pistol = Guns(BLACK,20,57,600,600,"pistol",pistolPic)
    gunList.add(pistol)

    global ump
    ump = Guns(BLACK,20,57,500,600,"ump",umpPic)
    gunList.add(ump)

    global cz75
    cz75 = Guns(BLACK,30,32,200,600,"cz75",cz75Pic)
    gunList.add(cz75)

    global rampart17
    rampart17 = Guns(BLACK,30,79,200,400,"rampart-17",rampart17Pic)
    gunList.add(rampart17)

    global rpg
    rpg = Guns(BLACK,30,68,200,200,"rpg",rpgPic)
    gunList.add(rpg)

    global grenadeLauncher
    grenadeLauncher = Guns(BLACK,30,68,350,200,"grenade launcher",grenadeLauncherPic)
    gunList.add(grenadeLauncher)


def deathScreen(display,player):#functions that makes the display switch from the game screen to the after death screen
    if player.dead:
        display = "death"
    else:
        display = display
    
    return display
    
    

# Boss functions

#Loop until the close button is clicked
done = False

#Used to manage the framerate
clock = pygame.time.Clock()

player = Player(BEIGE,40,40,400,420)
playerList.add(player)
leftArm = LeftArm(player)
allSpriteList.add(player)
allSpriteList.add(leftArm)
Hud = HUD(GREY)



#_______Main program loop__________

while not done:
    #_____Main event loop_______

    for event in pygame.event.get(): #The user did something
        if event.type == pygame.QUIT:#If the user attempts to close the window
            done = True #Telling us to exit the loop and therefore the window
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:# "the if current stage is not 7" is meant for the reversal of movemnet in stage 7 
                if currentStage is not 7:
                    player.changeVelocity(0,-4)
                if currentStage is 7 and player.stopTimer >= 201:# the player.stopTimer prevents the player from moving for a set period of time in the final stage's cutscene
                    player.changeVelocity(0,4)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:#if s or down arrow is pressed
                if currentStage is not 7:
                    player.changeVelocity(0,4)#regular down movement
                if currentStage is 7 and player.stopTimer >= 201:
                    player.changeVelocity(0,-4)#stage 7 down movement
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:#if a or left arrow is pressed
                if currentStage is not 7:
                    player.changeVelocity(-4,0)#regular left movement
                if currentStage is 7 and player.stopTimer >= 201:
                     player.changeVelocity(4,0)#stage 7 down movement
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:#if d or right arrow is pressed
                if currentStage is not 7:
                    player.changeVelocity(4,0)#regular right movement
                if currentStage is 7 and player.stopTimer >= 201:
                    player.changeVelocity(-4,0)#stage 7 right movement
            if event.key == pygame.K_LSHIFT:
                #code infrastructure in place for sprintingg, which would grant player temporary speed but would have a cool down.
                #When we finish this game in the summer, we will implement this
                isSprinting = True
            if event.key == pygame.K_e:#if e is pressed
                player.switch = True#cycle between fists and weapon
                gunPickList = pygame.sprite.spritecollide(player,gunList,False)
                for gun in gunPickList:
                    reloading = False
                    reloadDelay = 0
                    #making gun that you are holding into a variable gunName
                    if gun.name == "shotgun":
                        gunName = "shotgun"
                    if gun.name == "s12":
                        gunName = "s12"
                    if gun.name == "mp40":
                        gunName = "mp40"
                    if gun.name == "m1927":
                        gunName = "m1927"
                    if gun.name == "raygun":
                        gunName = "raygun"
                        raygun.bulletTime = 30#delay in between shots
                    if gun.name == "railgun":
                        gunName = "railgun"
                    if gun.name == "pistol":
                        gunName = "pistol"
                    if gun.name == "ump":
                        gunName = "ump"
                    if gun.name == "carbine":
                        gunName = "carbine"
                        carbine.bulletTime = 30#delay in between shots
                    if gun.name == "awp":
                        gunName = "awp"
                    if gun.name == "ak47":
                        gunName = "ak47"
                    if gun.name == "revolver":
                        gunName = "revolver"
                        revolver.bulletTime = 180#delay in between shots
                    if gun.name == "cz75":
                        gunName = "cz75"
                    if gun.name == "rampart-17":
                        gunName = "rampart-17"
                    if gun.name == "rpg":
                        gunName = "rpg"
                    if gun.name == "grenade launcher":
                        gunName = "grenade launcher"
                    gunList.remove(gun)
                    isArmed = True
                    
            if event.key == pygame.K_r and player.switch == False:#is r is pressed
                reload = True#gun starts to reload
                
            if event.key == pygame.K_q:#is q is pressed
                if isArmed:#if you already have a gun
                    if player.switch == False:
                        player.switch = True
                    else:
                        player.switch = False
            if event.key == pygame.K_i:# this alters the players sprite once "I" is pressed via a series of corresponding false and true statments
                if base:
                    orange = True
                    base = False
                    chrome = False
                    firefox1 = False
                    firefox2 = False
                    internetExplorer = False
                    EA = False
                elif orange:
                    chrome = True
                    base = False
                    orange = False
                    firefox1 = False
                    firefox2 = False
                    internetExplorer = False
                    EA = False
                elif chrome:
                    base = False
                    orange = False
                    chrome = False
                    firefox1 = True
                    firefox2 = False
                    internetExplorer = False
                    EA = False
                elif firefox1:
                    base = False
                    orange = False
                    chrome = False
                    firefox1 = False
                    firefox2 = True
                    internetExplorer = False
                    EA = False
                elif firefox2:
                    base = False
                    orange = False
                    chrome = False
                    firefox1 = False
                    firefox2 = False
                    internetExplorer = True
                    EA = False
                elif internetExplorer:
                    base = False
                    orange = False
                    chrome = False
                    firefox1 = False
                    firefox2 = False
                    internetExplorer = False
                    EA = True
                elif EA:
                    base = True
                    orange = False
                    chrome = False
                    firefox1 = False
                    firefox2 = False
                    internetExplorer = False
                    EA = False
            if event.key == pygame.K_g and pistol.suppressed == False:# if " g " is pressed, the tradtional sprite is switched with one containing the supressor and supressor parameters true
                #only a feautre with the starting glock pistol, decreases damage, but increases stealth to enemies making them less aler to shots
                #blits a new image and uses a new supressed sound
                if gunName == "pistol":
                    pistol.suppressed = True
                    
            elif event.key == pygame.K_g and pistol.suppressed == True:#if you have the supressor on and press g again it will switch back
                if gunName == "pistol":
                    pistol.suppressed = False
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:#if you press escape or p
                if display == "game":
                    display = "pause"#makes screen display pause menu
            
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:# when a button is released the correspondong velocity is canceled out, resulting in a stationary sprite
                if currentStage is not 7:
                    player.changeVelocity(0,4)#regular up movement
                if currentStage is 7 and player.stopTimer >= 201: 
                    player.changeVelocity(0,-4)#stage 7 up movement
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if currentStage is not 7:
                    player.changeVelocity(0,-4)#regular down movement
                if currentStage is 7 and player.stopTimer >= 201:
                    player.changeVelocity(0,4)#stage 7 down movement
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if currentStage is not 7:
                    player.changeVelocity(4,0)#regular left movement
                if currentStage is 7 and player.stopTimer >= 201:
                    player.changeVelocity(-4,0)#stage 7 left movement
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if currentStage is not 7:
                    player.changeVelocity(-4,0)#regular right movement
                if currentStage is 7 and player.stopTimer >= 201:
                    player.changeVelocity(4,0)#stage 7 right movement
                
            if event.key == pygame.K_r:
                reload = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and display == "game":
                #this segment of code is about shooting the guns and the sound they make. it will make sure the ammo of the gun is above 0 and that the player doesnt have his fists out.
                #if the gun has a range limiter or a bulletTime, it will be used in if statments to implement the delays. it will also make and add the bullet to a k=list
                if gunName == "shotgun":
                    if shotgun.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        if shotgun.bulletTime >= 35:
                            shotgun.bulletTime = 0
                            startShot = False
                            bullet = Bullet(BLACK,10,10,gunName,shotgun.rect.x,shotgun.rect.y)
                            shotgun.ammo -= 1
                            bullet.trajectory(mx,my)
                            bullet.rangeLimit = True
                            bullets.add(bullet)
                            sound = pygame.mixer.Sound("Sounds/R870.wav")
                            channel = sound.play()
                if gunName == "s12":
                    if s12.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        if s12.bulletTime >= 15:
                            s12.bulletTime = 0
                            startShot = False
                            bullet = Bullet(BLACK,10,10,gunName,s12.rect.x,s12.rect.y)
                            s12.ammo -= 1
                            bullet.trajectory(mx,my)
                            bullet.rangeLimit = True
                            bullets.add(bullet)
                            sound = pygame.mixer.Sound("Sounds/S12.wav")
                            channel = sound.play()
                if gunName == "pistol":
                    if pistol.ammo > 0 and isArmed and not player.switch:
                        bullet = Bullet((104,102,102),5,5,gunName,pistol.rect.x,pistol.rect.y)
                        pistol.ammo -= 1
                        bullet.trajectory(mx,my)
                        bullets.add(bullet)
                        if pistol.suppressed == True:
                            sound = pygame.mixer.Sound("Sounds/S_M1911_1.wav")
                            channel = sound.play()
                        else:
                            sound = pygame.mixer.Sound("Sounds/M1911.wav")
                            channel = sound.play()
                if gunName == "carbine":
                    if carbine.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        if carbine.bulletTime >= 30:
                            carbine.bulletTime = 0
                            startShot = False
                            bullet = Bullet(BLACK,9,9,gunName,carbine.rect.x,carbine.rect.y)
                            carbine.ammo -= 1
                            bullet.trajectory(mx,my)
                            bullets.add(bullet)
                            sound = pygame.mixer.Sound("Sounds/Carbine.wav")
                            channel = sound.play()
                if gunName == "raygun":
                    if raygun.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        if raygun.bulletTime >= 30:
                            raygun.bulletTime = 0
                            startShot = False
                            bullet = Bullet(GREEN,9,9,gunName,raygun.rect.x,raygun.rect.y)
                            raygun.ammo -= 1
                            bullet.trajectory(mx,my)
                            bullets.add(bullet)
                            sound = pygame.mixer.Sound("Sounds/RayGun.wav")
                            channel = sound.play()
                if gunName == "awp":
                    if awp.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        if awp.bulletTime >= 50:
                            awp.bulletTime = 0
                            startShot = False
                            bullet = Bullet(BLACK,10,10,gunName,awp.rect.x,awp.rect.y)
                            awp.ammo -= 1
                            bullet.trajectory(mx,my)
                            bullets.add(bullet)
                            sound = pygame.mixer.Sound("Sounds/AWP.wav")
                            channel = sound.play()
                if gunName == "revolver":
                    if revolver.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        if revolver.bulletTime >= 20:
                            revolver.bulletTime = 0
                            startShot = False
                            bullet = Bullet(BLACK,7,7,gunName,revolver.rect.x,revolver.rect.y)
                            revolver.ammo -= 1
                            bullet.trajectory(mx,my)
                            bullets.add(bullet)
                            sound = pygame.mixer.Sound("Sounds/Revolver.wav")
                            channel = sound.play()
                if gunName == "rampart-17":
                    if rampart17.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        if rampart17.bulletTime >= 35:
                            rampart17.bulletTime = 0
                            startShot = False
                            bullet = Bullet(BLACK,8,8,gunName,rampart17.rect.x,rampart17.rect.y)
                            rampart17.ammo -= 1
                            bullet.trajectory(mx,my)
                            bullets.add(bullet)
                            sound = pygame.mixer.Sound("Sounds/Rampart.wav")
                            channel = sound.play()
                if gunName == "rpg":
                    if rpg.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        rpg.bulletTime = 0
                        bullet = Bullet((190,100,100),10,10,gunName,rpg.rect.x,rpg.rect.y)
                        rpg.ammo -= 1
                        bullet.trajectory(mx,my)
                        bullet.rangeLimit = True
                        bullets.add(bullet)
                        sound = pygame.mixer.Sound("Sounds/RPG.wav")
                        channel = sound.play()
                if gunName == "grenade launcher":
                    if grenadeLauncher.ammo > 0 and isArmed and not player.switch:
                        startShot = True
                        if grenadeLauncher.bulletTime >= 40:
                            startShot = False
                            grenadeLauncher.bulletTime = 0
                            bullet = Bullet((190,100,100),10,10,gunName,grenadeLauncher.rect.x,grenadeLauncher.rect.y)
                            grenadeLauncher.ammo -= 1
                            bullet.trajectory(mx,my)
                            bullet.rangeLimit = True
                            bullets.add(bullet)
                            sound = pygame.mixer.Sound("Sounds/GL.wav")
                            channel = sound.play()
                        
                            
                if player.switch or not isArmed:
                    breakWall(walls,leftArm,50)#mechanic for breaking walls with your hands
 
# Mouse Infromation
    mx,my = pygame.mouse.get_pos()
    mouseDown = pygame.mouse.get_pressed()
    #_______Game logic goes here________
    '''
    this deals with the different screens and the navigation between said screens as well as the selection of certain options, such as god mode or fps display.
    '''
    display = deathScreen(display,player)#calling death screen function
    if display == "start":#start screen
        #in this next segment of code, it shows the various things for all the six screens we have, our start screen, options, instrictions, pause, death, and select
        #we make our mous visible and stop using the target on the screen. whenever we have a certain display, we blit the picture onto the screen, and draw out
        #certain rects that can be clicked on the screen. for example, on the start screen, there is a play, options, and instrucions rect, which must be made
        #with new coordinates to match the picture. everytime you hover over them, it makes a noise, and when you click itll bring you to another display or
        #in the case of pressing resume or exit it will bring you back in game or quit the game for you. on a few screens there is a back rect in the top left
        #which is made as well
        pygame.mouse.set_visible(True)#mouse can be seen
        screen.blit(startPage,[0,0])#blits start screen picture to screen
        #defines clickable rects on the screen
        playRect = pygame.Rect(537,410,82,38)
        optionsRect = pygame.Rect(684,411,131,40)
        instructRect = pygame.Rect(558,495,198,42)
        if playRect.collidepoint(mx,my):#if you are on the playRect
            pygame.draw.rect(screen,BLACK,playRect,3)
            sound = pygame.mixer.Sound("Sounds/hover.wav")#plays sound triggered on hovering over option
            channel = sound.play()
            if mouseDown[0]:#if you click
                display = "select"#change display 
        if optionsRect.collidepoint(mx,my):
            start = True#came from start screen
            pygame.draw.rect(screen,BLACK,optionsRect,3)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0]:#if you click 
                display = "options"
        if instructRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,instructRect,3)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0]:#if you click 
                display = "instructions"

                
    if display == "pause":
        pygame.mouse.set_visible(True)
        screenCap = screen.copy()#screenshot
        screen.blit(screenCap,[0,0])
        screen.blit(pauseScreen,[0,0])
        resumeRect = pygame.Rect(516,255,323,67)
        optionsRect = pygame.Rect(516,375,323,67)
        saveRect = pygame.Rect(516,488,325,67)
        if resumeRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,resumeRect,4)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0]:
                display = "game"
        if optionsRect.collidepoint(mx,my):
            start = False#if you are clicking options from the pause screen
            pygame.draw.rect(screen,BLACK,optionsRect,4)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0]:
                display = "options"
        if saveRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,saveRect,4)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0]:
                screen.fill(BLACK)
                done = True
                saveGame()

                
    if display == "instructions": # The instructions screen has basic info about the game
        screen.blit(instructionsPage,[0,0])
        backRect = pygame.Rect(25,34,50,30)
        pygame.draw.rect(screen,RED,backRect)
        backText = point20Font.render("Back",True,BLACK)
        screen.blit(backText,[27,38])
        if backRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,backRect,1)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0]:
                display = "start"


                
    if display == "options":
        screen.blit(optionsScreen,[0,0])
        backRect = pygame.Rect(25,34,50,30)
        pygame.draw.rect(screen,RED,backRect)
        backText = point20Font.render("Back",True,BLACK)
        screen.blit(backText,[27,38])
        godRectOn = pygame.Rect(677,339,20,20)
        godRectOff = pygame.Rect(727,339,20,20)
        pygame.draw.rect(screen,BLACK,godRectOn,4)
        pygame.draw.rect(screen,BLACK,godRectOff,4)
        if godRectOn.collidepoint(mx,my):
            pygame.draw.rect(screen,RED,godRectOn,4)
            if mouseDown[0] and not player.godMode:#if you click and you arent god mode
                pygame.draw.rect(screen,RED,godRectOn,4)
                sound = pygame.mixer.Sound("Sounds/hover.wav")
                channel = sound.play()
                player.godMode = True
        if godRectOff.collidepoint(mx,my):
            pygame.draw.rect(screen,RED,godRectOff,4)
            if mouseDown[0] and player.godMode:#if you click and you are god mode
                pygame.draw.rect(screen,RED,godRectOff,4)
                sound = pygame.mixer.Sound("Sounds/hover.wav")
                channel = sound.play()
                player.godMode = False
                player.level = 1
        if player.godMode:#checkmarks if you're god mode or not
            screen.blit(check,[677,325])
        if not player.godMode:
            screen.blit(check,[727,325])
        
        if backRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,backRect,1)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0] and start:#if you came from start screen
                display = "start"
            elif mouseDown[0] and start == False:#if you came from pause screen
                display = "pause"

        fpsOn = pygame.Rect(677,409,20,20)
        fpsOff = pygame.Rect(727,409,20,20)
        pygame.draw.rect(screen,BLACK,fpsOn,4)
        pygame.draw.rect(screen,BLACK,fpsOff,4)

        if fpsOn.collidepoint(mx,my):
            pygame.draw.rect(screen,RED,fpsOn,4)
            if mouseDown[0] and not Hud.fpsDisplay:#if fps display is off and you click
                pygame.draw.rect(screen,RED,fpsOn,4)
                sound = pygame.mixer.Sound("Sounds/hover.wav")
                channel = sound.play()
                Hud.fpsDisplay = True
                
        if fpsOff.collidepoint(mx,my):
            pygame.draw.rect(screen,RED,fpsOff,4)
            if mouseDown[0] and Hud.fpsDisplay:#if fps display is oN and you click
                pygame.draw.rect(screen,RED,fpsOff,4)
                sound = pygame.mixer.Sound("Sounds/hover.wav")
                channel = sound.play()
                Hud.fpsDisplay = False 

        if Hud.fpsDisplay:#checkmarks if you have fps display on or not
            screen.blit(check,[677,399,20,20])
        if not Hud.fpsDisplay:
            screen.blit(check,[727,399,20,20])

        #text to show if you have it on or off on top of both options
        offText = point20Font.render("Off",True,BLACK)
        screen.blit(offText,[727,310])

        onText = point20Font.render("On",True,BLACK)
        screen.blit(onText,[677,310])

        
        
    if display == "death":
        if player.screenTimer <= 249:
            i = player.screenTimer
            screen.fill((i,i,i))
        player.screenTimer += 1
        if player.screenTimer >= 250:
            screen.blit(deathAlert,[0,0])
            pygame.mouse.set_visible(True)
            respawnRect = pygame.Rect(535,426,217,39)
            exitRect = pygame.Rect(13,17,175,44)
            if respawnRect.collidepoint(mx,my):
                pygame.draw.rect(screen,BLACK,respawnRect,4)
                sound = pygame.mixer.Sound("Sounds/hover.wav")
                channel = sound.play()
                if mouseDown[0]:
                    clearStage()
                    screen.fill(WHITE)
                    player.health = 300
                    #currentStage = changeStage(player,currentStage,lastStage)
                    oneTimeDraw = True
                    player.dead = False
                    display = "game"
                    player.screenTimer = 0
                    pygame.mixer.music.load("Sounds/startScreen.wav")
                    pygame.mixer.music.play(15)
                    
            if exitRect.collidepoint(mx,my):
                pygame.draw.rect(screen,BLACK,exitRect,4)
                sound = pygame.mixer.Sound("Sounds/hover.wav")
                channel = sound.play()
                if mouseDown[0]:
                    screen.fill(BLACK)
                    done = True
            
            saveRect = pygame.Rect(535,510,220,41)
            if saveRect.collidepoint(mx,my):
                pygame.draw.rect(screen,BLACK,saveRect,4)
                sound = pygame.mixer.Sound("Sounds/hover.wav")
                channel = sound.play()
                if mouseDown[0]:
                    screen.fill(BLACK)
                    done = True
                    saveGame()#will save and end the game
    
        
                
    if display == "select": # The screen allows the player to load an old game or start a new one
        screen.blit(selectScreen,[0,0])
        loadGameRect = pygame.Rect(525,265,290,50)
        newGameRect = pygame.Rect(525,355,290,50)
        exitGameRect = pygame.Rect(525,569,290,50)
        backRect = pygame.Rect(25,34,50,30)
        pygame.draw.rect(screen,RED,backRect)
        backText = point20Font.render("Back",True,BLACK)
        screen.blit(backText,[27,38])
        if backRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,backRect,1)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0]:
                display = "start"
                
        if loadGameRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,loadGameRect,3)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if loadGameRect.collidepoint(mx,my):
                pygame.draw.rect(screen,BLACK,loadGameRect,3)
                # This block takes information from the txt file to change the weapon
                # the player is using, the stage the player is on, and the players level
                if mouseDown[0]:
                    if len(loadInfo) > 2:
                        isArmed = True
                        gunName = loadInfo[2]
                    currentStage = int(loadInfo[0])
                    if currentStage == 1: # If the player's save file has the level being on, the last stage will change so that the player spawns in the box
                        lastStage = currentStage
                    else:
                        lastStage = currentStage - 1
                    display = "game"
                        
                    oneTimeDraw = True
                    display = "game"
                
        if newGameRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,newGameRect,3)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            # This resets the player completely and spawns them in the box at the first level
            if mouseDown[0]:
                clearStage() # clears the stage in case anything spawned from the save file
                currentStage = 1
                lastStage = 1
                gunName = ""
                player.level = 1
                player.switch = True
                oneTimeDraw = True
                display = "game"
        if exitGameRect.collidepoint(mx,my):
            pygame.draw.rect(screen,BLACK,exitGameRect,5)
            sound = pygame.mixer.Sound("Sounds/hover.wav")
            channel = sound.play()
            if mouseDown[0]:
                done = True
                screen.fill(BLACK)
    if display == "game":
        saveRect = pygame.Rect(1170,30,40,40)
        if saveRect.collidepoint(mx,my) and mouseDown[0]:
            saveGame()
        if currentStage is not 7:
            player.move(walls)
        if currentStage is 7:
            if player.stopTimer >= 500:
                player.move(walls)
            
        currentObj = obj(currentStage,currentStage)
        player.takeDmg()
        player.death()
        pumpMines.update()
                
        if startShot:# this starts off the shoot timer in between shots, delaying the next bullet by a certain amount.
            if gunName == "awp":
                awp.bulletTime += 1
            if gunName == "shotgun":
                shotgun.bulletTime += 1
            if gunName == "s12":
                s12.bulletTime += 1
            if gunName == "carbine":
                carbine.bulletTime += 1
            if gunName == "raygun":
                raygun.bulletTime += 1
            if gunName == "revolver":
                revolver.bulletTime += 1
            if gunName == "rampart-17":
                rampart17.bulletTime += 1
            if gunName == "grenade launcher":
                grenadeLauncher.bulletTime += 1

        # Reloading the gun
        if reload:
            reloading = True
        if reloading:
            reloadDelay += 1
            if reloadDelay >= 301:
                reloadDelay = 0
                reloading = False
            
        if reloading:#if you have started the reload process by pressing r
            #this segment of code has many different gun names. the ammo for the gun must be under its max capacity. afte that, it will start to play the reload sound
            #it has a parameter set up so that the gun only reloads after it's reloadDelay which was defined before is fully met. when the reloadDelay has finished,
            #the gun will be reloaded and the reloadDelay will be set back to 0
            if gunName == "railgun" and railgun.ammo < 100:
                sound = pygame.mixer.Sound("Sounds/Minigun_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 250:
                    reloadGun(railgun)
                    reloadDelay = 0
                    reloading = False
            if gunName == "mp40" and mp40.ammo < 32:
                sound = pygame.mixer.Sound("Sounds/MP40_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 120:
                    reloadGun(mp40)
                    reloadDelay = 0
                    reloading = False
            if gunName == "m1927" and m1927.ammo < 50:
                sound = pygame.mixer.Sound("Sounds/M1927_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 180:
                    reloadGun(m1927)
                    reloadDelay = 0
                    reloading = False
            if gunName == "shotgun" and shotgun.ammo < 5:
                sound = pygame.mixer.Sound("Sounds/R870_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 100:
                    reloadGun(shotgun)
                    reloadDelay = 0
                    reloading = False
            if gunName == "s12" and s12.ammo < 8:
                sound = pygame.mixer.Sound("Sounds/S12_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 100:
                    reloadGun(s12)
                    reloadDelay = 0
                    reloading = False
            if gunName == "pistol" and pistol.ammo < 8:
                sound = pygame.mixer.Sound("Sounds/M1911_Reload.wav")
                channel = sound.play()
                if  reloadDelay >= 93:
                    reloadGun(pistol)
                    reloadDelay = 0
                    reloading = False
            if gunName == "ump" and ump.ammo < 24:
                sound = pygame.mixer.Sound("Sounds/UMP45_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 30:
                    reloadGun(ump)
                    reloadDelay = 0
                    reloading = False
            if gunName == "carbine" and carbine.ammo < 18:
                sound = pygame.mixer.Sound("Sounds/Carbine_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 90:
                    reloadGun(carbine)
                    reloadDelay = 0
                    reloading = False
            if gunName == "raygun" and raygun.ammo < 20:
                sound = pygame.mixer.Sound("Sounds/RayGun_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 90:
                    reloadDelay = 0
                    reloading = False
                    reloadGun(raygun)
            if gunName == "awp" and awp.ammo < 4:
                sound = pygame.mixer.Sound("Sounds/AWP_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 220:
                    reloadGun(awp)
                    reloadDelay = 0
                    reloading = False
            if gunName == "ak47" and ak47.ammo < 30:
                sound = pygame.mixer.Sound("Sounds/AK47_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 90:
                    reloadGun(ak47)
                    reloadDelay = 0
                    reloading = False
            if gunName == "revolver" and revolver.ammo < 6:
                sound = pygame.mixer.Sound("Sounds/Revolver_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 180:
                    reloadGun(revolver)
                    reloadDelay = 0
                    reloading = False
            if gunName == "cz75" and cz75.ammo < 6:
                sound = pygame.mixer.Sound("Sounds/Carbine_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 100:
                    reloadGun(cz75)
                    reloadDelay = 0
                    reloading = False
            if gunName == "rampart-17" and rampart17.ammo <= 15:
                sound = pygame.mixer.Sound("Sounds/Rampart_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 70:
                    reloadGun(rampart17)
                    reloadDelay = 0
                    reloading = False
            if gunName == "rpg" and rpg.ammo <= 0:
                sound = pygame.mixer.Sound("Sounds/RPG-7.wav")
                channel = sound.play()
                if reloadDelay >= 240:
                    reloadGun(rpg)
                    reloadDelay = 0
                    reloading = False
            if gunName == "grenade launcher" and grenadeLauncher.ammo <= 4:
                sound = pygame.mixer.Sound("Sounds/GL_Reload.wav")
                channel = sound.play()
                if reloadDelay >= 200:
                    reloadGun(grenadeLauncher)
                    reloadDelay = 0
                    reloading = False  
        
        screen.fill(WHITE) #Clears the screen to white. DO NOT put drawing code above this
        

        #_______Drawing code goes here______
        drawStage(currentStage)
        Hud.update(gunName,None,None,currentStage,clock,enemyList,currentObj)
        drawZone(zoneList)
        
        
        # Updating the player
        for gun in gunList:
            gun.drawGun()
            gun.rect.x = gun.x
            gun.rect.y = gun.y
        playerSprite(player.rect.x + 20,player.rect.y + 20,base,orange)
        
        
        if not isArmed:#if you have fists out
            leftArm.update(mouseDown)
            player.rightArm(mx,my)
            gunName = ""

        if not player.switch:#if you have a gun
            updateGun(isArmed,mouseDown)
        else:
            leftArm.update(mouseDown)
            player.rightArm(mx,my)


        #Drawing levels
        if currentStage != changeStage(player,currentStage,lastStage):
            lastStage = currentStage
            oneTimeDraw = True
            clearStage()
            currentStage = changeStage(player,currentStage,lastStage)

        #this segment of code is about all the different stages. it calls the stage function if you are there, so the stage will be drawm.
        #depending on where you are coming from, there will be a certain place where you will spawn. there is also a lastStage variable,
        #which is just for the x and y values of where you will spawn in.
        if currentStage == 1 and oneTimeDraw:
            stage1(player)
            if lastStage == 2:
                player.rect.x = 600
                player.rect.y = 100
            if lastStage == 5:
                player.rect.x = 1200
                player.rect.y = 400
            if lastStage == 0:
                player.rect.x = 400
                player.rect.y = 420
            if lastStage == 8:
                player.rect.x = 600
                player.rect.y = 650
            oneTimeDraw = False
        if currentStage == 2 and oneTimeDraw:
            stage2(player)
            if lastStage == 1:
                player.rect.x = 600
                player.rect.y = 650
            if lastStage == 3:
                player.rect.x = 500
                player.rect.y = 130
            oneTimeDraw = False
        if currentStage == 3 and oneTimeDraw:
            stage3(player)
            if lastStage == 2:
                player.rect.x = 600
                player.rect.y = 650
            if lastStage == 4:
                player.rect.x = 600
                player.rect.y = 130
            oneTimeDraw = False
        if currentStage == 4 and oneTimeDraw:
            stage4(player)
            player.rect.x = 600
            player.rect.y = 650
            oneTimeDraw = False
        if currentStage == 5 and oneTimeDraw:
            stage5(player)
            if lastStage == 1:
                player.rect.x = 75
                player.rect.y = 380
            if lastStage == 6:
                player.rect.x = 1200
                player.rect.y = 400
            oneTimeDraw = False
        if currentStage == 6 and oneTimeDraw:
            stage6(player)
            if lastStage == 5:
                player.rect.x = 75
                player.rect.y = 380
            oneTimeDraw = False
        if currentStage == 7 and oneTimeDraw:
            stage7(player)
            if lastStage == 6:
                player.rect.x = 75
                player.rect.y = 380
            oneTimeDraw = False 
        if currentStage == 8 and oneTimeDraw:
            stage8(player)
            if lastStage == 1:
                player.rect.x = 652
                player.rect.y = 125
            if lastStage == 9:
                player.rect.x = 600
                player.rect.y = 650
            oneTimeDraw = False
        if currentStage == 9 and oneTimeDraw:
            stage9(player)
            if lastStage == 8:
                player.rect.x = 652
                player.rect.y = 140
            if lastStage == 10:
                player.rect.x = 600
                player.rect.y = 650
            oneTimeDraw = False
        if currentStage == 10 and oneTimeDraw:
            stage10(player)
            if lastStage == 9:
                player.rect.x = 652
                player.rect.y = 145
            oneTimeDraw = False

        if currentStage == 7:
            player.stopTimer += 1
            if player.stopTimer >= 500:
                pass
            else:
            #this segment of code is for stage 7, the final boss fight. the players velocity is flipped, and there is a short cutscene where the player cant move
                player.changeVelocity(-player.vx,-player.vy)
                player.switch = True#cant pull out gun while vutscene is going
                #in this next segment, there will be words put onto the screen, based on timers. in this time, there is no movement
                if player.stopTimer >= 0 and player.stopTimer <= 150:
                    keyAlertText = largeFont.render("STOP",True,RED)
                    screen.blit(keyAlertText,[550,300])
                if player.stopTimer >= 50 and player.stopTimer <= 150:
                    keyAlertText = largeFont.render("Don't Move",True,RED)
                    screen.blit(keyAlertText,[550,350])
                if player.stopTimer >= 150 and player.stopTimer <= 250:
                    keyAlertText = largeFont.render("You will die",True,RED)
                    screen.blit(keyAlertText,[550,350])
                if player.stopTimer >= 250:
                    keyAlertText = largeFont.render("But first...let's have some fun",True,RED)
                    screen.blit(keyAlertText,[550,350])
                if player.stopTimer >= 400:
                    if player.stopTimer%5 == 0:#this part makes the screen flash between white and black really fast
                        pygame.draw.rect(screen,BLACK,(30,75,1308,665))
                    else:
                        pygame.draw.rect(screen,WHITE,(30,75,1308,665))
                    
                
                    
                    
        if currentStage == 69 and oneTimeDraw:
            devRoom(player)
            player.rect.x = 600
            player.rect.y = 650
            oneTimeDraw = False
        fullAutoWeapons(mouseDown,gunName,isArmed,player.switch)#calling full auto weapons function

        #updating enemies in list
        for ghost in ghostList:
            ghost.updateGhost(player.rect.x,player.rect.y)
        for shooter in shooterList:
            shooter.updateShooter()
        for enemySniper in sniperEnemyList:
            enemySniper.updateSniper(player,sniperEnemyPic)

        # boss functions
        for beefy in beefyList:
            beefy.updateBeefy(bossKilledList)
        for pump in pumpList:
            pump.updatePump(bossKilledList)
        for bottom in bottomList:
            bottom.updateBottom()

        #calling update functions
        beefyBalls.update()
        shootBalls(bullets,beefyBalls)
        shootBeefy(bullets,beefyList)
        shootPump(bullets,pumpList)
        shootBottom(bullets,bottomList)
        shootShooters(bullets,shooterList)
        shootGhosts(bullets,ghostList)
        shootSnipers(bullets,sniperEnemyList)
        shootWall(bullets,walls,50)
        destroyBullet(bullets)
        bullets.draw(screen)
        bullets.update()
        shrapnel.draw(screen)
        shrapnel.update()
        shooterBullets.draw(screen)
        shooterBullets.update()
        sniperBullets.draw(screen)
        sniperBullets.update()
        limitRange(bullets,gunName)
        walls.draw(screen)
        zoneList.update(zoneList,player)
        endGame(Hud.gameOver)
        
        if my >= 75: #if your mouse isnt on the hud, there will be a target crosshair showing instead
            screen.blit(crossHair,[mx - 25,my - 25])
            pygame.mouse.set_visible(False)#mouse will be invisible
        else:
            pygame.mouse.set_visible(True)

    pygame.display.flip() #Updates the screen with what was drawn
    if internetExplorer:
        clock.tick(25) # This sets framerate to 25 if the current sprite is internet explorer
    else:
        clock.tick(60)# This sets framerate to 70
loadFile.close()
try:
    saveFile.close()
except:
    pass
pygame.quit()
