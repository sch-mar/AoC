#!/bin/bash

y=$(date '+%Y')
d=$(date '+%-d')
dd=$(date '+%d')

if ! [ -d "$y" ]; then
	mkdir "$y"
fi

if ! [ -d "$y/$dd" ]; then
	mkdir "$y/$dd"
fi

path="$y/$dd/"

#check files
for f in part1.py example input; do
	if ! [ -f "$path$f" ]; then
		touch "$path$f"
		if [ "$f" = "input" ]; then
			curl -b "session=53616c7465645f5ffa8137f2aa5ac770794b863a31ae75aea6733e8d7c49a1243091c45634a0b5781cc6017b651acff9" https://adventofcode.com/$y/day/$d/input>$path$f
		fi
	fi
done

