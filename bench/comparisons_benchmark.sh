#!/bin/sh

./generate_makefiles.py
g++ measure.cpp -o measure

printf "|        N      |ReMake Time (s)| Make Time (s) |ReMake Mem (MB)| Make Mem (MB) |\n"
printf "|---------------|---------------|---------------|---------------|---------------|\n"
for i in 1 10 100 1000 10000; do
    m_o=`./measure /usr/bin/make -f makefile-$i a1` 
    rm_o=`./measure ../remake.py -f makefile-$i a1`
    m_o=`echo "$m_o" | grep seconds`
    rm_o=`echo "$rm_o" | grep seconds`
    m_t=`echo "$m_o" | cut -d ' ' -f 1`
    rm_t=`echo "$rm_o" | cut -d ' ' -f 1`
    m_m=`echo "$m_o" | cut -f 2 | cut -d ' ' -f 1`
    rm_m=`echo "$rm_o" | cut -f 2 | cut -d ' ' -f 1`
    printf "|%15s|%15s|%15s|%15s|%15s|\n" "$i" "$rm_t" "$m_t" "$rm_m" "$m_m"
done
