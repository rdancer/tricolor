#!/bin/sh
# tricolor_test.sh -- run all test images and all colours through the program

# Get the directory of the current script
script_dir="$(dirname "$(realpath "$0")")"

cat "$script_dir/colors.txt" \
| tr ',' ' ' \
| while read color1 color2 color3; do
    # Need to use find(1) because not all the extensions always exist
    find "$script_dir" \
            -maxdepth 1 \
            \( \
            -iname \*.jpeg \
            -or -iname \*.jpg \
            -or -iname \*.png \
            \) \
            -exec \
    python3 "$script_dir/../tricolor.py" {} \
            --color "$color1" \
            --color "$color2" \
            --color "$color3" \
            --plot \;
done
