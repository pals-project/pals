%---------------------------------------------------------------------------------------------------
(s:tracking.params)=
## TrackingP: Parameters Pertaining to Tracking.

Tracking parameters are highly program specific but it is useful to have a dedicated group
so that such program specific parameters can be clearly identified.

Example:
```{code} yaml
TrackingP:
  SciBmad:
    ds_step: 0.3
    tracking_method: scibmad_standard
    ...
```
The above set parameters specific to the SciBmad simulation ecosystem.
