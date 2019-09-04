# Nice tutorial: https://info.gwdg.de/~ceulig/docs-dev/doku.php?id=en:services:application_services:high_performance_computing:mpi4py

from mpi4py import MPI
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

host = os.uname()[1]

print("Hello from processor "+str(rank)+" out of "+str(size)+" on "+host)
