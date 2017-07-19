#!/bin/sh
ldapsearch -LLL "(uid=z*)" cn | sort -b -r | grep -e 'cn'
