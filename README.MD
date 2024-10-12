# Tricolor

Apply tricolor posterization to images with specified colours.

Colours in `colors.txt` shamelessly stolen from (accessed 2024-10-22)
https://webflow.com/blog/best-color-combinations

## Examples

More examples in [`examples/`](./examples)

<div align=center>
<img width="100%" alt="Lena" src="https://raw.githubusercontent.com/rdancer/tricolor/refs/heads/master/test/output/plots/lena_masked/Lena_masked_plot_0x1E2761_0x7A2048_0x408EC6.jpeg">
<img width="100%" alt="Lego" src="https://raw.githubusercontent.com/rdancer/tricolor/refs/heads/master/test/output/plots/lego/Lego_plot_0x375E97_0xFB6542_0xFFBB00.jpeg">
<img width="100%" alt="Starry Night" src="https://raw.githubusercontent.com/rdancer/tricolor/refs/heads/master/test/output/plots/starry_night/Starry_Night_plot_0x330000_0x73605B_0xD09683.jpeg ">
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

### Normal usage

```
$ python3 tricolor.py test/Lena.jpeg --color 0xFF0000 --color 0xFFFFFF --color 0x0000FF
Saved: Lena_0xFF0000_0xFFFFFF_0x0000FF.png
```

### Produce test images in all the colour combinations from `test/colors.txt`

```
$ ./test/tricolor_test.sh
Saved: Lego_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Lego_plot_0x1E2761_0x408EC6_0x7A2048.png
Saved: Lena_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Lena_plot_0x1E2761_0x408EC6_0x7A2048.png
Saved: Starry_Night_0x1E2761_0x408EC6_0x7A2048.png
Saved plot: Starry_Night_plot_0x1E2761_0x408EC6_0x7A2048.png
...
```

## Note on spelling

We use American English (in particular, *"color"*) in code. In comments and documentation, it
matters not (I prefer to use British English --rdancer).

