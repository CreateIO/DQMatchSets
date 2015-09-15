#!/bin/bash

# this script creates a new branch from the specifiec param then outputs
#   that to the create repo for use in deploying the code to our servers

# syntax: deploy_branch.sh <branchname>

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$DIR/../create"

echo $DIR
echo $BASEDIR

branch=${1:-}

git co -b $branch
git commit -a -m "New deploy branch"
git push origin $branch
echo "$branch" > "$BASEDIR/DQTemplateBranch.txt"
