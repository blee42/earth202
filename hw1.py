from __future__ import division
import math

def c1(a, pm, pc, rc):
	# rc / a
	radius = rc / a;

	# moment of inertia
	I = (8 / 15) * math.pi * ((pm * math.pow(a,5)) + ((pc - pm) * math.pow(rc,5)))

	# mass
	M = (4 / 3) * math.pi * ((pm * math.pow(a,3)) + ((pc - pm) * math.pow(rc,3)))

	# moment of inertia ratio I/Ma^2
	ratio = I / (M * math.pow(a,2))

	return {
		'rc/a': radius,
		'I': I,
		'M': M,
		'I/Ma^2': ratio}

print("inputs (with units): ")
print("a (km) - radius")
print("pm (kg/m^3) - mantle density")
print ("pc (kg/m^3) - core density")
print ("rc (km) - core radius\n")

print("outputs (with units): ")
print("rc/a (unitless)")
print("I (kgkm^2) - moment of inertia")
print("M (kg) - mass")
print("I/Ma^2 (unitless) - moment of inertia ratio\n")

print("C-1.")
b = c1(6371, 5514, 5514, 3485)
print("b. pm = pc")
print(b)
print ("When pm = pc, I/Ma^2 equals 0.4 because there is uniform density distribution\n")

c = c1(5, 1, 0, 0.99*5)
print ("c. pc = 0 and rc = 0.99a")
print(c)
print ("When pc = 0 and rc = 0.99a, I/Ma^2 equals 0.667 because all of the density is in the shell\n")

d = c1(2439, 2100, 5427, 1220)
print ("d. plausible two-layer model for Mercury")
print (d)
print("A plausible two-layer model for Mercury assuming that I/Ma^2 equals 0.35 is")
print("a = 2439 km")
print ("pm = 2100 kg/m^3")
print ("pc = 5427 kg/m^3")
print ("rc = 1220 km")

