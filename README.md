# level3-capstone

Short description or introduction to your Django project.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Docker](#docker)

## Getting Started

Make sure Django is installed in the VE or installed on your device
Go to the root of the files in cmd or any ide you like and type
Django manage.py run server
and Django should run perfectly

### Prerequisites

List the prerequisites that the user needs to have installed before they can use your project. For example:

- Python 3.11.4
- Django
- (requiements.txt)

### Installation

1. Clone this repository (git clone https://github.com/Haydn-Cook/level3-capstone)
2. If not already install Python on your device
3. Install pip on your device if not already installed
4. Set up a venv (it is recommended to run in a venv so that only the requirements for the project are present)(to make a venv type  python -m venv venv_name)
5. Install the requirements for the program (requirements.txt)(pip install -r requirements.txt)
6. Once all the above is done navigate to the root of the program
7. In the console run the following command (python manage.py runsever)
8. In your browser navigate to https//:127.0.0.1:8000/
9. Everything should run smoothly

### Docker
1. Install docker or use docker playground
2. navigate to the root of the programe in docker
3. build the image (docker build -t [name of image] ./)
4. run image (docker run -p 8000:8000 [name of image])
