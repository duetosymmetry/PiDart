# Nice tutorial: https://info.gwdg.de/~ceulig/docs-dev/doku.php?id=en:services:application_services:high_performance_computing:mpi4py

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print("Hello from processor "+str(rank)+" out of "+str(size))

# Compute a number that depends on the processor you're on
# In real life, you would divide up a big calculation into parts,
# so each part had a different result for x
x = 2**rank

# Add up the values of x on each processor
rootProc = 0
sum = comm.reduce(x, op=MPI.SUM, root=rootProc)

if rank == rootProc:
  print(sum)

