#!/bin/bash

# today
y=$(date '+%Y')
d=$(date '+%-d')
dd=$(date '+%d')
echo "today: $y, $d, $dd"

# flags
while getopts h?ny:dr opt; do
	case "$opt" in
		h|\?)
			#show_help
			exit 0
			;;
		n)
			next=True
			# find last day
			maxyear=$(ls|egrep "[0-9]"|tail -n 1)
			echo "maxyear: $maxyear"
			maxday=$(ls $maxyear|egrep "[0-9]"|tail -n 1)
			echo "maxday: $maxday"
			# 0<maxday<25: day=maxday+1
			# else: day=1, y++
			# DO NOT ALLOW OTHER OPTS
			;;
		y)
			y=$optarg
			# CHECK FORMAT (%d{4})
			echo "changed year to $y"
			;;
		d)
			day=$optarg
			# CHECK FORMAT ([1-9]{,2}), 0<day<=25
			echo "changed day to $day"
			# d= ..., dd=...
			;;
		r)
			# RANDOM NOT YET SOLVED DAY
			;;
	esac
done

# year dir
if ! [ -d "$y" ]; then
	mkdir "$y"
fi
echo "mkdir $y"

# day dir
if ! [ -d "$y/$dd" ]; then
	mkdir "$y/$dd"
fi
echo "mkdir $y/$dd"

path="$y/$dd/"
echo "path: $path"

# check files
for f in solution.py example input; do
	echo -n "file: $f "
	if ! [ -f "$path$f" ]; then
		echo "not existing"
		touch "$path$f"
		if [ "$f" = "input" ]; then
			echo "curl"
			#curl -b "session=53616c7465645f5ffa8137f2aa5ac770794b863a31ae75aea6733e8d7c49a1243091c45634a0b5781cc6017b651acff9" https://adventofcode.com/$y/day/$d/input>$path$f
		fi
	else
		echo "already exists"
	fi
done

