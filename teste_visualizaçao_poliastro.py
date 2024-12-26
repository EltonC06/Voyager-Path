import matplotlib.pyplot as plt
from astropy.coordinates.builtin_frames.utils import norm
from poliastro.ephem import Ephem
from poliastro.plotting.static import StaticOrbitPlotter
from poliastro.bodies import Sun, Earth, Mars
from poliastro.twobody import Orbit
from astropy.time import Time
from poliastro.plotting import OrbitPlotter2D
from poliastro.maneuver import Maneuver
from astropy import units as u

# Esse codigo deve ser usado em uma celula do Jupyter
epoch = Time("2024-12-26", scale="tdb") # Definição de Efemérides
terra_ephem = Ephem.from_body(Earth, epoch, attractor=Sun)
marte_ephem = Ephem.from_body(Mars, epoch, attractor=Sun)

# Defini vetores de posição e velocidade baseado no tempo
terra_r, terra_v = terra_ephem.rv(epochs=epoch)
marte_r, marte_v = marte_ephem.rv(epochs=epoch)

terra_r = terra_r.to(u.m)  # Converte de AU para metros
terra_v = terra_v.to(u.m / u.s)  # Converte de km/s para m/s

marte_r = marte_r.to(u.m)  # Converte de AU para metros
marte_v = marte_v.to(u.m / u.s)  # Converte de km/s para m/s

# Defini orbitas a partir de vetores de posição e velocidade

marte_orbit = Orbit.from_vectors(Sun, marte_r, marte_v, epoch)
terra_orbit = Orbit.from_vectors(Sun, terra_r, terra_v, epoch)

# Transferencia de hohnmann
manobra = Maneuver.hohmann(terra_orbit, marte_orbit.r_p)

# Transforamndo o objeto Maneuver em Orbit baseado na orbita da terra
orbita_transferencia = terra_orbit.apply_maneuver(manobra)

# Visualizar 2d:
op = OrbitPlotter2D()
op.plot(marte_orbit, label="Marte", color="red")
op.plot(terra_orbit, label="Terra", color="blue")
op.plot(orbita_transferencia, label="Transferencia", color="black",)
