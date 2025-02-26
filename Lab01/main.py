from Lab01.Domanda import Domanda
from Lab01.Giocatore import Giocatore


def main():
    print("Esecuzione programma:")
    domanda1 = Domanda(
    "Capitale dell'Italia?",
    0,
    "Roma",
    ["Milano", "Berlino", "Parigi"]
    )
    domanda1.mostra_domanda()
    giocatori = leggi_giocatori_e_punti("punti.txt")
    for giocatore in giocatori:
        giocatore.stampa_giocatote()


def leggi_giocatori_e_punti(nomeFile):
    giocatori = []
    with open(nomeFile) as f:
        for line in f:
            line = line.strip("\n")
            campi = line.split(" ")
            giocatore = Giocatore(campi[0],int(campi[1]))
            giocatori.append(giocatore)

    return giocatori




main()