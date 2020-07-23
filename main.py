import pygame as pg
import numpy as np
import visualizer as vis
from svg.path import parse_path

WINDOW = (800, 800)
TITLE = "svg-mirrors"
FRAMERATE = 60

def main():
    pg.init()
    screen = pg.display.set_mode(WINDOW)
    pg.display.set_caption(TITLE)

    loop(screen)

def loop(screen):
    clock = pg.time.Clock()
    cont = True

    pfad = parse_path("M 8,30A 20,20 0,0,1 50,30A 20,20 0,0,1 90,30Q 90,60 50,90Q 10,60 10,30 z")

    vis.animSVG(screen, (255, 255, 255), pfad, (6, 6), (0, 0), 2, 3, FRAMERATE, clock)
    line = vis.animLine(screen, (255, 255, 255), (100, 100), (200, 300), 3, 1, 60, clock)

    while cont:
        for event in pg.event.get(): #Wenn Fenster geschlossen --> Main Loop beenden
            if event.type==pg.QUIT:
                cont=False

        #Fenster clearen, mit schwarzem Hintergrund füllen
        #screen.fill((0, 0, 0))

        #--ZEICHENVORGANG
        vis.drawSVG(screen, (255, 255, 255), pfad, (6, 6), (0, 0), 0.01, 2)
        pg.draw.rect(screen, (255, 255, 255), line)

        #Fenster updaten
        pg.display.flip()

        #max. 60fps
        clock.tick(FRAMERATE)

main()