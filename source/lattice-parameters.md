## Lattice parameters

Lattice parameters are parameters that are not associated with any lattice element but with the
lattice as a whole. This section standardizes the names and meanings of such.

The suffixes `_a`, `_b`, and `_c` refer to the three normal modes of oscillation. 
Without coupling, the `a`-mode represents horizontal motion and the `b`-mode
represents vertical motion. 
The `c`-mode is identified as the longitudinal (synchrotron) mode. 
See [TwissP](#s:twiss.params) for more on the normal mode decomposition.

Except for the emittances, these parameters are properties of a [periodic](#s:beamline.components)
branch such as a storage ring.

Derivatives with respect to momentum are taken with respect to
{math}`\delta = \Delta P/P_0`, the momentum deviation relative to the reference momentum {math}`P_0`,
whatever the setting of [`phase_space_coordinates`](#s:phase.space).

- `chromaticity_a`, `chromaticity_b` [rad]

  The linear chromaticities of the `a` and `b` modes. The chromaticity is the derivative of the tune
  with respect to {math}`\delta`, evaluated at {math}`\delta = 0`:
  ```{math}
    \text{chromaticity\_a} = \frac{d \, (\text{tune\_a})}{d\delta}, \qquad
    \text{chromaticity\_b} = \frac{d \, (\text{tune\_b})}{d\delta}
  ```
  Here the tune at a given {math}`\delta` is the tune about the periodic orbit of a particle with
  that constant momentum deviation (that is, with RF cavities off). Since tunes are in radians,
  these chromaticities are {math}`2\pi` times the chromaticity {math}`dQ/d\delta`, where {math}`Q`
  is the tune in units of {math}`2\pi`.

- `emittance_a`, `emittance_b`, `emittance_c` [m]

  The normal mode emittances (also called eigen emittances) of the beam. If {math}`\Sigma` is the
  {math}`6 \times 6` matrix of second moments of the phase space coordinates
  `(x, px, y, py, z, pz)` about the beam centroid, then the eigenvalues of {math}`\Sigma \, S` are
  {math}`\pm i \epsilon_a`, {math}`\pm i \epsilon_b`, and {math}`\pm i \epsilon_c`, where
  {math}`S` is the block diagonal matrix
  ```{math}
    S = \begin{pmatrix}
      0 & 1 & 0 & 0 & 0 & 0 \\
     -1 & 0 & 0 & 0 & 0 & 0 \\
      0 & 0 & 0 & 1 & 0 & 0 \\
      0 & 0 &-1 & 0 & 0 & 0 \\
      0 & 0 & 0 & 0 & 0 & 1 \\
      0 & 0 & 0 & 0 &-1 & 0
    \end{pmatrix}
  ```
  Each eigenvalue pair is assigned to a mode using its eigenvectors.

  Unlike the other lattice parameters, the emittance is a property of the beam and not of the
  lattice alone. It may be set as an input, for example the design emittance of a proton ring, or
  written as an output by a program that computes it, for example the equilibrium emittance of an
  electron ring set by the balance between radiation damping and quantum excitation.
  Emittances do not change under linear symplectic transport. Where they do vary along a branch,
  for example with acceleration in a linac, the values refer to the start of the branch.

- `fractional_tune_a`, `fractional_tune_b`, `fractional_tune_c` [rad]

  The fractional part of the tune, in the range {math}`[0, 2\pi)`:
  ```{math}
    \text{fractional\_tune} = \text{tune} - 2\pi \left\lfloor \frac{\text{tune}}{2\pi} \right\rfloor
  ```
  Unlike the tune, the fractional tune can be found from the one-pass transfer matrix alone. The
  eigenvalues of this matrix come in pairs {math}`e^{\pm i \theta}`, and {math}`\theta`, with its
  sign fixed by the clockwise convention described under `tune_a`, is the fractional tune.
  Since `tune_c` is negative above transition, `fractional_tune_c` is then just below
  {math}`2\pi`.

- `momentum_compaction` [-]

  The momentum compaction factor {math}`\alpha_p`. This is the fractional change, per unit
  {math}`\delta`, in the length {math}`L` of the periodic orbit for one pass, evaluated at
  {math}`\delta = 0` with RF cavities off:
  ```{math}
    \alpha_p = \frac{1}{L} \frac{dL}{d\delta}
  ```
  To linear order, for a lattice that bends only in the horizontal plane,
  ```{math}
    \alpha_p = \frac{1}{L} \oint \frac{\eta_x}{\rho} \, ds
  ```
  where {math}`\rho` is the bending radius of the reference orbit and {math}`\eta_x` is the
  [dispersion](#s:dispersion). Also see `slip_factor`.

- `normalized_emittance_a`, `normalized_emittance_b`, `normalized_emittance_c` [m]

  The normal mode emittances scaled by the reference momentum:
  ```{math}
    \epsilon_N = \beta \gamma \, \epsilon = \frac{P_0}{m \, c} \, \epsilon
  ```
  where {math}`\beta` and {math}`\gamma` are the relativistic factors of the reference particle
  and {math}`m` is its mass. The values refer to the same place as the emittances do. Under
  acceleration the emittance shrinks as {math}`1/\beta\gamma` (adiabatic damping) while the
  normalized emittance stays constant, which is why the normalized emittance is normally used for
  linacs.

- `slip_factor` [-]

  The phase slip factor {math}`\eta_p`. This is the fractional change, per unit {math}`\delta`,
  in the time {math}`T` for a particle on the periodic orbit to make one pass, evaluated at
  {math}`\delta = 0` with RF cavities off:
  ```{math}
    \eta_p = \frac{1}{T} \frac{dT}{d\delta}
  ```
  To first order the slip factor is related to the momentum compaction by
  ```{math}
    \eta_p = \alpha_p - \frac{1}{\gamma^2}
  ```
  where {math}`\gamma` is the Lorentz factor of the reference particle. The slip factor is zero at
  the transition energy {math}`\gamma_t = 1/\sqrt{\alpha_p}`, negative below transition, and
  positive above. Some authors use the opposite sign.

- `spin_tune` [rad]

  The closed orbit spin tune {math}`\nu_0`. This is the angle by which a spin on the periodic
  orbit rotates about the closed orbit invariant spin direction {math}`{\bf n}_0` over one pass.
  If {math}`(q_1, q_x, q_y, q_z)` is the [spin quaternion](#s:spin) for one pass along the periodic
  orbit, then
  ```{math}
    \nu_0 = 2 \, \text{atan2} \left( |(q_x, q_y, q_z)|, \, |q_1| \right), \qquad
    {\bf n}_0 = \frac{\text{sign}(q_1)}{|(q_x, q_y, q_z)|} \, (q_x, q_y, q_z)
  ```
  The spin tune is ambiguous in two ways. Adding any multiple of {math}`2\pi` gives an equally
  valid tune, and replacing {math}`{\bf n}_0` with {math}`-{\bf n}_0` changes the sign of the tune.
  PALS resolves this by requiring the spin tune to be in the range {math}`[0, \pi]`, with
  {math}`{\bf n}_0` chosen to match. The formulas above follow this convention.

- `tune_a`, `tune_b`, `tune_c` [rad]

  The normal mode tunes. The tune of a mode is its phase advance over one pass along the periodic
  orbit. For the `a` and `b` modes, this is the change in the [TwissP](#s:twiss.params) phases
  `phi_a` and `phi_b` from the start to the end of the branch. The tune includes the whole number
  of oscillations. For example, a mode that completes 10.3 oscillations per pass has a tune of
  {math}`10.3 \cdot 2\pi \approx 64.72` radians. See `fractional_tune_a` for the part in
  {math}`[0, 2\pi)`. Tunes are defined only when the motion is stable.

  A positive tune is a clockwise rotation in phase space, for example in the {math}`(x, p_x)` plane
  plotted with {math}`x` on the horizontal axis. PALS uses this convention for all three modes.
  With it, the synchrotron tune `tune_c` is positive below transition and negative above
  transition.
