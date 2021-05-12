import random
import sys

import pygame
from pygame import *

# ====================================   GLOBAL VARIABLES  ==================


SCREENHEIGHT = 600
SCREENWIDTH = 1000
icon = pygame.image.load('ludoicon.ico')
pygame.display.set_icon(icon)
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS ={}
FPS = 30
diceOut = 0

r1x,r1y = 272,77
r2x,r2y = 371,77
r3x,r3y = 272, 163
r4x,r4y  = 371, 163

g1x,g1y  = 616,423
g2x,g2y = 708,423
g3x,g3y  = 708,506
g4x,g4y = 616, 506

r1Open = False
r2Open = False
r3Open = False
r4Open = False

g1Open = False
g2Open = False
g3Open = False
g4Open = False

r1Passed = False
r2Passed = False
r3Passed = False
r4Passed = False
  
g1Passed = False
g2Passed = False
g3Passed = False
g4Passed = False

r1num,r2num,r3num,r4num = 11,12,13,14
g1num,g2num,g3num,g4num = 21,22,23,24

notChose = True
redTurn = True

# ========================   MOVING FUNC    =====================

def move1(piece):

    global r1x, r2x, r3x, r4x, r1y, r2y, r3y, r4y, g1x, g2x, g3x, g4x, g1y, g2y, g3y, g4y,diceOut
    global r1Passed,r2Passed,r3Passed,r4Passed,g1Passed,g2Passed,g3Passed,g4Passed
    global r1Open,r2Open,r3Open,r4Open,g1Open,g2Open,g3Open,g4Open
    global r1num,r2num,r3num,r4num,g1num,g2num,g4num,g3num
    

    if piece == reD[0]:

        #  ==========   moves  ============
        

        if ((r1x>239 and r1y > 229) and (r1x <420 and r1y <271)):
            r1x+=32
            r1num+=1


        if ((r1x>427 and r1y > 33) and (r1x <475 and r1y <220)):
            r1y-= 32
            r1num+=1

        if ((r1x>523 and r1y > 33) and (r1x <571 and r1y <225)): 
            r1y+=32
            r1num+=1

        if ((r1x>577 and r1y > 226) and (r1x <761 and r1y <272)): 
            r1x+=31
            r1num+=1

        if ((r1x>580 and r1y > 327) and (r1x <762 and r1y <370)): 
            r1x-=31
            r1num+=1

        if ((r1x>527 and r1y > 376) and (r1x <575 and r1y <564)):
            r1y+=31
            r1num+=1

        if ((r1x>423 and r1y > 377) and (r1x <477 and r1y <588)): 
            r1y-=31
            r1num+=1

        if ((r1x>238 and r1y > 327) and (r1x <420 and r1y <370)): 
            r1x-=31
            r1num+=1

        if ((r1x>269 and r1y > 276) and (r1x <423 and r1y <324)): 
            r1x+=32
            r1num+=1

        if r1x== 485 and r1y ==38: 
            r1x+=45
            r1num+=1

        if r1x == 738 and r1y == 293: 
            r1y+=45
            r1num+=1

        if r1x == 487 and r1y == 537: 
            r1x-=45 
            r1num+=1

        if r1x == 239 and r1y == 292: 
            r1x +=32
            r1num=100

        # ========  Turns  ===========

        if ((r1x>425 and r1y > 228) and (r1x <464 and r1y <268)): 
            r1x = 439
            r1y = 197
            r1num=201

        if ((r1x>427 and r1y > 0) and (r1x <475 and r1y <30)): 
            r1x = 485
            r1y = 38

        if ((r1x>525 and r1y > 225) and (r1x <576 and r1y <276)): 
            r1x = 580
            r1y = 240
            r1num=301

        if ((r1x>764 and r1y > 227) and (r1x <801 and r1y <275)): 
            r1x = 738
            r1y = 293
    
        if ((r1x>531 and r1y > 329) and (r1x <577 and r1y <375)): 
            r1x = 539
            r1y = 380
            r1num=401
        
        if ((r1x>527 and r1y > 565) and (r1x <577 and r1y <598)): 
            r1x = 487
            r1y = 537

        if ((r1x>425 and r1y > 326) and (r1x <477 and r1y <376)): 
            r1x = 395
            r1y = 338
            r1num=501
        
        if ((r1x>201 and r1y > 327) and (r1x <235 and r1y <374)): 
            r1x = 239
            r1y = 292

        #==========   Check WiN   ====================

        if ((r1x>428 and r1y > 289) and (r1x <435 and r1y <298)):r1Passed = True
        if r1Passed:
            GAME_SOUNDS['pass'].play()
            r1x+=2
            
    if piece == reD[1]:

        #  ==========   moves  ============
        

        if ((r2x>239 and r2y > 229) and (r2x <420 and r2y <271)):
            r2x+=32
            r2num+=1

        if ((r2x>427 and r2y > 33) and (r2x <475 and r2y <220)):
            r2y-= 32
            r2num+=1

        if ((r2x>523 and r2y > 33) and (r2x <571 and r2y <225)): 
            r2y+=32
            r2num+=1

        if ((r2x>577 and r2y > 226) and (r2x <761 and r2y <272)):
            r2x+=31
            r2num+=1

        if ((r2x>580 and r2y > 327) and (r2x <762 and r2y <370)):
            r2x-=31
            r2num+=1

        if ((r2x>527 and r2y > 376) and (r2x <575 and r2y <564)): 
            r2y+=31
            r2num+=1

        if ((r2x>423 and r2y > 377) and (r2x <477 and r2y <588)): 
            r2y-=31
            r2num+=1

        if ((r2x>238 and r2y > 327) and (r2x <420 and r2y <370)): 
            r2x-=31
            r2num+=1

        if ((r2x>269 and r2y > 276) and (r2x <423 and r2y <324)): 
            r2x+=32
            r2num+=1

        if r2x== 485 and r2y ==38: 
            r2x+=45
            r2num+=1

        if r2x == 738 and r2y == 293: 
            r2y+=45
            r2num+=1

        if r2x == 487 and r2y == 537: 
            r2x-=45 
            r2num+=1

        if r2x == 239 and r2y == 292: 
            r2x +=32
            r2num=100

        # ========  Turns  ===========

        if ((r2x>425 and r2y > 228) and (r2x <464 and r2y <268)): 
            r2x = 439
            r2y = 197
            r2num = 201

        if ((r2x>427 and r2y > 0) and (r2x <475 and r2y <30)): 
            r2x = 485
            r2y = 38

        if ((r2x>525 and r2y > 225) and (r2x <576 and r2y <276)): 
            r2x = 580
            r2y = 240
            r2num = 301

        if ((r2x>764 and r2y > 227) and (r2x <801 and r2y <275)): 
            r2x = 738
            r2y = 293
    
        if ((r2x>531 and r2y > 329) and (r2x <577 and r2y <375)): 
            r2x = 539
            r2y = 380
            r2num = 401
        
        if ((r2x>527 and r2y > 565) and (r2x <577 and r2y <598)): 
            r2x = 487
            r2y = 537

        if ((r2x>425 and r2y > 326) and (r2x <477 and r2y <376)): 
            r2x = 395
            r2y = 338
            r2num = 501
        
        if ((r2x>201 and r2y > 327) and (r2x <235 and r2y <374)): 
            r2x = 239
            r2y = 292

        #==========   Check WiN   ====================

        if ((r2x>428 and r2y > 289) and (r2x <435 and r2y <298)):r2Passed = True
        if r2Passed:
            GAME_SOUNDS['pass'].play()
            r2x+=2

    if piece == reD[2]:

        #  ==========   moves  ============
        

        if ((r3x>239 and r3y > 229) and (r3x <420 and r3y <271)):
            r3x+=32
            r3num+=1

        if ((r3x>427 and r3y > 33) and (r3x <475 and r3y <220)):
            r3y-= 32
            r3num+=1

        if ((r3x>523 and r3y > 33) and (r3x <571 and r3y <225)):
            r3y+=32
            r3num+=1

        if ((r3x>577 and r3y > 226) and (r3x <761 and r3y <272)): 
            r3x+=31
            r3num+=1

        if ((r3x>580 and r3y > 327) and (r3x <762 and r3y <370)):
            r3x-=31
            r3num+=1

        if ((r3x>527 and r3y > 376) and (r3x <575 and r3y <564)): 
            r3y+=31
            r3num+=1

        if ((r3x>423 and r3y > 377) and (r3x <477 and r3y <588)):
            r3y-=31
            r3num+=1

        if ((r3x>238 and r3y > 327) and (r3x <420 and r3y <370)): 
            r3x-=31
            r3num+=1

        if ((r3x>269 and r3y > 276) and (r3x <423 and r3y <324)):
            r3x+=32
            r3num+=1

        if r3x== 485 and r3y ==38: 
            r3x+=45
            r3num+=1

        if r3x == 738 and r3y == 293: 
            r3y+=45
            r3num+=1

        if r3x == 487 and r3y == 537: 
            r3x-=45 
            r3num+=1

        if r3x == 239 and r3y == 292: 
            r3x +=32
            r3num=100

        # ========  Turns  ===========

        if ((r3x>425 and r3y > 228) and (r3x <464 and r3y <268)): 
            r3x = 439
            r3y = 197
            r3num = 201

        if ((r3x>427 and r3y > 0) and (r3x <475 and r3y <30)): 
            r3x = 485
            r3y = 38

        if ((r3x>525 and r3y > 225) and (r3x <576 and r3y <276)): 
            r3x = 580
            r3y = 240
            r3num = 301

        if ((r3x>764 and r3y > 227) and (r3x <801 and r3y <275)): 
            r3x = 738
            r3y = 293
    
        if ((r3x>531 and r3y > 329) and (r3x <577 and r3y <375)): 
            r3x = 539
            r3y = 380
            r3num = 401
        
        if ((r3x>527 and r3y > 565) and (r3x <577 and r3y <598)): 
            r3x = 487
            r3y = 537

        if ((r3x>425 and r3y > 326) and (r3x <477 and r3y <376)): 
            r3x = 395
            r3y = 338
            r3num = 501
        
        if ((r3x>201 and r3y > 327) and (r3x <235 and r3y <374)): 
            r3x = 239
            r3y = 292

        #==========   Check WiN   ====================

        if ((r3x>428 and r3y > 289) and (r3x <435 and r3y <298)):r3Passed = True
        if r3Passed:
            GAME_SOUNDS['pass'].play()
            r3x+=2

    if piece == reD[3]:

        #  ==========   moves  ============
        

        if ((r4x>239 and r4y > 229) and (r4x <420 and r4y <271)):
            r4x+=32
            r4num+=1

        if ((r4x>427 and r4y > 33) and (r4x <475 and r4y <220)):
            r4y-= 32
            r4num+=1

        if ((r4x>523 and r4y > 33) and (r4x <571 and r4y <225)): 
            r4y+=32
            r4num+=1

        if ((r4x>577 and r4y > 226) and (r4x <761 and r4y <272)):
            r4x+=31
            r4num+=1

        if ((r4x>580 and r4y > 327) and (r4x <762 and r4y <370)): 
            r4x-=31
            r4num+=1

        if ((r4x>527 and r4y > 376) and (r4x <575 and r4y <564)):
            r4y+=31
            r4num+=1

        if ((r4x>423 and r4y > 377) and (r4x <477 and r4y <588)): 
            r4y-=31
            r4num+=1

        if ((r4x>238 and r4y > 327) and (r4x <420 and r4y <370)): 
            r4x-=31
            r4num+=1

        if ((r4x>269 and r4y > 276) and (r4x <423 and r4y <324)): 
            r4x+=32
            r4num+=1

        if r4x== 485 and r4y ==38: 
            r4x+=45
            r4num+=1

        if r4x == 738 and r4y == 293: 
            r4y+=45
            r4num+=1

        if r4x == 487 and r4y == 537: 
            r4x-=45 
            r4num+=1

        if r4x == 239 and r4y == 292: 
            r4x +=32
            r4num=100

        # ========  Turns  ===========

        if ((r4x>425 and r4y > 228) and (r4x <464 and r4y <268)): 
            r4x = 439
            r4y = 197
            r4num = 201

        if ((r4x>427 and r4y > 0) and (r4x <475 and r4y <30)): 
            r4x = 485
            r4y = 38

        if ((r4x>525 and r4y > 225) and (r4x <576 and r4y <276)): 
            r4x = 580
            r4y = 240
            r4num = 301

        if ((r4x>764 and r4y > 227) and (r4x <801 and r4y <275)): 
            r4x = 738
            r4y = 293
    
        if ((r4x>531 and r4y > 329) and (r4x <577 and r4y <375)): 
            r4x = 539
            r4y = 380
            r4num = 401
        
        if ((r4x>527 and r4y > 565) and (r4x <577 and r4y <598)): 
            r4x = 487
            r4y = 537

        if ((r4x>425 and r4y > 326) and (r4x <477 and r4y <376)): 
            r4x = 395
            r4y = 338
            r4num = 501
        
        if ((r4x>201 and r4y > 327) and (r4x <235 and r4y <374)): 
            r4x = 239
            r4y = 292

        #==========   Check WiN   ====================

        if ((r4x>428 and r4y > 289) and (r4x <435 and r4y <298)):r4Passed = True
        if r4Passed:
            GAME_SOUNDS['pass'].play()
            r4x+=1

    
    if piece == greeN[0]:

        #  ==========   moves  ============

        if ((g1x>23-1 and g1y > 229-1) and (g1x <420-1 and g1y <271-1)):
            g1x+=32
            g1num+=1

        if ((g1x>427-1 and g1y > 33-1) and (g1x <475-1 and g1y <220-1)):
            g1y-= 32
            g1num+=1

        if ((g1x>523-1 and g1y > 33-1) and (g1x <571-1 and g1y <225-1)): 
            g1y+=32
            g1num+=1

        if ((g1x>577-1 and g1y > 226-1) and (g1x <761-1 and g1y <272-1)): 
            g1x+=31
            g1num+=1

        if ((g1x>580-1 and g1y > 327-1) and (g1x <762-1 and g1y <370-1)): 
            g1x-=31
            g1num+=1

        if ((g1x>527-1 and g1y > 376-1) and (g1x <575-1 and g1y <564-1)): 
            g1y+=31
            g1num+=1

        if ((g1x>423-1 and g1y > 377-1) and (g1x <477-1 and g1y <588-1)): 
            g1y-=31
            g1num+=1

        if ((g1x>238-1 and g1y > 327-1) and (g1x <420-1 and g1y <370-1)): 
            g1x-=31
            g1num+=1

        if ((g1x>579-1 and g1y > 276-1) and (g1x <732-1 and g1y <327-1)): 
            g1x-=32
            g1num+=1

        if g1x== 485-1 and g1y ==38-1: 
            g1x+=45
            g1num+=1

        if g1x == 487-1 and g1y == 537-1: 
            g1x-=45 
            g1num+=1

        if g1x == 241-1 and g1y == 292-1: 
            g1y -=45
            g1num+=1

        if g1x == 739-1 and g1y == 293-1: 
            g1x-=31
            g1num=800
        # ======== Turns  ===========

        if ((g1x>425-1 and g1y > 228-1) and (g1x <464-1 and g1y <268-1)): 
            g1x = 439-1
            g1y = 197-1
            g1num=201

        if ((g1x>427-1 and g1y > 0-1) and (g1x <475-1 and g1y <30-1)): 
            g1x = 485-1
            g1y = 38-1

        if ((g1x>525-1 and g1y > 225-1) and (g1x <576-1 and g1y <276-1)): 
            g1x = 580-1
            g1y = 240-1
            g1num = 301

        if ((g1x>764-1 and g1y > 227-1) and (g1x <801-1 and g1y <275-1)): 
            g1x = 739-1
            g1y = 293-1
    
        if ((g1x>531-1 and g1y > 329-1) and (g1x <577-1 and g1y <375-1)): 
            g1x = 539-1
            g1y = 380-1
            g1num = 401
        
        if ((g1x>527-1 and g1y > 565-1) and (g1x <577-1 and g1y <598-1)): 
            g1x = 487-1
            g1y = 537-1

        if ((g1x>425-1 and g1y > 326-1) and (g1x <477-1 and g1y <376-1)): 
            g1x = 395-1
            g1y = 338-1
            g1num=501
        
        if ((g1x>201-1 and g1y > 327-1) and (g1x <235-1 and g1y <374-1)): 
            g1x = 241-1
            g1y = 292-1

        #==========   Check WiN   ====================

        if ((g1x>544-1 and g1y > 289-1) and (g1x <554-1 and g1y <301-1 )):g1Passed = True
        if g1Passed:
            GAME_SOUNDS['pass'].play()
            g1x-=2
        
    if piece == greeN[1]:

        #  ==========   moves  ============

        if ((g2x>23-1 and g2y > 229-1) and (g2x <420-1 and g2y <271-1)):
            g2x+=32
            g2num+=1

        if ((g2x>427-1 and g2y > 33-1) and (g2x <475-1 and g2y <220-1)):
            g2y-= 32
            g2num+=1

        if ((g2x>523-1 and g2y > 33-1) and (g2x <571-1 and g2y <225-1)): 
            g2y+=32
            g2num+=1

        if ((g2x>577-1 and g2y > 226-1) and (g2x <761-1 and g2y <272-1)): 
            g2x+=31
            g2num+=1

        if ((g2x>580-1 and g2y > 327-1) and (g2x <762-1 and g2y <370-1)): 
            g2x-=31
            g2num+=1

        if ((g2x>527-1 and g2y > 376-1) and (g2x <575-1 and g2y <564-1)): 
            g2y+=31
            g2num+=1

        if ((g2x>423-1 and g2y > 377-1) and (g2x <477-1 and g2y <588-1)):
            g2y-=31
            g2num+=1

        if ((g2x>238-1 and g2y > 327-1) and (g2x <420-1 and g2y <370-1)): 
            g2x-=31
            g2num+=1

        if ((g2x>579-1 and g2y > 276-1) and (g2x <732-1 and g2y <327-1)):
            g2x-=32
            g2num+=1

        if g2x== 485-1 and g2y ==38-1:
            g2x+=45
            g2num+=1

        if g2x == 487-1 and g2y == 537-1:
            g2x-=45 
            g2num+=1

        if g2x == 241-1 and g2y == 292-1: 
            g2y -=45
            g2num+=1

        if g2x == 739-1 and g2y == 293-1: 
            g2x-=31
            g2num=800
        # ========  Turns  ===========

        if ((g2x>425-1 and g2y > 228-1) and (g2x <464-1 and g2y <268-1)): 
            g2x = 439-1
            g2y = 197-1
            g2num = 201

        if ((g2x>427-1 and g2y > 0-1) and (g2x <475-1 and g2y <30-1)): 
            g2x = 485-1
            g2y = 38-1

        if ((g2x>525-1 and g2y > 225-1) and (g2x <576-1 and g2y <276-1)): 
            g2x = 580-1
            g2y = 240-1
            g2num = 301

        if ((g2x>764-1 and g2y > 227-1) and (g2x <801-1 and g2y <275-1)): 
            g2x = 739-1
            g2y = 293-1
    
        if ((g2x>531-1 and g2y > 329-1) and (g2x <577-1 and g2y <375-1)): 
            g2x = 539-1
            g2y = 380-1
            g2num = 401
        
        if ((g2x>527-1 and g2y > 565-1) and (g2x <577-1 and g2y <598-1)): 
            g2x = 487-1
            g2y = 537-1

        if ((g2x>425-1 and g2y > 326-1) and (g2x <477-1 and g2y <376-1)): 
            g2x = 395-1
            g2y = 338-1
            g2num = 501
        
        if ((g2x>201-1 and g2y > 327-1) and (g2x <235-1 and g2y <374-1)): 
            g2x = 241-1
            g2y = 292-1

        #==========   Check WiN   ====================

        if ((g2x>544-1 and g2y > 289-1) and (g2x <554-1 and g2y <301-1 )):g2Passed = True
        if g2Passed:
            GAME_SOUNDS['pass'].play()
            g2x-=2
        
    if piece == greeN[2]:

        #  ==========   moves  ============

        if ((g3x>23-1 and g3y > 229-1) and (g3x <420-1 and g3y <271-1)):
            g3x+=32
            g3num+=1

        if ((g3x>427-1 and g3y > 33-1) and (g3x <475-1 and g3y <220-1)):
            g3y-= 32
            g3num+=1

        if ((g3x>523-1 and g3y > 33-1) and (g3x <571-1 and g3y <225-1)): 
            g3y+=32
            g3num+=1

        if ((g3x>577-1 and g3y > 226-1) and (g3x <761-1 and g3y <272-1)): 
            g3x+=31
            g3num+=1

        if ((g3x>580-1 and g3y > 327-1) and (g3x <762-1 and g3y <370-1)): 
            g3x-=31
            g3num+=1

        if ((g3x>527-1 and g3y > 376-1) and (g3x <575-1 and g3y <564-1)): 
            g3y+=31
            g3num+=1

        if ((g3x>423-1 and g3y > 377-1) and (g3x <477-1 and g3y <588-1)): 
            g3y-=31
            g3num+=1

        if ((g3x>238-1 and g3y > 327-1) and (g3x <420-1 and g3y <370-1)): 
            g3x-=31
            g3num+=1

        if ((g3x>579-1 and g3y > 276-1) and (g3x <732-1 and g3y <327-1)): 
            g3x-=32
            g3num+=1

        if g3x== 485-1 and g3y ==38-1: 
            g3x+=45
            g3num+=1

        if g3x == 487-1 and g3y == 537-1: 
            g3x-=45 
            g3num+=1

        if g3x == 241-1 and g3y == 292-1: 
            g3y -=45
            g3num+=1

        if g3x == 739-1 and g3y == 293-1: 
            g3x-=31
            g3num=800
        # ========  Turns  ===========

        if ((g3x>425-1 and g3y > 228-1) and (g3x <464-1 and g3y <268-1)): 
            g3x = 439-1
            g3y = 197-1
            g3num = 201

        if ((g3x>427-1 and g3y > 0-1) and (g3x <475-1 and g3y <30-1)): 
            g3x = 485-1
            g3y = 38-1

        if ((g3x>525-1 and g3y > 225-1) and (g3x <576-1 and g3y <276-1)): 
            g3x = 580-1
            g3y = 240-1
            g3num = 301

        if ((g3x>764-1 and g3y > 227-1) and (g3x <801-1 and g3y <275-1)): 
            g3x = 739-1
            g3y = 293-1
    
        if ((g3x>531-1 and g3y > 329-1) and (g3x <577-1 and g3y <375-1)): 
            g3x = 539-1
            g3y = 380-1
            g3num = 401
        
        if ((g3x>527-1 and g3y > 565-1) and (g3x <577-1 and g3y <598-1)): 
            g3x = 487-1
            g3y = 537-1

        if ((g3x>425-1 and g3y > 326-1) and (g3x <477-1 and g3y <376-1)): 
            g3x = 395-1
            g3y = 338-1
            g3num = 501
        
        if ((g3x>201-1 and g3y > 327-1) and (g3x <235-1 and g3y <374-1)): 
            g3x = 241-1
            g3y = 292-1

        #==========   Check WiN   ====================

        if ((g3x>544-1 and g3y > 289-1) and (g3x <554-1 and g3y <301-1 )):g3Passed = True
        if g3Passed:
            GAME_SOUNDS['pass'].play()
            g3x-=2    
            
    if piece == greeN[3]:

        #  ==========   moves  ============

        if ((g4x>23-1 and g4y > 229-1) and (g4x <420-1 and g4y <271-1)):
            g4x+=32
            g4num+=1

        if ((g4x>427-1 and g4y > 33-1) and (g4x <475-1 and g4y <220-1)):
            g4y-= 32
            g4num+=1

        if ((g4x>523-1 and g4y > 33-1) and (g4x <571-1 and g4y <225-1)): 
            g4y+=32
            g4num+=1

        if ((g4x>577-1 and g4y > 226-1) and (g4x <761-1 and g4y <272-1)): 
            g4x+=31
            g4num+=1

        if ((g4x>580-1 and g4y > 327-1) and (g4x <762-1 and g4y <370-1)):
            g4x-=31
            g4num+=1

        if ((g4x>527-1 and g4y > 376-1) and (g4x <575-1 and g4y <564-1)): 
            g4y+=31
            g4num+=1

        if ((g4x>423-1 and g4y > 377-1) and (g4x <477-1 and g4y <588-1)): 
            g4y-=31
            g4num+=1

        if ((g4x>238-1 and g4y > 327-1) and (g4x <420-1 and g4y <370-1)): 
            g4x-=31
            g4num+=1

        if ((g4x>579-1 and g4y > 276-1) and (g4x <732-1 and g4y <327-1)): 
            g4x-=32
            g4num+=1

        if g4x== 485-1 and g4y ==38-1: 
            g4x+=45
            g4num+=1

        if g4x == 487-1 and g4y == 537-1: 
            g4x-=45 
            g4num+=1

        if g4x == 241-1 and g4y == 292-1: 
            g4y -=45
            g4num+=1

        if g4x == 739-1 and g4y == 293-1: 
            g4x-=31
            g4num=800

        # ========  Turns  ===========

        if ((g4x>425-1 and g4y > 228-1) and (g4x <464-1 and g4y <268-1)): 
            g4x = 439-1
            g4y = 197-1
            g4num = 201

        if ((g4x>427-1 and g4y > 0-1) and (g4x <475-1 and g4y <30-1)): 
            g4x = 485-1
            g4y = 38-1

        if ((g4x>525-1 and g4y > 225-1) and (g4x <576-1 and g4y <276-1)): 
            g4x = 580-1
            g4y = 240-1
            g4num = 301

        if ((g4x>764-1 and g4y > 227-1) and (g4x <801-1 and g4y <275-1)): 
            g4x = 739-1
            g4y = 293-1
    
        if ((g4x>531-1 and g4y > 329-1) and (g4x <577-1 and g4y <375-1)): 
            g4x = 539-1
            g4y = 380-1
            g4num = 401
        
        if ((g4x>527-1 and g4y > 565-1) and (g4x <577-1 and g4y <598-1)): 
            g4x = 487-1
            g4y = 537-1

        if ((g4x>425-1 and g4y > 326-1) and (g4x <477-1 and g4y <376-1)): 
            g4x = 395-1
            g4y = 338-1
            g4num = 501
        
        if ((g4x>201-1 and g4y > 327-1) and (g4x <235-1 and g4y <374-1)): 
            g4x = 241-1
            g4y = 292-1

        #==========   Check WiN   ====================

        if ((g4x>544-1 and g4y > 289-1) and (g4x <554-1 and g4y <301-1 )):g4Passed = True
        if g4Passed:
            GAME_SOUNDS['pass'].play()
            g4x-=2
    
    Checkwin()

# =========================   Functions  ==========================

def welcomeScreen():
    while True:
        m_pos = pygame.mouse.get_pos()
        SCREEN.blit(GAME_SPRITES['welcome'],(0,0))
        SCREEN.blit(GAME_SPRITES['exitButton'],(600,400))
        SCREEN.blit(GAME_SPRITES['playButton'],(300,400))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if (m_pos[0]>300 and m_pos[1]>400) and (m_pos[0] < 450 and m_pos[1] < 450):
                SCREEN.blit(GAME_SPRITES['overplay'],(300,400))
                GAME_SOUNDS['point'].play()
                if event.type == MOUSEBUTTONDOWN:
                    GAME_SOUNDS['click'].play()
                    gameLoop()
            if (m_pos[0]>600 and m_pos[1]>400) and (m_pos[0] < 750 and m_pos[1] < 650):
                SCREEN.blit(GAME_SPRITES['overexit'],(600,400))
                GAME_SOUNDS['point'].play()
                if event.type == MOUSEBUTTONDOWN:
                    GAME_SOUNDS['click'].play()
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

def gameLoop():
    global diceOut, notChose,redTurn
    global r1x, r2x, r3x, r4x, r1y, r2y, r3y, r4y, g1x, g2x, g3x, g4x, g1y, g2y, g3y, g4y

    
    
    # =================
    

    SCREEN.blit(GAME_SPRITES['mainGame'],(0,0))
    

    while True:    
        m_pos = pygame.mouse.get_pos()
        SCREEN.blit(GAME_SPRITES['mainGame'],(0,0))
        SCREEN.blit(GAME_SPRITES['backButton'],(100,21))
        greenTurn = not redTurn
        
        SCREEN.blit(GAME_SPRITES['redGoti'][0],(r1x,r1y))
        SCREEN.blit(GAME_SPRITES['redGoti'][1],(r2x,r2y))
        SCREEN.blit(GAME_SPRITES['redGoti'][2],(r3x,r3y))
        SCREEN.blit(GAME_SPRITES['redGoti'][3],(r4x,r4y))
        SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g1x,g1y))
        SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g2x,g2y))
        SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g3x,g3y))
        SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g4x,g4y))


        # This code is for other two colours
        '''
        b1 = SCREEN.blit(GAME_SPRITES['blueGoti'][0],(616,80))
        b2 = SCREEN.blit(GAME_SPRITES['blueGoti'][1],(616,166))
        b3 = SCREEN.blit(GAME_SPRITES['blueGoti'][2],(712,80))
        b4 = SCREEN.blit(GAME_SPRITES['blueGoti'][3],(712,166))
            
        y1 = SCREEN.blit(GAME_SPRITES['yellowGoti'][3],(277, 420))
        y2 = SCREEN.blit(GAME_SPRITES['yellowGoti'][3],(277, 506))
        y3 = SCREEN.blit(GAME_SPRITES['yellowGoti'][3],(373, 420))
        y4 = SCREEN.blit(GAME_SPRITES['yellowGoti'][3],(373, 506))
        '''

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            if (m_pos[0] > 100 and m_pos[1]> 21) and (m_pos[0] < 211 and m_pos[1] < 82):
                SCREEN.blit(GAME_SPRITES['overback'],(100,21))
                GAME_SOUNDS['point'].play()
                if event.type == MOUSEBUTTONDOWN:
                    GAME_SOUNDS['click'].play()
                    welcomeScreen()
            if event.type == KEYDOWN and event.key == K_SPACE:
                if redTurn:
                    GAME_SOUNDS['roll'].play()
                    diceOut = random.randint(0,5)
                    if diceOut != 5:redTurn = False
                    notChose = True
                    redMove()
                    
                if greenTurn:
                    GAME_SOUNDS['roll'].play()
                    diceOut = random.randint(0,5)
                    if diceOut != 5:redTurn = True
                    notChose = True
                    greenMove()
                    
        if redTurn:
            SCREEN.blit(GAME_SPRITES['cover'], (400,-25))
            SCREEN.blit(text2,(410, 10))
        if greenTurn:
            SCREEN.blit(GAME_SPRITES['cover'], (400,-25))
            SCREEN.blit(text3,(410, 10))
        
        
        pygame.display.update()

def redMove():
    global diceOut, r1x, r2x, r3x, r4x, r1y, r2y, r3y, r4y,r1Open,r2Open,r3Open,r4Open,reD,notChose
    global r1num,r2num,r3num,r4num,g1num,g2num,g3num,g4num
    SCREEN.blit(GAME_SPRITES['mainGame'],(0,0))
    

    SCREEN.blit(GAME_SPRITES['redGoti'][0],(r1x,r1y))
    SCREEN.blit(GAME_SPRITES['redGoti'][1],(r2x,r2y))
    SCREEN.blit(GAME_SPRITES['redGoti'][2],(r3x,r3y))
    SCREEN.blit(GAME_SPRITES['redGoti'][3],(r4x,r4y))
    SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g1x,g1y))
    SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g2x,g2y))
    SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g3x,g3y))
    SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g4x,g4y))
    SCREEN.blit(GAME_SPRITES['cover'], (400,-25))
    SCREEN.blit(text2,(410, 10))

    SCREEN.blit(GAME_SPRITES['dice'][diceOut],(100,200 ))
    
    diceOut+=1
    piece = reD[0]
    

    while notChose:
        SCREEN.blit(GAME_SPRITES['backButton'],(100,21))
        
        m_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (m_pos[0] > 100 and m_pos[1]> 21) and (m_pos[0] < 211 and m_pos[1] < 82):
                SCREEN.blit(GAME_SPRITES['overback'],(100,21))
                GAME_SOUNDS['point'].play()
                if event.type == MOUSEBUTTONDOWN:
                    GAME_SOUNDS['click'].play()
                    welcomeScreen()
            if ((not r1Open and not r2Open) and (not r3Open and not r4Open)) and ((not r1Passed and not r2Passed) and (not r3Passed and not r4Passed)):
                notChose = False
            if event.type == MOUSEBUTTONDOWN:
                if not r1Passed:
                    if ((m_pos[0] >r1x and m_pos[1]>r1y) and (m_pos[0] < r1x+reD[0].get_width() and m_pos[1]< r1y+reD[0].get_height())):
                        piece = reD[0]
                        notChose=False
                if not r2Passed:
                    if ((m_pos[0] >r2x and m_pos[1]>r2y) and (m_pos[0] < r2x+reD[0].get_width() and m_pos[1]< r2y+reD[0].get_height())):
                        piece = reD[1]
                        notChose=False
                if not r3Passed:
                    if ((m_pos[0] >r3x and m_pos[1]>r3y) and (m_pos[0] < r3x+reD[0].get_width() and m_pos[1]< r3y+reD[0].get_height())):
                        piece = reD[2]
                        notChose=False
                if not r4Passed:
                    if ((m_pos[0] >r4x and m_pos[1]>r4y) and (m_pos[0] < r4x+reD[0].get_width() and m_pos[1]< r4y+reD[0].get_height())):
                        piece = reD[3]
                        notChose=False
        pygame.display.update()


    if piece==reD[0]:
        if r1Open == False:
            if diceOut == 6:
                r1Open = True
                r1x =269
                r1y = 234
                r1num = 509
                diceOut=0
        if r1Open:
            if diceOut == 1:
                move1(reD[0])
            if diceOut == 2:
                for turn in range(2):
                    move1(reD[0])
            if diceOut == 3:
                for turn in range(3):
                    move1(reD[0])      
            if diceOut == 4:
                for turn in range(4):
                    move1(reD[0])
            if diceOut == 5:
                for turn in range(5):
                    move1(reD[0])
            if diceOut == 6:
                for turn in range(6):
                    move1(reD[0])
    if piece==reD[1]:
        if r2Open == False:
            if diceOut == 6:
                r2Open = True
                r2x =269
                r2y = 236
                r2num=509
                diceOut=0
        if r2Open:
            if diceOut == 1:
                move1(reD[1])
            if diceOut == 2:
                for turn in range(2):
                    move1(reD[1])
            if diceOut == 3:
                for turn in range(3):
                    move1(reD[1])      
            if diceOut == 4:
                for turn in range(4):
                    move1(reD[1])
            if diceOut == 5:
                for turn in range(5):
                    move1(reD[1])
            if diceOut == 6:
                for turn in range(6):
                    move1(reD[1])
    if piece==reD[2]:
        if r3Open == False:
            if diceOut == 6:
                r3Open = True
                r3x =269
                r3y = 232
                r3num = 509
                diceOut=0
        if r3Open:
            if diceOut == 1:
                move1(reD[2])
            if diceOut == 2:
                for turn in range(2):
                    move1(reD[2])
            if diceOut == 3:
                for turn in range(3):
                    move1(reD[2])      
            if diceOut == 4:
                for turn in range(4):
                    move1(reD[2])
            if diceOut == 5:
                for turn in range(5):
                    move1(reD[2])
            if diceOut == 6:
                for turn in range(6):
                    move1(reD[2])
    if piece==reD[3]:
        if r4Open == False:
            if diceOut == 6:
                r4Open = True
                r4x =269
                r4y = 239
                r4num = 509
                diceOut=0
        if r4Open:
            if diceOut == 1:
                move1(reD[3])
            if diceOut == 2:
                for turn in range(2):
                    move1(reD[3])
            if diceOut == 3:
                for turn in range(3):
                    move1(reD[3])      
            if diceOut == 4:
                for turn in range(4):
                    move1(reD[3])
            if diceOut == 5:
                for turn in range(5):
                    move1(reD[3])
            if diceOut == 6:
                for turn in range(6):
                    move1(reD[3])
            
    CheckCut()
    # print(diceOut)
        
def greenMove():
    global diceOut, g1x, g2x, g3x, g4x, g1y, g2y, g3y, g4y,g1Open,g2Open,g3Open,g4Open,notChose
    global r1num,r2num,r3num,r4num,g1num,g2num,g3num,g4num
    SCREEN.blit(GAME_SPRITES['mainGame'],(0,0))

    SCREEN.blit(GAME_SPRITES['redGoti'][0],(r1x,r1y))
    SCREEN.blit(GAME_SPRITES['redGoti'][1],(r2x,r2y))
    SCREEN.blit(GAME_SPRITES['redGoti'][2],(r3x,r3y))
    SCREEN.blit(GAME_SPRITES['redGoti'][3],(r4x,r4y))
    SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g1x,g1y))
    SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g2x,g2y))
    SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g3x,g3y))
    SCREEN.blit(GAME_SPRITES['greenGoti'][3],(g4x,g4y))
    SCREEN.blit(GAME_SPRITES['cover'], (400,-25))
    SCREEN.blit(text3,(410, 10))

    SCREEN.blit(GAME_SPRITES['dice'][diceOut],(800,200 ))
    diceOut+=1
    piece = greeN[0]

    while notChose:
        SCREEN.blit(GAME_SPRITES['backButton'],(100,21))
        
        m_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (m_pos[0] > 100 and m_pos[1]> 21) and (m_pos[0] < 211 and m_pos[1] < 82):
                SCREEN.blit(GAME_SPRITES['overback'],(100,21))
                GAME_SOUNDS['point'].play()
                if event.type == MOUSEBUTTONDOWN:
                    GAME_SOUNDS['click'].play()
                    welcomeScreen()
            if ((not g1Open and not g2Open) and (not g3Open and not g4Open)) and ((not g1Passed and not g2Passed) and (not g3Passed and not g4Passed)):
                notChose = False
            if event.type == MOUSEBUTTONDOWN:
                if not g1Passed:
                    if ((m_pos[0] >g1x and m_pos[1]>g1y) and (m_pos[0] < g1x+greeN[0].get_width() and m_pos[1]< g1y+greeN[0].get_height())):
                        piece = greeN[0]
                        notChose=False
                if not g2Passed:
                    if ((m_pos[0] >g2x and m_pos[1]>g2y) and (m_pos[0] < g2x+greeN[0].get_width() and m_pos[1]< g2y+greeN[0].get_height())):
                        piece = greeN[1]
                        notChose=False
                if not g3Passed:
                    if ((m_pos[0] >g3x and m_pos[1]>g3y) and (m_pos[0] < g3x+greeN[0].get_width() and m_pos[1]< g3y+greeN[0].get_height())):
                        piece = greeN[2]
                        notChose=False
                if not g4Passed:
                    if ((m_pos[0] >g4x and m_pos[1]>g4y) and (m_pos[0] < g4x+greeN[0].get_width() and m_pos[1]< g4y+greeN[0].get_height())):
                        piece = greeN[3]
                        notChose=False
        pygame.display.update()


    if piece==greeN[0]:
        if g1Open == False:
            if diceOut == 6:
                g1Open = True
                g1x =706
                g1y = 341
                g1num=309
                diceOut=0
        if g1Open:
            if diceOut == 1:
                move1(greeN[0])
            if diceOut == 2:
                for turn in range(2):
                    move1(greeN[0])
            if diceOut == 3:
                for turn in range(3):
                    move1(greeN[0])      
            if diceOut == 4:
                for turn in range(4):
                    move1(greeN[0])
            if diceOut == 5:
                for turn in range(5):
                    move1(greeN[0])
            if diceOut == 6:
                for turn in range(6):
                    move1(greeN[0])
    if piece==greeN[1]:
        if g2Open == False:
            if diceOut == 6:
                g2Open = True
                g2x =706
                g2y = 343
                g2num=309
                diceOut=0
        if g2Open:
            if diceOut == 1:
                move1(greeN[1])
            if diceOut == 2:
                for turn in range(2):
                    move1(greeN[1])
            if diceOut == 3:
                for turn in range(3):
                    move1(greeN[1])      
            if diceOut == 4:
                for turn in range(4):
                    move1(greeN[1])
            if diceOut == 5:
                for turn in range(5):
                    move1(greeN[1])
            if diceOut == 6:
                for turn in range(6):
                    move1(greeN[1])
    if piece==greeN[2]:
        if g3Open == False:
            if diceOut == 6:
                g3Open = True
                g3x =706
                g3y = 346
                g3num=309
                diceOut=0
        if g3Open:
            if diceOut == 1:
                move1(greeN[2])
            if diceOut == 2:
                for turn in range(2):
                    move1(greeN[2])
            if diceOut == 3:
                for turn in range(3):
                    move1(greeN[2])      
            if diceOut == 4:
                for turn in range(4):
                    move1(greeN[2])
            if diceOut == 5:
                for turn in range(5):
                    move1(greeN[2])
            if diceOut == 6:
                for turn in range(6):
                    move1(greeN[2])
    if piece==greeN[3]:
        if g4Open == False:
            if diceOut == 6:
                g4Open = True
                g4x =706
                g4y = 339
                g4num=309
                diceOut=0
        if g4Open:
            if diceOut == 1:
                move1(greeN[3])
            if diceOut == 2:
                for turn in range(2):
                    move1(greeN[3])
            if diceOut == 3:
                for turn in range(3):
                    move1(greeN[3])      
            if diceOut == 4:
                for turn in range(4):
                    move1(greeN[3])
            if diceOut == 5:
                for turn in range(5):
                    move1(greeN[3])
            if diceOut == 6:
                for turn in range(6):
                    move1(greeN[3])

    CheckCut()
    # print(diceOut)

def Checkwin():
    font4 = pygame.font.SysFont('comicsans',110)
    if ((r1x>426 and r1y > 274) and (r1x <467 and r1y <321)):
        if ((r2x>426 and r2y > 274) and (r2x <467 and r2y <321)):
            if ((r3x>426 and r3y > 274) and (r3x <467 and r3y <321)):
                if ((r4x>426 and r4y > 274) and (r4x <467 and r4y <321)):
                    GAME_SOUNDS['win'].play()
                    redText = font4.render('RED WINS',1,(220,10,10))
                    SCREEN.blit(redText,(300,150))
                    pygame.display.update()
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()

    if ((g1x>529 and g1y > 278) and (g1x <568 and g1y <326)):
        if ((g2x>529 and g2y > 278) and (g2x <568 and g2y <326)):
            if ((g3x>529 and g3y > 278) and (g3x <568 and g3y <326)):
                if ((g4x>529 and g4y > 278) and (g4x <568 and g4y <326)):
                    GAME_SOUNDS['win'].play()
                    greenText = font4.render('GREEN WINS',1,(10,220,10))
                    SCREEN.blit(greenText,(280,150))
                    pygame.display.update()
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()

def CheckCut():
    global r1x, r2x, r3x, r4x, r1y, r2y, r3y, r4y,r1Open,r2Open,r3Open,r4Open,g1x, g2x, g3x, g4x, g1y, g2y, g3y, g4y,g1Open,g2Open,g3Open,g4Open
    global r1num,r2num,r3num,r4num,g1num,g2num,g3num,g4num

    if not redTurn: # it is RED TURN

        if r1num == g1num:
            GAME_SOUNDS['cut'].play()
            g1x = 616
            g1y = 423
            g1num = 21
            g1Open = False
        if r2num == g1num:
            GAME_SOUNDS['cut'].play()
            g1x = 616
            g1y = 423
            g1num = 21
            g1Open = False
        if r3num == g1num:
            GAME_SOUNDS['cut'].play()
            g1x = 616
            g1y = 423
            g1num = 21
            g1Open = False
        if r4num == g1num:
            GAME_SOUNDS['cut'].play()
            g1x = 616
            g1y = 423
            g1num = 21
            g1Open = False

        if r1num == g2num:
            GAME_SOUNDS['cut'].play()
            g2x,g2y = 708,423
            g2num = 22
            g2Open = False
        if r2num == g2num:
            GAME_SOUNDS['cut'].play()
            g2x,g2y = 708,423
            g2num = 22
            g2Open = False
        if r3num == g2num:
            GAME_SOUNDS['cut'].play()
            g2x,g2y = 708,423
            g2num = 22
            g2Open = False
        if r4num == g2num:
            GAME_SOUNDS['cut'].play()
            g2x,g2y = 708,423
            g2num = 22
            g2Open = False

        if r1num == g3num:
            GAME_SOUNDS['cut'].play()
            g3x,g3y  = 708,506
            g3num = 23
            g3Open = False
        if r2num == g3num:
            GAME_SOUNDS['cut'].play()
            g3x,g3y  = 708,506
            g3num = 23
            g3Open = False
        if r3num == g3num:
            GAME_SOUNDS['cut'].play()
            g3x,g3y  = 708,506
            g3num = 23
            g3Open = False
        if r4num == g3num:
            GAME_SOUNDS['cut'].play()
            g3x,g3y  = 708,506
            g3num = 23
            g3Open = False
        
        if r1num == g4num:
            GAME_SOUNDS['cut'].play()
            g4x,g4y = 616, 506
            g4num = 23
            g4Open = False
        if r2num == g4num:
            GAME_SOUNDS['cut'].play()
            g4x,g4y = 616, 506
            g4num = 23
            g4Open = False
        if r3num == g4num:
            GAME_SOUNDS['cut'].play()
            g4x,g4y = 616, 506
            g4num = 23
            g4Open = False
        if r4num == g4num:
            GAME_SOUNDS['cut'].play()
            g4x,g4y = 616, 506
            g4num = 23
            g4Open = False
        
    if redTurn: # it is GREEN TURN

        if r1num == g1num:
            GAME_SOUNDS['cut'].play()
            r1x = 272
            r1y = 77
            r1num = 11
            r1Open = False
        if r1num == g2num:
            GAME_SOUNDS['cut'].play()
            r1x = 272
            r1y = 77
            r1num = 11
            r1Open = False
        if r1num == g3num:
            GAME_SOUNDS['cut'].play()
            r1x = 272
            r1y = 77
            r1num = 11
            r1Open = False
        if r1num == g4num:
            GAME_SOUNDS['cut'].play()
            r1x = 272
            r1y = 77
            r1num = 11
            r1Open = False

        if r2num == g1num:
            GAME_SOUNDS['cut'].play()
            r2x,r2y = 371,77
            r2num = 11
            r2Open = False 
        if r2num == g2num:
            GAME_SOUNDS['cut'].play()
            r2x,r2y = 371,77
            r2num = 11
            r2Open = False 
        if r2num == g3num:
            GAME_SOUNDS['cut'].play()
            r2x,r2y = 371,77
            r2num = 11
            r2Open = False 
        if r2num == g4num:
            GAME_SOUNDS['cut'].play()
            r2x,r2y = 371,77
            r2num = 11
            r2Open = False 
    
        if r3num == g1num:
            GAME_SOUNDS['cut'].play()
            r3x,r3y = 272, 163
            r3num = 11
            r3Open = False 
        if r3num == g2num:
            GAME_SOUNDS['cut'].play()
            r3x,r3y = 272, 163
            r3num = 11
            r3Open = False
        if r3num == g3num:
            GAME_SOUNDS['cut'].play()
            r3x,r3y = 272, 163
            r3num = 11
            r3Open = False
        if r3num == g4num:
            GAME_SOUNDS['cut'].play()
            r3x,r3y = 272, 163
            r3num = 11
            r3Open = False

        if r4num == g1num:
            GAME_SOUNDS['cut'].play()
            r4x,r4y  = 371, 163
            r4num = 11
            r4Open = False
        if r4num == g2num:
            GAME_SOUNDS['cut'].play()
            r4x,r4y  = 371, 163
            r4num = 11
            r4Open = False
        if r4num == g3num:
            GAME_SOUNDS['cut'].play()
            r4x,r4y  = 371, 163
            r4num = 11
            r4Open = False
        if r4num == g4num:
            GAME_SOUNDS['cut'].play()
            r4x,r4y  = 371, 163
            r4num = 11
            r4Open = False
        
# =========================  Main Game  ==========================

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Ludo Game - By Anurag')
    
    
    GAME_SPRITES['overplay']= pygame.image.load('images/overplay.png')
    GAME_SPRITES['mainGame']= pygame.image.load('images/mainGameScreen.png')
    GAME_SPRITES['welcome']= pygame.image.load('images/welcomescreen.png')
    GAME_SPRITES['playButton']= pygame.image.load('images/playButton.png')
    GAME_SPRITES['exitButton']= pygame.image.load('images/exitButton.png')
    GAME_SPRITES['overexit']= pygame.image.load('images/overexit.png')
    reD = GAME_SPRITES['redGoti']= [
        pygame.image.load('images/redgoti.png'),
        pygame.image.load('images/redgoti.png'),
        pygame.image.load('images/redgoti.png'),
        pygame.image.load('images/redgoti.png')
    ]
    GAME_SPRITES['blueGoti']= [
        pygame.image.load('images/bluegoti.png'),
        pygame.image.load('images/bluegoti.png'),
        pygame.image.load('images/bluegoti.png'),
        pygame.image.load('images/bluegoti.png')
    ]
    greeN = GAME_SPRITES['greenGoti']= [
        pygame.image.load('images/greengoti.png'),
        pygame.image.load('images/greengoti.png'),
        pygame.image.load('images/greengoti.png'),
        pygame.image.load('images/greengoti.png')
    ]
    GAME_SPRITES['yellowGoti']= [
        pygame.image.load('images/yellowgoti.png'),
        pygame.image.load('images/yellowgoti.png'),
        pygame.image.load('images/yellowgoti.png'),
        pygame.image.load('images/yellowgoti.png')
    ]

    GAME_SPRITES['dice'] = (
        pygame.image.load('images/dice1.png'),
        pygame.image.load('images/dice2.png'),
        pygame.image.load('images/dice3.png'),
        pygame.image.load('images/dice4.png'),
        pygame.image.load('images/dice5.png'),
        pygame.image.load('images/dice6.png'),
    )

    GAME_SPRITES['backButton'] = pygame.image.load('images/backButton.png')
    GAME_SPRITES['overback'] = pygame.image.load('images/overback.png')
    GAME_SPRITES['cover'] = pygame.image.load('images/cover.png')


    GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.ogg')
    GAME_SOUNDS['click'] = pygame.mixer.Sound('audio/click.ogg')
    GAME_SOUNDS['cut'] = pygame.mixer.Sound('audio/cut.ogg')
    GAME_SOUNDS['win'] = pygame.mixer.Sound('audio/win.ogg')
    GAME_SOUNDS['pass'] = pygame.mixer.Sound('audio/pass.ogg')
    GAME_SOUNDS['roll'] = pygame.mixer.Sound('audio/roll.ogg')

    font= pygame.font.SysFont('comicsans',16)
    font1= pygame.font.SysFont('comicsans',28)
    font2= pygame.font.SysFont('comicsans',25)
    text = font.render('PRESS SPACE TO ROLL THE DICE',1,(255,255,255))
    text2 = font1.render('RED PLAYER TURN',1,(202,0,61))
    text3 = font2.render('GREEN PLAYER TURN',1,(0,134,53))

 


    welcomeScreen()
