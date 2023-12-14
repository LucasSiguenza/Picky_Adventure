import pygame

def reescalar_imagenes(lista_imagenes, tamaño):
        for imagen in range(len(lista_imagenes)):
            lista_imagenes[imagen] = pygame.transform.scale(lista_imagenes[imagen], tamaño)

def girar_imagenes(lista_original: list, flip_x: bool, flip_y: bool) -> list:
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

#PERSONAJE
personaje_quieto_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Quieto\\0.png")]
personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha, True, False)

personaje_camina_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Camina\\0.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Camina\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Camina\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Camina\\3.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Corre\\0.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Corre\\0.png")]
personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)

personaje_salta_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Salta\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Salta\\1.png")]
personaje_salta_izquierda = girar_imagenes(personaje_salta_derecha, True, False)


personaje_lanza_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\0.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\3.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\3.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\3.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\4.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\4.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\4.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\5.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\5.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Lanza\\5.png")]

personaje_lanza_izquierda = girar_imagenes(personaje_lanza_derecha, True, False)

personaje_ataca_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Ataca\\0.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Ataca\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Ataca\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Ataca\\3.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jugador\\Ataca\\4.png")]
personaje_ataca_izquierda = girar_imagenes(personaje_ataca_derecha, True, False)

reduccion = 10
reescalar_imagenes(personaje_quieto_derecha, (232/reduccion, 439/reduccion))
reescalar_imagenes(personaje_quieto_izquierda, (232/reduccion, 439/reduccion))
reescalar_imagenes(personaje_camina_derecha, (362/reduccion, 439/reduccion))
reescalar_imagenes(personaje_camina_izquierda, (362/reduccion, 439/reduccion))
reescalar_imagenes(personaje_salta_derecha, (362/reduccion, 439/reduccion))
reescalar_imagenes(personaje_salta_izquierda, (362/reduccion, 439/reduccion))
reescalar_imagenes(personaje_lanza_derecha, (377/reduccion, 439/reduccion))
reescalar_imagenes(personaje_lanza_izquierda, (377/reduccion, 439/reduccion))
reescalar_imagenes(personaje_ataca_derecha, (536/reduccion, 495/reduccion))
reescalar_imagenes(personaje_ataca_izquierda, (536/reduccion, 495/reduccion))

diccionario_animaciones_personaje = {"quieto_derecha" : personaje_quieto_derecha,
                                    "quieto_izquierda" : personaje_quieto_izquierda,
                                    "camina_derecha" : personaje_camina_derecha,
                                    "camina_izquierda" : personaje_camina_izquierda,
                                    "salta_derecha" : personaje_salta_derecha,
                                    "salta_izquierda" : personaje_salta_izquierda,
                                    "lanza_derecha" : personaje_lanza_derecha,
                                    "lanza_izquierda" : personaje_lanza_izquierda,
                                    "ataca_derecha" : personaje_ataca_derecha,
                                    "ataca_izquierda" : personaje_ataca_izquierda,}

#PLATAFORMAS
plataforma_metal = [pygame.image.load("AA Picky Adventure\\Imágenes\\Plataforma hielo.png")]
plataforma_hielo = [pygame.image.load("AA Picky Adventure\\Imágenes\\Plataforma hielo.png")]

reescalar_imagenes(plataforma_hielo, (40, 40))
reescalar_imagenes(plataforma_metal, (40, 40))

diccionario_plataformas = {"metal" : plataforma_metal,
                            "hielo" : plataforma_hielo}

#ITEMS
#RECOMPENSAS
recompensa_moneda = [pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\0.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\0.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\0.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\1.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\1.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\1.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\2.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\2.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\2.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\3.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\3.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\3.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\4.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\4.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\4.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\5.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\5.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Moneda\\\\5.png")]

recompensa_corazon = [pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\0.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\0.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\0.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\1.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\1.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\1.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\2.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\2.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\2.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\3.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\3.png"),
            pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Corazon\\3.png")]

recompensa_bola_nieve = [pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Copo de nieve\\Copo de nieve.png")]

reescalar_imagenes(recompensa_moneda, (20, 20))
reescalar_imagenes(recompensa_corazon, (40, 40))
reescalar_imagenes(recompensa_bola_nieve, (40,40))

diccionario_recompensas = {"moneda" : recompensa_moneda,
                            "corazon" : recompensa_corazon,
                            "bola_nieve" : recompensa_bola_nieve}


#TRAMPAS
trampa_pinchos = [pygame.image.load("AA Picky Adventure\\Imágenes\\Items\\Pincho\\0.png")]

trampa_lanzador_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Torreta\\0.png")]
trampa_lanzador_izquierda = girar_imagenes(trampa_lanzador_derecha, True, False)

reescalar_imagenes(trampa_pinchos, (20, 50))
reescalar_imagenes(trampa_lanzador_izquierda, (15, 40))
reescalar_imagenes(trampa_lanzador_derecha, (15, 40))

diccionario_trampas = {"pinchos" : trampa_pinchos,
                        "lanzador_derecha" : trampa_lanzador_derecha,
                        "lanzador_izquierda" : trampa_lanzador_izquierda}


#PROYECTIL
proyectil_pingu_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Proyectiles\\2.png")]
proyectil_pingu_izquierda = girar_imagenes(proyectil_pingu_derecha, True, False)

proyectil_mecha_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Proyectiles\\0.png")]
proyectil_mecha_izquierda = girar_imagenes(proyectil_mecha_derecha, True, False)

reescalar_imagenes(proyectil_pingu_derecha, (40, 12))
reescalar_imagenes(proyectil_pingu_izquierda, (40, 12))
reescalar_imagenes(proyectil_mecha_derecha, (40, 12))
reescalar_imagenes(proyectil_mecha_izquierda, (40, 12))

diccionario_proyectiles = {"proyectil_pingu_derecha" : proyectil_pingu_derecha,
                        "proyectil_pingu_izquierda" : proyectil_pingu_izquierda,
                        "proyectil_mecha_derecha" : proyectil_mecha_derecha,
                        "proyectil_mecha_izquierda" : proyectil_mecha_izquierda}

#ENEMIGOS
enemigo_quieto_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Quieto\\0.png")]
enemigo_quieto_izquierda = girar_imagenes(enemigo_quieto_derecha, True, False)

enemigo_camina_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\0.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\1.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\2.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\3.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\4.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\5.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\6.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\7.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\8.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\9.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Corre\\10.png")]
enemigo_camina_izquierda = girar_imagenes(enemigo_camina_derecha, True, False)

enemigo_salta_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Salta\\0.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Salta\\1.png")]
enemigo_salta_izquierda = girar_imagenes(enemigo_salta_derecha, True, False)


enemigo_lanza_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\0.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\1.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\2.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\3.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\4.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\5.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\6.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\7.png")]
enemigo_lanza_izquierda = girar_imagenes(enemigo_lanza_derecha, True, False)

enemigo_ataca_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\0.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\1.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\2.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\3.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\4.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\5.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\6.png"),
                        pygame.image.load("AA Picky Adventure\\Imágenes\\Enemigo\\Ataca\\7.png")]
enemigo_ataca_izquierda = girar_imagenes(enemigo_ataca_derecha, True, False)

reduccion = 10
reescalar_imagenes(enemigo_quieto_derecha, (232/reduccion, 439/reduccion))
reescalar_imagenes(enemigo_quieto_izquierda, (232/reduccion, 439/reduccion))
reescalar_imagenes(enemigo_camina_derecha, (362/reduccion, 439/reduccion))
reescalar_imagenes(enemigo_camina_izquierda, (362/reduccion, 439/reduccion))
reescalar_imagenes(enemigo_salta_derecha, (362/reduccion, 439/reduccion))
reescalar_imagenes(enemigo_salta_izquierda, (362/reduccion, 439/reduccion))
reescalar_imagenes(enemigo_lanza_derecha, (377/reduccion, 439/reduccion))
reescalar_imagenes(enemigo_lanza_izquierda, (377/reduccion, 439/reduccion))
reescalar_imagenes(enemigo_ataca_derecha, (536/reduccion, 495/reduccion))
reescalar_imagenes(enemigo_ataca_izquierda, (536/reduccion, 495/reduccion))


diccionario_animaciones_enemigo = {"quieto_derecha" : enemigo_quieto_derecha,
                                    "quieto_izquierda" : enemigo_quieto_izquierda,
                                    "camina_derecha" : enemigo_camina_derecha,
                                    "camina_izquierda" : enemigo_camina_izquierda,
                                    "salta_derecha" : enemigo_salta_derecha,
                                    "salta_izquierda" : enemigo_salta_izquierda,
                                    "lanza_derecha" : enemigo_lanza_derecha,
                                    "lanza_izquierda" : enemigo_lanza_izquierda,
                                    "ataca_derecha" : enemigo_ataca_derecha,
                                    "ataca_izquierda" : enemigo_ataca_izquierda}


#BOSS MECHA
boss_mecha_quieto_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Quieto\\0.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Quieto\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Quieto\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Quieto\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Quieto\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Quieto\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Quieto\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Quieto\\3.png"),]
boss_mecha_quieto_izquierda = girar_imagenes(boss_mecha_quieto_derecha, True, False)

boss_mecha_camina_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\0.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\1.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\2.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\2.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\2.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\2.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\3.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\3.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\3.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\4.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\4.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\4.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\5.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\5.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\5.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Corre\\6.png")]
boss_mecha_camina_izquierda = girar_imagenes(boss_mecha_camina_derecha, True, False)

boss_mecha_salta_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Salta\\0.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Salta\\1.png")]
boss_mecha_salta_izquierda = girar_imagenes(boss_mecha_salta_derecha, True, False)


boss_mecha_lanza_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\0.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\1.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\1.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\1.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\2.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\2.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\2.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\3.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\3.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\3.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\4.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\4.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\4.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\5.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\5.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\5.png")
                            ,pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Ataca\\6.png")]
boss_mecha_lanza_izquierda = girar_imagenes(boss_mecha_lanza_derecha, True, False)

boss_mecha_ataca_derecha = [pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\0.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\1.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\2.png"),
                            pygame.image.load("AA Picky Adventure\\Imágenes\\Jefe final\\Melee\\3.png")]
boss_mecha_ataca_izquierda = girar_imagenes(boss_mecha_ataca_derecha, True, False)

reduccion = 5
reescalar_imagenes(boss_mecha_quieto_derecha, (273/reduccion, 468/reduccion))
reescalar_imagenes(boss_mecha_quieto_izquierda, (273/reduccion, 468/reduccion))
reescalar_imagenes(boss_mecha_camina_derecha, (366/reduccion, 468/reduccion))
reescalar_imagenes(boss_mecha_camina_izquierda, (366/reduccion, 468/reduccion))
reescalar_imagenes(boss_mecha_salta_derecha, (400/reduccion, 468/reduccion))
reescalar_imagenes(boss_mecha_salta_izquierda, (400/reduccion, 468/reduccion))
reescalar_imagenes(boss_mecha_lanza_derecha, (360/reduccion, 468/reduccion))
reescalar_imagenes(boss_mecha_lanza_izquierda, (360/reduccion, 468/reduccion))
reescalar_imagenes(boss_mecha_ataca_derecha, (517/reduccion, 546/reduccion))
reescalar_imagenes(boss_mecha_ataca_izquierda, (517/reduccion, 546/reduccion))

diccionario_animaciones_boss_mecha = {"quieto_derecha" : boss_mecha_quieto_derecha,
                                    "quieto_izquierda" : boss_mecha_quieto_izquierda,
                                    "camina_derecha" : boss_mecha_camina_derecha,
                                    "camina_izquierda" : boss_mecha_camina_izquierda,
                                    "salta_derecha" : boss_mecha_salta_derecha,
                                    "salta_izquierda" : boss_mecha_salta_izquierda,
                                    "lanza_derecha" : boss_mecha_lanza_derecha,
                                    "lanza_izquierda" : boss_mecha_lanza_izquierda,
                                    "ataca_derecha" : boss_mecha_ataca_derecha,
                                    "ataca_izquierda" : boss_mecha_ataca_izquierda}