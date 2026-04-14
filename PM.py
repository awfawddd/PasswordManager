import json
import os
import time
class PasswordManager:
    def __init__(self):
        self.file = "passwords.json"
        if os.path.exists(self.file):
            with open(self.file, "r", encoding="utf-8") as f:
                self.dati = json.load(f)
        else:
            self.dati = {}

    def salva(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.dati, f, ensure_ascii=False, indent=4)
    def aggiungi(self, sito, username, password):
        self.dati[sito] = {"username": username, "password": password}
        self.salva()
    def rimuovi(self, sito):
        del self.dati[sito]
        self.salva()
    def cerca(self, sito):
        if sito in self.dati:
            print(self.dati[sito]["username"])
            print(self.dati[sito]["password"])
        else:
            print("Sito non trovato.")
    def mostra(self):
        if self.dati:
            for sito in self.dati:
                print(sito, "-", self.dati[sito]["username"], "-", self.dati[sito]["password"])
        else:
            print("Niente dati")
pm = PasswordManager()
while True: 
    cosa = input("Cosa vuoi fare: ")
    cosa_lower = cosa.lower()
    if cosa_lower.startswith("aggiungi"):
        sito = input("Inserisci nome sito: ")
        username = input("Inserisci nome utente: ")
        password = input("Inserisci password: ")
        pm.aggiungi(sito, username, password)
        print("Salvato!")
    elif cosa_lower.startswith("rimuovi"):
        sito = input("Sito da rimuovere: ")
        pm.rimuovi(sito)
        print("Rimosso!")
    elif cosa_lower.startswith("cerca"):
        sito = input("Sito da cercare: ")
        pm.cerca(sito)
    elif cosa_lower.startswith("mostra"):
        pm.mostra()
    elif cosa_lower == "esci":
        break
    # esci dal programma