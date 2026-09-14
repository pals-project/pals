# PALS Examples

Example lattices for the Particle Accelerator Language Standard, as physics examples (suitable for integration tests) and small unit tests.

## Layout

| Path | Contents |
| --- | --- |
| `fodo.pals.yaml` | The introductory example: elements, a FODO cell, `inherit`, `repeat`, a lattice, and `use`. |
| `machine/` | A small facility exercising the heavier constructs together: a multipass line, in-place element definitions, `inherit`, a repeated sub-line, a Fork into a dump branch, `include`, and two lattices sharing one line. Entry point: `machine.pals.yaml`. |
| `modular_machine/` | A machine split over several files combined with `load`: the layout, one settings file, and a joiner that stacks them and adds a tweak of its own. Entry point: `joiner.pals.yaml`. |
| `unit_tests/` | A corpus of small, single-feature lattices for unit tests, organized by feature. See `unit_tests/README.md`. |

## Validation

Every self-contained PALS file here must expand without problems.
Two kinds of files are not self-contained and only carry meaning through the file that
names them:

- members of a `load` family (for example `modular_machine/settings.pals.yaml`)
  are combined by their `joiner.pals.yaml`, which is the file to expand;
- files spliced in by `include` (for example
  `machine/subline_elements.subpals.yaml`) hold a facility-entry sequence, not
  a full PALS document; per the standard's notation section they carry the
  `.subpals.yaml` suffix.
