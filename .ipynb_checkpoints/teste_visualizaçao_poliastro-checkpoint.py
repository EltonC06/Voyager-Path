from poliastro.ephem import Ephem
from poliastro.plotting.static import StaticOrbitPlotter
from poliastro.bodies import Sun, Earth, Mars
from poliastro.twobody import Orbit
from astropy.time import Time

epoch = Time("2024-12-26", scale="tdb") # Definição de Efemérides
terra_ephem = Ephem.from_body(Earth, epoch)
marte_ephem = Ephem.from_body(Mars, epoch)

# Defini orbitas
terra_orbit = Orbit.from_ephem(Sun, terra_ephem, epoch)
marte_orbit = Orbit.from_ephem(Sun, marte_ephem, epoch)

# Visualizar 2d:
plotter = StaticOrbitPlotter()
plotter.plot(terra_orbit, label="Planeta Elton")
plotter.plot(marte_orbit, label="Marte")

