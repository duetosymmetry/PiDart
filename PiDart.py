import math
import random

throws = 1e7

i = 0
hits = 0
while i < throws:
  x = random.random()
  y = random.random()
  if (x * x + y * y) < 1:
    hits = hits + 1
  i = i + 1

pi = 4.0 * float(hits) / float(throws)
piError = abs(pi - math.pi)/math.pi
print("Pi estimate: "+str(pi))
print("Pi error: "+str(piError))
print("Darts thrown: "+str(throws))
