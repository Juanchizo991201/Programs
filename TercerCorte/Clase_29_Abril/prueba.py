import gravedad
import CyGravedad
import time

### Initialize the planet

earth = gravedad.planet()
earth.x = 100 * 10**3
earth.y = 300 * 10**3
earth.z = 700 * 10**3
earth.vx = 2.000 * 10**2
earth.vy = 29.870 * 10**3
earth.vz = 0.0034 * 10**3
earth.m = 5.9742 * 10**24

### Initialize the planet in python

earthCy = gravedad.planet()
earthCy.x = 100 * 10**3
earthCy.y = 300 * 10**3
earthCy.z = 700 * 10**3
earthCy.vx = 2.000 * 10**2
earthCy.vy = 29.870 * 10**3
earthCy.vz = 0.0034 * 10**3
earthCy.m = 5.9742 * 10**24

time_span = 400
n_steps = 2000000

inicio = time.time()
gravedad.step_time(earth, time_span, n_steps)
tiempoPy = time.time() - inicio

inicio = time.time()
CyGravedad.step_time(earthCy, time_span, n_steps)
tiempoCy = time.time() - inicio

speedUp = round(tiempoCy/tiempoPy,3)

print("Python time = {}\n".format(tiempoPy))
print("Cython time = {}\n".format(tiempoCy))
print("SpeedUp = {}\n".format(speedUp))


