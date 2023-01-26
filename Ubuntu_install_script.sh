#!/bin/sh

## this script is meant to be run on ubutu for setting up the compile env

sudo apt install python3-pip
sudo apt install verilator
sudo apt-get install git perl python3 make autoconf g++ flex bison ccache
sudo apt-get install libgoogle-perftools-dev numactl perl-doc
sudo apt-get install libfl2  # Ubuntu only (ignore if gives error)
sudo apt-get install libfl-dev  # Ubuntu only (ignore if gives error)
sudo apt-get install zlibc zlib1g zlib1g-dev  # Ubuntu only (ignore if gives error)
pip install pyinstaller
pip install PyQt5
