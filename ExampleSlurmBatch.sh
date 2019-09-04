#!/bin/bash -
#SBATCH -J PiDartMpi       
#SBATCH -o PiDartMpi.stdout
#SBATCH -e PiDartMpi.stderr
#SBATCH -n 64                  
#SBATCH --ntasks-per-node 32
#SBATCH -p compute
#SBATCH -t 2:00:00
#SBATCH -A sxs
#SBATCH --no-requeue
#SBATCH -D .

# Distributed under the MIT License.
# See LICENSE.txt for details.


umask 0022

module load openmpi/1.10.7
source /home/geoffrey/apps/anaconda3/bin/activate root

date
mpirun -np 64 python PiDartMpi.py &> PiDartMpi.out
date
