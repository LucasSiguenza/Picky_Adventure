import pygame
from pygame.locals import *

from Formularios.API_Forms.GUI_button import *
from Formularios.API_Forms.GUI_slider import *
from Formularios.API_Forms.GUI_textbox import *
from Formularios.API_Forms.GUI_label import *
from Formularios.API_Forms.GUI_form import *
from Formularios.API_Forms.GUI_button_image import *
from Formularios.API_Forms.GUI_checkbox import *
from Formularios.API_Forms.GUI_picture_box import *
from Formularios.GUI.GUI_form_ajustes import *
from Formularios.GUI.GUI_form_seleccion_nivel import *
from Formularios.GUI.GUI_form_menu_ranking import *


class FormMenuPrincipal(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        self.fondo = pygame.image.load("AA Picky Adventure\\Formularios\\Recursos GUI\\Pingufondo.png")
        self.fondo = pygame.transform.scale(self.fondo, (screen.get_width(), screen.get_height()))

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        self.screen = screen
        lore_1 = "Una pingüina fue modificada genéticamente en rusia,"
        lore_2 = "desarrollando poderes psíquicos que le permitieron manifestar su espíritu."
        lore_3 = "Hoy busca venganza"
        lore_4 ="ELLA ES PICKY"

        self.btn_ajustes = Button_Image(self._slave, x, y, 150, 400, 100, 100, "AA Picky Adventure\\Formularios\\Recursos GUI\\ajustes.png", self.btn_ajustes_click, "Ajustes")
        self.btn_jugar = Button_Image(self._slave, x, y, 265, 380, 150, 150, "AA Picky Adventure\\Formularios\\Recursos GUI\\Boton_play_3.png", self.btn_jugar_click, "Jugar")
        self.btn_ranking = Button_Image(self._slave, x, y, 430, 400, 100, 100, "AA Picky Adventure\\Formularios\\Recursos GUI\\ranking.png", self.btn_ranking_click, "Ranking")
        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "MENU PRINCIPAL", "Comic Sans", 30, "Black", "AA Picky Adventure\\Formularios\\Recursos GUI\\casilla_1.png")
        self.label_instrucciones = Label(self._slave, 100, 120, 480, 50, "Tecla F -> Lanzar | Tecla G -> Atacar", "Comic Sans", 20, "Black", "AA Picky Adventure\\Formularios\\Recursos GUI\\casilla_2.png")
        self.label_lore_1 = Label(self._slave, 0, 180, 650, 30, lore_1, "Comic Sans", 15, "Red", "AA Picky Adventure\\Formularios\\Recursos GUI\\casilla_1.png")
        self.label_lore_2 = Label(self._slave, 0, 210, 650, 30, lore_2, "Comic Sans", 15, "Red", "AA Picky Adventure\\Formularios\\Recursos GUI\\casilla_1.png")
        self.label_lore_3 = Label(self._slave, 0, 240, 650, 30, lore_3, "Comic Sans", 15, "Red", "AA Picky Adventure\\Formularios\\Recursos GUI\\casilla_1.png")
        self.label_lore_4 = Label(self._slave, 0, 290, 650, 50, lore_4, "Comic Sans", 30, "Red", "AA Picky Adventure\\Formularios\\Recursos GUI\\casilla_1.png")
        
        self.lista_widgets.append(self.label_lore_4)
        self.lista_widgets.append(self.label_lore_3)
        self.lista_widgets.append(self.label_lore_2)
        self.lista_widgets.append(self.label_lore_1)
        self.lista_widgets.append(self.btn_ajustes)
        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.btn_ranking)
        self.lista_widgets.append(self.label_titulo)
        self.lista_widgets.append(self.label_instrucciones)

        pygame.mixer.init()
        pygame.mixer.music.load("AA Picky Adventure\\Sonidos\\musica_fondo.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self.screen.blit(self.fondo, (0,0))
            if self.active:
                self.draw()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)


    def btn_ajustes_click(self, param):
        form_ajustes = FormAjustes(self._master,
                                        300,
                                        50,
                                        680,
                                        620,
                                        True,
                                        "AA Picky Adventure\\Formularios\\Recursos GUI\\interfaz.png")
        self.show_dialog(form_ajustes)

    def btn_jugar_click(self, param):
        form_seleccion_nivel = FormSeleccionNivel(self._master, 
                                        300,
                                        50,
                                        680,
                                        620,
                                        True,
                                        "AA Picky Adventure\\Formularios\\Recursos GUI\\Interfaz_1.png")
        self.show_dialog(form_seleccion_nivel)

    def btn_ranking_click(self, texto):
        lista_puntajes = self.obtener_top_tres_jugadores_db()
        
        form_ranking = FormMenuRanking(self._master,
                                        300,
                                        50,
                                        680,
                                        620,
                                        True,
                                        "AA Picky Adventure\\Formularios\\Recursos GUI\\interfaz_2.png",
                                        lista_puntajes,
                                        240,
                                        70,
                                        5
                                        )
        self.show_dialog(form_ranking)

    def obtener_top_tres_jugadores_db(self):
        with sqlite3.connect("AA Picky Adventure\\datos_jugadores.db") as conexion:
            try:
                lista_puntajes = []
                cursor = conexion.execute("select * from Puntuaciones order by puntaje desc limit 3")
                for fila in cursor:
                    dic = {}
                    dic["Nivel"] = fila[1]
                    dic["Jugador"] = fila[2]
                    dic["Puntaje"] = fila[3]
                    lista_puntajes.append(dic)
                print("Datos seleccionados con exito")
                return lista_puntajes
            except:
                print("Hubo un error al intentar seleccionar los datos de la base de datos :(")

