#!/bin/sh

./generate_makefiles.py
g++ measure.cpp -o measure

printf "|        N      |ReMake Time (s)|ReMake Mem (MB)|\n"
printf "|---------------|---------------|---------------|\n"
for i in 10 100 1000 10000 100000 1000000; do
    rm_o=`./measure ../remake.py -n -f makefile-$i a1`
    rm_o=`echo "$rm_o" | grep seconds`
    rm_t=`echo "$rm_o" | cut -d ' ' -f 1`
    rm_m=`echo "$rm_o" | cut -f 2 | cut -d ' ' -f 1`
    printf "|%15s|%15s|%15s|\n" "$i" "$rm_t" "$rm_m"
done
