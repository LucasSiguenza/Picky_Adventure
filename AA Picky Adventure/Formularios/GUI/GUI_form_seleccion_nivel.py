import pygame
from pygame.locals import *

from Formularios.API_Forms.GUI_label import *
from Formularios.API_Forms.GUI_form import *
from Formularios.API_Forms.GUI_button_image import *
from Formularios.GUI.GUI_form_contenedor_nivel import *
from Clases.Manejador_Niveles import Manejador_Niveles

class FormSeleccionNivel(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        self.fondo = pygame.image.load("AA Picky Adventure\\Imágenes\\Ambientación\\fondo_selec_lvl.jpeg")
        self.fondo = pygame.transform.scale(self.fondo, (screen.get_width(), screen.get_height()))

        self.manejador_niveles = Manejador_Niveles(self._master)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self.screen = screen
        self.nivel_uno_completado = True
        self.nivel_dos_completado = True
        
        self._slave = aux_imagen

        self._btn_nivel_1 = Button_Image(screen=self._slave,
                                        x = 95,
                                        y = 220,
                                        master_x = x,
                                        master_y = y,
                                        w = 150,
                                        h = 150,
                                        onclick = self.entrar_nivel,
                                        onclick_param = "nivel_uno",
                                        path_image = "AA Picky Adventure\\Formularios\\Recursos GUI\\btn_1.png")
        
        self._btn_nivel_2 = Button_Image(screen=self._slave,
                                        x = 265,
                                        y = 220,
                                        master_x = x,
                                        master_y = y,
                                        w = 150,
                                        h = 150,
                                        onclick = self.entrar_nivel,
                                        onclick_param = "nivel_dos",
                                        path_image = "AA Picky Adventure\\Formularios\\Recursos GUI\\btn_2.png")
        
        self._btn_nivel_3 = Button_Image(screen=self._slave,
                                        x = 435,
                                        y = 220,
                                        master_x = x,
                                        master_y = y,
                                        w = 150,
                                        h = 150,
                                        onclick = self.entrar_nivel,
                                        onclick_param = "nivel_tres",
                                        path_image = "AA Picky Adventure\\Formularios\\Recursos GUI\\btn_3.png")
        
        self._btn_home = Button_Image(screen=self._slave,
                                        x = 290,
                                        y = 400,
                                        master_x = x,
                                        master_y = y,
                                        w = 100,
                                        h = 100,
                                        onclick = self.btn_home_click,
                                        onclick_param = "home",
                                        path_image = "AA Picky Adventure\\Formularios\\Recursos GUI\\home.png")
        
        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "SELECCIONAR NIVEL", "Comic Sans", 30, "Black", "AA Picky Adventure\\Formularios\\Recursos GUI\\casilla_1.png")
        
        self.lista_widgets.append(self._btn_nivel_1)
        self.lista_widgets.append(self._btn_nivel_2)
        self.lista_widgets.append(self._btn_nivel_3)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.label_titulo)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self.screen.blit(self.fondo, (0,0))
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        if nombre_nivel == "nivel_dos":
            if self.nivel_uno_completado:
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
                self.show_dialog(form_contenedor_nivel)
            else:
                print("Primero complete el nivel 1")
        elif nombre_nivel == "nivel_tres":
            if self.nivel_uno_completado and self.nivel_dos_completado:
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
                self.show_dialog(form_contenedor_nivel)
            else:
                print("Primero complete el nivel 1 y 2")
        else:
            nivel = self.manejador_niveles.get_nivel(nombre_nivel)
            form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
            self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()