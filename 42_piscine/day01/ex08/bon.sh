#!/bin/sh
ldapsearch | grep "don" | grep -c "cn:"
