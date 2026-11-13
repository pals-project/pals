# PALS Unit-Test Lattices

Small, single-feature PALS documents that can be used as unit tests.
Each file demonstrates one behavior of PALS
and states, in its header comment, what it shows and the section of the
standard (or the original test) it comes from. Together they can serve as a
conformance corpus for programs that read PALS: a reader should accept every
file here, and where the header states derived values, expansion should
reproduce them.

Every file is valid input; there are no deliberately malformed documents here.

## Directories

| Directory | Feature |
| --- | --- |
| `document/` | The PALS root node: documented root keys, prose (authors/notes/reminders), extension labels with extension data, and `include` at three levels of the tree. |
| `elements/` | Element parameters and their dependent-parameter bookkeeping: reference propagation through a drift/quadrupole/bend line, RF voltage/gradient/active-length relations, bend geometry (angle, radius, chord, straight), the default bend actual field, integrated electric multipoles, Twiss momentum dependence, and the Fiducial, FloorShift, BeamBeam, UnionEle, Patch, and Girder elements. |
| `beamlines/` | Lattice branches and line construction: a branch taking its root BeamLine from its name, an explicit branch `inherit`, `repeat` with nested sub-lines, line item placement, direction reversal, parameter values given on a line item, and superposition. |
| `multipass/` | Multipass lines, flat and nested. |
| `forks/` | Forks: the minimal form, named new branches, forking into an existing branch, destination bookkeeping (`forked_to` / `ForkFromP`), a forked-to line with its own BeginningEle, and a web of forks across two root branches. |
| `expressions/` | Expressions: constants and variables (long and compact forms), every mathematical function, `expr(...)`, `random_gauss()`, references to other elements' parameters, and species-name constants with `mass_of(...)`. |
| `controllers/` | Controllers: ABSOLUTE (single, summed, pattern-matched targets), RELATIVE, a controller driving another controller's variable, a controller reaching into a branch, and a controller with MetaP and an equation-valued variable. |
| `sets/` | `set` and the compact `sets` form: pattern-matched targets, `PARAMETER` and `SELF` in value expressions, a set on a later-repeated definition, `absolute_error` and `relative_error`, sets on dependent parameter groups, and a random set under `post_expansion`. |
| `adjustments/` | Post-expansion `adjustments`: an `optimize` block that varies quadrupole strengths to match the fractional tunes of a ring. |
| `loading/` | Families of files combined with `load`: SELF placement (explicit and implicit), nested and diamond-shaped load graphs, relative path resolution, merging of dictionary-valued root keys, version agreement, and `load` combined with `include`. |

## Validation

Every document outside `loading/` should expand with zero problems, except the
`.subpals.yaml` files in `document/include/`: they are spliced in by
`include` and are not complete documents, so the file to expand is
`document/include/main.pals.yaml`. Files that use `random_gauss()` have no
fixed derived values to reproduce.
In `loading/`, the file to expand is each family's
`joiner.pals.yaml`; the families are deliberately minimal (mostly `notes`
entries that make the combination order observable), so expanding a joiner
combines its family cleanly and then reports only that there is no lattice to
expand — except `loading/basic/`, whose joiner expands a complete lattice
with zero problems.

## Adding a test

- Test one feature per file. Start the file with a header comment that says
  what it shows, any derived values expansion should reproduce, and the
  section of the standard it comes from.
- Start every branch with a `BeginningEle`; it holds the `ReferenceP` values.
- Define the root BeamLine under `facility` and list it by name in the
  Lattice's `branches`.
- Give extension data an `extension: <label>` key, and register the label
  under `extension_labels.names`.
- Use at most one `use` statement.
- When adding a directory, add a row for it to the table above.
