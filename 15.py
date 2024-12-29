import random
import time
import json
from datetime import datetime
import sys

def caricamento(durata=1.5, messaggio="Caricamento"):
    caratteri = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    inizio = time.time()
    i = 0
    while time.time() - inizio < durata:
        sys.stdout.write(f'\r{messaggio} {caratteri[i % len(caratteri)]}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print("\r" + " " * (len(messaggio) + 2))

def pulisci_schermo():
    print("\n" * 50)

class Zona:
    def __init__(self, nome, descrizione, tipo, pericolo=1):
        self.nome = nome
        self.descrizione = descrizione
        self.tipo = tipo
        self.pericolo = pericolo
        self.collegamenti = []
        self.oggetti_interagibili = [
            "chiave magnetica",
            "documento classificato",
            "strumento scientifico",
            "chip di memoria",
            "batteria quantica",
            "dispositivo sconosciuto"
        ]

class GiocatoreLevel15:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = []
        self.posizione_attuale = None
        self.salute = 100
        self.livello_radiazioni = 0
        self.scoperte = RegistroScoperte()
        self.ha_accesso_radar = False
        self.ha_accesso_terminale = False
        
    def muovi(self, nuova_zona):
        self.posizione_attuale = nuova_zona
        print(f"\nTi sei spostato in: {nuova_zona.nome}")
        
    def raccogli_oggetto(self, oggetto):
        self.inventario.append(oggetto)
        print(f"\nHai raccolto: {oggetto}")
class SistemaEsplorazione:
    def __init__(self):
        self.scoperte = []
        self.zone_esplorate = set()
        
    def esplora_zona(self, zona, giocatore):
        dettagli = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'zona': zona.nome,
            'oggetti_trovati': []
        }
        
        print(f"\nEsplorando: {zona.nome}")
        print(f"{zona.descrizione}")
        
        if random.random() < 0.3:
            oggetto = random.choice(zona.oggetti_interagibili)
            dettagli['oggetti_trovati'].append(oggetto)
            print(f"\nHai trovato: {oggetto}")
            giocatore.inventario.append(oggetto)
        
        self.scoperte.append(dettagli)
        self.zone_esplorate.add(zona.nome)
        return dettagli

class TerminaleComputer:
    def __init__(self):
        self.sistema_operativo = "Avalon 2.4"
        self.file_disponibili = {
            'log_ricerca': 'Documenti sulle ricerche delle macchine',
            'radar_dati': 'Dati del sistema radar',
            'email': 'Comunicazioni tra ricercatori',
            'manuali_tecnici': 'Documentazione sulle macchine'
        }
        self.email_sistema = [
            {
                'mittente': 'Dr. [REDATTO]',
                'oggetto': 'Anomalie spaziali',
                'contenuto': 'Le macchine stanno generando distorsioni sempre più frequenti.'
            },
            {
                'mittente': 'Sistema',
                'oggetto': 'AVVISO AUTOMATICO',
                'contenuto': 'Rilevata collisione tra livelli nel settore 7.'
            },
            {
                'mittente': 'Tecnico Capo',
                'oggetto': 'Manutenzione urgente',
                'contenuto': 'I sistemi di contenimento stanno cedendo.'
            }
        ]
    
    def accedi(self):
        caricamento(1.5, "Accesso al sistema Avalon 2.4")
        print(f"\nTerminale {self.sistema_operativo} - Accesso effettuato")
        return self.menu_principale()
    def menu_principale(self):
        while True:
            print("\nMenu Terminale:")
            print("1. Accedi ai file")
            print("2. Sistema Radar")
            print("3. Email")
            print("4. Esci")
            
            scelta = input("Seleziona opzione: ")
            if scelta == "1":
                self.mostra_file()
            elif scelta == "2":
                self.sistema_radar()
            elif scelta == "3":
                self.leggi_email()
            elif scelta == "4":
                break
    
    def mostra_file(self):
        caricamento(1, "Caricamento file")
        print("\nFile disponibili:")
        for nome, descrizione in self.file_disponibili.items():
            print(f"- {nome}: {descrizione}")
    
    def sistema_radar(self):
        caricamento(1.5, "Inizializzazione radar")
        radar = SistemaRadar()
        radar.aggiorna_radar()
    
    def leggi_email(self):
        caricamento(1, "Caricamento messaggi")
        for email in self.email_sistema:
            print(f"\nDa: {email['mittente']}")
            print(f"Oggetto: {email['oggetto']}")
            print(f"Contenuto: {email['contenuto']}")
            print("-" * 50)

class SistemaRadar:
    def __init__(self):
        self.oggetti_tracciati = []
        self.collegamenti = []
        self.anomalie = []
    
    def aggiorna_radar(self):
        caricamento(2, "Scansione radar in corso")
        self.genera_movimento()
        self.mostra_stato_radar()
    
    def genera_movimento(self):
        self.oggetti_tracciati = [
            {"id": 1, "tipo": "livello", "posizione": "centrale", "movimento": "stabile"},
            {"id": 2, "tipo": "anomalia", "posizione": "nord-est", "movimento": "oscillante"},
            {"id": 3, "tipo": "distorsione", "posizione": "sud", "movimento": "erratico"}
        ]
        
        self.anomalie = [
            {"tipo": "collisione", "intensità": random.randint(1, 10)},
            {"tipo": "distorsione", "intensità": random.randint(1, 10)}
        ]
    
    def mostra_stato_radar(self):
        print("\nStato Radar:")
        for oggetto in self.oggetti_tracciati:
            print(f"Oggetto {oggetto['id']}: {oggetto['tipo']} - {oggetto['posizione']} - {oggetto['movimento']}")
        
        print("\nAnomalie rilevate:")
        for anomalia in self.anomalie:
            print(f"- {anomalia['tipo'].upper()}: Intensità {anomalia['intensità']}")
class PericoliAmbientali:
    def __init__(self):
        self.pericoli = {
            'radiazioni': {
                'descrizione': 'Radiazioni dalla porta del vuoto',
                'effetto': 'degrado_salute',
                'intensità': range(5, 15)
            },
            'depressurizzazione': {
                'descrizione': 'Rischio depressurizzazione nelle zone danneggiate',
                'effetto': 'danno_immediato',
                'intensità': range(10, 25)
            },
            'macchinari_instabili': {
                'descrizione': 'Macchinari che potrebbero esplodere',
                'effetto': 'esplosione',
                'intensità': range(15, 30)
            },
            'zone_buie': {
                'descrizione': 'Zone completamente buie e pericolose',
                'effetto': 'disorientamento',
                'intensità': range(3, 8)
            }
        }
    
    def controlla_pericoli(self, zona):
        caricamento(1, "Analisi ambientale")
        pericoli_presenti = []
        for nome_pericolo, dati_pericolo in self.pericoli.items():
            if random.random() < 0.2:
                pericoli_presenti.append({
                    'tipo': nome_pericolo,
                    'descrizione': dati_pericolo['descrizione'],
                    'livello_rischio': random.choice(dati_pericolo['intensità']),
                    'effetto': dati_pericolo['effetto']
                })
        return pericoli_presenti

class RegistroScoperte:
    def __init__(self):
        self.scoperte = []
        self.timestamp_inizio = datetime.now()
        self.categorie_scoperte = {
            'documenti': [],
            'anomalie': [],
            'oggetti': [],
            'zone': []
        }
    
    def aggiungi_scoperta(self, scoperta):
        caricamento(1, "Registrazione scoperta")
        dettaglio_scoperta = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'tipo': scoperta['tipo'],
            'descrizione': scoperta['descrizione'],
            'coordinate': scoperta.get('coordinate', 'Sconosciute'),
            'categoria': scoperta.get('categoria', 'generale')
        }
        
        self.scoperte.append(dettaglio_scoperta)
        if dettaglio_scoperta['categoria'] in self.categorie_scoperte:
            self.categorie_scoperte[dettaglio_scoperta['categoria']].append(dettaglio_scoperta)
            
        print(f"\nNuova scoperta registrata: {dettaglio_scoperta['tipo']}")
    
    def esporta_registro(self):
        return json.dumps({
            'totale_scoperte': len(self.scoperte),
            'tempo_esplorazione': str(datetime.now() - self.timestamp_inizio),
            'scoperte_per_categoria': {k: len(v) for k, v in self.categorie_scoperte.items()},
            'dettagli': self.scoperte
        }, indent=4, ensure_ascii=False)
class GestoreEventi:
    def __init__(self):
        self.eventi_attivi = {}
        self.eventi_disponibili = {
            'collisione_livelli': {
                'nome': 'Collisione tra Livelli',
                'descrizione': 'Due forme sul radar si sovrappongono, causando una distorsione spaziale.',
                'probabilita': 0.1,
                'requisiti': ['accesso_radar'],
                'conseguenze': ['apertura_varco', 'distorsione_spaziale']
            },
            'malfunzionamento_macchine': {
                'nome': 'Malfunzionamento Macchinari',
                'descrizione': 'I macchinari iniziano a comportarsi in modo anomalo.',
                'probabilita': 0.25,
                'requisiti': ['zona_macchine'],
                'conseguenze': ['esplosione', 'radiazioni']
            },
            'scoperta_documenti': {
                'nome': 'Archivio Segreto',
                'descrizione': 'Un terminale rivela documenti classificati sui collegamenti tra livelli.',
                'probabilita': 0.15,
                'requisiti': ['accesso_terminale'],
                'conseguenze': ['nuove_informazioni', 'aggiornamento_mappa']
            },
            'anomalia_spaziale': {
                'nome': 'Anomalia Spaziale',
                'descrizione': 'Lo spazio intorno a te inizia a distorcersi.',
                'probabilita': 0.2,
                'requisiti': ['zona_vuoto'],
                'conseguenze': ['teletrasporto', 'danno']
            }
        }

    def genera_evento(self, giocatore, zona_attuale):
        caricamento(1.5, "Analisi eventi ambientali")
        eventi_possibili = []
        for id_evento, evento in self.eventi_disponibili.items():
            if self.verifica_requisiti(evento['requisiti'], giocatore, zona_attuale):
                if random.random() < evento['probabilita']:
                    eventi_possibili.append(id_evento)
        
        if eventi_possibili:
            return self.attiva_evento(random.choice(eventi_possibili), giocatore)
        return None

    def verifica_requisiti(self, requisiti, giocatore, zona_attuale):
        for req in requisiti:
            if req == 'accesso_radar' and not giocatore.ha_accesso_radar:
                return False
            elif req == 'zona_macchine' and 'macchine' not in zona_attuale.tipo:
                return False
            elif req == 'accesso_terminale' and not giocatore.ha_accesso_terminale:
                return False
            elif req == 'zona_vuoto' and 'vuoto' not in zona_attuale.tipo:
                return False
        return True

    def attiva_evento(self, id_evento, giocatore):
        evento = self.eventi_disponibili[id_evento]
        caricamento(2, f"Attivazione evento: {evento['nome']}")
        print(f"\nEVENTO SPECIALE: {evento['nome']}")
        print(evento['descrizione'])
        
        for conseguenza in evento['conseguenze']:
            self.applica_conseguenza(conseguenza, giocatore)
        
        self.eventi_attivi[id_evento] = {
            'timestamp': datetime.now(),
            'stato': 'attivo'
        }
        
        return evento

    def applica_conseguenza(self, conseguenza, giocatore):
        conseguenze = {
            'apertura_varco': lambda: self.apri_varco(giocatore),
            'distorsione_spaziale': lambda: self.distorsione_spaziale(giocatore),
            'esplosione': lambda: self.esplosione(giocatore),
            'radiazioni': lambda: self.radiazioni(giocatore),
            'nuove_informazioni': lambda: self.nuove_informazioni(giocatore),
            'aggiornamento_mappa': lambda: self.aggiorna_mappa(giocatore),
            'teletrasporto': lambda: self.teletrasporto(giocatore),
            'danno': lambda: self.danno(giocatore)
        }
        
        if conseguenza in conseguenze:
            conseguenze[conseguenza]()

class Level15Game:
    def __init__(self):
        self.giocatore = None
        self.gestore_eventi = GestoreEventi()
        self.sistema_esplorazione = SistemaEsplorazione()
        self.pericoli = PericoliAmbientali()
        self.inizializza_zone()
        
    def inizializza_zone(self):
        self.zone = {
            'controllo': Zona('Sala Controllo', 'Una grande sala piena di terminali e schermi.', ['controllo', 'sicuro'], 1),
            'macchine': Zona('Sala Macchine', 'Enormi macchinari ronzano dietro vetri rinforzati.', ['macchine', 'pericolo'], 3),
            'corridoio': Zona('Corridoio Principale', 'Un lungo corridoio bianco con luci fluorescenti.', ['corridoio'], 2),
            'laboratorio': Zona('Laboratorio', 'Un laboratorio abbandonato con strumenti strani.', ['ricerca'], 2),
            'vuoto': Zona('Stanza del Vuoto', 'Una stanza con una porta che da sul vuoto cosmico.', ['vuoto', 'pericolo'], 4)
        }
        
        # Definizione collegamenti
        self.zone['controllo'].collegamenti = [self.zone['corridoio'], self.zone['macchine']]
        self.zone['macchine'].collegamenti = [self.zone['controllo'], self.zone['laboratorio']]
        self.zone['corridoio'].collegamenti = [self.zone['controllo'], self.zone['laboratorio'], self.zone['vuoto']]
        self.zone['laboratorio'].collegamenti = [self.zone['corridoio'], self.zone['macchine']]
        self.zone['vuoto'].collegamenti = [self.zone['corridoio']]

    def inizia_gioco(self):
        pulisci_schermo()
        print("=== BACKROOMS: LEVEL 15 ===")
        print("La Stazione Tecnologica Infinita")
        caricamento(2, "Inizializzazione Level 15")
        
        nome = input("\nInserisci il tuo nome: ")
        self.giocatore = GiocatoreLevel15(nome)
        self.giocatore.posizione_attuale = self.zone['controllo']
        
        self.tutorial()
        self.loop_principale()
    
    def tutorial(self):
        print("\nBenvenuto nel Level 15...")
        caricamento(1, "Caricamento tutorial")
        print("\nTi trovi in una struttura futuristica infinita.")
        print("Corridoi bianchi e grigi si estendono all'infinito.")
        print("Macchine misteriose ronzano dietro vetri rinforzati.")
        input("\nPremi INVIO per continuare...")
    
    def loop_principale(self):
        while self.giocatore.salute > 0:
            pulisci_schermo()
            self.mostra_stato()
            self.gestisci_input()
            
            caricamento(1, "Elaborazione azioni")
            
            if random.random() < 0.3:
                self.gestore_eventi.genera_evento(self.giocatore, self.giocatore.posizione_attuale)
            
            pericoli = self.pericoli.controlla_pericoli(self.giocatore.posizione_attuale)
            if pericoli:
                self.gestisci_pericoli(pericoli)
            
            time.sleep(1)
        
        print("\nGAME OVER")
    
    def mostra_stato(self):
        print(f"\nPosizione: {self.giocatore.posizione_attuale.nome}")
        print(f"Salute: {self.giocatore.salute}")
        print(f"Livello Radiazioni: {self.giocatore.livello_radiazioni}")
        print("\nAzioni disponibili:")
        print("1. Esplora")
        print("2. Usa terminale")
        print("3. Sposta")
        print("4. Inventario")
        print("5. Registro scoperte")
        print("6. Esci")
    
    def gestisci_input(self):
        azione = input("\nCosa vuoi fare? ")
        
        if azione == "1":
            caricamento(2, "Esplorazione in corso")
            self.sistema_esplorazione.esplora_zona(self.giocatore.posizione_attuale, self.giocatore)
        elif azione == "2":
            caricamento(1, "Accesso al terminale")
            terminale = TerminaleComputer()
            terminale.accedi()
        elif azione == "3":
            self.cambia_zona()
        elif azione == "4":
            self.mostra_inventario()
        elif azione == "5":
            self.mostra_registro()
        elif azione == "6":
            self.termina_gioco()
    
    def cambia_zona(self):
        print("\nZone disponibili:")
        for i, zona in enumerate(self.giocatore.posizione_attuale.collegamenti):
            print(f"{i+1}. {zona.nome}")
            
        scelta = input("\nScegli zona (numero): ")
        caricamento(2, "Spostamento in corso")
        try:
            nuova_zona = self.giocatore.posizione_attuale.collegamenti[int(scelta)-1]
            self.giocatore.muovi(nuova_zona)
        except:
            print("Scelta non valida!")
    
    def mostra_inventario(self):
        caricamento(1, "Apertura inventario")
        if self.giocatore.inventario:
            print("\nInventario:")
            for item in self.giocatore.inventario:
                print(f"- {item}")
        else:
            print("\nInventario vuoto!")
    
    def mostra_registro(self):
        caricamento(1, "Caricamento registro")
        print("\nRegistro Scoperte:")
        print(self.giocatore.scoperte.esporta_registro())
    
    def gestisci_pericoli(self, pericoli):
        for pericolo in pericoli:
            print(f"\nATTENZIONE: {pericolo['descrizione']}")
            self.giocatore.salute -= pericolo['livello_rischio']
    
    def termina_gioco(self):
        caricamento(2, "Salvataggio dati")
        print("\nGrazie per aver esplorato il Level 15!")
        sys.exit()


if __name__ == "__main__":
    gioco = Level15Game()
    gioco.inizia_gioco()
