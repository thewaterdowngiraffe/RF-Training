# Git
## Goals
understand git
enforce standards.
## what is Git
read [here](https://github.com/git/git/blob/e83c5163316f89bfbde7d9ab23ca2e25604af290/README)

Git is used to track changes made to a repository.
it allows for historical changes

## WARNINGS
once it is posted to git its perminent so be careful
NEVER ADD THE FOLLOWING
- passwords
- API keys
- private info

## how to use it

### standard commits
commit your changes
add a summary of what you did

### branches
use branches to create parralel isolated workstreams that can be merged back together.

have a main (prod) branch and at least a dev branch.
when adding in a feature it is recommended to create a branch for that feature and merge it back when you are done.

when you merge a branch you must do the following:
- summarize all changes made
- review every single line change (more commits and frequnt merges make this easier)
    - fix all issues before merging the code
    - treat all code the same (even if you created it).

### merge conflicts
merge conflicts occur when changes are made to the same section of code between the merging branches.
when fixing a merge conflict all changes are made on the destination branch. to reduce the risk of this happening make frequent commits (system can track changes better) and organize the code better.
## [`.gitignore`](../.gitignore)
this is where you tell git what it can and can not track.
its recomended to use this to hide config files and cache dirs.

# Tasks
1. Connect to this repo.
2. Create a branch.
3. Add Lesson 5 to the code.
4. Create a pull request into the `testing` branch.
5. The code will be auto reviewed, fix all issues.
    1. unit tests must pass
    2. unit test coverage must be 100%
    3. robocop must have no issues.
6. Delete the pull request.
7. Pull new changes from the main branch to your working branch
8. review any changes
9. merge changes into your branch.
10. make all things pass


