(s:wire.params)=
## WireP: Wire Parameters

The `WireP` parameter group describes a wire scanner, a thin wire that is stepped across a particle
beam to measure a one-dimensional projection of the beam's transverse distribution.
The components of this group and their defaults are:
```{code} yaml
WireP:
  angle: 0          # [rad] Angle of the wire with respect to the x-axis.
  n_steps: 1        # [integer] Number of wire positions used during a scan.
  start_offset: 0   # [m] Wire offset at the start of the scan.
  end_offset: 0     # [m] Wire offset at the end of the scan.
  width: 0          # [m] Wire width (diameter).
```

```{figure} figures/wire.svg
:width: 50%
:name: f:wire

Wire scanner geometry in the transverse plane of the element's body coordinates.
The "beam axis" is the {math}`x = y = 0` axis. The scan moves the wire, at constant `angle`,
from `start_offset` to `end_offset`.
```

All parameters are in the transverse plane of the element's [body coordinates](#s:coords).
The `angle` is the angle of the wire with respect to the {math}`x`-axis, measured towards
the {math}`+y`-axis, as shown in {numref}`f:wire`.
The scan direction is perpendicular to the wire, along the unit vector
{math}`(-\sin(\text{angle}), \cos(\text{angle}))`.
The offsets `start_offset` and `end_offset` are signed distances from the {math}`x = y = 0` axis to
the wire, measured along the scan direction. In {numref}`f:wire`, `start_offset` is negative
and `end_offset` is positive. A scan places the wire at `n_steps` positions, evenly spaced
from `start_offset` to `end_offset`.
