#!/bin/bash
module load anaconda/2021.05
module load cuda/11.6
module load gcc/9.3

source activate openmmlab
export PYTHONUNBUFFERED=1

python tools/train.py \
       configs/resnet18/resnet18_b32_flower.py \
       --work-dir work/resnet18_b32_flower
