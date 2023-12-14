import pygame, random
from pygame.locals import *

from Clases.Configuraciones import *
from Clases.Nivel import *
from Clases.Personaje_Principal import Personaje_Principal



class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        #PANTALLA
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()
        
        #GENERACION ALEATORIA
        
        y = random.randint(0,100)%2
        z = random.randint(0,100)%2
        x = random.randint(0,100)%2

        match x:
            case 0:
                x = random.randint(7,9)
            case _:
                x = 0
        match y:
            case 0:
                y = random.randint(7,9)
            case _:
                y = 0
        match z:
            case 0:
                z = random.randint(7,9)
            case _:
                z = 0
        if x == y and x == z:
            x = 10
            y = 7
            z = 7

        fondo = pygame.image.load("AA Picky Adventure\\Imágenes\\Ambientación\\fondo lvl1.jpg")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        pygame.mixer.init()
        pygame.mixer.music.load("AA Picky Adventure\\Sonidos\\lvl_1.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        #PERSONAJE PRINCIPAL
        mi_personaje = Personaje_Principal(diccionario_animaciones_personaje, "quieto_derecha", (160, 440), x)

        '''POSICIONES OBJETOS ESCENARIO:
        0 -> Vacio
        1 -> Plataforma Hielo
        2 -> Plataforma Metal
        3 -> Recompensa Moneda
        4 -> Recompensa Corazon
        5 -> Recompensa Copo de Nieve
        6 -> Trampa Pinchos
        7 -> Enemigo (Camina y Ataca)
        8 -> Enemigo (Quieto(der) y Lanza)
        9 -> Enemigo (Quieto(izq) y Lanza)
        10 -> BOSS (Camina, Salta, Lanza y Ataca)
        '''
        escenario =[
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 5, 0, 0, 0, 0, x, 0, 0, 0, 0, y, 0, 0, 0, 0, 0, 0, z, 0, 0, 0, 0, x, 0, 0, 0, 0, 5, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 7, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, z, 0, z, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 7, 0, 2],
        [2, x, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, y, z, 2],
        [2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 5, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 5, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        ]


        self.blitear_escenario(escenario)

        super().__init__(pantalla, mi_personaje, fondo)

        
