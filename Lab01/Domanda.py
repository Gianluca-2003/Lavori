class Domanda:

    def __init__(self, testo, difficolta, risposta_corretta, altre_risposte):
        self.testo = testo
        self.difficolta = difficolta
        self.risposta_corretta = risposta_corretta
        self.altre_risposte = altre_risposte


    def mostra_domanda(self):
        print(f"Livello: {self.difficolta}) {self.testo}")
        import random
        random.shuffle(self.altre_risposte)
        for i,opzione in enumerate(self.altre_risposte):
            print(f"{i+1}). {opzione}")

    def indice_domanda_giusta(self):
        indice_corretto = self.altre_risposte.index(self.risposta_corretta)
        return indice_corretto +1

