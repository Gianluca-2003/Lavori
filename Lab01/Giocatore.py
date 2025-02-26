class Giocatore:
    def __init__(self, nome,punti):
        self.nome = nome
        self.punti = punti

    def stampa_giocatote(self):
        print(f"{self.nome} {self.punti}")