#!/bin/bash

# This is where the software (scripts, tools) is:
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# This is where the reports show up. Default is the "report"
# subdirectory of the base directory, but you can customize this with
# the TESTREPORTS environment variable:
REPORTS=${TESTREPORTS:-${BASE}/reports}

if [ ! -d $REPORTS ]; then
    mkdir -p $REPORTS || exit 1
fi

source $BASE/VER

REPORTFILE="$REPORTS/$TEST-$VER-$(date +%Y-%m-%d-%H%M).txt"

apitest() {
    echo -n "$section "
    if "$@"; then
        echo "[OK]   $@" >> $REPORTFILE
    else
        echo "[FAIL] $@" >> $REPORTFILE
    fi
}

echo "[INFO] Test: $TEST"                     > $REPORTFILE
echo "[INFO] Version: $VER"                  >> $REPORTFILE 
echo "[INFO] Started $(date) on $(hostname)" >> $REPORTFILE
starttime=$(date +%s)

for i in $(ls -v $BASE/probes/[0-9]*.sh); do
    section=$(echo $i | sed 's/^.*\///;s/_.*$//')
    subject=$(echo $i | sed 's/^.*_test-//;s/\.sh$//;s/-/ /g')
    sectionfile="$REPORTS/protocol-$section.txt"
    startsection=$(date +%s)
    
    echo -n "Testing section $section: $subject ..."
    echo -e "\n[SECT] Testing section $section: $subject" >> $REPORTFILE
    
    echo "--- [$(date)] --- $i" >> $sectionfile 
    source $i >> $sectionfile 2>&1
    endsection=$(date +%s)
    dursection=$((endsection - startsection))
    echo " ($dursection seconds to complete)."
    echo "[SUMM] Section $section took $dursection seconds to complete." >> $REPORTFILE
done

endtime=$(date +%s)
runtime=$((endtime - starttime))

echo -e "\n[INFO] Finished $(date) ($runtime seconds)" >> $REPORTFILE

total=$(egrep -c 'FAIL|OK' $REPORTFILE)
failed=$(grep -c 'FAIL'    $REPORTFILE)
passed=$(grep -c 'OK'      $REPORTFILE)
quote=$((100 * passed / total))
echo "[INFO] $total tests total, $passed passed, $failed failed ($quote% coverage)" >> $REPORTFILE
