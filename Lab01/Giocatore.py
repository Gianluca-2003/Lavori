class Giocatore:
    def __init__(self, nome,punti):
        self.nome = nome
        self.punti = punti

    def stampa_giocatote(self):
        print(f"{self.nome} {self.punti}")

    def __lt__(self, other):
        """Confronta due giocatori in base al punteggio (ordine decrescente)"""
        return self.punti > other.punti