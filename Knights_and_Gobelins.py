from pygame import *
import pygame
from time import *
import time
from random import *
import math
import os
import collections

##Classe
class Joueur :
    def __init__(self, x,y,symbol,color,avance) :
        self.x = x
        self.y = y
        self.symbol = symbol
        self.color = color
        self.avance = avance
        ##Stats
        self.pvmax = 100 #PV Max
        self.pvactuel = 100 #PV Actuel
        self.atk = 10 #Atk
        self.defense = 0 #Def
        self.etat = False #Stun / Root [Etat]
        self.mort = False #Mort
        ##Inventaire


    def pion(self) :
        ##Couleur
        #Jaune
        if self.color == 'jaune' :
            pion = pygame.image.load('Pion/Pion Jaune.png')
            Screen.blit(pion,(self.x,self.y))
        #Bleu
        if self.color == 'bleu' :
            pion = pygame.image.load('Pion/Pion Bleu.png')
            Screen.blit(pion,(self.x,self.y))
        #Vert
        if self.color == 'vert' :
            pion = pygame.image.load('Pion/Pion Vert.png')
            Screen.blit(pion,(self.x,self.y))
        #Violet
        if self.color == 'violet' :
            pion = pygame.image.load('Pion/Pion Violet.png')
            Screen.blit(pion,(self.x,self.y))
        ##Symbole
        #Shield
        if self.symbol == 'shield' :
            pion = pygame.image.load('Pion/Shield.png')
            Screen.blit(pion,(self.x,self.y))
        #Wizard
        if self.symbol == 'wizard' :
            pion = pygame.image.load('Pion/Wizard.png')
            Screen.blit(pion,(self.x,self.y))
        #Sword
        if self.symbol == 'sword' :
            pion = pygame.image.load('Pion/Sword.png')
            Screen.blit(pion,(self.x,self.y))
        #Bow
        if self.symbol == 'bow' :
            pion = pygame.image.load('Pion/Bow.png')
            Screen.blit(pion,(self.x,self.y))
        if self.symbol == 'dead' :
            pion = pygame.image.load('Pion/dead.png')
            Screen.blit(pion,(self.x,self.y))


    def move(self,Liste_Case,nombre_de):
        if self.mort == False :
            self.avance += nombre_de
            for i in range(1,32):
                if i == self.avance :
                    if self.color == 'jaune' :
                        self.x = Liste_Case[i].x  + 5
                        self.y = Liste_Case[i].y + 5
                    if self.color == 'bleu' :
                        self.x = Liste_Case[i].x  + 55
                        self.y = Liste_Case[i].y + 5
                    if self.color == 'violet' :
                        self.x = Liste_Case[i].x  + 5
                        self.y = Liste_Case[i].y + 55
                    if self.color == 'vert' :
                        self.x = Liste_Case[i].x  + 55
                        self.y = Liste_Case[i].y + 55
            if self.avance > 32 :
                if self.color == 'jaune' :
                    self.x = Liste_Case[0].x  + 5
                    self.y = Liste_Case[0].y + 5
                if self.color == 'bleu' :
                    self.x = Liste_Case[0].x  + 55
                    self.y = Liste_Case[0].y + 5
                if self.color == 'violet' :
                    self.x = Liste_Case[0].x  + 5
                    self.y = Liste_Case[0].y + 55
                if self.color == 'vert' :
                    self.x = Liste_Case[0].x  + 55
                    self.y = Liste_Case[0].y + 55
                self.avance = 0

    def battle(self,type_du_comba, joueur):
        cadre = pygame.image.load('HUD/comba/derrierplan.png')
        Screen.blit(cadre,(0,0))
        ##Mob
        if type_du_comba == 'mob' :
            monstre = randrange(0,101)
            if monstre <= 10 :
                monstrei = pygame.image.load('HUD/comba/monstre/dbat.png')
                Screen.blit(monstrei,(0,0))
            if 10 < monstre <= 20 :
                monstrei = pygame.image.load('HUD/comba/monstre/drat.png')
                Screen.blit(monstrei,(0,0))
            if 20 < monstre <= 30 :
                monstrei = pygame.image.load('HUD/comba/monstre/goblins.png')
                Screen.blit(monstrei,(0,0))
            if 30 < monstre <= 40 :
                monstrei = pygame.image.load('HUD/comba/monstre/kobold.png')
                Screen.blit(monstrei,(0,0))
            if 40 < monstre <= 50 :
                monstrei = pygame.image.load('HUD/comba/monstre/skeletton.png')
                Screen.blit(monstrei,(0,0))
            if 50 < monstre <= 60 :
                monstrei = pygame.image.load('HUD/comba/monstre/slime.png')
                Screen.blit(monstrei,(0,0))
            if 60 < monstre <= 70 :
                monstrei = pygame.image.load('HUD/comba/monstre/snake.png')
                Screen.blit(monstrei,(0,0))
            if 70 < monstre <= 80 :
                monstrei = pygame.image.load('HUD/comba/monstre/dracoy.png')
                Screen.blit(monstrei,(0,0))
            if 80 < monstre <= 90 :
                monstrei = pygame.image.load('HUD/comba/monstre/ghost.png')
                Screen.blit(monstrei,(0,0))
            if 90 < monstre <= 100 :
                monstrei = pygame.image.load('HUD/comba/monstre/grenouille.png')
                Screen.blit(monstrei,(0,0))
            xzone = randint(50,820)
            zone = pygame.image.load('HUD/comba/zone mob.png')
            Screen.blit(zone,(xzone,0))
            xcurs = randint(50,940)
            curseur = pygame.image.load('HUD/comba/curseur.png')
            Screen.blit(curseur,(xcurs,0))
            clock.tick(120000)
            pygame.display.update()
            comba_on = True
            sens = True
            speed = 4
            while comba_on == True :
                if xcurs >= 896 :
                    sens = False
                    speed += 0.5
                elif xcurs <= 0 :
                    sens = True
                    speed += 0.5
                elif speed >= 10 :
                    speed = 10
                if sens == True :
                    xcurs += speed
                elif sens == False :
                    xcurs -= speed
                Screen.blit(cadre,(0,0))
                Screen.blit(zone,(xzone,0))
                Screen.blit(curseur,(xcurs,0))
                clock.tick(120000)
                pygame.display.update()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            print(xcurs)
                            if xzone-20 <= xcurs <= xzone+20 :
                                refresh_plateau()
                                clock.tick(120000)
                                pygame.display.update()
                                comba_on = False
                            else :
                                hit = pygame.image.load('HUD/hit.png')
                                joueur.pvactuel -= 10
                                print (joueur.pvactuel)
                                Screen.blit(hit,(0,0))
                                clock.tick(120000)
                                pygame.display.update()
                                refresh_plateau()
                                Screen.blit(monstrei,(0,0))
                                Screen.blit(cadre,(0,0))
                                Screen.blit(zone,(xzone,0))
                                Screen.blit(curseur,(xcurs,0))
                                if joueur.pvactuel <= 0 :
                                    refresh_plateau()
                                    comba_on = False
                            clock.tick(120000)
                            pygame.display.update()
        ##Horde
        if type_du_comba == 'horde' :
            monstre = randrange(0,101)
            if monstre <= 12.5 :
                monstrei = pygame.image.load('HUD/comba/horde/hordebr.png')
                Screen.blit(monstrei,(0,0))
            if 12.5 < monstre <= 25 :
                monstrei = pygame.image.load('HUD/comba/horde/hordeg.png')
                Screen.blit(monstrei,(0,0))
            if 25 < monstre <= 37.5 :
                monstrei = pygame.image.load('HUD/comba/horde/horde snake.png')
                Screen.blit(monstrei,(0,0))
            if 37.5 < monstre <= 50 :
                monstrei = pygame.image.load('HUD/comba/horde/horde slime.png')
                Screen.blit(monstrei,(0,0))
            if 50 < monstre <= 62.5 :
                monstrei = pygame.image.load('HUD/comba/horde/horde skeletton.png')
                Screen.blit(monstrei,(0,0))
            if 62.5 < monstre <= 75 :
                monstrei = pygame.image.load('HUD/comba/horde/horde ghost.png')
                Screen.blit(monstrei,(0,0))
            if 75 < monstre <= 87.5 :
                monstrei = pygame.image.load('HUD/comba/horde/horde frog.png')
                Screen.blit(monstrei,(0,0))
            if 87.5 < monstre <= 100 :
                monstrei = pygame.image.load('HUD/comba/horde/horde dracoy.png')
                Screen.blit(monstrei,(0,0))
            xzone1 = randint(50,820)
            zone1 = pygame.image.load('HUD/comba/zone mob.png')
            zone1p = True
            xzone2 = randint(50,820)
            zone2 = pygame.image.load('HUD/comba/zone mob.png')
            zone2p = True
            xzone3 = randint(50,820)
            zone3 = pygame.image.load('HUD/comba/zone mob.png')
            zone3p = True
            Screen.blit(zone1,(xzone1,0))
            Screen.blit(zone2,(xzone2,0))
            Screen.blit(zone3,(xzone3,0))
            xcurs = randint(50,940)
            curseur = pygame.image.load('HUD/comba/curseur.png')
            Screen.blit(curseur,(xcurs,0))
            clock.tick(120000)
            pygame.display.update()
            comba_on = True
            sens = True
            speed = 4.5
            while comba_on == True :
                if xcurs >= 896 :
                    sens = False
                    speed += 0.5
                elif xcurs <= 0 :
                    sens = True
                    speed += 0.5
                elif speed >= 10 :
                    speed = 10
                if sens == True :
                    xcurs += speed
                elif sens == False :
                    xcurs -= speed
                Screen.blit(cadre,(0,0))
                if zone1p == True :
                    Screen.blit(zone1,(xzone1,0))
                if zone2p == True :
                    Screen.blit(zone2,(xzone2,0))
                if zone3p == True :
                    Screen.blit(zone3,(xzone3,0))
                Screen.blit(curseur,(xcurs,0))
                clock.tick(120000)
                pygame.display.update()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            print(xcurs)
                            if xzone1-20 <= xcurs <= xzone1+20 :
                                zone1p = False
                                clock.tick(120000)
                                pygame.display.update()
                            elif xzone2-20 <= xcurs <= xzone2+20 :
                                zone2p = False
                                clock.tick(120000)
                                pygame.display.update()
                            elif xzone3-20 <= xcurs <= xzone3+20 :
                                zone3p = False
                                clock.tick(120000)
                                pygame.display.update()
                            else :
                                hit = pygame.image.load('HUD/hit.png')
                                joueur.pvactuel -= 10
                                print (joueur.pvactuel)
                                Screen.blit(hit,(0,0))
                                clock.tick(120000)
                                pygame.display.update()
                                refresh_plateau()
                                Screen.blit(monstrei,(0,0))
                                Screen.blit(cadre,(0,0))
                                if zone1p == True :
                                    Screen.blit(zone1,(xzone1,0))
                                if zone2p == True :
                                    Screen.blit(zone2,(xzone2,0))
                                if zone3p == True :
                                    Screen.blit(zone3,(xzone3,0))
                                Screen.blit(curseur,(xcurs,0))
                                if joueur.pvactuel <= 0 :
                                    refresh_plateau()
                                    comba_on = False
                            clock.tick(120000)
                            pygame.display.update()
                            if zone1p == False and zone2p == False and zone3p == False :
                                refresh_plateau()
                                comba_on = False
                            clock.tick(120000)
                            pygame.display.update()
class Case :
    def __init__(self, x,y,biome) :
        self.x = x
        self.y = y
        self.biome = biome
    def draw(self):
        #Plaine
        if self.biome == 'plaine' :
            case = pygame.image.load('Case/Plaine.png')
            Screen.blit(case,(self.x,self.y))
        #Ocean
        if self.biome == 'ocean' :
            case = pygame.image.load('Case/Ocean.png')
            Screen.blit(case,(self.x,self.y))
        #Desert
        if self.biome == 'desert' :
            case = pygame.image.load('Case/Desert.png')
            Screen.blit(case,(self.x,self.y))
        #Neige
        if self.biome == 'neige' :
            case = pygame.image.load('Case/Snow.png')
            Screen.blit(case,(self.x,self.y))
        #Chateau
        if self.biome == 'chateau' :
            case = pygame.image.load('Case/Chateau.png')
            Screen.blit(case,(self.x,self.y))
    def evenementset(self,numero_de_l_evenement):
        self.numero = numero_de_l_evenement
    def evenementactive(self, joueur,Liste_Case):
        pygame.event.clear()
        ##Donjon
        if self.numero <= 7 :
            print("sur Donjon")
            y = -800
            g = pygame.image.load('Donjon/Donjon 32.png')
            Screen.blit(g,(0,y))
            for i in range (0,16) :
                y += 50
                refresh_plateau()
                Screen.blit(g,(0,y))
                clock.tick(120000)
                pygame.display.update()
            refresh_plateau()
            clock.tick(120000)
            pygame.display.update()
            a = 0
            if a == 0 and len(Liste_Joueur) == 2 : Cowboy()
            elif a == 1 or len(Liste_Joueur) >= 2: Brigand(len(Liste_Joueur))
            refresh_plateau()
            clock.tick(120000)
            pygame.display.update()
        ##Village
        if 7 < self.numero <= 15 :
            print("sur Village")
        ##Sanctuaire
        if 15 < self.numero <= 20 :
            print("sur Sanctuaire")
            if 15 < self.numero <= 20 :
                print("sur Sanctuaire")
                sanctuaire = Sanctuaire()
                groupe_de_sanc = pygame.sprite.Group(sanctuaire)
                for i in range(17) :
                    groupe_de_sanc.update()
                    groupe_de_sanc.draw(Screen)
                    clock.tick(120000)
                    pygame.display.update()
                refresh_plateau()
            dif = randrange(0,3)
            if dif == 0 :
                dif = 'easy'
            elif dif == 1 :
                dif = 'medium'
            elif dif == 2 :
                dif = 'hard'
            a = randrange(0,2)
            if a == 0 :
                Spam(dif)
            if a == 1 :
                Archer()
            clock.tick(120000)
            pygame.display.update()
            refresh_plateau()
            clock.tick(120000)
            pygame.display.update()
        ##Horde
        if 20 < self.numero <= 21 :
            print("sur Horde")
            horde = pygame.image.load('HUD/Event/horde.png')
            Screen.blit(horde,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
            clock.tick(120000)
            pygame.display.update()
            joueur.battle('horde',joueur)
        ##Tresor
        if 21 < self.numero <= 26 :
            print("sur Tresor")
            tresor = pygame.image.load('HUD/Event/dresor.png')
            Screen.blit(tresor,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Marchand Itinerant
        if 26 < self.numero <= 31 :
            print("sur Marchand")
        ##Monstre
        if 31 < self.numero <= 36 :
            print("sur Monstre")
            monstre = pygame.image.load('HUD/Event/monstre.png')
            Screen.blit(monstre,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
            clock.tick(120000)
            pygame.display.update()
            joueur.battle('mob',joueur)
        ##Foudre
        if 36 < self.numero <= 37 :
            print("sur Diathanael Foudre")
            front = pygame.image.load('Diathanael/Foudre.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Feu
        if 37 < self.numero <= 38 :
            print("sur Diathanael Feu")
            front = pygame.image.load('Diathanael/Feu.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Eau
        if 38 < self.numero <= 39 :
            print("sur Diathanael Eau")
            front = pygame.image.load('Diathanael/Eau.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Terre
        if 39 < self.numero <= 40 :
            print("sur Diathanael Terre")
            front = pygame.image.load('Diathanael/Terre.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Air
        if 40 < self.numero <= 41 :
            print("sur Diathanael Air")
            front = pygame.image.load('Diathanael/Air.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Metal
        if 41 < self.numero <= 42 :
            print("sur Diathanael Metal")
            front = pygame.image.load('Diathanael/Metal.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Tenebres
        if 42 < self.numero <= 43 :
            print("sur Diathanael Tenebres")
            front = pygame.image.load('Diathanael/Tenebres.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
            joueur.move(Liste_Case,-2)
            clock.tick(120000)
            pygame.display.update()
         ##Lumieres
        if 43 < self.numero <= 44 :
            print("sur Diathanael Lumieres")
            front = pygame.image.load('Diathanael/Lumiere.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Poisse
        if 44 < self.numero <= 45 :
            print("sur Diathanael Poisse")
            front = pygame.image.load('Diathanael/Poisse.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Ether
        if 45 < self.numero <= 46 :
            print("sur Diathanael Ether")
            front = pygame.image.load('Diathanael/Ether.png')
            Screen.blit(front,(0,0))
            clock.tick(120000)
            pygame.display.update()
            eventfini = False
            while not eventfini :
                #import pdb; pdb.set_trace()
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print('noice')
                            refresh_plateau()
                            clock.tick(120000)
                            pygame.display.update()
                            eventfini = True
        ##Rien
        if 46 < self.numero <= 100 :
            print("Y a R")

class Rain(pygame.sprite.Sprite):
    def __init__(self):
        super(Rain, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Menu/Pluie/Pluie 4.png'))
        self.images.append(pygame.image.load('Menu/Pluie/Pluie 5.png'))
        self.images.append(pygame.image.load('Menu/Pluie/Pluie 6.png'))
        self.images.append(pygame.image.load('Menu/Pluie/Pluie 7.png'))
        self.images.append(pygame.image.load('Menu/Pluie/Pluie 8.png'))
        self.images.append(pygame.image.load('Menu/Pluie/Pluie 9.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5,5,150,198)
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

class Sanctuaire(pygame.sprite.Sprite):
    def __init__(self):
        super(Sanctuaire, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Sanctuaire/sword 1.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 2.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 3.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 4.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 5.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 6.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 7.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 8.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 9.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 10.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 11.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 12.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 13.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 14.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 15.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 16.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 17.png'))
        self.images.append(pygame.image.load('Sanctuaire/sword 18.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5,5,150,198)
    def update(self):
        refresh_plateau()
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
##Plateau
def plateau(Liste_Case, nb_joueur, symbolJ1 , symbolJ2, symbolJ3 , symbolJ4):
    ##BackGround
    background = pygame.image.load('Case/Background.png')
    Screen.blit(background,(0,0))
    ##Plaine
    for i in range(1,2):
        for j in range (1,8):
            case = Case(1000-100*i,800-100*j, 'plaine')
            case.draw()
            Liste_Case.append(case)
    ##Desert
    for i in range(1,10):
        for j in range (1):
            case = Case(1000-100*i,0+100*j, 'desert')
            case.draw()
            Liste_Case.append(case)
    ##Ocean
    for i in range(0,1):
        for j in range (0,7):
            case = Case(0+100*i,0+100*j, 'ocean')
            case.draw()
            Liste_Case.append(case)
    ##Neige
    for i in range(0,9):
        for j in range (7,8):
            case = Case(0+100*i,0+100*j, 'neige')
            case.draw()
            Liste_Case.append(case)
    ##Chateau
    case = Case(450,350, 'chateau')
    case.draw()
    Liste_Case.append(case)
    ##Set Evenement Var
    Nb_Donjon = 0
    Nb_Village = 0
    Nb_Sanctuaire = 0
    Nb_Horde = 0
    Nb_Tresor = 0
    Nb_Marchand = 0
    Nb_Monstre = 0
    Nb_Diathanael = 0
    ##Set Evenement Case
    for i in range (1,32):
        Liste_Case[i].evenementset(randrange(0,101))
        if Liste_Case[i].numero <= 7 :
            #Donjon
            Nb_Donjon += 1
        if 7 < Liste_Case[i].numero <= 15 :
            #Village
            Nb_Village += 1
        if 15 < Liste_Case[i].numero <= 20 :
            #Sanctuaire
            Nb_Sanctuaire += 1
        if 20 < Liste_Case[i].numero <= 21 :
            #Horde
            Nb_Horde += 1
        if 21 < Liste_Case[i].numero <= 26 :
            #Tresor
            Nb_Tresor += 1
        if 26 < Liste_Case[i].numero <= 31 :
            #Marchand Itinerant
            Nb_Marchand += 1
        if 31 < Liste_Case[i].numero <= 36 :
            #Monstre
            Nb_Monstre += 1
        if 36 < Liste_Case[i].numero <= 37 :
            #Foudre
            Nb_Diathanael += 1
        if 37 < Liste_Case[i].numero <= 38 :
            #Feu
            Nb_Diathanael += 1
        if 38 < Liste_Case[i].numero <= 39 :
            #Eau
            Nb_Diathanael += 1
        if 39 < Liste_Case[i].numero <= 40 :
            #Terre
            Nb_Diathanael += 1
        if 40 < Liste_Case[i].numero <= 41 :
            #Air
            Nb_Diathanael += 1
        if 41 < Liste_Case[i].numero <= 42 :
            #Metal
            Nb_Diathanael += 1
        if 42 < Liste_Case[i].numero <= 43 :
            #Tenebres
            Nb_Diathanael += 1
        if 43 < Liste_Case[i].numero <= 44 :
            #Lumieres
            Nb_Diathanael += 1
        if 44 < Liste_Case[i].numero <= 45 :
            #Poisse
            Nb_Diathanael += 1
        if 45 < Liste_Case[i].numero <= 46 :
            #Ether
            Nb_Diathanael += 1
    ##Regularisation d'exces
    #Donjon
    if Nb_Donjon > 5 :
        while Nb_Donjon > 5 :
            for i in range (1,32):
                if Liste_Case[i].numero <= 7 :
                    Liste_Case[i].numero = randrange(47,101)
                    Nb_Donjon -= 1
                    break
    #Village
    if Nb_Village > 4 :
        while Nb_Village > 4 :
            for i in range (1,32):
                if 7 < Liste_Case[i].numero <= 15 :
                    Liste_Case[i].numero = randrange(47,101)
                    Nb_Village -= 1
                    break
    #Sanctuaire
    if Nb_Sanctuaire > 5 :
        while Nb_Sanctuaire > 5 :
            for i in range (1,32):
                if 15 < Liste_Case[i].numero <= 20 :
                   Liste_Case[i].numero = randrange(47,101)
                   Nb_Sanctuaire -= 1
                   break
    #Horde
    if Nb_Horde > 4 :
        while Nb_Horde > 4 :
            for i in range (1,32):
                if 20 < Liste_Case[i].numero <= 21 :
                    Liste_Case[33-i].numero = randrange(47,101)
                    Nb_Horde -= 1
                    break
    #Tresor
    if Nb_Tresor > 2 :
        while Nb_Tresor > 2 :
            for i in range (1,32):
                if 21 < Liste_Case[i].numero <= 26 :
                    Liste_Case[i].numero = randrange(47,101)
                    Nb_Tresor -= 1
                    break
    #Marchand
    if Nb_Marchand > 3 :
        while Nb_Marchand > 3 :
            for i in range (1,32):
                    if 26 < Liste_Case[i].numero <= 31 :
                        Liste_Case[i].numero = randrange(47,101)
                        Nb_Marchand -= 1
                        break
    #Monstre
    if Nb_Monstre > 7 :
        while Nb_Monstre > 7 :
            for i in range (1,32):
                if 31 < Liste_Case[i].numero <= 36 :
                    Liste_Case[i].numero = randrange(47 ,101)
                    Nb_Monstre -= 1
                    break
    #Diathanael
    if Nb_Diathanael > 7 :
        while Nb_Diathanael > 7 :
            for i in range (1,32):
                if 37 < Liste_Case[i].numero <= 46 :
                    Liste_Case[i].numero = randrange(47,101)
                    Nb_Diathanael -= 1
                    break
    ##Regularisation d'absence
    #Donjon
    if Nb_Donjon < 3 :
        while Nb_Donjon < 3 :
            for i in range (1,32):
                if 46 < Liste_Case[i].numero <= 100 :
                    Liste_Case[i].numero = randrange(0,8)
                    Nb_Donjon += 1
                    break
    #Village
    if Nb_Village < 3 :
        while Nb_Village < 3 :
            for i in range (1,32):
                if 46 < Liste_Case[i].numero <= 100 :
                    Liste_Case[i].numero = randrange(7,16)
                    Nb_Village += 1
                    break
    #Sanctuaire
    if Nb_Sanctuaire < 4 :
        while Nb_Sanctuaire < 4 :
            for i in range (1,32):
                if 46 < Liste_Case[i].numero <= 100 :
                   Liste_Case[i].numero = randrange(15,21)
                   Nb_Sanctuaire += 1
                   break
    #Horde
    if Nb_Horde < 4 :
        while Nb_Horde < 4 :
            for i in range (1,32):
                if 46 < Liste_Case[i].numero <= 100 :
                    Liste_Case[i].numero = randrange(20,22)
                    Nb_Horde += 1
                    break
    #Tresor
    if Nb_Tresor < 1 :
        while Nb_Tresor < 1 :
            for i in range (1,32):
                if 46 < Liste_Case[i].numero <= 100 :
                    Liste_Case[i].numero = randrange(21,27)
                    Nb_Tresor += 1
                    break
    #Marchand
    if Nb_Marchand < 2 :
        while Nb_Marchand < 2 :
            for i in range (1,32):
                if 46 < Liste_Case[i].numero <= 100 :
                    Liste_Case[i].numero = randrange(26,32)
                    Nb_Marchand += 1
                    break
    #Monstre
    if Nb_Monstre < 5 :
        while Nb_Monstre < 5 :
            for i in range (1,32):
                if 46 < Liste_Case[i].numero <= 100 :
                    Liste_Case[i].numero = randrange(31,37)
                    Nb_Monstre += 1
                    break
    #Diathanael
    if Nb_Diathanael < 6 :
        while Nb_Diathanael < 6 :
            for i in range (1,32):
                if 46 < Liste_Case[i].numero <= 100 :
                    Liste_Case[i].numero = randrange(36,47)
                    Nb_Diathanael += 1
                    break
    ##Affiche Event
    for i in range (1,32):
        if Liste_Case[i].numero <= 7 :
            #Donjon
            event = pygame.image.load('Case/Donjon.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Donjon")
        if 7 < Liste_Case[i].numero <= 15 :
            #Village
            event = pygame.image.load('Case/Village.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Village")
        if 15 < Liste_Case[i].numero <= 20 :
            #Sanctuaire
            event = pygame.image.load('Case/Sanctuaire.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Sanctuaire")
        if 20 < Liste_Case[i].numero <= 21 :
            #Horde
            event = pygame.image.load('Case/Surprise.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Horde")
        if 21 < Liste_Case[i].numero <= 26 :
            #Tresor
            event = pygame.image.load('Case/Surprise.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Tresor")
        if 26 < Liste_Case[i].numero <= 31 :
            #Marchand Itinerant
            event = pygame.image.load('Case/Marchand.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Marchand Itinerant")
        if 31 < Liste_Case[i].numero <= 36 :
            #Monstre
            event = pygame.image.load('Case/Combat.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Monstre")
        if 36 < Liste_Case[i].numero <= 37 :
            #Foudre
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 37 < Liste_Case[i].numero <= 38 :
            #Feu
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 38 < Liste_Case[i].numero <= 39 :
            #Eau
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 39 < Liste_Case[i].numero <= 40 :
            #Terre
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 40 < Liste_Case[i].numero <= 41 :
            #Air
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 41 < Liste_Case[i].numero <= 42 :
            #Metal
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 42 < Liste_Case[i].numero <= 43 :
            #Tenebres
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 43 < Liste_Case[i].numero <= 44 :
            #Lumieres
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 44 < Liste_Case[i].numero <= 45 :
            #Poisse
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 45 < Liste_Case[i].numero <= 46 :
            #Ether
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
            print("Diathanael")
        if 46 < Liste_Case[i].numero <= 100 :
            #Rien
            print("Rien")
    ##Contour de Terrain
    pygame.draw.line(Screen,(0,0,0),(997,0),(997,800),5)
    pygame.draw.line(Screen,(0,0,0),(0,3),(1000,3),5)
    pygame.draw.line(Screen,(0,0,0),(3,0),(3,800),5)
    pygame.draw.line(Screen,(0,0,0),(0,797),(1000,797),5)
    ##Contour de Biomes
    pygame.draw.line(Screen,(0,0,0),(894,100),(894,700),10)#Plaine
    pygame.draw.line(Screen,(0,0,0),(900,105),(100,105),10)#Desert
    pygame.draw.line(Screen,(0,0,0),(103,100),(103,700),10)#Ocean
    pygame.draw.line(Screen,(0,0,0),(100,693),(900,693),10)#Neige
    ##2J MAX
    if nb_joueur >= 2 :
        if symbolJ1 == 1 :
            j1 = Joueur(905,705,'shield','jaune',0)
            j1.pion()
            Liste_Joueur.append(j1)
        if symbolJ1 == 2 :
            j1 = Joueur(905,705,'bow','jaune',0)
            j1.pion()
            Liste_Joueur.append(j1)
        if symbolJ1 == 3 :
            j1 = Joueur(905,705,'sword','jaune',0)
            j1.pion()
            Liste_Joueur.append(j1)
        if symbolJ1 == 4 :
            j1 = Joueur(905,705,'wizard','jaune',0)
            j1.pion()
            Liste_Joueur.append(j1)
        if symbolJ2 == 1 :
            j2 = Joueur(955,705,'shield','bleu',0)
            j2.pion()
            Liste_Joueur.append(j2)
        if symbolJ2 == 2 :
            j2 = Joueur(955,705,'bow','bleu',0)
            j2.pion()
            Liste_Joueur.append(j2)
        if symbolJ2 == 3 :
            j2 = Joueur(955,705,'sword','bleu',0)
            j2.pion()
            Liste_Joueur.append(j2)
        if symbolJ2 == 4 :
            j2 = Joueur(955,705,'wizard','bleu',0)
            j2.pion()
            Liste_Joueur.append(j2)
    ##3J MAX
    if nb_joueur >= 3 :
        if symbolJ3 == 1 :
            j3 = Joueur(905,755,'shield','violet',0)
            j3.pion()
            Liste_Joueur.append(j3)
        if symbolJ3 == 2 :
            j3 = Joueur(905,755,'bow','violet',0)
            j3.pion()
            Liste_Joueur.append(j3)
        if symbolJ3 == 3 :
            j3 = Joueur(905,755,'sword','violet',0)
            j3.pion()
            Liste_Joueur.append(j3)
        if symbolJ3 == 4 :
            j3 = Joueur(905,755,'wizard','violet',0)
            j3.pion()
            Liste_Joueur.append(j3)
    ##4J MAX
    if nb_joueur == 4 :
        if symbolJ4 == 1 :
            j4 = Joueur(955,755,'shield','vert',0)
            j4.pion()
            Liste_Joueur.append(j4)
        if symbolJ4 == 2 :
            j4 = Joueur(955,755,'bow','vert',0)
            j4.pion()
            Liste_Joueur.append(j4)
        if symbolJ4 == 3 :
            j4 = Joueur(955,755,'sword','vert',0)
            j4.pion()
            Liste_Joueur.append(j4)
        if symbolJ4 == 4 :
            j4 = Joueur(955,755,'wizard','vert',0)
            j4.pion()
            Liste_Joueur.append(j4)
def refresh_plateau() :
    ##BackGround
    background = pygame.image.load('Case/Background.png')
    Screen.blit(background,(0,0))
    ##Case
    for i in range(len(Liste_Case)):
        Liste_Case[i].draw()
    ##Event
    for i in range (1,32):
        if Liste_Case[i].numero <= 7 :
            #Donjon
            event = pygame.image.load('Case/Donjon.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 7 < Liste_Case[i].numero <= 15 :
            #Village
            event = pygame.image.load('Case/Village.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 15 < Liste_Case[i].numero <= 20 :
            #Sanctuaire
            event = pygame.image.load('Case/Sanctuaire.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 20 < Liste_Case[i].numero <= 21 :
            #Horde
            event = pygame.image.load('Case/Surprise.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 21 < Liste_Case[i].numero <= 26 :
            #Tresor
            event = pygame.image.load('Case/Surprise.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 26 < Liste_Case[i].numero <= 31 :
            #Marchand Itinerant
            event = pygame.image.load('Case/Marchand.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 31 < Liste_Case[i].numero <= 36 :
            #Monstre
            event = pygame.image.load('Case/Combat.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 36 < Liste_Case[i].numero <= 37 :
            #Foudre
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 37 < Liste_Case[i].numero <= 38 :
            #Feu
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 38 < Liste_Case[i].numero <= 39 :
            #Eau
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 39 < Liste_Case[i].numero <= 40 :
            #Terre
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 40 < Liste_Case[i].numero <= 41 :
            #Air
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 41 < Liste_Case[i].numero <= 42 :
            #Metal
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 42 < Liste_Case[i].numero <= 43 :
            #Tenebres
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 43 < Liste_Case[i].numero <= 44 :
            #Lumieres
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 44 < Liste_Case[i].numero <= 45 :
            #Poisse
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
        if 45 < Liste_Case[i].numero <= 46 :
            #Ether
            event = pygame.image.load('Case/Diathanael.png')
            Screen.blit(event,(Liste_Case[i].x,Liste_Case[i].y))
    ##Contour de Terrain
    pygame.draw.line(Screen,(0,0,0),(997,0),(997,800),5)
    pygame.draw.line(Screen,(0,0,0),(0,3),(1000,3),5)
    pygame.draw.line(Screen,(0,0,0),(3,0),(3,800),5)
    pygame.draw.line(Screen,(0,0,0),(0,797),(1000,797),5)
    ##Contour de Biomes
    pygame.draw.line(Screen,(0,0,0),(894,100),(894,700),10)#Plaine
    pygame.draw.line(Screen,(0,0,0),(900,105),(100,105),10)#Desert
    pygame.draw.line(Screen,(0,0,0),(103,100),(103,700),10)#Ocean
    pygame.draw.line(Screen,(0,0,0),(100,693),(900,693),10)#Neige
    ##Pion
    for i in range (len(Liste_Joueur)):
        Liste_Joueur[i].pion()
    Barre = pygame.image.load('HUD/Barre.png')
    Screen.blit(Barre,(0,0))
##Pratique
def dice() :
    result = randrange(0,7)
    return result
##Mini-Jeux
def Brigand(nb_joueur):
    YJ1 = 0
    YJ2 = 0
    J1 = pygame.image.load('mini/bandit/joueur/J1.png')
    Screen.blit(J1,(0,YJ1))
    J2 = pygame.image.load('mini/bandit/joueur/J2.png')
    Screen.blit(J2,(0,YJ2))
    Touche1J1 = False
    Touche2J1 = False
    Touche1J2 = False
    Touche2J2 = False
    if nb_joueur == 2 :
        bg = pygame.image.load('mini/bandit/background/backgroundJ2.png')
        Screen.blit(bg,(0,0))
    elif nb_joueur == 3 :
        bg = pygame.image.load('mini/bandit/background/backgroundJ3.png')
        Screen.blit(bg,(0,0))
        YJ3 = 0
        J3 = pygame.image.load('mini/bandit/joueur/J3.png')
        Screen.blit(J3,(0,YJ3))
        Touche1J3 = False
        Touche2J3 = False
    elif nb_joueur == 4 :
        bg = pygame.image.load('mini/bandit/background/backgroundJ4.png')
        Screen.blit(bg,(0,0))
        YJ3 = 0
        J3 = pygame.image.load('mini/bandit/joueur/J3.png')
        Screen.blit(J3,(0,YJ3))
        YJ4 = 0
        J4 = pygame.image.load('mini/bandit/joueur/J4.png')
        Screen.blit(J4,(0,YJ4))
        Touche1J3 = False
        Touche2J3 = False
        Touche1J4 = False
        Touche2J4 = False
    clock.tick(120000)
    pygame.display.update()
    game = True
    while game == True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_a and not Touche1J1 :
                    print('J1 Touche 1')
                    Touche1J1 = True
                if event.key == pygame.K_s and not Touche2J1 :
                    print('J1 Touche 2')
                    Touche2J1 = True
                if event.key == pygame.K_g and not Touche1J2 :
                    print('J2 Touche 1')
                    Touche1J2 = True
                if event.key == pygame.K_h and not Touche2J2 :
                    print('J2 Touche 2')
                    Touche2J2 = True
                if nb_joueur >= 3 :
                    if event.key == pygame.K_k and not Touche1J3 :
                        print('J3 Touche 1')
                        Touche1J3 = True
                    if event.key == pygame.K_l and not Touche2J3 :
                        print('J3 Touche 2')
                        Touche2J3 = True
                if nb_joueur == 4 :
                    if event.key == pygame.K_LEFT and not Touche1J4 :
                        print('J4 Touche 1')
                        Touche1J4 = True
                    if event.key == pygame.K_RIGHT and not Touche2J4 :
                        print('J4 Touche 2')
                        Touche2J4 = True
        Screen.blit(bg,(0,0))
        if Touche1J1 and Touche2J1 :
            YJ1 -= 20
            print(YJ1)
            Touche1J1 = False
            Touche2J1 = False
        if Touche1J2 and Touche2J2 :
            YJ2 -= 20
            print(YJ2)
            Touche1J2 = False
            Touche2J2 = False
        if nb_joueur >= 3 :
            if Touche1J3 and Touche2J3 :
                YJ3 -= 20
                print(YJ3)
                Touche1J3 = False
                Touche2J3 = False
        if nb_joueur == 4 :
            if Touche1J4 and Touche2J4  :
                YJ4 -= 20
                print(YJ4)
                Touche1J4 = False
                Touche2J4 = False
        if Touche1J1 == True :
            Touche = pygame.image.load('mini/bandit/touche/Touche1.png')
            Screen.blit(Touche,(0,0))
        if Touche2J1 == True :
            Touche = pygame.image.load('mini/bandit/touche/Touche2.png')
            Screen.blit(Touche,(0,0))
        if Touche1J2 == True :
            Touche = pygame.image.load('mini/bandit/touche/Touche1.png')
            Screen.blit(Touche,(270,0))
        if Touche2J2 == True :
            Touche = pygame.image.load('mini/bandit/touche/Touche2.png')
            Screen.blit(Touche,(270,0))
        if nb_joueur >= 3 :
            if Touche1J3 == True :
                Touche = pygame.image.load('mini/bandit/touche/Touche1.png')
                Screen.blit(Touche,(503,0))
            if Touche2J3 == True :
                Touche = pygame.image.load('mini/bandit/touche/Touche2.png')
                Screen.blit(Touche,(503,0))
        if nb_joueur == 4 :
            if Touche1J4 == True :
                Touche = pygame.image.load('mini/bandit/touche/Touche1.png')
                Screen.blit(Touche,(772,0))
            if Touche2J4 == True :
                Touche = pygame.image.load('mini/bandit/touche/Touche2.png')
                Screen.blit(Touche,(772,0))
        Screen.blit(J1,(0,YJ1))
        Screen.blit(J2,(0,YJ2))
        if nb_joueur >= 3 : Screen.blit(J3,(0,YJ3))
        if nb_joueur == 4 : Screen.blit(J4,(0,YJ4))
        if YJ1 == -720 :
            Vic = pygame.image.load('mini/bandit/vicJ1.png')
            Screen.blit(Vic,(0,0))
            clock.tick(120000)
            pygame.display.update()
            pygame.time.wait(3000)
            for i in range (0,len(Liste_Joueur)):
                Liste_Joueur[i].pvactuel -= 5
            Liste_Joueur[0].pvactuel += 10
            game = False
        if YJ2 == -720 :
            Vic = pygame.image.load('mini/bandit/vicJ2.png')
            Screen.blit(Vic,(0,0))
            clock.tick(120000)
            pygame.display.update()
            pygame.time.wait(3000)
            for i in range (0,len(Liste_Joueur)):
                Liste_Joueur[i].pvactuel -= 5
            Liste_Joueur[1].pvactuel += 10
            game = False
        if nb_joueur >= 3 and YJ3 == -720 :
            Vic = pygame.image.load('mini/bandit/vicJ3.png')
            Screen.blit(Vic,(0,0))
            clock.tick(120000)
            pygame.display.update()
            pygame.time.wait(3000)
            for i in range (0,len(Liste_Joueur)):
                Liste_Joueur[i].pvactuel -= 5
            Liste_Joueur[2].pvactuel += 10
            game = False
        if nb_joueur == 4 and YJ4 == -720 :
            Vic = pygame.image.load('mini/bandit/vicJ4.png')
            Screen.blit(Vic,(0,0))
            clock.tick(120000)
            pygame.display.update()
            pygame.time.wait(3000)
            for i in range (0,len(Liste_Joueur)):
                Liste_Joueur[i].pvactuel -= 5
            Liste_Joueur[3].pvactuel += 10
            game = False
        clock.tick(120000)
        pygame.display.update()

def Cowboy():
    J1_Push = False
    J2_Push = False
    back = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\crprov.png')
    Screen.blit(back,(0,0))
    CaR = 3250
    clock.tick(120000)
    pygame.display.update()
    pygame.time.wait(CaR)
    back = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr7.png')
    Screen.blit(back,(0,0))
    CaRi = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr3.png')
    Screen.blit(CaRi,(0,0))
    clock.tick(120000)
    pygame.display.update()
    pygame.time.wait(850)
    back = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr7.png')
    Screen.blit(back,(0,0))
    CaRi = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr2.png')
    Screen.blit(CaRi,(0,0))
    clock.tick(120000)
    pygame.display.update()
    pygame.time.wait(850)
    back = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr7.png')
    Screen.blit(back,(0,0))
    CaRi = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr1.png')
    Screen.blit(CaRi,(0,0))
    clock.tick(120000)
    pygame.display.update()
    pygame.time.wait(850)
    back = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr7.png')
    Screen.blit(back,(0,0))
    CaRi = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr7goat.png')
    Screen.blit(CaRi,(0,0))
    clock.tick(120000)
    pygame.display.update()
    pygame.time.wait(850)
    back = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cr7.png')
    Screen.blit(back,(0,0))
    pygame.display.update()
    pygame.time.wait(850)
    Temp_Ref = time.time()
    Temp_J2 = float()
    Temp_J1 = float()
    while J1_Push == False and J2_Push == False :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                J1_Push = True
                J2_Push = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_a :
                    if J1_Push == False :
                        print("J1")
                        J1_Push = True
                        Temp_J1 = time.time()
                        break
                    else :
                        print('Deja Appuye')
                if event.key == pygame.K_l :
                    if J2_Push == False :
                        print("J2")
                        J2_Push = True
                        Temp_J2 = time.time()
                        break
                    else :
                        print('Deja Appuye')
        clock.tick(120000)
        pygame.display.update()
    clock.tick(120000)
    pygame.display.update()
    if int(Temp_J2) > int(Temp_J1) :
        print("J2 win")
        Liste_Joueur[0].pvactuel -= 5
        CaRi = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cictoireJ2.png')
        Screen.blit(CaRi,(0,0))
        clock.tick(120000)
        pygame.display.update()
        pygame.time.wait(3000)
    elif int(Temp_J2) < int(Temp_J1) :
        print("J1 win")
        Liste_Joueur[1].pvactuel -= 5
        CaRi = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\cictoireJ1.png')
        Screen.blit(CaRi,(0,0))
        clock.tick(120000)
        pygame.display.update()
        pygame.time.wait(3000)
    elif Temp_J2 == Temp_J1 :
        print("Tie !")
        CaRi = pygame.image.load('D:\Games\K&G\Ressources\Flat\mini\cowboy\ctie.png')
        Screen.blit(CaRi,(0,0))
        clock.tick(120000)
        pygame.display.update()
        pygame.time.wait(3000)

def Spam(difficulte):
    if difficulte == 'easy':
        objectif = 25
        sec = 15
    if difficulte == 'medium':
        objectif = 50
        sec = 15
    if difficulte == 'hard':
        objectif = 55
        sec = 10
    font = pygame.font.SysFont("Myriad Pro", 72)
    timerref = time.time()
    clic = 0
    temps  = False
    CaRi = pygame.image.load('mini/spam/off.png')
    Screen.blit(CaRi,(0,0))
    clock.tick(120000)
    pygame.display.update()
    game = True
    while game == True :
        timer = time.time()
        print(int(timer - timerref))
        if int(timer - timerref) == sec :
            temps = True
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                temps = True
            if event.type == pygame.MOUSEBUTTONDOWN :
                x,y = pygame.mouse.get_pos()
                if 428 < x < 573 and 329 < y < 474 :
                    clic += 1
                    print(clic)
                    CaRi = pygame.image.load('mini/spam/on.png')
                    Screen.blit(CaRi,(0,0))
                    if 0 <= clic <= 9 :
                        text = font.render(str(clic), True, (223, 232, 240))
                        Screen.blit(text,(210,75))
                    elif 10 <= clic <= 99 :
                        text = font.render(str(clic), True, (223, 232, 240))
                        Screen.blit(text,(195,75))
                    if 0 <= sec - int(timer - timerref) <= 9 :
                        text = font.render(str(sec - int(timer - timerref)), True, (223, 232, 240))
                        Screen.blit(text,(795,75))
                    elif 10 <= sec - int(timer - timerref) <= 99 :
                        text = font.render(str(sec - int(timer - timerref)), True, (223, 232, 240))
                        Screen.blit(text,(785,75))
                    timer = time.time()
                    print(int(timer - timerref))
                    if int(timer - timerref) == sec :
                        temps = True
                    clock.tick(120000)
                    pygame.display.update()
        if objectif <= clic :
            CaRi = pygame.image.load('mini/spam/victoire.png')
            Screen.blit(CaRi,(0,0))
            clock.tick(120000)
            pygame.display.update()
            pygame.time.wait(3000)
            game = False
        if temps == True :
            CaRi = pygame.image.load('mini/spam/defaite.png')
            Screen.blit(CaRi,(0,0))
            clock.tick(120000)
            pygame.display.update()
            pygame.time.wait(3000)
            game = False
        CaRi = pygame.image.load('mini/spam/off.png')
        Screen.blit(CaRi,(0,0))
        if 0 <= clic <= 9 :
            text = font.render(str(clic), True, (223, 232, 240))
            Screen.blit(text,(210,75))
        elif 10 <= clic <= 99 :
            text = font.render(str(clic), True, (223, 232, 240))
            Screen.blit(text,(195,75))
        if 0 <= sec - int(timer - timerref) <= 9 :
            text = font.render(str(sec - int(timer - timerref)), True, (223, 232, 240))
            Screen.blit(text,(795,75))
        elif 10 <= sec - int(timer - timerref) <= 99 :
            text = font.render(str(sec - int(timer - timerref)), True, (223, 232, 240))
            Screen.blit(text,(785,75))
        clock.tick(120000)
        pygame.display.update()

def Archer() :
    Hit1 = False
    Hit2 = False
    sec = 10
    tic = 0
    tic2 = 0
    timerref = time.time()
    font = pygame.font.SysFont("Myriad Pro", 72)
    y = 0-randint(20,130)
    y2 = 0-randint(20,130)
    start = randint((0-1175),(0-575))
    start2 = randint((0-1350),(0-650))
    bg = pygame.image.load('mini/archer/bg.png')
    target = pygame.image.load('mini/archer/cible.png')
    target2 = pygame.image.load('mini/archer/cible 2.png')
    fg = pygame.image.load('mini/archer/fg.png')
    Screen.blit(target,(start,y))
    Screen.blit(target2,(start2,y2))
    Screen.blit(bg,(0,0))
    Screen.blit(fg,(0,0))
    pygame.display.update()
    game = True
    while game == True :
        timer = time.time()
        tic += 1
        if 1 <= tic <= 5:
            y += 3
            y2 += 3
        if 6 <= tic <= 10:
            y -= 3
            y2 -= 3
        if tic == 10 :
            tic = 0
        start2 += randrange((3+int(timer - timerref)),(14+int(timer - timerref)))
        start += randrange((3+int(timer - timerref)),(14+int(timer - timerref)))
        HitBox1X = (start+500)
        HitBox1Y = (y+500)
        HitBox2X = (start2+500)
        HitBox2Y = (y2+357)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                h,v = pygame.mouse.get_pos()
                h2,v2 = pygame.mouse.get_pos()
                sqh = (h - HitBox1X)**2
                sqh2 = (h2 - HitBox2X)**2
                sqv = (v - HitBox1Y)**2
                sqv2 = (v2 - HitBox2Y)**2
                if math.sqrt(sqh + sqv) < 88:
                    print('NICE ! CAESAR CHAN ! 1st Target !')
                    Hit1 = True
                if math.sqrt(sqh2 + sqv2) < 88:
                    print('NICE ! CAESAR CHAN ! 2nd Target !')
                    Hit2 = True
        if Hit1 == True  :
            y = 0-randint(20,130)
            start = randint((0-1000),100)
            Hit1 = False
        if Hit2 == True  :
            y2 = 0-randint(20,130)
            start2 = randint((0-1000),100)
            Hit2 = False
        if start >= 600 or start2 >= 600 :
            print('PERDU')
            t = pygame.image.load('mini/archer/defaite.png')
            Screen.blit(t,(0,0))
            clock.tick(120000)
            pygame.display.update()
            pygame.time.wait(3000)
            game = False
        if (sec - int(timer - timerref))<= 0 :
            print('GAGNE')
            t = pygame.image.load('mini/archer/victoire.png')
            Screen.blit(t,(0,0))
            clock.tick(120000)
            pygame.display.update()
            pygame.time.wait(3000)
            game = False
        pygame.draw.circle(Screen, (0, 0, 0),(HitBox2X,HitBox2Y), 88)
        pygame.draw.circle(Screen, (0, 0, 0),(HitBox1X,HitBox1Y), 88)
        Screen.blit(bg,(0,0))
        Screen.blit(target2,(start2,y2))
        Screen.blit(target,(start,y))
        Screen.blit(fg,(0,0))
        text = font.render(str(sec - int(timer - timerref))+"''", True, (223, 232, 240))
        Screen.blit(text,(465,10))
        pygame.display.update()

##Les Loop de jeu
def gameloop(Liste_Case, nb_joueur, symbolJ1 , symbolJ2, symbolJ3 , symbolJ4,currentplayer, action) :
    plateau(Liste_Case, nb_joueur, symbolJ1 , symbolJ2, symbolJ3 , symbolJ4)
    clock=pygame.time.Clock()
    GameExit = False
    while not GameExit :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                GameExit = True
        for i in range(0,len(Liste_Joueur)):
            if Liste_Joueur[i].pvactuel <= 0 :
                Liste_Joueur[i].mort = True
                Liste_Joueur[i].symbol = 'dead'
        ##Tour J1
        if currentplayer == 1 :
            pygame.display.update()
            if action[0] == False  :
                refresh_plateau()
                HUDDebut = pygame.image.load('HUD/J1 - Begin.png')
                Screen.blit(HUDDebut,(0,0))
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_SPACE:
                            refresh_plateau()
                            action[0] = True
                    if event.type == pygame.QUIT:
                        GameExit = True
            if action[0] == True :
                if event.type == pygame.QUIT:
                     GameExit = True
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q and Liste_Joueur[currentplayer - 1].mort == False  :
                        actual_dice = dice()
                        if actual_dice == 1 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice1.png')
                            Liste_Joueur[0].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[0].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[0],Liste_Case)
                            action[1] = True
                        if actual_dice == 2 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice2.png')
                            Liste_Joueur[0].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[0].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[0],Liste_Case)
                            action[1] = True
                        if actual_dice == 3 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice3.png')
                            Liste_Joueur[0].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[0].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[0],Liste_Case)
                            action[1] = True
                        if actual_dice == 4 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice4.png')
                            Liste_Joueur[0].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[0].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[0],Liste_Case)
                            action[1] = True
                        if actual_dice == 5 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice5.png')
                            Liste_Joueur[0].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[0].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[0],Liste_Case)
                            action[1] = True
                        if actual_dice == 6 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice6.png')
                            Liste_Joueur[0].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[0].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[0],Liste_Case)
                            action[1] = True
                    if Liste_Joueur[currentplayer - 1].mort == True :
                         skull =  pygame.image.load('HUD/skull.png')
                         Screen.blit(skull,(0,0))
                         pygame.display.update()
                    if event.key == pygame.K_w :
                        currentplayer +=1
                        if currentplayer > nb_joueur :
                            currentplayer = 1
                        action[0] = False
                        action[1] = False
        ##Tour J2
        if currentplayer == 2 :
            pygame.display.update()
            if action[0] == False :
                refresh_plateau()
                HUDDebut = pygame.image.load('HUD/J2 - Begin.png')
                Screen.blit(HUDDebut,(0,0))
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_SPACE:
                            refresh_plateau()
                            action[0] = True
            if action[0] == True :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q and Liste_Joueur[currentplayer - 1].mort == False :
                        actual_dice = dice()
                        if actual_dice == 1 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice1.png')
                            Liste_Joueur[1].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[1].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[1],Liste_Case)
                            action[1] = True
                        if actual_dice == 2 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice2.png')
                            Liste_Joueur[1].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[1].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[1],Liste_Case)
                            action[1] = True
                        if actual_dice == 3 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice3.png')
                            Liste_Joueur[1].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[1].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[1],Liste_Case)
                            action[1] = True
                        if actual_dice == 4 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice4.png')
                            Liste_Joueur[1].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[1].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[1],Liste_Case)
                            action[1] = True
                        if actual_dice == 5 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice5.png')
                            Liste_Joueur[1].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[1].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[1],Liste_Case)
                            action[1] = True
                        if actual_dice == 6 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice6.png')
                            Liste_Joueur[1].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[1].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[1],Liste_Case)
                            action[1] = True
                    if Liste_Joueur[currentplayer - 1].mort == True :
                         skull =  pygame.image.load('HUD/skull.png')
                         Screen.blit(skull,(0,0))
                         pygame.display.update()
                    if event.key == pygame.K_w :
                        currentplayer +=1
                        if currentplayer > nb_joueur :
                            currentplayer = 1
                        action[0] = False
                        action[1] = False
        ##Tour J3
        if currentplayer == 3 :
            pygame.display.update()
            if action[0] == False :
                refresh_plateau()
                HUDDebut = pygame.image.load('HUD/J3 - Begin.png')
                Screen.blit(HUDDebut,(0,0))
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_SPACE:
                            refresh_plateau()
                            action[0] = True
            if action[0] == True :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q and Liste_Joueur[currentplayer - 1].mort == False :
                        actual_dice = dice()
                        if actual_dice == 1 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice1.png')
                            Liste_Joueur[2].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[2].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[2],Liste_Case)
                            action[1] = True
                        if actual_dice == 2 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice2.png')
                            Liste_Joueur[2].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[2].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[2],Liste_Case)
                            action[1] = True
                        if actual_dice == 3 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice3.png')
                            Liste_Joueur[2].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[2].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[2],Liste_Case)
                            action[1] = True
                        if actual_dice == 4 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice4.png')
                            Liste_Joueur[2].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[2].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[2],Liste_Case)
                            action[1] = True
                        if actual_dice == 5 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice5.png')
                            Liste_Joueur[2].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[2].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[2],Liste_Case)
                            action[1] = True
                        if actual_dice == 6 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice6.png')
                            Liste_Joueur[2].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[2].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[2],Liste_Case)
                            action[1] = True
                    if Liste_Joueur[currentplayer - 1].mort == True :
                         skull =  pygame.image.load('HUD/skull.png')
                         Screen.blit(skull,(0,0))
                         pygame.display.update()
                    if event.key == pygame.K_w :
                        currentplayer +=1
                        if currentplayer > nb_joueur :
                            currentplayer = 1
                        action[0] = False
                        action[1] = False
        ##Tour J4
        if currentplayer == 4 :
            pygame.display.update()
            if action[0] == False :
                refresh_plateau()
                HUDDebut = pygame.image.load('HUD/J4 - Begin.png')
                Screen.blit(HUDDebut,(0,0))
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_SPACE:
                            refresh_plateau()
                            action[0] = True
            if action[0] == True :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q and Liste_Joueur[currentplayer - 1].mort == False :
                        actual_dice = dice()
                        if actual_dice == 1 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice1.png')
                            Liste_Joueur[3].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[3].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[3],Liste_Case)
                            action[1] = True
                        if actual_dice == 2 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice2.png')
                            Liste_Joueur[3].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[3].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[3],Liste_Case)
                            action[1] = True
                        if actual_dice == 3 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice3.png')
                            Liste_Joueur[3].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[3].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[3],Liste_Case)
                            action[1] = True
                        if actual_dice == 4 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice4.png')
                            Liste_Joueur[3].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[3].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[3],Liste_Case)
                            action[1] = True
                        if actual_dice == 5 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice5.png')
                            Liste_Joueur[3].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[3].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[3],Liste_Case)
                            action[1] = True
                            pygame.display.update()
                        if actual_dice == 6 and action[1]  == False :
                            refresh_plateau()
                            de =  pygame.image.load('Dice/dice6.png')
                            Liste_Joueur[3].move(Liste_Case,actual_dice)
                            refresh_plateau()
                            Screen.blit(de,(0,0))
                            for i in range(1,32):
                                if i == Liste_Joueur[3].avance :
                                    Liste_Case[i].evenementactive(Liste_Joueur[3],Liste_Case)
                            action[1] = True
                            pygame.display.update()
                    if Liste_Joueur[currentplayer - 1].mort == True :
                         skull =  pygame.image.load('HUD/skull.png')
                         Screen.blit(skull,(0,0))
                         pygame.display.update()
                    if event.key == pygame.K_w :
                        currentplayer +=1
                        if currentplayer > nb_joueur :
                            currentplayer = 1
                        action[0] = False
                        action[1] = False
        if nb_joueur == 2 :
            if Liste_Joueur[0].mort == True :
                skull =  pygame.image.load('HUD/Boss Battle - J2 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
            if Liste_Joueur[1].mort == True :
                skull =  pygame.image.load('HUD/Boss Battle - J1 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
        if nb_joueur == 3 :
            if Liste_Joueur[0].mort == True and Liste_Joueur[2].mort == True :
                skull =  pygame.image.load('HUD/Boss Battle - J2 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
            if Liste_Joueur[1].mort == True and Liste_Joueur[2].mort == True :
                skull =  pygame.image.load('HUD/Boss Battle - J1 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
            if Liste_Joueur[1].mort == True and Liste_Joueur[0].mort == True :
                skull =  pygame.image.load('HUD/Boss Battle - J3 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
        if nb_joueur == 4 :
            if Liste_Joueur[0].mort == True and Liste_Joueur[2].mort == True and Liste_Joueur[3].mort == True:
                skull =  pygame.image.load('HUD/Boss Battle - J2 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
            if Liste_Joueur[1].mort == True and Liste_Joueur[2].mort == True and Liste_Joueur[3].mort == True:
                skull =  pygame.image.load('HUD/Boss Battle - J1 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
            if Liste_Joueur[1].mort == True and Liste_Joueur[0].mort == True and Liste_Joueur[3].mort == True:
                skull =  pygame.image.load('HUD/Boss Battle - J3 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
            if Liste_Joueur[1].mort == True and Liste_Joueur[0].mort == True and Liste_Joueur[2].mort == True:
                skull =  pygame.image.load('HUD/Boss Battle - J4 Win.png')
                Screen.blit(skull,(0,0))
                pygame.display.update()
                pygame.time.wait(3000)
                GameExit = True
        pygame.display.update()
        clock.tick(120000)

def selec_joueur(Liste_Case,nb_joueur,symbolJ1 , symbolJ2, symbolJ3 , symbolJ4) :
    SelecMenu = False
    clock=pygame.time.Clock()
    while not SelecMenu :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                SelecMenu = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    print('Jouer')
                    currentplayer = 1
                    action = [False,False]
                    gameloop(Liste_Case, nb_joueur, symbolJ1 , symbolJ2, symbolJ3 , symbolJ4,currentplayer,action)
                    SelecMenu = True
        #Nombre de joueur
            #Fleche w/ Mouse
            if event.type == pygame.MOUSEBUTTONUP :
                x,y = pygame.mouse.get_pos()
                if 150 < x < 218 and 125 < y < 150 :
                    print('noice')
                    if nb_joueur == 2 :
                        nb_joueur = 2
                    else :
                        nb_joueur -= 1
                if 295 < x < 360 and 125 < y < 150 :
                    print('noice')
                    if nb_joueur == 4 :
                        nb_joueur = 4
                    else :
                        nb_joueur += 1
            #Fleche w/ Key
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    print('noice')
                    if nb_joueur == 2 :
                        nb_joueur = 2
                    else :
                        nb_joueur -= 1
                if event.key == pygame.K_RIGHT :
                    print('noice')
                    if nb_joueur == 4 :
                        nb_joueur = 4
                    else :
                        nb_joueur += 1
            ##Pion
             ##J1
            if event.type == pygame.MOUSEBUTTONUP :
                x,y = pygame.mouse.get_pos()
                if 143 < x < 178 and 278 < y < 292 :
                    print('noice gauche')
                    if symbolJ1 == 1 :
                        symbolJ1 = 1
                    else :
                        symbolJ1 -= 1
                if 230 < x < 263 and 278 < y < 292 :
                    print('noice droit')
                    if symbolJ1 == 4 :
                        symbolJ1 = 4
                    else :
                        symbolJ1 += 1
            ##J2
            if event.type == pygame.MOUSEBUTTONUP :
                x,y = pygame.mouse.get_pos()
                if 143 < x < 178 and 360 < y < 380 :
                    print('noice gauche')
                    if symbolJ2 == 1 :
                        symbolJ2 = 1
                    else :
                        symbolJ2 -= 1
                if 230 < x < 263 and 360 < y < 380 :
                    print('noice droit')
                    if symbolJ2 == 4 :
                        symbolJ2 = 4
                    else :
                        symbolJ2 += 1
            ##J3
            if event.type == pygame.MOUSEBUTTONUP :
                x,y = pygame.mouse.get_pos()
                if 143 < x < 178 and 430 < y < 450 :
                    print('noice gauche')
                    if symbolJ3 == 1 :
                        symbolJ3 = 1
                    else :
                        symbolJ3 -= 1
                if 230 < x < 263 and 430 < y < 450 :
                    print('noice droit')
                    if symbolJ3 == 4 :
                        symbolJ3 = 4
                    else :
                        symbolJ3 += 1
            ##J4
            if event.type == pygame.MOUSEBUTTONUP :
                x,y = pygame.mouse.get_pos()
                if 143 < x < 178 and 502 < y < 521 :
                    print('noice gauche')
                    if symbolJ4 == 1 :
                        symbolJ4 = 1
                    else :
                        symbolJ4 -= 1
                if 230 < x < 263 and 502 < y < 521 :
                    print('noice droit')
                    if symbolJ4 == 4 :
                        symbolJ4 = 4
                    else :
                        symbolJ4 += 1
        #Affichage Mode
        if nb_joueur == 2 :
            BackgroundSelecJoueur = pygame.image.load('Menu/Selection/Mode 2J.png')
            Screen.blit(BackgroundSelecJoueur,(0,0))
        if nb_joueur == 3 :
            BackgroundSelecJoueur = pygame.image.load('Menu/Selection/Mode 3J.png')
            Screen.blit(BackgroundSelecJoueur,(0,0))
        if nb_joueur == 4 :
            BackgroundSelecJoueur = pygame.image.load('Menu/Selection/Mode 4J.png')
            Screen.blit(BackgroundSelecJoueur,(0,0))
    #Affichage Pion
        #J1
        if symbolJ1 == 1 :
            pion = pygame.image.load('Pion/Jaune Shield.png')
            Screen.blit(pion,(185,269))
        if symbolJ1 == 2 :
            pion = pygame.image.load('Pion/Jaune Bow.png')
            Screen.blit(pion,(185,269))
        if symbolJ1 == 3 :
            pion = pygame.image.load('Pion/Jaune Sword.png')
            Screen.blit(pion,(185,269))
        if symbolJ1 == 4 :
            pion = pygame.image.load('Pion/Jaune Wizard.png')
            Screen.blit(pion,(185,269))
        #J2
        if symbolJ2 == 1 :
            pion = pygame.image.load('Pion/Bleu Shield.png')
            Screen.blit(pion,(185,353))
        if symbolJ2 == 2 :
            pion = pygame.image.load('Pion/Bleu Bow.png')
            Screen.blit(pion,(185,353))
        if symbolJ2 == 3 :
            pion = pygame.image.load('Pion/Bleu Sword.png')
            Screen.blit(pion,(185,353))
        if symbolJ2 == 4 :
            pion = pygame.image.load('Pion/Bleu Wizard.png')
            Screen.blit(pion,(185,353))
        #J3
        if nb_joueur >= 3 :
            if symbolJ3 == 1 :
                pion = pygame.image.load('Pion/Violet Shield.png')
                Screen.blit(pion,(185,423))
            if symbolJ3 == 2 :
                pion = pygame.image.load('Pion/Violet Bow.png')
                Screen.blit(pion,(185,423))
            if symbolJ3 == 3 :
                pion = pygame.image.load('Pion/Violet Sword.png')
                Screen.blit(pion,(185,423))
            if symbolJ3 == 4 :
                pion = pygame.image.load('Pion/Violet Wizard.png')
                Screen.blit(pion,(185,423))
        #J4
        if nb_joueur == 4 :
            if symbolJ4 == 1 :
                pion = pygame.image.load('Pion/Vert Shield.png')
                Screen.blit(pion,(185,490))
            if symbolJ4 == 2 :
                pion = pygame.image.load('Pion/Vert Bow.png')
                Screen.blit(pion,(185,490))
            if symbolJ4 == 3 :
                pion = pygame.image.load('Pion/Vert Sword.png')
                Screen.blit(pion,(185,490))
            if symbolJ4 == 4 :
                pion = pygame.image.load('Pion/Vert Wizard.png')
                Screen.blit(pion,(185,490))
        next = pygame.image.load('Menu/Selection/Appuyer sur Espace.png')
        Screen.blit(next,(0,0))
        clock.tick(120000)
        pygame.display.update()

def menu(Liste_Case) :
    clock=pygame.time.Clock()
    pluie = Rain()
    groupe_de_pluie = pygame.sprite.Group(pluie)
    MenuAnim = False
    while not MenuAnim :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                MenuAnim = True
            ##Jouer
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    nb_joueur = 2
                    symbolJ1 = 1
                    symbolJ2 = 1
                    symbolJ3 = 1
                    symbolJ4 = 1
                    print('Jouer')
                    selec_joueur(Liste_Case, nb_joueur, symbolJ1 , symbolJ2, symbolJ3 , symbolJ4)
                    MenuAnim = True
            if event.type == pygame.MOUSEBUTTONUP :
                x,y = pygame.mouse.get_pos()
                if 68 < x < 400 and 650 < y < 777 :
                    nb_joueur = 2
                    symbolJ1 = 1
                    symbolJ2 = 1
                    symbolJ3 = 1
                    symbolJ4 = 1
                    print('Jouer')
                    selec_joueur(Liste_Case, nb_joueur,symbolJ1 , symbolJ2, symbolJ3 , symbolJ4)
                    MenuAnim = True
            if event.type == pygame.MOUSEBUTTONUP :
                x,y = pygame.mouse.get_pos()
                if 600 < x < 930 and 650 < y < 777 :
                    nb_joueur = 2
                    symbolJ1 = 1
                    symbolJ2 = 1
                    symbolJ3 = 1
                    symbolJ4 = 1
                    print('Regles')
                    selec_joueur(Liste_Case, nb_joueur,symbolJ1 , symbolJ2, symbolJ3 , symbolJ4)
                    MenuAnim = True
        TitleBackground = pygame.image.load("Menu/Title Screen - Background.png")
        Screen.blit(TitleBackground,(0,0))
        groupe_de_pluie.update()
        groupe_de_pluie.draw(Screen)
        Buttons = pygame.image.load('Menu/Title Screen - Buttons.png')
        Screen.blit(Buttons,(0,0))
        Title = pygame.image.load('Menu/Title Screen - Title.png')
        Screen.blit(Title,(0,0))
        clock.tick(120000)
        pygame.display.update()

## Main()
#Debut
pygame.init()
#Debut

dx = 1000
dy = 800
Liste_Case = []
Liste_Joueur = []
Screen = pygame.display.set_mode((dx,dy), pygame.DOUBLEBUF)
Screen.set_alpha(None)
pygame.display.set_caption('Knights and Goblins')
clock = pygame.time.Clock()
menu(Liste_Case)

#Fin
pygame.quit()
#Fin
