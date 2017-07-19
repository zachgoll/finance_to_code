#!/bin/sh
ifconfig -a | sort | awk '/^[[:space:]]*ether/ { print $2 }'

