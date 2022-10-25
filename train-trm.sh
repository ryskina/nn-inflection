#!/bin/bash

#SBATCH -N 1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8g
#SBATCH --gres=gpu:1
#SBATCH -t 0
#SBATCH --array=2-2%1
#SBATCH --output=./logs/trm-elr_%A_%a.txt
#SBATCH --job-name=trm-elr_%A_%a

set -x  # echo commands to stdout
set -e  # exit on error

params=$(tail -n+${SLURM_ARRAY_TASK_ID} params-trm.txt | head -n1)

cd /projects/tir4/users/mryskina/morphological-inflection/neural-transducer
source ~/anaconda3/etc/profile.d/conda.sh

conda activate nt2
bash example/sigmorphon2020-shared-tasks/task0-trm.sh $params
conda deactivate
