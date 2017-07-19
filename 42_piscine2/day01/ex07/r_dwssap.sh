#!/bin/sh
FT_LINE1=8
FT_LINE2=16
cat /etc/passwd | egrep -E -v '^#' | sed '1!n;d' | cut -d : -f 1 | rev | sort -r | sed -n "$FT_LINE1,$FT_LINE2 p" | tr '\n' ',' | sed 's/,/, /g' | rev | sed '$ s/,/./'	| rev
