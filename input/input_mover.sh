#! /usr/bin/env bash

for y in */
do
	if [ -d "$y" ] && [ ${#y} -eq 5 ]
	then
		if ! [ -d "aoc_input/$y" ]
		then
			mkdir "aoc_input/$y"
		fi
		for d in $y*/
		do
			for f in $(find $d -name "*input*") $(find $d -name "*example*")
			do
				if [ -f "$f" ]
				then
					if ! [ -d "aoc_input/$d" ]
					then
						mkdir "aoc_input/$d"
					fi
					mv "$f" "aoc_input/$f"
				fi
			done
		done
	fi
done

