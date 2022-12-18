#!/usr/bin/env sh
x=$(uname -r)
make -C /usr/src/linux-headers-"$x" M=$PWD modules