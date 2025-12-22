(s:fork.params)=
## ForkP: Fork Parameters

The `ForkP` parameter group holds parameters for a `Fork` element.
The components of this group and their defaults are:
```{code} yaml
ForkP:
  to_line: ""               # [string] Beam line to fork to
  to_ele: ""                # [string] Element forked to.
  direction: FORWARDS       # [string] Switch: Longitudinal Direction of travel of injected beam.
  propagate_reference: ...  # [Boolean] Propagate reference species and energy?  ... TODO: description, default ...
```
The possible values of the optional `direction` switch are:
```{code} yaml
  direction: FORWARDS   # Injected particle propagates in forward direction. Default.
  direction: BACKWARDS  # Injected particle propagates in reverse direction.
```

See the [](#s:forking) chapter for more details.

