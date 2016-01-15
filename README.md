# Multicast Demo

Python Twisted UDP multicast client/server

## Installation

    $ mkvirutalenv --python=$(which python3) multicast-demo
    $ pip install -r requirements.txt

## Quick start

    # Activate virtualenv
    $ workon multicast-demo

    # Start the server
    $ python multicast_demo.py

    # Start one or many clients
    $ python multicast_demo.py --client
