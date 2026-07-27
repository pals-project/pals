%---------------------------------------------------------------------------------------------------
(s:twiss.params)=
## TwissP: Initial Twiss, coupling, and dispersion Parameters.

Typically this parameter group is used to specify the initial Twiss, coupling and dispersion
parameters at the beginning of a lattice branch.
For a [BeginningEle](#s:beginningele) element, `TwissP` is an input parameter group that sets these
initial values.
For all other element kinds that have a [ReferenceP](#s:ref.params) group, `TwissP` is an
[output parameter](#s:io.params) group.

Note that PALS itself does not define how any `TwissP` component is calculated: that is outside the
scope of PALS.
A program is free to compute the Twiss parameters and write them out for each element of an
expanded lattice so that other programs may read them back in.

The components if `TwissP` are:
```{code} yaml
alpha_a       # [-] "a" mode alpha
alpha_b       # [-] "b" mode alpha
beta_a        # [m] "a" mode beta
beta_b        # [m] "b" mode beta
cmat11        # [-] c[1,1] coupling matrix component.
cmat12        # [m] c[1,2] coupling matrix component.
cmat21        # [1/m] c[2,1] coupling matrix component.
cmat22        # [-] c[2,2] coupling matrix component.
eta_x         # [m] x-axis dispersion
eta_y         # [m] y-axis dispersion
etap_x        # [-] x-axis momentum dispersion.
etap_y        # [-] y-axis momentum dispersion.
deta_x_ds     # [-] x-axis dispersion derivative.
deta_y_ds     # [-] y-axis dispersion derivative.
phi_a         # [rad] "a" mode phase.
phi_b         # [rad] "b" mode phase.
```
Discussion of the normal mode decomposition is found in Sagan and Rubin {footcite:p}`Sagan:Coupling`.
Dispersion parameters are documented in the [Dispersion](#s:dispersion) section.

