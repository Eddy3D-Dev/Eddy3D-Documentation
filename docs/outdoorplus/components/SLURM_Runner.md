## ![](../images/icons/SLURM_Runner.png) SLURM Runner

![](../images/components/SLURM_Runner-crop.png)

Write SLURM batch (sbatch) files to run a wind study on an HPC cluster.

#### Input
* ##### Case 
The wind study to generate cluster job files for.
* ##### CA 
SLURM charge account.
* ##### NE 
SLURM notification email.
* ##### MCPU 
RAM per CPU in GB, e.g. 10 for 10G.
* ##### JD 
Duration of the SLURM job in hours.
* ##### OFLD 
Cluster module-load command for OpenFOAM.

#### Output