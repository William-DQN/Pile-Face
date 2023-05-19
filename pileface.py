#Ce code va nous permettre de répondre à une question proposant 2 réponses et ce aléatoirement
import random
input("Quel est le problème ? : ")
choix = input("Veillez entrez un choix : ")
choix2 = input("Veillez entrez un second choix : ")
rand = random.randint(1, 10000)
if rand % 2:
    print("Voilà votre réponse : " + choix)
else:
    print("Voilà votre réponse : " + choix2)
