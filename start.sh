#!/bin/bash

# today
y=$(date '+%Y')
d=$(date '+%-d')
echo "today: $y, $d"

# flags
while getopts h?ny:dr opt; do
	case "$opt" in
		h|\?)
			#show_help
			echo "the h flag has no function yet"
			exit 0
			;;
		n)
			next=True
			# find last day
			maxyear=$(ls|egrep "[0-9]"|tail -n 1)
			echo "maxyear: $maxyear"
			maxday=$(ls $maxyear -v|egrep "[0-9]"|tail -n 1)
			echo "maxday: $maxday"
			if (( 0<$maxday && $maxday<25 )); then # next day of latest year
				echo "0<maxday<25"
				y=$maxyear
				d=$((${maxday//0}+1))
				echo $y $d
			else # MISSING: WHEN RUN ON 1st DEC
				echo "there is no newer puzzle than the latest one, you have to wait until december : )"
				exit 0
			fi
			# DO NOT ALLOW OTHER OPTS
			# for testing only:
			exit 0
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
			# d= ...
			;;
		r)
			# RANDOM NOT YET SOLVED DAY
			echo "the r flag has no function yet"
			exit 0
			;;
	esac
done

# year dir
if ! [ -d "$y" ]; then
	mkdir "$y"
fi
echo "mkdir $y"

# day dir
if ! [ -d "$y/$d" ]; then
	mkdir "$y/$d"
fi
echo "mkdir $y/$d"

path="$y/$d/"
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

