#!/bin/bash

lang=$1

for split in "form" "lemma"
do
    for encoding in "grapheme" "phoneme"
    do
        echo $lang $split $encoding
        tail /projects/tir4/users/mryskina/morphological-inflection/neural-transducer/checkpoints/sigmorphon20-$split/$encoding/transformer/dropout0.3/$lang.log -n 1
    done
done