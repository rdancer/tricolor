# Tricolor

Apply tricolor posterization to images with specified colors.

Colours in `colors.txt` shamelessly stolen from (accessed 2024-10-22)
https://webflow.com/blog/best-color-combinations

<div align=center>
![Lena](./test/output/hi_res/lena_hi_res/Lena_plot_0x1E2761_0x408EC6_0x7A2048.jpeg)
![Lego](./test/output/hi_res/lego_hi_res/Lego_plot_0x375E97_0xFB6542_0xFFBB00.jpeg)
![Starry Night](./test/output/hi_res/starry_night_hi_res/Starry_Night_plot_0x330000_0x73605B_0xD09683.jpeg)
</div>

```
$ pip install -r requirements.txt
$ python3 tricolor.py --help
positional arguments:
  images         Paths to input image files.

options:
  -h, --help     show this help message and exit
  --color COLOR  Hex color code (e.g., 0x1E2761). Specify exactly three times.
  --plot         If set, generates a plot with the original, tricolor image, and color swatches.

$ ./tricolour_test.sh
Saved: Lego_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Lego_plot_0x1E2761_0x408EC6_0x7A2048.png
Saved: Lena_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Lena_plot_0x1E2761_0x408EC6_0x7A2048.png
Saved: Starry_Night_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Starry_Night_plot_0x1E2761_0x408EC6_0x7A2048.png
...
```
