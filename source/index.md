# PALS: Particle Accelerator Language Standard

The **Particle Accelerator Language Standard (PALS)** defines a common, language-neutral
way to describe the lattices and machine information of particle accelerators and storage
rings — so that this information can be shared freely between simulation programs,
published, archived, and analyzed with a single, unified description.

A PALS-based lattice can hold the information for an entire machine complex, from beam
creation through to the dump lines, enabling start-to-end simulations built on a single
lattice. PALS itself does not perform simulations or tracking; it is the standardized
*description* that simulation programs read from and write to.

```{admonition} Why PALS?
:class: tip

- **Portability** between applications and differing algorithms
- **Open access** description of scientific data for publishing and archiving
- **A unified basis** for post-processing, visualization, and analysis
```

## Explore the standard

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} 🚀 Overview
:link: overview
:link-type: doc

What PALS is, what it is not, and how simulation programs interact with a PALS file.
:::

:::{grid-item-card} 📐 Fundamentals
:link: fundamentals
:link-type: doc

Core concepts, notation, and coordinate conventions used throughout the schema.
:::

:::{grid-item-card} 🧩 Lattice Elements
:link: lattice-elements
:link-type: doc

The standardized element kinds, their parameters, and how they are grouped.
:::

:::{grid-item-card} 🔗 Beamlines & Construction
:link: beamlines
:link-type: doc

Organizing elements into lines and branches to describe an entire machine complex.
:::

:::{grid-item-card} 💻 Implementations
:link: code-packages
:link-type: doc

Code packages and simulation programs that read and write PALS files.
:::

:::{grid-item-card} 🤝 Contributing
:link: contributing
:link-type: doc

Governance, how to contribute, and guidelines for writing documentation.
:::

::::

```{toctree}
:maxdepth: 2
:hidden:
:caption: Overview

overview.md
definitions.md
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Schema

notation.md
fundamentals.md
coordinates.md
lattice-elements.md
lattice-element-kinds.md
lattice-element-parameters.md
lattice-element-parameter-groups.md
beamlines.md
lattice-construction.md
multipass.md
miscellaneous.md
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Physics

bend-multipoles.md
dispersion.md
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Implementations

code-packages.md
simulations.md
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Extensions

extensions.md
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Back Matter

governance.md
contributing.md
how-to-write-docs.md
```

