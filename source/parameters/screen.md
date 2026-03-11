(s:screen.params)=
## ScreenP: Screen Parameters

The `ScreenP` parameter group contains parameters for describing a 2-dimensional diagnostic screen used to measure the transverse distribution of a particle beam.
The components of this group and their defaults are:
```{code} yaml
ScreenP:
  resolution_x: 0  # [int] Number of screen pixels in the horizontal direction.
  resolution_y: 0  # [int] Number of screen pixels in the vertical direction.
  pixel_size: 0    # [m] Size of screen pixels.
  mirror_x: false  # [Boolean] If true, mirror the horizontal image.
  mirror_y: false  # [Boolean] If turn, mirror the vertical image.
```