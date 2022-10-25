#!/bin/bash

lang=$1
echo $lang

for split in "form" "lemma"
do
    chars_graph=$(cut -f1 /projects/tir4/users/mryskina/morphological-inflection/task0-data/split-by-$split/grapheme/$lang.trn | tr -d '\n' | wc -m)
    chars_phon=$(cut -f1 /projects/tir4/users/mryskina/morphological-inflection/task0-data/split-by-$split/phoneme/$lang.trn | tr -d '\n' | wc -m)
    lines=$(cut -f1 /projects/tir4/users/mryskina/morphological-inflection/task0-data/split-by-$split/grapheme/$lang.trn | wc -l)
    echo -e "$((${chars_graph} / ${lines}))\t$((${chars_phon} / ${lines}))\t$lines"
done