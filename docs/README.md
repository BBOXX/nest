# How to deploy new docs

Run `make_docs.sh` script.

It does the following:

1. Have two source folders; as follows:
```
    .
    ├── locust-nest (master)
    └── locust-nest-docs/html (gh-pages)
```
2. Runs `make docs` in the master branch.

3. Adds and commits the newly generated docs to gh-pages branch.
