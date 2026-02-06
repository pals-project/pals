# How to Write Documentation

The documentation uses the [MyST](https://mystmd.org/) markup language and renders to 
[Sphinx](https://www.sphinx-doc.org) as HTML, PDF or EPUB documents.

To build the documentation locally, from the root directory of the repository create a conda environment with
```{code} bash
conda env create -y -f environment.yml
```
This only needs to be done once.
To activate this environment, use
```{code} bash
conda activate pals
```
This needs to be done with any new window.

Then, compile the documentation with

::::{tab-set}

:::{tab-item} HTML
```{code} bash
make html
```
:::

:::{tab-item} PDF
```{code} bash
make latexpdf
```
:::

::::

Open the file `build/html/index.html` with your web browser to visualize.
You are now ready to edit the markdown files that compose the documentation!

If you like to atuomatically rebuild changes on save of edited files, 
run in your particle-accelerator-lattice-standard directory:
```{code} bash
sphinx-autobuild source/ build/html
```
and open the URL shown in the terminal, usually [http://127.0.0.1:8000](http://127.0.0.1:8000).

If you add new markdown files, do not forget to add them to the table of contents defined `source/index.md`.
Finally, once you are happy with your changes, do not forget to commit and push them to your branch and open a pull request on GitHub.
