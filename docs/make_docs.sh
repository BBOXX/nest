# !/bin/bash

# Ensure the script always runs from the same location
script_path=$(dirname "$0")
cd "$script_path"

# `make html` into locust-nest-docs/html
mkdir ../../locust-nest-docs
git clone git@github.com:ps-george/locust-nest -b gh-pages ../../locust-nest-docs/html
make html

# Commit/push changes
echo -e "\nCommit to gh-pages branch? [y/n]"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
    cd ../../locust-nest-docs/html
    if [ $# -ne 1 ]; then
        echo -e "Enter commit message:"
        read commit_msg
    else
        commit_msg=$1
    fi

    git add -A; git commit -m "$commit_msg"
    echo -e "\nPush to origin? [y/n]"
    read answer2
    if [ "$answer2" != "${answer2#[Yy]}" ] ;then
        git push;
    fi
    cd ../../locust-nest/docs
fi

# Remove build dir
echo -e "\nRemove build dir (locust-nest-docs)? [y/n]"
read answer3
if [ "$answer3" != "${answer3#[Yy]}" ] ;then
    rm -rf ../../locust-nest-docs
fi