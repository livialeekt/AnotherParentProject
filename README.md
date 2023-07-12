# AnotherParentProject
AnotherParent Project for submodule lunch and learn

Initialize the repo for submodules
    `git submodule init`
   
To add a submodule to the repo
    `git submodule add {git repo} {directory}`
    `git submodule add git@github.com:livialeekt/ChildProject.git`

The entire repo will get dropped into the directory and you'll be able to use the files from the Child repo

To pull the new code into the repo
    `git submodule update --recursive --remote --merge`