from random import choice
from komputer import najlepszy_ruch, czy_koniec, najlepsze_ruchy
import pygame
pygame.init()
czcionka = pygame.font.Font(None, 140)
X = czcionka.render('X', True, (255, 0, 0))
O = czcionka.render('O', True, (0, 0, 255))
def draw(screen, plansza):
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 300), 1)
    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 2)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 2)
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 300), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (300, 0), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (300, 300), 1)
    for i in range(3):
        for j in range(3):
            if plansza[i][j] == 1:
                X_rect = X.get_rect()
                X_rect.center = (j * 100 + 55, i * 100 + 60)
                screen.blit(X, X_rect)
            elif plansza[i][j] == -1:
                O_rect = O.get_rect()
                O_rect.center = (j * 100 + 50, i * 100 + 55)
                screen.blit(O, O_rect)
    pygame.display.flip()
# choosen = 0
screen = pygame.display.set_mode((300, 300))
# while not choosen:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             choosen = 'X'
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = event.pos
#             if x < 150:
#                 choosen = 'O'
#             else:
#                 choosen = 'X'
#     screen.fill((255, 255, 255))
#     X_rect = X.get_rect()
#     X_rect.center = (100, 150)
#     screen.blit(X, X_rect)
#     O_rect = O.get_rect()
#     O_rect.center = (200, 150)
#     screen.blit(O, O_rect)
#     pygame.display.flip()
# kolor = choosen
kolor = choice(['X', 'O'])
plansza = [[0,0,0],[0,0,0],[0,0,0]]
running = True
koniec_gry = False
if kolor == 'X':
    plansza = najlepszy_ruch(plansza, najlepsze_ruchy)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not koniec_gry:
            x, y = event.pos
            i, j = y // 100, x // 100
            if plansza[i][j] == 0:
                plansza[i][j] = -1 if kolor == 'X' else 1
                if czy_koniec(plansza) != 2:
                    koniec_gry = True
                    break
                plansza = najlepszy_ruch(plansza, najlepsze_ruchy)
                if czy_koniec(plansza) != 2:
                    koniec_gry = True
    draw(screen, plansza)