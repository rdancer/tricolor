#!/bin/sh
# tricolor_test.sh -- run all test images and all colours through the program

cat colors.txt \
| tr ',' ' ' \
| while read color1 color2 color3; do
    python3 tricolor.py test/* \
            --color "$color1" \
            --color "$color2" \
            --color "$color3" \
            --plot
done
