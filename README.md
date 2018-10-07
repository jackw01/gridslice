# gridslice
Command line tool for slicing an image on a grid. Good for spritesheets and that kind of thing.

## Install
`pip install gridslice`

## Usage
```
usage: gridslice [-h]
                 input_image_path start_x start_y width height slices_x slices_y

Command line tool for slicing an image on a grid.

positional arguments:
  input_image_path  Path to the input image file
  start_x           Start x
  start_y           Start y
  width             Slice width
  height            Slice height
  slices_x          Number of x slices
  slices_y          Number of y slices

optional arguments:
  -h, --help        show this help message and exit
```

`start_x` and `start_y` represent the top corner of the area to take slices from. `width` and `height` are the size of each slice. `slices_x` and `slices_y` are the number of slices of the specified size to make in each direction.
