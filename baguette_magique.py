from Crypto.Cipher import ChaCha20
from base64 import b64encode, b64decode
from hashlib import sha256

NONCE = b"hedwighedwig"

def créer_baguette_magique():
    with open("key", "rb") as f:
        KEY = f.read()
    return sha256(KEY).digest() # Voir avec Ollivander

def ensorceler_message(sortilège, baguette_magique):
    sortilège_de_sortie = ChaCha20.new(key=baguette_magique, nonce=NONCE)
    message_ensorcelé = sortilège_de_sortie.encrypt(sortilège)
    return b64encode(message_ensorcelé).decode('utf-8')

def désensorceler_message(ensorcelé, baguette_magique):
    # Vous aurez besoin de la formule apprise dans le cours du professeur Rogue
    pass

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une baguette magique
    baguette_magique = créer_baguette_magique()

    # Sortilège à ensorceler
    with open("flag", "rb") as f:
        sortilège_à_ensorceler = f.read()

    # Ensorceler le sortilège
    sortilège_ensorcelé = ensorceler_message(sortilège_à_ensorceler, baguette_magique)
    print("Sortilège ensorcelé:", sortilège_ensorcelé)

    with open("encoded.bin", "w") as f:
        f.write(sortilège_ensorcelé)

    # Désensorceler le sortilège
    sortilège_désensorcelé = désensorceler_message(sortilège_ensorcelé, baguette_magique)
    print("Sortilège désensorcelé:", sortilège_désensorcelé)
