import time
import random
import sys
import os

# Ajuste para o Python achar as pastas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from security.stinger_log import Stinger

class SilkQueue:
    def process(self, bot_id):
        print(f"  ⏳ [SILK QUEUE] Retendo Bot {bot_id}... Cadência em 1.0s")
        time.sleep(1) 

class SpiderSmashEngine:
    def __init__(self):
        self.hits = {}
        self.stinger = Stinger()
        self.silk = SilkQueue()

    def handle_request(self, bot_id):
        if self.stinger.check_immunity(bot_id):
            return f"❌ [O FERRÃO] Neutralizado: {bot_id} já está na base."

        self.hits[bot_id] = self.hits.get(bot_id, 0) + 1

        if self.hits[bot_id] < 3:
            return f"🟢 [GATEWAY] {bot_id}: Requisição {self.hits[bot_id]}/3"

        print(f"⚠️ [ALERTA] Padrão Detectado em {bot_id}!")
        self.stinger.mark_bot(bot_id)
        self.silk.process(bot_id)
        return f"🕸️ [SPIDER SMASH] Bot {bot_id} capturado e reciclado."

engine = SpiderSmashEngine()
bots_simulados = ["Bot-Alpha", "Bot-Beta"]

print("\n--- 🕷️ INICIANDO PROTOCOLO SPIDER SMASH ---\n")

for i in range(8):
    bot_da_vez = random.choice(bots_simulados)
    print(engine.handle_request(bot_da_vez))
    time.sleep(0.3)