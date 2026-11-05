# ![](/images/icons/SLURM_Runner.png) SLURM Runner - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22SLURM%20Runner%22)

![](/images/components/SLURM_Runner-crop.png)

Write SLURM batch (sbatch) files to run a wind study on an HPC cluster.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | The wind study to generate cluster job files for. | `Generic Data` |
| Charge Account | CA | SLURM charge account. | `Text` |
| Notification Email | NE | SLURM notification email. | `Text` |
| Memory per CPU | MCPU | RAM per CPU in GB, e.g. 10 for 10G. | `Integer` |
| Job duration | JD | Duration of the SLURM job in hours. | `Integer` |
| OpenFOAM load command | OFLD | Cluster module-load command for OpenFOAM. | `Text` |

#### Output

*None*