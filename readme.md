# Repository Description

This repository contains examples and subsystems illustrating how we can use python programing in a variety of different contexts. The layout of this repo is currently composed of three main directories to shed lights on the core aspect of this beautiful computing tool:

1. Basic examples: this repository contains basic and 'must know' topics such as core data types, classes and object oriented programing, slicing, etc.

2. common applications: the goal behind this directory is illustrate some of the most common applications in which Python rules! For instance, test automation, web-sockets, repository management, etc.

3. handy_packages: this directory provides a glance into packages that can be imported in variety of different project to facilitate the deveopment and representation like Pandas, Numpy, and matplotlib.

It is worth mentioning that, this repository is currently a work under construction which gets updated with new contents regualrly and it would stay in this status until a tag to the branch would be issued.


# Usage Notes

To use this repository, there are two ways. First just cloning the repository and then run the examples directly on the host machine. The second way, which is the recommended way, is to build and run the docker container on the host machine for guaranteed reproducable results. To do so, you only need to do the following

First: building the container image:
`docker build -t python-examples .`

Next, running the container:
`docker run --rm python-examples python $PATH_TO_FILE`

where `path` variable to the file is something like `./basic_examples/string_manipulation/source.py`

To abort, use `exit` to abort the container.