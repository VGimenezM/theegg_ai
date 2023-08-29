import tiempo
import random

random.seed(94)

t = random.randint(1,100)
altura = tiempo.tierra(t)
print(f"La altura en la tierra con un tiempo de {t} es de {altura}")

t = random.randint(1,100)
altura= tiempo.jupiter(t)
print(f"La altura en jupiter con un tiempo de {t} es de {altura}")

t = random.randint(1,100)
altura = tiempo.marte(t)
print(f"La altura en marte con un tiempo de {t} es de {altura}")




