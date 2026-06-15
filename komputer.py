from random import choice
import pickle
with open('ruchy.pickle', 'rb') as f:
    najlepsze_ruchy = pickle.load(f)
def najlepszy_ruch(plansza, najlepsze_ruchy):
    plansza2 = tuple(tuple(x) for x in plansza)
    ruchy_1 = []
    ruchy0 = []
    ruchy1 = []
    for k,v in najlepsze_ruchy[plansza2].items():
        if v == -1:
            ruchy_1.append(k)
        elif v == 0:
            ruchy0.append(k)
        else:
            ruchy1.append(k) 
    if len(ruchy_1) > 0:
        return list(list(x) for x in choice(ruchy_1))
    elif len(ruchy0) > 0:
        return list(list(x) for x in choice(ruchy0))
    elif len(ruchy1) > 0:
        return list(list(x) for x in choice(ruchy1))
def czy_koniec(plansza):
    for i in range(3):
        if plansza[i][0] == plansza[i][1] == plansza[i][2] != 0:
            return 1
        if plansza[0][i] == plansza[1][i] == plansza[2][i] != 0:
            return 1
    if plansza[0][0] == plansza[1][1] == plansza[2][2] != 0:
        return 1
    if plansza[0][2] == plansza[1][1] == plansza[2][0] != 0:
        return 1
    if 0 not in [p for x in plansza for p in x]:
        return 0
    return 2