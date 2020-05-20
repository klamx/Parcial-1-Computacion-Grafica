import pygame
import math
from libreria import *

def dibujarIsometricoPlanta(ven, cara1, cara2, cara3, cara4, cara5, cara6, cara7, C = BLANCO):
    # Cara6
    Poligono(ven, cara6, C, 0)
    Poligono(ven, cara6, NEGRO)

    # Cara7
    Poligono(ven, cara7, BLANCO, 0)
    Poligono(ven, cara7, NEGRO)

    # Cara1
    Poligono(ven, cara1, BLANCO, 0)
    Poligono(ven, cara1, NEGRO)

    # Cara2
    Poligono(ven, cara2, BLANCO, 0)
    Poligono(ven, cara2, NEGRO)

    # Cara3
    Poligono(ven, cara3, BLANCO, 0)
    Poligono(ven, cara3, NEGRO)

    # Cara 4
    Poligono(ven, cara4, BLANCO, 0)
    Poligono(ven, cara4, NEGRO)

    # Cara5
    Poligono(ven, cara5, C, 0)
    Poligono(ven, cara5,NEGRO)

def dibujarIsometricoAlzada(ven, cara1, cara2, cara3, cara4, cara5, cara6, cara7, C = BLANCO):
    # Cara6
    Poligono(ven, cara6, BLANCO, 0)
    Poligono(ven, cara6, NEGRO)

    # Cara7
    Poligono(ven, cara7, BLANCO, 0)
    Poligono(ven, cara7, NEGRO)

    # Cara1
    Poligono(ven, cara1, C, 0)
    Poligono(ven, cara1, NEGRO)

    # Cara2
    Poligono(ven, cara2, BLANCO, 0)
    Poligono(ven, cara2, NEGRO)

    # Cara3
    Poligono(ven, cara3, C, 0)
    Poligono(ven, cara3, NEGRO)

    # Cara 4
    Poligono(ven, cara4, BLANCO, 0)
    Poligono(ven, cara4, NEGRO)

    # Cara5
    Poligono(ven, cara5, BLANCO, 0)
    Poligono(ven, cara5,NEGRO)

def dibujarIsometricoPerfil(ven, cara1, cara2, cara3, cara4, cara5, cara6, cara7, C = BLANCO):
    # Cara6
    Poligono(ven, cara6, BLANCO, 0)
    Poligono(ven, cara6, NEGRO)

    # Cara7
    Poligono(ven, cara7, C, 0)
    Poligono(ven, cara7, NEGRO)

    # Cara1
    Poligono(ven, cara1, BLANCO, 0)
    Poligono(ven, cara1, NEGRO)

    # Cara2
    Poligono(ven, cara2, C, 0)
    Poligono(ven, cara2, NEGRO)

    # Cara3
    Poligono(ven, cara3, BLANCO, 0)
    Poligono(ven, cara3, NEGRO)

    # Cara 4
    Poligono(ven, cara4, C, 0)
    Poligono(ven, cara4, NEGRO)

    # Cara5
    Poligono(ven, cara5, BLANCO, 0)
    Poligono(ven, cara5,NEGRO)

def dibujarPuntos(ven, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36):
    Punto(ventana, p1)
    Punto(ventana, p2)
    Punto(ventana, p3)
    Punto(ventana, p4)
    Punto(ventana, p5)
    Punto(ventana, p6)
    Punto(ventana, p7)
    Punto(ventana, p8)
    Punto(ventana, p9)
    Punto(ventana, p10)
    Punto(ventana, p11)
    Punto(ventana, p12)
    Punto(ventana, p13)
    Punto(ventana, p14)
    Punto(ventana, p15)
    Punto(ventana, p16)
    Punto(ventana, p17)
    Punto(ventana, p18)
    Punto(ventana, p19)
    Punto(ventana, p20)
    Punto(ventana, p21)
    Punto(ventana, p22)
    Punto(ventana, p23)
    Punto(ventana, p24)
    Punto(ventana, p25)
    Punto(ventana, p26)
    Punto(ventana, p27)
    Punto(ventana, p28)
    Punto(ventana, p29)
    Punto(ventana, p30)
    Punto(ventana, p31)
    Punto(ventana, p32)
    Punto(ventana, p33)
    Punto(ventana, p34)
    Punto(ventana, p35)
    Punto(ventana, p36)


if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    # Se asigana nombre a la ventana
    pygame.display.set_caption("Parcial 1 computacion grafica")
    origen = [ANCHO // 2, ALTO // 2]
    valorEscalamiento1 = 0.5
    # valor de rotacion
    x = 0
    fin = False

    # Puntos para las vistas
    # bloque1
    p1 = [60,100]
    p2 = [120, 100]
    p3 = [180, 100]
    p4 = [240, 100]
    p5 = [300, 100]
    p6 = [360, 100]
    # bloque2
    p7 = [60, 160]
    p8 = [120, 160]
    p9 = [180, 160]
    p10 = [240, 160]
    p11 = [300, 160]
    p12 = [360, 160]
    # bloque3
    p13 = [60, 220]
    p14 = [120, 220]
    p15 = [180, 220]
    p16 = [240, 220]
    p17 = [300, 220]
    p18 = [360, 220]
    # bloque3
    p19 = [60, 280]
    p20 = [120, 280]
    p21 = [180, 280]
    p22 = [240, 280]
    p23 = [300, 280]
    p24 = [360, 280]
    # bloque4
    p25 = [60, 340]
    p26 = [120, 340]
    p27 = [180, 340]
    p28 = [240, 340]
    p29 = [300, 340]
    p30 = [360, 340]
    # bloque5
    p31 = [60, 400]
    p32 = [120, 400]
    p33 = [180, 400]
    p34 = [240, 400]
    p35 = [300, 400]
    p36 = [360, 400]


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


    # Plano(ventana,origen)
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            # Gestion de eventos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    ventana.fill(NEGRO)
                    #Plano(ventana,origen)

                    # Se dibujan las caras en el plano
                    dibujarIsometricoPlanta(ventana, cara1, cara2, cara3, cara4, cara5, cara6, cara7, MORADO)

                # Vista alzada
                if event.key == pygame.K_2:
                    ventana.fill(NEGRO)
                    # Se dibuja el Isometrico
                    dibujarIsometricoAlzada(ventana, cara1, cara2, cara3, cara4, cara5, cara6, cara7, VERDE)
                    # Se dibujan los Puntos
                    dibujarPuntos(ventana, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36)
                    # Dibuajar vistas
                    ls1 = [p4, p6, p30, p28]
                    Poligono(ventana, ls1, VERDE)
                    Linea(ventana, p5, p29, VERDE)

                # Vista de Planta
                if event.key == pygame.K_3:
                    ventana.fill(NEGRO)
                    # Se dibuja el isometrico
                    dibujarIsometricoPlanta(ventana, cara1, cara2, cara3, cara4, cara5, cara6, cara7, MORADO)
                    # Se dibujan los Puntos
                    dibujarPuntos(ventana, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36)
                    ls1 = [p4, p5, p17, p16]
                    ls2 = [p5, p6, p36, p35, p29, p28, p4]
                    Poligono(ventana, ls1, MORADO)
                    Poligono(ventana, ls2, MORADO)

                # VIsta de Perfil
                if event.key == pygame.K_4:
                    ventana.fill(NEGRO)
                    # Se dibuja el isometrico
                    dibujarIsometricoPerfil(ventana, cara1, cara2, cara3, cara4, cara5, cara6, cara7, ROJO)
                    # Se dibujan los Puntos
                    dibujarPuntos(ventana, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36)
                    ls1 = [p1, p6, p30, p25]
                    Poligono(ventana, ls1, ROJO)
                    Linea(ventana, p3, p15, ROJO)
                    Linea(ventana, p15, p13, ROJO)
                    Linea(ventana, p5, p29, ROJO)

                # Escalamient -
                if event.key == pygame.K_5:
                    ventana.fill(NEGRO)
                    # Se escalan los Puntos
                    Aescalado = escalapf(origen, AP, valorEscalamiento1)
                    Bescalado = escalapf(origen, BP, valorEscalamiento1)
                    Cescalado = escalapf(origen, CP, valorEscalamiento1)
                    Descalado = escalapf(origen, DP, valorEscalamiento1)
                    Eescalado = escalapf(origen, EP, valorEscalamiento1)
                    Fescalado = escalapf(origen, FP, valorEscalamiento1)
                    Gescalado = escalapf(origen, GP, valorEscalamiento1)
                    Hescalado = escalapf(origen, HP, valorEscalamiento1)
                    Iescalado = escalapf(origen, IP, valorEscalamiento1)
                    Jescalado = escalapf(origen, JP, valorEscalamiento1)
                    Kescalado = escalapf(origen, KP, valorEscalamiento1)
                    Lescalado = escalapf(origen, LP, valorEscalamiento1)
                    Mescalado = escalapf(origen, MP, valorEscalamiento1)
                    Nescalado = escalapf(origen, NP, valorEscalamiento1)
                    Oescalado = escalapf(origen, OP, valorEscalamiento1)
                    Pescalado = escalapf(origen, PP, valorEscalamiento1)
                    Qescalado = escalapf(origen, QP, valorEscalamiento1)
                    # Se crean las caras escaladas
                    cara1Esc = [Aescalado, Bescalado, Cescalado, Descalado]
                    cara2Esc = [Aescalado, Descalado, Fescalado, Eescalado]
                    cara3Esc = [Gescalado, Eescalado, Fescalado, Hescalado]
                    cara4Esc = [Iescalado, Jescalado, Kescalado, Lescalado, Hescalado, Gescalado]
                    cara5Esc = [Lescalado, Oescalado, Nescalado, Mescalado, Cescalado, Descalado, Fescalado, Hescalado]
                    cara6Esc = [Jescalado, Pescalado, Qescalado, Kescalado]
                    cara7Esc = [Pescalado, Nescalado, Oescalado, Qescalado]
                    # Se dibuja el isometrico escalado
                    dibujarIsometricoPlanta(ventana, cara1Esc, cara2Esc, cara3Esc, cara4Esc, cara5Esc, cara6Esc, cara7Esc, MORADO)

                #rotacion en z derecha
                if event.key == pygame.K_7:
                    ventana.fill(NEGRO)
                    x -= 30
                    # Creacion de puntos para la figura
                    # Cara1
                    # Se crean los puntos cartesianos
                    A = polar_a_cartesiano(50, 30 + x)
                    B = polar_a_cartesiano(100, 30 + x)
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
                    E = polar_a_cartesiano(50, 150 + x)
                    F = polar_a_cartesiano(50, 150 + x)
                    # Se transforman los puntos cartesianos a pantalla
                    EP = Cart_A_Pantalla(AP, E)
                    FP = Cart_A_Pantalla(DP, F)
                    # Se crea una lista con los puntos que forman la cara2
                    cara2 = [AP, DP, FP, EP]

                    # Cara3
                    # Se crean los putos cartesianos
                    G = polar_a_cartesiano(50, 150 + x)
                    H = traslacion(G, [0, 200])
                    # Se transforman los puntos cartesianos a pantalla
                    GP = Cart_A_Pantalla(origen, G)
                    HP = Cart_A_Pantalla(origen, H)
                    # Se crea una lista con los puntos que forman la cara3
                    cara3 = [GP, EP, FP, HP]

                    # Cara4
                    # Se crean los puntos cartesianos
                    I = polar_a_cartesiano(250, 150 + x)
                    J = traslacion(I, [0, 100])
                    # Punto auxiliar para hallar los puntos K y L
                    Aux1 = polar_a_cartesiano(150, 150 + x)
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
                    M = polar_a_cartesiano(250, 150 + x)
                    N = polar_a_cartesiano(250, 150 + x)
                    O = polar_a_cartesiano(150, 150 + x)
                    # Se transforman los puntos cartesianos a pantalla
                    MP = Cart_A_Pantalla(CP, M)
                    NP = Cart_A_Pantalla(DP, N)
                    OP = Cart_A_Pantalla(DP, O)
                    # Se crea una lista con los puntos que forman la cara5
                    cara5 = [LP, OP, NP, MP, CP, DP, FP, HP]

                    # Cara6
                    # Se crean los puntos cartesianos
                    P = polar_a_cartesiano(50, 30 + x)
                    Q = polar_a_cartesiano(50, 30 + x)
                    # Se tranasforman los puntos cartesianos a pantalla
                    PP = Cart_A_Pantalla(JP, P)
                    QP = Cart_A_Pantalla(KP, Q)
                    # Se crea una lista con los puntos que forman la cara6
                    cara6 = [JP, PP, QP, KP]

                    # Cara7
                    # Se crea una lista con los puntos que forman la cara7
                    cara7 = [PP, NP, OP, QP]
                    # Dinujar isometrico
                    dibujarIsometricoPlanta(ventana, cara1, cara2, cara3, cara4, cara5, cara6, cara7, MORADO)

                # rotacion en z izquierda
                if event.key == pygame.K_6:
                    ventana.fill(NEGRO)
                    x += 30
                    # Creacion de puntos para la figura
                    # Cara1
                    # Se crean los puntos cartesianos
                    A = polar_a_cartesiano(50, 30 + x)
                    B = polar_a_cartesiano(100, 30 + x)
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
                    E = polar_a_cartesiano(50, 150 + x)
                    F = polar_a_cartesiano(50, 150 + x)
                    # Se transforman los puntos cartesianos a pantalla
                    EP = Cart_A_Pantalla(AP, E)
                    FP = Cart_A_Pantalla(DP, F)
                    # Se crea una lista con los puntos que forman la cara2
                    cara2 = [AP, DP, FP, EP]

                    # Cara3
                    # Se crean los putos cartesianos
                    G = polar_a_cartesiano(50, 150 + x)
                    H = traslacion(G, [0, 200])
                    # Se transforman los puntos cartesianos a pantalla
                    GP = Cart_A_Pantalla(origen, G)
                    HP = Cart_A_Pantalla(origen, H)
                    # Se crea una lista con los puntos que forman la cara3
                    cara3 = [GP, EP, FP, HP]

                    # Cara4
                    # Se crean los puntos cartesianos
                    I = polar_a_cartesiano(250, 150 + x)
                    J = traslacion(I, [0, 100])
                    # Punto auxiliar para hallar los puntos K y L
                    Aux1 = polar_a_cartesiano(150, 150 + x)
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
                    M = polar_a_cartesiano(250, 150 + x)
                    N = polar_a_cartesiano(250, 150 + x)
                    O = polar_a_cartesiano(150, 150 + x)
                    # Se transforman los puntos cartesianos a pantalla
                    MP = Cart_A_Pantalla(CP, M)
                    NP = Cart_A_Pantalla(DP, N)
                    OP = Cart_A_Pantalla(DP, O)
                    # Se crea una lista con los puntos que forman la cara5
                    cara5 = [LP, OP, NP, MP, CP, DP, FP, HP]

                    # Cara6
                    # Se crean los puntos cartesianos
                    P = polar_a_cartesiano(50, 30 + x)
                    Q = polar_a_cartesiano(50, 30 + x)
                    # Se tranasforman los puntos cartesianos a pantalla
                    PP = Cart_A_Pantalla(JP, P)
                    QP = Cart_A_Pantalla(KP, Q)
                    # Se crea una lista con los puntos que forman la cara6
                    cara6 = [JP, PP, QP, KP]

                    # Cara7
                    # Se crea una lista con los puntos que forman la cara7
                    cara7 = [PP, NP, OP, QP]
                    # Dinujar isometrico
                    dibujarIsometricoPlanta(ventana, cara1, cara2, cara3, cara4, cara5, cara6, cara7, MORADO)



        # Plano(ventana, origen)
        pygame.display.flip()
