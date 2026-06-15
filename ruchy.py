import pickle
drzewo_gry = {}
najlepsze_ruchy = {}
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
def moziwe_ruchy(plansza):
    if czy_koniec(plansza) != 2:
        return {'i': (czy_koniec(plansza), {})}
    ruchy = {}
    for i in range(3):
        for j in range(3):
            if plansza[i][j] == 0:
                a = [[x for x in p] for p in plansza]
                a[i][j] = -1 if sum(p for x in plansza for p in x) > 0 else 1
                b = moziwe_ruchy(a)
                a2 = tuple(tuple(x) for x in a)
                plansza2 = tuple(tuple(x) for x in plansza)
                if plansza2 not in najlepsze_ruchy:
                    najlepsze_ruchy[plansza2] = {}
                najlepsze_ruchy[plansza2][a2] = (-min(v[0] for v in b.values()))
                ruchy[a2] = (-min(v[0] for v in b.values()),b)
    return ruchy
drzewo_gry = moziwe_ruchy([[0,0,0],
                           [0,0,0],
                           [0,0,0]])
with open('ruchy.pickle', 'wb') as f:
    pickle.dump(najlepsze_ruchy, f)
