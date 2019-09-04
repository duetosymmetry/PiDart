import math
import random
from mpi4py import MPI

import time # optional, for timing only
startTime = time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

throws = 1e7 // size

i = 0
hits = 0
while i < throws:
  x = random.random()
  y = random.random()
  if (x * x + y * y) < 1:
    hits = hits + 1
  i = i + 1

rootProc = 0

throwsAllProcs = throws * size
hitsAllProcs = comm.reduce(hits, op=MPI.SUM, root=rootProc)

if rank == rootProc:
  pi = 4.0 * float(hitsAllProcs) / float(throwsAllProcs)

  piError = abs(pi - math.pi)/math.pi
  print("Pi estimate: "+str(pi))
  print("Pi error: "+str(piError))
  print("Darts thrown: "+str(throwsAllProcs))
  print("Runtime (s): "+str(time.time()-startTime))
