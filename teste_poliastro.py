# Como calcular tempo de viagem de ponto A ate ponto B em determinada Data?
# 1º Saber posições iniciais de ponto A e B
# 2º Calcular a transferencia mais eficiente (trajetoria de hohnmann)
# 3º Calcular o tempo de viagem dessa transferencia
import math

from poliastro.bodies import Earth, Mars, Sun, Jupiter
from poliastro.maneuver import Maneuver
from poliastro.twobody import Orbit
from poliastro.util import time_range
from astropy import units as u
from astropy.time import Time
from poliastro.ephem import Ephem


# Definição de data inicial de partida (pelo usuario)
epoch = Time("2024-12-25 00:00:00", scale="tdb")

# Obter o vetor posição e velocidade da terra e marte em tempo real
terra_ephem = Ephem.from_body(Earth, epoch)
marte_ephem = Ephem.from_body(Mars, epoch)

print(f"Efemerides Terra: {terra_ephem}")
print(f"Efemerides Marte: {marte_ephem}")

# vetores de posição e de velocidade da terra e marte
r_terra, v_terra = terra_ephem.rv(epoch)
r_marte, v_marte = marte_ephem.rv(epoch)

print(f"Terra (Vetores e velocidade): {r_terra} | {v_terra}")
print(f"Marte (Vetores e velocidade): {r_marte} | {v_marte}")

# Criar orbitas da Terra e Marte baseado nos vetores
terra_orbita = Orbit.from_vectors(Sun, r_terra, v_terra, epoch)
marte_orbita = Orbit.from_vectors(Sun, r_marte, v_marte, epoch)

print(f"Orbita Terra: {terra_orbita}")
print(f"Orbita Marte: {marte_orbita}")

# Transforma orbita em semieixos


# Estimulando tempo de viagem
#flight_time = man.get_total_time().to(u.day)


# print(f"Tempo estimado de viagem da Terra até Marte partindo da data de hoje: {transfer_time.to(u.day):.2f} dias")

# efemerides -> vetores -> orbita -> calcular
