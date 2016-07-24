Stelligent Role
=========

[![CircleCI](https://circleci.com/gh/dbryant4/stelligent.svg?style=svg)](https://circleci.com/gh/dbryant4/stelligent)

This Ansible role installs Nginx and copies the `index.html` file found in the `files/` directory of this repo.

Requirements
------------

- CentOS 6
- [Docker](https://www.docker.com/) ([Docker for mac](https://docs.docker.com/engine/installation/mac/#/docker-for-mac) if using on OSX)
- Molecule from my development branch due to new features waiting to be merged: 
   `pip install git+git://github.com/dbryant4/molecule.git@docker-ports`
- Ansible which should have been installed by Molecule

Getting Started
---------------

1. To get started, run `molecule converge`. This will create a docker container and will run the Ansible provisioner. This step might take a few minutes for the first time.

2. Once complete, point your browser to [http://127.0.0.1](http://127.0.0.1) to view the index page. If using Docker Machine, point your browser to that IP.

3. For automated tests, run `molecule verify` which will run all of the automated [Testinfra](https://github.com/philpep/testinfra) tests in the `tests/` directory.

4. To stop the Docker container, run `molecule destroy`.

License
-------

MIT

Author Information
------------------

Derrick Bryant 

dbryant4@gmail.com

[http://dbryant.xyz](http://dbryant.xyz)

