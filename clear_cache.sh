#!/bin/bash
# this removes all cached template files from the specified branch and server
#   thereby enabling server to recognize it needs to fetch new ones.

if [ $# -eq 0 ]; then
    echo $0: usage: clear_cahce branch_name [server=prod]
    exit 1
fi

dq_branch="$1"
trex2="54.174.189.191"
trex3="52.5.247.238"
trex4="52.7.222.113"
trex5="52.7.158.57"

echo $2
if [ "$2" == "server=prod" ]; then
    echo "Clearing cache from dq-prod"
    curl "$trex2/DQ/clearCache?branch=${dq_branch}&passphrase=test-Access*98765!"
    echo ""
    curl "$trex5/DQ/clearCache?branch=${dq_branch}&passphrase=test-Access*98765!"
    echo ""
else
    echo "Clearing cache from dq-test"
    curl "$trex3/DQ/clearCache?branch=${dq_branch}&passphrase=test-Access*98765!"
    echo ""
    curl "$trex4/DQ/clearCache?branch=${dq_branch}&passphrase=test-Access*98765!"
    echo ""
fi