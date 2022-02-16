# made this to learn more about clicking and stuff in pygame

import pygame
import math
import sys
import time

pygame.init()

# basic ui stuff
dis = pygame.display.set_mode((370, 590))
pygame.display.set_caption("Calculator")
calc_icon = pygame.image.load("calc_icon.png")
pygame.display.set_icon(calc_icon)
font = pygame.font.Font("freesansbold.ttf", 64)
big_font = pygame.font.Font("freesansbold.ttf", 128)
small_font = pygame.font.Font("freesansbold.ttf", 32)

b_wh = 80  # button width / height

top_y = 140  # top row y pos
second_y = 230
third_y = 320
fourth_y = 410
last_y = 500

left_x = 10  # first button from the left x pos
s_x = 100
t_x = 190
l_x = 280

calc_sum = ""
stored_sum = ""
calc_func = ""


def draw_buttons_and_screen():
    # screen
    pygame.draw.rect(dis, (50, 50, 50), (10, 10, 350, 120))
    # buttons
    # 1st row
    pygame.draw.rect(dis, (50, 50, 50), (left_x, top_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (s_x, top_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (t_x, top_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (l_x, top_y, b_wh, b_wh))
    # second row
    pygame.draw.rect(dis, (50, 50, 50), (left_x, second_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (s_x, second_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (t_x, second_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (l_x, second_y, b_wh, b_wh))
    # third row
    pygame.draw.rect(dis, (50, 50, 50), (left_x, third_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (s_x, third_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (t_x, third_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (l_x, third_y, b_wh, b_wh))
    # 4th row
    pygame.draw.rect(dis, (50, 50, 50), (left_x, fourth_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (s_x, fourth_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (t_x, fourth_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (l_x, fourth_y, b_wh, b_wh))
    # last row
    pygame.draw.rect(dis, (50, 50, 50), (left_x, last_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (s_x, last_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (t_x, last_y, b_wh, b_wh))
    pygame.draw.rect(dis, (50, 50, 50), (l_x, last_y, b_wh, b_wh))


def draw_functions():
    dis.blit(font.render("÷", True, (255, 255, 255)), (l_x + 20, fourth_y + 10))
    dis.blit(font.render("X", True, (255, 255, 255)), (l_x + 20, third_y + 10))
    dis.blit(big_font.render("-", True, (255, 255, 255)), (l_x + 20, second_y - 25))
    # top row
    dis.blit(font.render("√", True, (255, 255, 255)), (left_x + 20, top_y + 10))
    dis.blit(small_font.render("x^y", True, (255, 255, 255)), (s_x + 15, top_y + 25))
    dis.blit(font.render("%", True, (255, 255, 255)), (t_x + 15, top_y + 10))
    dis.blit(font.render("+", True, (255, 255, 255)), (l_x + 20, top_y + 5))


def draw_numbers():
    # last row
    dis.blit(font.render("C", True, (255, 255, 255)), (left_x + 15, last_y + 10))
    dis.blit(font.render("0", True, (255, 255, 255)), (s_x + 22, last_y + 10))
    dis.blit(font.render(".", True, (255, 255, 255)), (t_x + 30, last_y + 10))
    dis.blit(font.render("=", True, (255, 255, 255)), (l_x + 22, last_y + 10))
    # 3rd row
    dis.blit(font.render("1", True, (255, 255, 255)), (left_x + 20, fourth_y + 10))
    dis.blit(font.render("2", True, (255, 255, 255)), (s_x + 22, fourth_y + 10))
    dis.blit(font.render("3", True, (255, 255, 255)), (t_x + 22, fourth_y + 10))
    # 2nd row
    dis.blit(font.render("4", True, (255, 255, 255)), (left_x + 20, third_y + 10))
    dis.blit(font.render("5", True, (255, 255, 255)), (s_x + 22, third_y + 10))
    dis.blit(font.render("6", True, (255, 255, 255)), (t_x + 22, third_y + 10))
    # 1st row
    dis.blit(font.render("7", True, (255, 255, 255)), (left_x + 20, second_y + 10))
    dis.blit(font.render("8", True, (255, 255, 255)), (s_x + 22, second_y + 10))
    dis.blit(font.render("9", True, (255, 255, 255)), (t_x + 22, second_y + 10))


def draw_answer():
    # screen
    dis.blit(font.render(f"{calc_sum}", True, (255, 255, 255)), (20, 60))


running = True
while running:

    mouse_pos = pygame.mouse.get_pos()  # get mouse position
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    dis.fill((0, 0, 0))
    calc_sum = calc_sum[:8]  # limits the string length to 8

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print("ok")

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_x, mouse_y)
            # last row
            if mouse_x in range(10, 91) and mouse_y in range(500, 581):  # clear button
                calc_sum = ""
            elif mouse_x in range(100, 181) and mouse_y in range(500, 581):
                calc_sum += "0"
            elif mouse_x in range(190, 271) and mouse_y in range(500, 581):
                if not "." in calc_sum:  # in order to ensure that there is only 1 "."
                    calc_sum += "."


            # = function
            elif mouse_x in range(280, 361) and mouse_y in range(140, 581)\
                    or mouse_x in range(100, 361) and mouse_y in range(140, 221):
                if not stored_sum == "":
                    try:
                        if calc_func == "+":
                            calc_sum = str(float(calc_sum) + float(stored_sum))
                            stored_sum = ""
                        if calc_func == "-":
                            calc_sum = str(float(stored_sum) - float(calc_sum))
                            stored_sum = ""
                        if calc_func == "*":
                            calc_sum = str(float(stored_sum) * float(calc_sum))
                            stored_sum = ""
                        if calc_func == "/":
                            if calc_sum == "0":
                                calc_sum = "nice try"
                                dis.fill((255, 0, 0))
                                draw_answer()
                                pygame.display.update()
                                time.sleep(2)
                                calc_sum = ""
                                stored_sum = ""
                            else:
                                calc_sum = str(float(stored_sum) / float(calc_sum))
                                stored_sum = ""
                        if calc_func == "**":
                            calc_sum = str(float(stored_sum) ** float(calc_sum))
                            stored_sum = ""
                        if calc_func == "%":
                            if calc_sum == "0":
                                calc_sum = "nice try"
                                dis.fill((255, 0, 0))
                                draw_answer()
                                pygame.display.update()
                                time.sleep(2)
                                calc_sum = ""
                                stored_sum = ""
                            else:
                                calc_sum = str(float(stored_sum) % float(calc_sum))
                                stored_sum = ""
                    except:
                        calc_sum = "bruh"
                        draw_answer()
                        pygame.display.update()
                        time.sleep(2)
                        calc_sum = ""
                        stored_sum = ""


            # numbers only
            elif mouse_x in range(10, 91) and mouse_y in range(410, 491):
                calc_sum += "1"
            elif mouse_x in range(100, 181) and mouse_y in range(410, 491):
                calc_sum += "2"
            elif mouse_x in range(190, 271) and mouse_y in range(410, 491):
                calc_sum += "3"
            # third row numbers only
            elif mouse_x in range(10, 91) and mouse_y in range(320, 401):
                calc_sum += "4"
            elif mouse_x in range(100, 181) and mouse_y in range(320, 401):
                calc_sum += "5"
            elif mouse_x in range(190, 271) and mouse_y in range(320, 401):
                calc_sum += "6"
            # second row numbers only
            elif mouse_x in range(10, 91) and mouse_y in range(230, 311):
                calc_sum += "7"
            elif mouse_x in range(100, 181) and mouse_y in range(230, 311):
                calc_sum += "8"
            elif mouse_x in range(190, 271) and mouse_y in range(230, 311):
                calc_sum += "9"

            # functions
            if mouse_x in range(280, 361) and mouse_y in range(410, 491):
                calc_func = "/"
                stored_sum = calc_sum
                calc_sum = ""
            if mouse_x in range(280, 361) and mouse_y in range(320, 401):
                calc_func = "*"
                stored_sum = calc_sum
                calc_sum = ""
            if mouse_x in range(280, 361) and mouse_y in range(230, 311):
                calc_func = "-"
                stored_sum = calc_sum
                calc_sum = ""
            if mouse_x in range(280, 361) and mouse_y in range(140, 221):
                calc_func = "+"
                stored_sum = calc_sum
                calc_sum = ""
            if mouse_x in range(190, 271) and mouse_y in range(140, 221):
                calc_func = "%"
                stored_sum = calc_sum
                calc_sum = ""
            if mouse_x in range(100, 181) and mouse_y in range(140, 221):
                calc_func = "**"
                stored_sum = calc_sum
                calc_sum = ""
            if mouse_x in range(10, 81) and mouse_y in range(140, 221):
                try:
                    calc_sum = str(math.sqrt(float(calc_sum)))
                except:
                    calc_sum = "bruh"
                    draw_answer()
                    pygame.display.update()
                    time.sleep(2)
                    calc_sum = ""

    draw_buttons_and_screen()
    draw_numbers()
    draw_functions()
    draw_answer()

    pygame.display.update()
