import pygame
import math
from libreria import *

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    # Se asigana nombre a la ventana
    pygame.display.set_caption("Parcial 1 computacion grafica")
    # Se define la fuente que se usara en el programa
    fuente = pygame.font.Font(None, 25)
    # Se definene las palabras para cada punto del parcial
    texto1 = fuente.render("Isometrico", 0, BLANCO)
    texto2 = fuente.render("Planta", 0, BLANCO)
    texto3 = fuente.render("Perfil", 0, BLANCO)
    texto4 = fuente.render("Alzada", 0, BLANCO)
    texto5 = fuente.render("Escalamineto +", 0, BLANCO)
    texto6 = fuente.render("Escalamiento -", 0, BLANCO)
    origen = [ANCHO // 2, ALTO // 2]
    fin = False

    # Puntos para las vistas
    p1 = [60,400]
    p2 = [120, 400]
    p3 = [180, 400]
    p4 = [240, 400]
    p5 = [300, 400]
    p6 = [60, 460]
    p7 = [120, 460]
    p8 = [180, 460]
    p9 = [240, 460]
    p10 = [300, 460]
    p11 = [60, 520]
    p12 = [120, 520]
    p13 = [180, 520]
    p14 = [240, 520]
    p15 = [300, 520]


    # Creacion de puntos para la figura
    # Cara1
    # Se crean los puntos cartesianos
    A = polar_a_cartesiano(50, 30)
    B = polar_a_cartesiano(100, 30)
    C = traslacion(B, [0, 200])
    D = traslacion(A, [0, 200])
    # Se transforman los puntos cartesianos a pantalla
    AP = Cart_A_Pantalla(origen, A)
    BP = Cart_A_Pantalla(origen, B)
    CP = Cart_A_Pantalla(origen, C)
    DP = Cart_A_Pantalla(origen, D)
    # Se crea una lista con los puntos que forman la cara!
    cara1 = [AP, BP, CP, DP]

    # Cara2
    # Se crean los puntos cartesianos
    E = polar_a_cartesiano(50, 150)
    F = polar_a_cartesiano(50, 150)
    # Se transforman los puntos cartesianos a pantalla
    EP = Cart_A_Pantalla(AP, E)
    FP = Cart_A_Pantalla(DP, F)
    # Se crea una lista con los puntos que forman la cara2
    cara2 = [AP, DP, FP, EP]

    # Cara3
    # Se crean los putos cartesianos
    G = polar_a_cartesiano(50, 150)
    H = traslacion(G, [0, 200])
    # Se transforman los puntos cartesianos a pantalla
    GP = Cart_A_Pantalla(origen, G)
    HP = Cart_A_Pantalla(origen, H)
    # Se crea una lista con los puntos que forman la cara3
    cara3 = [GP, EP, FP, HP]

    # Cara4
    # Se crean los puntos cartesianos
    I = polar_a_cartesiano(250, 150)
    J = traslacion(I, [0, 100])
    # Punto auxiliar para hallar los puntos K y L
    Aux1 = polar_a_cartesiano(150, 150)
    K = traslacion(Aux1, [0, 100])
    L = traslacion(Aux1, [0, 200])
    # Se transforman los puntos cartesianos a pantalla
    IP = Cart_A_Pantalla(origen, I)
    JP = Cart_A_Pantalla(origen, J)
    Aux1P = Cart_A_Pantalla(origen, Aux1)
    KP = Cart_A_Pantalla(origen, K)
    LP = Cart_A_Pantalla(origen, L)
    # Se crea una lista con los puntos que forman la cara4
    cara4 = [IP, JP, KP, LP, HP, GP]

    # Cara5
    # Se crean los puntos cartesianos
    M = polar_a_cartesiano(250, 150)
    N = polar_a_cartesiano(250, 150)
    O = polar_a_cartesiano(150, 150)
    # Se transforman los puntos cartesianos a pantalla
    MP = Cart_A_Pantalla(CP, M)
    NP = Cart_A_Pantalla(DP, N)
    OP = Cart_A_Pantalla(DP, O)
    # Se crea una lista con los puntos que forman la cara5
    cara5 = [LP, OP, NP, MP, CP, DP, FP, HP]

    # Cara6
    # Se crean los puntos cartesianos
    P = polar_a_cartesiano(50, 30)
    Q = polar_a_cartesiano(50, 30)
    # Se tranasforman los puntos cartesianos a pantalla
    PP = Cart_A_Pantalla(JP, P)
    QP = Cart_A_Pantalla(KP, Q)
    # Se crea una lista con los puntos que forman la cara6
    cara6 = [JP, PP, QP, KP]

    # Cara7
    # Se crea una lista con los puntos que forman la cara7
    cara7 = [PP, NP, OP, QP]


    Plano(ventana,origen)
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            # Gestion de eventos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    ventana.fill(NEGRO)
                    ventana.blit(texto1, [680, 20])
                    Plano(ventana,origen)

                    # Se dibujan las caras en el plano
                    # Cara6
                    Poligono(ventana, cara6, MORADO, 0)
                    Poligono(ventana, cara6, NEGRO)

                    # Cara7
                    Poligono(ventana, cara7, BLANCO, 0)
                    Poligono(ventana, cara7, NEGRO)

                    # Cara1
                    Poligono(ventana, cara1, BLANCO, 0)
                    Poligono(ventana, cara1, NEGRO)

                    # Cara2
                    Poligono(ventana, cara2, BLANCO, 0)
                    Poligono(ventana, cara2, NEGRO)

                    # Cara3
                    Poligono(ventana, cara3, BLANCO, 0)
                    Poligono(ventana, cara3, NEGRO)

                    # Cara 4
                    Poligono(ventana, cara4, BLANCO, 0)
                    Poligono(ventana, cara4, NEGRO)

                    # Cara5
                    Poligono(ventana, cara5, MORADO, 0)
                    Poligono(ventana, cara5,NEGRO)




        pygame.display.flip()
