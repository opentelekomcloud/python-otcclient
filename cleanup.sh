#!/bin/sh

for i in $(find -name '*.py'); do
    cat $i |\
    # exactly one space before and after an assignment, treat '==', '!=', and '"="':
    sed -r 's/(\S)=/\1 =/g;s/=(\S)/= \1/g;s/= =/==/g;s/! =/!=/g;s/" = "/"="/g' |\
    # no spaces after opening and no spaces before closing brackets: 
    sed -r 's/\(\s*/(/g;s/\s\)/)/g' |\
    # no spaces before and exactly one space after a comma:	
    sed -r 's/\s*,/,/g;s/,\s*/, /g' |\
    # remove trailing spaces:
    sed -r 's/\s*$//' |\
    # remove trailing CRs:
    sed -r 's/$//' \
    > $i.new
    echo -n "."
done
echo
