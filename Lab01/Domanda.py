class Domanda:

    def __init__(self, testo, difficolta, risposta_corretta, risposte_errate):
        self.testo = testo
        self.difficolta = difficolta
        self.risposta_corretta = risposta_corretta
        self.risposte_errate = risposte_errate


    def mostra_domanda(self):
        print(f"Livello: {self.difficolta}) {self.testo}")
        opzioni = self.risposte_errate + [self.risposta_corretta]
        import random
        random.shuffle(opzioni)
        for i,opzione in enumerate(opzioni):
            print(f"{i+1}). {opzione}")

