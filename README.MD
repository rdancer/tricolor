# Tricolor

Apply tricolor posterization to images with specified colors.

Colours in `colors.txt` shamelessly stolen from (accessed 2024-10-22)
https://webflow.com/blog/best-color-combinations

## Examples

More examples in [`examples/`](./examples)

<div align=center>
<img width="100%" alt="Lena" src="https://raw.githubusercontent.com/rdancer/tricolor/refs/heads/master/test/output/plots/lena_plot/Lena_plot_0x1E2761_0x408EC6_0x7A2048.jpeg">
<img width="100%" alt="Lego" src="https://raw.githubusercontent.com/rdancer/tricolor/refs/heads/master/test/output/plots/lego_plot/Lego_plot_0x375E97_0xFB6542_0xFFBB00.jpeg">
<img width="100%" alt="Starry Night" src="https://raw.githubusercontent.com/rdancer/tricolor/refs/heads/master/test/output/plots/starry_night_plot/Starry_Night_plot_0x330000_0x73605B_0xD09683.jpeg">
</div>

## Installation

```
$ pip install -r requirements.txt
```

## Usage

```
$ python3 tricolor.py --help
positional arguments:
  images         Paths to input image files.

options:
  -h, --help     show this help message and exit
  --color COLOR  Hex color code (e.g., 0x1E2761). Specify exactly three times.
  --plot         If set, generates a plot with the original, tricolor image, and color swatches.
```

```
$ python3 tricolor.py test/*.jpeg --color 0xFF0000 --color 0xFFFFFF --color 0x0000FF
```

```
$ ./tricolor_test.sh
Saved: Lego_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Lego_plot_0x1E2761_0x408EC6_0x7A2048.png
Saved: Lena_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Lena_plot_0x1E2761_0x408EC6_0x7A2048.png
Saved: Starry_Night_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Starry_Night_plot_0x1E2761_0x408EC6_0x7A2048.png
...
```
