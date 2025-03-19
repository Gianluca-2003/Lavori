from Lab01.Domanda import Domanda
from Lab01.Giocatore import Giocatore
import random


def main():
    print("Esecuzione programma:")
    giocatori = leggi_giocatori_e_punti("punti.txt")
    domande = leggi_domande("domande.txt")
    punteggio =gioca(domande)
    nome = input("Inserisci il tuo nome: ")
    aggiunto = False
    for giocatore in giocatori:
        if giocatore.nome == nome:
            aggiunto = True
            giocatore.punti += punteggio
    if aggiunto == False:
        giocatore = Giocatore(nome, punteggio)
        giocatori.append(giocatore)
    giocatori_ord = sorted(giocatori)
    print("CLASSIFICA: ")

    for giocatore in giocatori_ord:
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

def leggi_domande(nomeFile):
    domande = []
    with open(nomeFile) as file:
        righe = [line.strip() for line in file if line.strip()]

        i = 0
        while i < len(righe):
            testo = righe[i]
            difficolta = int(righe[i+1])
            risposta_corretta = righe[i+2]
            risposte_errate = [righe[i+2],righe[i+3], righe[i+4], righe[i+5]]
            domanda = Domanda(testo,difficolta,risposta_corretta,risposte_errate)
            domande.append(domanda)
            i += 6

    return domande

def trova_livello_max(domande):
    livello_max = 0
    for domanda in domande:
        if domanda.difficolta > livello_max:
            livello_max = domanda.difficolta
    return livello_max



def gioca(domande):
    ok = True
    punteggio = 0
    livello_max = trova_livello_max(domande)
    print(livello_max)
    random.shuffle(domande)
    cnt = 0
    while ok:
        for domanda in domande:
            random.shuffle(domande)
            if cnt> livello_max:
                ok = False
                break
            if domanda.difficolta == cnt:
                domanda.mostra_domanda()
                numero = int(input("Inserisci la tua risposta: " ))
                if numero != domanda.indice_domanda_giusta():
                    print("Risposta Sbagliata")
                    ok = False
                    break
                else:
                    print("Risposta corretta")
                    punteggio += 1
                    cnt += 1

    return punteggio




main()