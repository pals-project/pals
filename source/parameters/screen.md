(s:screen.params)=
## ScreenP: Screen Parameters

The `ScreenP` parameter group describes a two-dimensional diagnostic screen, together with the
camera that images it, used to measure the transverse distribution of a particle beam.
The components of this group and their defaults are:
```{code} yaml
ScreenP:
  resolution_x: 0     # [integer] Number of image pixels in the horizontal direction.
  resolution_y: 0     # [integer] Number of image pixels in the vertical direction.
  pixel_size: 0       # [m] Size of a pixel, as projected onto the screen.
  mirror_x: false     # [logical] Is the image mirrored horizontally?
  mirror_y: false     # [logical] Is the image mirrored vertically?
```
The horizontal and vertical directions of the image are aligned with the {math}`x` and {math}`y`
axes of the element's [body coordinates](#s:coords). Pixels are square, and `pixel_size` is the
length of a pixel side, as projected onto the screen.

A camera often views a screen by way of a mirror or from the back side of the screen, so the
image it records can be reversed relative to the body coordinates. If `mirror_x` is `false`, the
horizontal pixel index increases in the {math}`+x` direction. If `mirror_x` is `true`, the
horizontal pixel index increases in the {math}`-x` direction. `mirror_y` does the same for the
vertical pixel index and the {math}`y` axis. These parameters let a simulated image be compared
pixel by pixel with a measured one.
