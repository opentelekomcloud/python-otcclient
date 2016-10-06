#!/bin/bash
source VER

echo "$TEST $VER TEST $VER" >"$TEST-$VER.txt"

for i in `ls -v [0-9]*.sh`; do sh ./$i; done

echo "$TEST $VER TEST $VER" >>"$TEST-$VER.txt"
