#!/bin/bash

#SBATCH -N 1
#SBATCH --cpus-per-task=1
#SBATCH --mem=3g
#SBATCH --gres=gpu:1
#SBATCH -t 0
#SBATCH --array=1-12%6
#SBATCH --output=./logs/lstm_baseline5_%A_%a.txt
#SBATCH --job-name=lstm_baseline5_%A_%a

set -x  # echo commands to stdout
set -e  # exit on error

params=$(tail -n+${SLURM_ARRAY_TASK_ID} params-lstm.txt | head -n1)

cd /projects/tir4/users/mryskina/morphological-inflection/LemmaSplitting
source ~/anaconda3/etc/profile.d/conda.sh

conda activate goldman-etal
python -u lstm/Inflection.py $params
conda deactivate
