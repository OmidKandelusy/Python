This repository contains examples and subsystems illustrating how we can use python programing in a variety of different contexts. To use this repository, there are two ways. First just cloning the repository and then run the examples directly on the host machine. The second way, which is the recommended way, is to build and run the docker container on the host machine for guaranteed reproducable results. To do so, you only need to do the following

First building the container:
`docker build -t python-examples .`

Next, running the container:
`docker run --rm python-examples python $PATH_TO_FILE`

In case, there is a infinite loop running the program, use `exit` to abort the container.