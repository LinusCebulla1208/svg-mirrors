import pygame as pg
import numpy as np
import svg.path

# Diese Datei enthält verschiedene nützliche Methoden zum Zeichnen

def drawArray(screen, color:tuple, arr:list, line_width:float):
    screen.fill((0, 0, 0)) #Anzeige clearen/mit Schwarz füllen
    for i in range(len(arr)-1):
        curr_point = arr[i] #aktueller Punkt
        next_point = arr[i+1] #nächster Punkt
        pg.draw.line(screen, color, curr_point, next_point, line_width) #Linie von aktuellem zum nächsten Punkt
    pg.display.flip() # Anzeige aktualisieren

def drawSVG(screen, color:tuple, path:svg.path.path, scale:tuple, offset:tuple, stepsize, line_width:float):
    path_arr = []
    for i in np.arange(0, 1, stepsize):
        path_arr.append((scale[0] * path.point(i).real + offset[0], scale[1] * path.point(i).imag + offset[0]))
    drawArray(screen, color, path_arr, line_width)

def animSVG(screen, color:tuple, path:svg.path.path, scale:tuple, offset:tuple, line_width:float, time:float, framerate:float, clock): #Zeichnet einen SVG-Pfad (animiert); path: geparster SVG-Pfad, time:Animationszeit(in Sekunden); scale=(x_skalierung, y_skalierung), offset=(x_verschiebung, y_verschiebung)
        stepsize = 1/(time*framerate) #Benötigte Schrittweite um den Pfad in der angegebenen Zeit zu animieren
        svg_path_array = [(scale[0] * path.point(0).real + offset[0], scale[1] * path.point(0).imag + offset[1])] # Alle Punkte des SVG-Pfads in einem Array
        for i in np.arange(stepsize, 1, stepsize):
            #screen.fill((0, 0, 0)) #Bildschirm clearen/mit Schwarz füllen

            #---ZEICHENVORGANG
            next_point = (scale[0] * path.point(i+stepsize).real + offset[0], scale[1] * path.point(i+stepsize).imag + offset[1]) #nächster Punkt; "-------------"
            svg_path_array.append(next_point) #nächsten Punkt an Array anhängen --> Array neu Zeichnen
            drawArray(screen, color, svg_path_array, line_width) #--> Array wird "Stück für Stück" gezeichnet

            pg.display.flip() #Fenster updaten
            clock.tick(framerate)