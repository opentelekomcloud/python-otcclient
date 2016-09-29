source ./otcclient/tests/VER

echo "$TEST $VER TEST $VER" >"$TEST-$VER.txt"

for i in `ls -v otcclient/tests/[0-9]*.sh`; do sh ./$i; done

echo "$TEST $VER TEST $VER" >"$TEST-$VER.txt"