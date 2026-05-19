(s:wire.params)=
## WireP: Wire Parameters

The `WireP` parameter group contains parameters for describing a 1-dimensional diagnostic wire used to measure the transverse distribution of a particle beam.
The components of this group and their defaults are:
```{code} yaml
WireP:
  angle: 0        # [radian] Angle of the wire with respect to the horizontal axis.
  n_steps: 1      # [int] Number of steps used during a wire scan.
  start_offset: 0 # [m] Wire scan start offset from beam axis.
  end_offset: 0   # [m] Wire scan end offset from beam axis.
  width: 0        # [m] Wire width.
```

```{figure} figures/wire.svg
:width: 90%
:name: f.angle

In detail:
See diagram for parameter descriptions.