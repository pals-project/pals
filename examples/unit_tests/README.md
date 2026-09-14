# PALS Unit-Test Lattices

Small, single-feature PALS documents that can be used as unit tests.
Each file demonstrates one behavior of the
standard and states, in its header comment, what it shows and the test it
comes from. Together they can serve as a conformance corpus for programs that
read PALS: a reader should accept every file here, and where the header
states derived values, expansion should reproduce them.

Only lattices the tests treat as *valid* input were carried over; the
deliberately malformed documents the tests use to probe error reporting were
left behind.

## Directories

| Directory | Feature |
| --- | --- |
| `document/` | The PALS root node: documented root keys, prose (authors/notes/reminders), and extension labels with extension data. |
| `elements/` | Element parameters and their dependent-parameter bookkeeping: reference propagation through a drift/quadrupole/bend line, RF voltage/gradient/active-length relations, bend geometry (angle, radius, chord, straight), the default bend actual field, integrated electric multipoles, and Twiss momentum dependence. |
| `beamlines/` | Lattice branches and line construction: a branch taking its root BeamLine from its name, an explicit branch `inherit`, and `repeat` with nested sub-lines. |
| `multipass/` | Multipass lines, flat and nested. |
| `forks/` | Forks: the minimal form, named new branches, forking into an existing branch, destination bookkeeping (`forked_to` / `ForkFromP`), a forked-to line with its own BeginningEle, and a web of forks across two root branches. |
| `expressions/` | Expressions: constants and variables (map and sequence forms), mathematical functions, `expr(...)`, `random_gauss()`, references to other elements' parameters, and species-name constants with `mass_of(...)`. |
| `controllers/` | Controllers: ABSOLUTE (single, summed, pattern-matched targets), RELATIVE, a controller driving another controller's variable, and a controller reaching into a branch. |
| `sets/` | `set` and the compact `sets` form: pattern-matched targets, `PARAMETER` and `SELF` in value expressions, and a set on a later-repeated definition. |
| `loading/` | Families of files combined with `load`: SELF placement (explicit and implicit), nested and diamond-shaped load graphs, relative path resolution, merging of dictionary-valued root keys, version agreement, and `load` combined with `include`. |

## Validation

Every document outside `loading/` should expand with zero problems.
In `loading/`, the file to expand is each family's
`joiner.pals.yaml`; the families are deliberately minimal (mostly `notes`
entries that make the combination order observable), so expanding a joiner
combines its family cleanly and then reports only that there is no lattice to
expand — except `loading/basic/`, whose joiner expands a complete lattice
with zero problems.
