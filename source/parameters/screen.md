(s:screen.params)=
## ScreenP: Screen Parameters

The `ScreenP` parameter group describes a two-dimensional diagnostic screen, together with the
camera that images it, used to measure the transverse distribution of a particle beam.
The components of this group and their defaults are:
```{code} yaml
ScreenP:
  n_pixels_x: 0       # [integer] Number of image pixels in the horizontal direction.
  n_pixels_y: 0       # [integer] Number of image pixels in the vertical direction.
  pixel_size_x: 0     # [m] Horizontal size of a pixel, as projected onto the screen.
  pixel_size_y: 0     # [m] Vertical size of a pixel, as projected onto the screen.
  mirror_x: false     # [logical] Is the image mirrored horizontally?
  mirror_y: false     # [logical] Is the image mirrored vertically?
```
The horizontal and vertical directions of the image are aligned with the {math}`x` and {math}`y`
axes of the element's [body coordinates](#s:coords). `pixel_size_x` and `pixel_size_y` are the
width and height of a pixel, as projected onto the screen.

A camera often views a screen by way of a mirror or from the back side of the screen, so the
image it records can be reversed relative to the body coordinates. If `mirror_x` is `false`, the
horizontal pixel index increases in the {math}`+x` direction. If `mirror_x` is `true`, the
horizontal pixel index increases in the {math}`-x` direction. `mirror_y` does the same for the
vertical pixel index and the {math}`y` axis. These parameters let a simulated image be compared
pixel by pixel with a measured one.
